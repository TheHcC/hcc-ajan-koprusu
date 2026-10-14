#!/usr/bin/env python3
"""
okunur_yap.py — StudyPack .md dosyalarını telefonda ve bilgisayarda rahat okunur
HTML ve PDF'e çevirir. Kaynak .md dosyasına DOKUNMAZ; çıktılar yanındaki `_okuma/`
klasörüne yazılır.

Ne yapar:
  * Satırları ekran genişliğine göre sarar (uzun satır sorunu biter), metin
    genişliği ~65 karakterle sınırlanır.
  * Geniş tablolar dar ekranda ve PDF'te "kart" görünümüne döner (yatay kaydırma yok).
  * "CEVAP" başlıklı bölümler HTML'de kapalı gelir (tıkla-aç); PDF'te yeni sayfadan başlar.
  * Obsidian [[bağlantı|etiket]] yazımı düz etikete, > [!note] kutuları renkli kutuya döner.
  * Başa paket kimliği / durum / tarih kartı ve içindekiler eklenir.
  * PDF A5 boyutundadır: telefonda tam ekran, GoodNotes'ta not alınabilir.

Kurulum (bir kez):  pip install markdown-it-py pyyaml
PDF için: Microsoft Edge veya Google Chrome kurulu olması yeterli (Windows'ta Edge zaten var).
           (İsteğe bağlı) pip install playwright  → varsa onu kullanır.

Kullanım:
  python okunur_yap.py DOSYA_VEYA_KLASOR [...]            # yalnız okunması gereken durumdakiler
  python okunur_yap.py KLASOR --hepsi                       # durumuna bakmadan hepsi
  python okunur_yap.py DOSYA.md --yalniz-html               # PDF üretme
  python okunur_yap.py KLASOR --zorla                       # güncel olsa da yeniden üret

Okunması gereken durumlar (frontmatter `durum:` alanında geçen kelimeye göre):
  TASLAK, KONTROLLU, CALISILDI, OKUMA, ONAY  (büyük/küçük harf ve Türkçe karakter fark etmez)
"""
from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

try:
    from markdown_it import MarkdownIt
except ImportError:  # pragma: no cover
    sys.exit("Eksik paket: pip install markdown-it-py pyyaml")

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

OKUNACAK_DURUMLAR = ("TASLAK", "KONTROLLU", "CALISILDI", "OKUMA", "ONAY")
CIKTI_KLASORU = "_okuma"


# ---------------------------------------------------------------- yardımcılar

def ascii_buyuk(metin: str) -> str:
    """Türkçe karakterleri sadeleştirip büyük harfe çevirir (durum karşılaştırması için)."""
    tablo = str.maketrans("çğıöşüÇĞİÖŞÜâÂîÎûÛ", "cgiosuCGIOSUaAiIuU")
    return metin.translate(tablo).upper()


def slug(metin: str, kullanilan: set[str]) -> str:
    sade = ascii_buyuk(re.sub(r"<[^>]+>", "", metin)).lower()
    sade = unicodedata.normalize("NFKD", sade)
    sade = re.sub(r"[^a-z0-9]+", "-", sade).strip("-") or "bolum"
    aday, i = sade, 2
    while aday in kullanilan:
        aday, i = f"{sade}-{i}", i + 1
    kullanilan.add(aday)
    return aday


def frontmatter_ayir(metin: str) -> tuple[dict, str]:
    metin = metin.lstrip("\ufeff")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", metin, re.S)
    if not m:
        return {}, metin
    ham, govde = m.group(1), metin[m.end():]
    veri: dict = {}
    if yaml is not None:
        try:
            yuklenen = yaml.safe_load(ham)
            if isinstance(yuklenen, dict):
                veri = yuklenen
        except yaml.YAMLError:
            veri = {}
    if not veri:  # yaml yoksa / bozuksa basit anahtar: değer okuması
        for satir in ham.splitlines():
            if ":" in satir and not satir.startswith(" "):
                k, v = satir.split(":", 1)
                veri[k.strip()] = v.strip()
    return veri, govde


def obsidian_temizle(md: str) -> str:
    # [[yol|etiket]] → etiket ; [[yol]] → dosya adı ; ![[gömme]] → (gömme: ad)
    md = re.sub(r"!\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", lambda m: f"*(gömülü: {Path(m.group(1)).stem})*", md)
    md = re.sub(r"\[\[([^\]|]+)\\?\|([^\]]+)\]\]", r"**\2**", md)
    md = re.sub(r"\[\[([^\]]+)\]\]", lambda m: f"**{Path(m.group(1)).name}**", md)
    return md


# ------------------------------------------------------------ markdown → html

def md_to_html(govde: str) -> tuple[str, list[tuple[int, str, str]]]:
    mdi = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable(["table", "strikethrough"])
    tokens = mdi.parse(obsidian_temizle(govde))
    kullanilan: set[str] = set()
    basliklar: list[tuple[int, str, str]] = []
    for i, tok in enumerate(tokens):
        if tok.type == "heading_open":
            seviye = int(tok.tag[1])
            ic = tokens[i + 1].content if i + 1 < len(tokens) else ""
            kimlik = slug(ic, kullanilan)
            tok.attrSet("id", kimlik)
            basliklar.append((seviye, ic, kimlik))
    return mdi.renderer.render(tokens, mdi.options, {}), basliklar


CALLOUT_RE = re.compile(r"<blockquote>\s*<p>\[!(\w+)\][+-]?\s*", re.I)


def calloutlari_isle(govde_html: str) -> str:
    return CALLOUT_RE.sub(lambda m: f'<blockquote class="callout callout-{m.group(1).lower()}"><p>', govde_html)


def cevap_basligi_mi(baslik: str) -> bool:
    """'10. CEVAP', 'C1. ÇÖZÜM — (a)', '5. Tam kaynak cevap' → evet.
    'ÇÖZÜM SIRASI', 'Çözüm algoritması', 'Tarihsel cevap ↔ ...' → hayır."""
    b = ascii_buyuk(re.sub(r"<[^>]+>", "", baslik)).strip()
    b = re.sub(r"^[A-Z]?\d*[A-Z]?[.)]\s*", "", b)  # '10.', 'C1.', '5a.' gibi numaraları at
    if b.startswith(("CEVAP", "TAM KAYNAK CEVAP", "KAYNAK CEVAP")):
        return True
    return b.startswith("COZUM") and not re.match(r"COZUM\s+(SIRASI|ALGORITMA|ADIMLARI|YOLU)", b)


BASLIK_RE = re.compile(r"<h([1-6]) id=\"([^\"]+)\">(.*?)</h\1>", re.S)


def cevaplari_sar(govde_html: str, pdf: bool) -> str:
    """Başlığında CEVAP / ÇÖZÜM geçen bölümleri katlanır kutuya alır."""
    parcalar = []
    konum = 0
    eslesmeler = list(BASLIK_RE.finditer(govde_html))
    i = 0
    while i < len(eslesmeler):
        m = eslesmeler[i]
        seviye, baslik = int(m.group(1)), re.sub(r"<[^>]+>", "", m.group(3))
        if cevap_basligi_mi(baslik):
            # bölüm sonu: aynı veya üst seviyedeki sonraki başlık
            son = len(govde_html)
            j = i + 1
            while j < len(eslesmeler):
                if int(eslesmeler[j].group(1)) <= seviye:
                    son = eslesmeler[j].start()
                    break
                j += 1
            ic = govde_html[m.end():son]
            # bölüm sonundaki <hr /> kutunun dışında kalsın
            ic_kirp = re.sub(r"\s*<hr\s*/?>\s*$", "", ic)
            kalan = ic[len(ic_kirp):]
            parcalar.append(govde_html[konum:m.start()])
            acik = " open" if pdf else ""
            parcalar.append(
                f'<details class="cevap"{acik}><summary>{m.group(0)}'
                f'<span class="ipucu">Önce çöz · açmak için dokun</span></summary>'
                f'{ic_kirp}</details>{kalan}'
            )
            konum = son
            while j < len(eslesmeler) and eslesmeler[j].start() < son:
                j += 1
            i = j if j > i else i + 1
            continue
        i += 1
    parcalar.append(govde_html[konum:])
    return "".join(parcalar)


DURUM_RENK = {
    "TASLAK": "taslak", "KONTROLLU": "kontrollu", "CALISILDI": "calisildi",
    "OKUMA": "kontrollu", "ONAY": "kontrollu", "RELEASED": "calisildi", "KABUL": "calisildi",
}


def durum_sinifi(durum: str) -> str:
    d = ascii_buyuk(durum or "")
    for anahtar, sinif in DURUM_RENK.items():
        if anahtar in d:
            return sinif
    return "bilinmiyor"


CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d1d1b;--muted:#6b6a65;--line:#e4e1d8;--card:#ffffff;--accent:#1f5f8b;
--code:#f3f1ea;--warn:#a15c00;--warnbg:#fff4e0;--note:#1f5f8b;--notebg:#eaf2f8;--ok:#2f6b3a;--okbg:#e8f3ea;
--cevapbg:#f6f1fb;--cevap:#5b3d8a}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#e9e7e1;--muted:#a19f98;--line:#33322f;--card:#1e1e1c;
--accent:#7fb6dd;--code:#242422;--warn:#f0b35e;--warnbg:#2c2416;--note:#7fb6dd;--notebg:#18242d;--ok:#8fcf9a;--okbg:#17261a;
--cevapbg:#221c2b;--cevap:#c7a8f0}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.62 "Segoe UI",Inter,system-ui,-apple-system,Roboto,"Noto Sans",sans-serif;}
main{max-width:42rem;margin:0 auto;padding:20px 16px 64px}
h1{font-size:1.45rem;line-height:1.3;margin:.2em 0 .6em}
h2{font-size:1.2rem;line-height:1.35;margin:2em 0 .6em;padding-top:.6em;border-top:1px solid var(--line)}
h3{font-size:1.05rem;margin:1.5em 0 .4em}
p,li{overflow-wrap:break-word;hyphens:auto}
ul,ol{padding-left:1.3em}
li{margin:.25em 0}
a{color:var(--accent)}
hr{border:0;border-top:1px solid var(--line);margin:1.6em 0}
strong{font-weight:650}
code{background:var(--code);padding:.08em .32em;border-radius:4px;font:0.88em "Cascadia Mono",Consolas,"DejaVu Sans Mono",monospace}
pre{background:var(--code);padding:12px 14px;border-radius:8px;overflow-x:auto;font-size:.8rem;line-height:1.45}
pre code{background:none;padding:0;font-size:inherit}
blockquote{margin:1em 0;padding:.6em 1em;border-left:4px solid var(--line);background:var(--card);border-radius:0 8px 8px 0}
blockquote p{margin:.4em 0}
.callout-warning,.callout-caution,.callout-important{border-color:var(--warn);background:var(--warnbg)}
.callout-note,.callout-info,.callout-tip{border-color:var(--note);background:var(--notebg)}
.callout-success{border-color:var(--ok);background:var(--okbg)}
.kart{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px 14px;margin:0 0 18px;font-size:.88rem;color:var(--muted)}
.kart b{color:var(--fg)}
.rozet{display:inline-block;font-size:.75rem;font-weight:700;letter-spacing:.03em;padding:2px 8px;border-radius:999px;margin-left:6px;vertical-align:1px}
.rozet.taslak{background:var(--warnbg);color:var(--warn)}
.rozet.kontrollu{background:var(--notebg);color:var(--note)}
.rozet.calisildi{background:var(--okbg);color:var(--ok)}
.rozet.bilinmiyor{background:var(--code);color:var(--muted)}
nav.icindekiler{font-size:.9rem;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 14px;margin-bottom:8px}
nav.icindekiler summary{cursor:pointer;font-weight:600}
nav.icindekiler ol{margin:.4em 0;padding-left:1.2em}
.tablo{overflow-x:auto;margin:1em 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
th,td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;text-align:left;overflow-wrap:break-word}
th{background:var(--code)}
details.cevap{border:1px solid var(--cevap);background:var(--cevapbg);border-radius:10px;padding:0 14px;margin:1.4em 0}
details.cevap>summary{list-style:none;cursor:pointer;padding:10px 0}
details.cevap>summary::-webkit-details-marker{display:none}
details.cevap>summary h2,details.cevap>summary h3{display:inline;border:0;margin:0;padding:0;color:var(--cevap)}
details.cevap .ipucu{display:block;font-size:.78rem;color:var(--muted)}
details.cevap[open] .ipucu{display:none}
/* Dar ekranda (ve PDF'te) 3+ sütunlu tablolar kartlara dönüşür */
@media (max-width:640px){
  body{font-size:16.5px}
  table.kartli thead{display:none}
  table.kartli,table.kartli tbody,table.kartli tr,table.kartli td{display:block;width:100%}
  table.kartli tr{border:1px solid var(--line);border-radius:8px;margin:0 0 10px;padding:4px 0;background:var(--card)}
  table.kartli td{border:0;padding:4px 10px}
  table.kartli td::before{content:attr(data-etiket);display:block;font-size:.74rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.02em}
}
@page{size:A5;margin:12mm 11mm 14mm}
@media print{
  :root{--bg:#fff;--card:#fff}
  body{font-size:10.4pt;line-height:1.5;background:#fff}
  main{max-width:none;padding:0}
  h2{break-after:avoid;page-break-after:avoid}
  h3{break-after:avoid}
  tr,blockquote,pre{break-inside:avoid}
  pre{white-space:pre-wrap;font-size:7.6pt;overflow:visible}
  nav.icindekiler{display:none}
  details.cevap{break-before:page;page-break-before:always}
  details.cevap .ipucu{display:block}
  table.kartli thead{display:none}
  table.kartli,table.kartli tbody,table.kartli tr,table.kartli td{display:block;width:100%}
  table.kartli tr{border:1px solid var(--line);border-radius:6px;margin:0 0 6px;padding:2px 0}
  table.kartli td{border:0;padding:2px 8px}
  table.kartli td::before{content:attr(data-etiket);display:block;font-size:7pt;font-weight:700;color:#6b6a65;text-transform:uppercase}
}
"""

JS = r"""
document.querySelectorAll('table').forEach(function(t){
  var basliklar=[].map.call(t.querySelectorAll('thead th'),function(th){return th.textContent.trim();});
  if(basliklar.length>=3){t.classList.add('kartli');}
  t.querySelectorAll('tbody tr').forEach(function(tr){
    [].forEach.call(tr.children,function(td,i){td.setAttribute('data-etiket',basliklar[i]||'');});
  });
  var sar=document.createElement('div');sar.className='tablo';t.parentNode.insertBefore(sar,t);sar.appendChild(t);
});
"""


def sayfa_olustur(kaynak: Path, pdf: bool) -> str:
    metin = kaynak.read_text(encoding="utf-8")
    on, govde = frontmatter_ayir(metin)
    govde_html, basliklar = md_to_html(govde)
    govde_html = calloutlari_isle(govde_html)
    govde_html = cevaplari_sar(govde_html, pdf=pdf)

    baslik = str(on.get("baslik") or on.get("title") or next((b[1] for b in basliklar if b[0] == 1), kaynak.stem))
    kimlik = str(on.get("id") or on.get("study_pack_id") or kaynak.stem)
    durum = str(on.get("durum") or on.get("dogrulama_durumu") or "durum yok")
    tarih = str(on.get("tarih") or "")

    kart = (f'<div class="kart"><b>{html.escape(kimlik)}</b>'
            f'<span class="rozet {durum_sinifi(durum)}">{html.escape(durum)}</span>'
            + (f'<br>{html.escape(tarih)}' if tarih else "")
            + f'<br><span style="font-size:.8em">Kaynak: {html.escape(kaynak.name)}</span></div>')

    h2ler = [(b[1], b[2]) for b in basliklar if b[0] == 2]
    icindekiler = ""
    if len(h2ler) >= 4:
        maddeler = "".join(f'<li><a href="#{k}">{html.escape(t)}</a></li>' for t, k in h2ler)
        icindekiler = f'<nav class="icindekiler"><details><summary>İçindekiler</summary><ol>{maddeler}</ol></details></nav>'

    return (
        "<!doctype html><html lang=\"tr\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        f"<title>{html.escape(kimlik)}</title><style>{CSS}</style></head><body><main>"
        f"{kart}{icindekiler}{govde_html}</main><script>{JS}</script></body></html>"
    )


# ------------------------------------------------------------------ html → pdf

def tarayici_bul() -> str | None:
    adaylar = [
        os.environ.get("OKUNUR_TARAYICI", ""),
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for ad in ("msedge", "google-chrome", "chromium", "chromium-browser", "chrome"):
        yol = shutil.which(ad)
        if yol:
            adaylar.append(yol)
    return next((a for a in adaylar if a and Path(a).exists()), None)


def pdf_yaz(html_metni: str, hedef: Path) -> str:
    try:
        if os.environ.get("OKUNUR_MOTOR") == "tarayici":
            raise RuntimeError("tarayıcı motoru istendi")
        from playwright.sync_api import sync_playwright  # type: ignore
        with sync_playwright() as p:
            secenek = {}
            if os.environ.get("PLAYWRIGHT_CHROMIUM"):
                secenek["executable_path"] = os.environ["PLAYWRIGHT_CHROMIUM"]
            tarayici = p.chromium.launch(**secenek)
            sayfa = tarayici.new_page()
            sayfa.set_content(html_metni, wait_until="load")
            sayfa.pdf(path=str(hedef), prefer_css_page_size=True, print_background=True,
                      display_header_footer=True, header_template="<span></span>",
                      footer_template='<div style="font-size:7pt;width:100%;text-align:center;color:#888">'
                                      '<span class="pageNumber"></span> / <span class="totalPages"></span></div>')
            tarayici.close()
        return "playwright"
    except Exception as hata:  # playwright yok ya da tarayıcısı yok → Edge/Chrome
        tarayici = tarayici_bul()
        if not tarayici:
            raise RuntimeError(f"PDF için Edge/Chrome bulunamadı ve playwright çalışmadı ({hata}).")
        with tempfile.TemporaryDirectory() as gecici:
            gecici_html = Path(gecici) / "sayfa.html"
            gecici_html.write_text(html_metni, encoding="utf-8")
            komut = [tarayici, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                     f"--print-to-pdf={hedef.resolve()}", gecici_html.as_uri()]
            if os.name != "nt" and hasattr(os, "geteuid") and os.geteuid() == 0:
                komut.insert(1, "--no-sandbox")  # Linux'ta root olarak çalışırken gerekli
            subprocess.run(komut, check=True, capture_output=True, timeout=120)
        return Path(tarayici).name


# ------------------------------------------------------------------ toplu akış

def okunacak_mi(dosya: Path) -> bool:
    on, _ = frontmatter_ayir(dosya.read_text(encoding="utf-8"))
    durum = ascii_buyuk(str(on.get("durum") or on.get("dogrulama_durumu") or ""))
    return any(k in durum for k in OKUNACAK_DURUMLAR)


def dosyalari_topla(girdiler: list[str]) -> list[Path]:
    sonuc: list[Path] = []
    for g in girdiler:
        yol = Path(g)
        if yol.is_dir():
            sonuc += [p for p in sorted(yol.rglob("*.md")) if CIKTI_KLASORU not in p.parts and not p.name.startswith("_")]
        elif yol.suffix.lower() == ".md":
            sonuc.append(yol)
    return sonuc


def main() -> int:
    ap = argparse.ArgumentParser(description="StudyPack .md → okunur HTML + A5 PDF")
    ap.add_argument("girdiler", nargs="+")
    ap.add_argument("--hepsi", action="store_true", help="durum filtresi uygulama")
    ap.add_argument("--yalniz-html", action="store_true")
    ap.add_argument("--zorla", action="store_true", help="güncel olsa da yeniden üret")
    ap.add_argument("--cikti", help="tüm çıktıları tek klasöre yaz")
    a = ap.parse_args()

    dosyalar = dosyalari_topla(a.girdiler)
    tekil = len(dosyalar) == 1 and Path(a.girdiler[0]).is_file()
    uretilen = atlanan = 0
    for d in dosyalar:
        if not (a.hepsi or tekil or okunacak_mi(d)):
            continue
        hedef_klasor = Path(a.cikti) if a.cikti else d.parent / CIKTI_KLASORU
        hedef_klasor.mkdir(parents=True, exist_ok=True)
        hedef_html, hedef_pdf = hedef_klasor / f"{d.stem}.html", hedef_klasor / f"{d.stem}.pdf"
        guncel = hedef_html.exists() and hedef_html.stat().st_mtime >= d.stat().st_mtime
        if guncel and not a.zorla and (a.yalniz_html or hedef_pdf.exists()):
            atlanan += 1
            continue
        hedef_html.write_text(sayfa_olustur(d, pdf=False), encoding="utf-8")
        motor = "-"
        if not a.yalniz_html:
            motor = pdf_yaz(sayfa_olustur(d, pdf=True), hedef_pdf)
        uretilen += 1
        print(f"✓ {d.name} → {hedef_html.name}" + ("" if a.yalniz_html else f" + {hedef_pdf.name} [{motor}]"))
    print(f"Bitti: {uretilen} üretildi, {atlanan} zaten güncel.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
