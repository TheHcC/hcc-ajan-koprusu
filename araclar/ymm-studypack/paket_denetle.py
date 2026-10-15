#!/usr/bin/env python3
"""
paket_denetle.py — StudyPack temizliğinde "içerik kaybolmadı, içerik uydurulmadı"
kontrolü. Model değil, kural çalışır; aynı girdiye her seferinde aynı sonucu verir.

İki kip:

  1) Biçim denetimi (tek yeni paket):
       python paket_denetle.py bicim YENI_CALISMA.md [YENI_VAKA_1.md ...]

  2) Koruma denetimi (eski uzun paket → yeni dosyalar):
       python paket_denetle.py karsilastir ESKI.md YENI_CALISMA.md [YENI_VAKA_1.md ...] [--kaynak 01_ham/.../2020_1.md ...]
       --kaynak: VAKA'ya özgün soru/komisyon cevabı ham sınav dosyasından alındıysa o dosyalar.
       (Yeni dosyaların TOPLAMI eskiyle karşılaştırılır.)

Seçenek: --rapor RAPOR.md  → sonucu dosyaya da yazar.
Çıkış kodu: 0 = HATA yok (uyarılar olabilir), 1 = en az bir HATA var.

Ne HATA sayılır (iş durur, Cihan'a gelmez):
  * Yeni dosyada eski pakette OLMAYAN bir kanun/madde atfı (uydurma riski) —
    frontmatter `yeni_atiflar:` listesinde gerekçesiyle yazılmadıkça.
  * Yeni dosyada eski pakette olmayan bir özelge (tarih+sayı) atfı.
  * Eski paketteki komisyon cevap metninin (kaynak alıntı) yenide birebir bulunmaması.
  * Eski paketteki bir özelge atfının yenide kaybolması.
  * Google Docs kaçış bozukluğu (\\#, \\*\\*, \\_ gibi).
  * Zorunlu frontmatter alanı / SORU / CEVAP / Kaynak bölümü eksikliği; CEVAP'ın SORU'dan önce gelmesi.
  * Codex EK-4: ÇALIŞMA 18.000 baytı; VAKA tam komisyon cevabı
    bölümü çıkarıldıktan sonra yazılan metin 20.000 baytı aşması.

Ne UYARI sayılır (Cihan'ın / denetçinin bakacağı liste):
  * Eski paketteki bir sayı, tarih, oran veya madde atfının yenide geçmemesi
    (kısaltmada bilinçli atılmış olabilir — yenideki `cikarilanlar:` alanına yazılırsa uyarı düşer).
  * Yenide eski pakette olmayan sayı/oran (yeni hesap örneği olabilir; verify.py ile doğrulanmalı).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

ZORUNLU_ALANLAR = ("id", "ders", "durum", "kaynak", "tarih", "uretici")
GECERLI_DURUMLAR = ("TASLAK", "KONTROLLU", "CALISILDI")
BOYUT_SINIRI = {"CALISMA": 18_000, "VAKA": 20_000}
BOYUT_TAVANI = dict(BOYUT_SINIRI)

KANUNLAR = r"(VUK|GVK|KVK|KDVK|KDV|ÖTVK|DVK|HK|ÇVÖA|AATUHK|TTK|İYUK|6183|213|193|5520|3065|7456|7524|7440|5746|3568)"
MADDE_RE = re.compile(
    KANUNLAR + r"(?:['’]?(?:n[ıiuü]n|un|ün|in))?\s*(?:m\.?|md\.?|madde(?:si)?)?\s*"
    r"(?:geçici\s+|mük(?:errer)?\.?\s*|ek\s+)?(\d{1,3}(?:/[A-ZÇĞİÖŞÜa-zçğıöşü0-9]{1,3})?(?:[-–][a-zçğıöşü](?:\(\d\))?)?)",
)
OZELGE_RE = re.compile(r"(\d{2}\.\d{2}\.\d{4})\s+tarih(?:li)?\s+ve\s+[^\n]{0,60}?([\w\[\]().\-/]+)\s+sayılı", re.I)
SAYI_RE = re.compile(r"(?<![\w.,])(?:%\s?\d+(?:,\d+)?|\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+,\d+|\d{4,})(?![\w])")
TARIH_RE = re.compile(r"\b\d{2}\.\d{2}\.\d{4}\b")
KACIS_RE = re.compile(r"\\[#*_\[\]>|-]")


# --------------------------------------------------------------- okuma araçları

def oku(yol: Path) -> tuple[dict, str]:
    metin = yol.read_text(encoding="utf-8").lstrip("\ufeff")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", metin, re.S)
    if not m:
        return {}, metin
    on: dict = {}
    if yaml is not None:
        try:
            yuk = yaml.safe_load(m.group(1))
            on = yuk if isinstance(yuk, dict) else {}
        except yaml.YAMLError:
            on = {}
    if not on:  # YAML bozuksa (değerde ': ' vb.) basit anahtar: değer okuması
        for satir in m.group(1).splitlines():
            if ":" in satir and not satir.startswith((" ", "-")):
                k, v = satir.split(":", 1)
                on[k.strip()] = v.strip()
    return on, metin[m.end():]


def sade(s: str) -> str:
    return s.translate(str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")).upper()


def bosluk_normalize(s: str) -> str:
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


ZINCIR_RE = re.compile(r"\s*(?:\+|,|ve|ile)\s*(?:m\.?\s*)?(\d{1,3}(?:/[A-Za-zçğıöşü0-9]{1,3})?(?:[-–][a-zçğıöşü](?:\(\d\))?)?)(?!\d)(?![.,]\d)")


def madde_atiflari(metin: str) -> set[str]:
    """'GVK m.75 + 94/6 + 96' → {GVK 75, GVK 94/6, GVK 96}."""
    sonuc = set()
    for m in MADDE_RE.finditer(metin):
        kanun = {"KDV": "KDVK", "213": "VUK", "193": "GVK", "5520": "KVK", "3065": "KDVK"}.get(m.group(1), m.group(1))
        sonuc.add(f"{kanun} {m.group(2).replace('–', '-').lower()}")
        konum = m.end()
        while (z := ZINCIR_RE.match(metin, konum)):
            sonuc.add(f"{kanun} {z.group(1).replace('–', '-').lower()}")
            konum = z.end()
    return sonuc


def ozelge_atiflari(metin: str) -> set[str]:
    return {f"{t} / {s}" for t, s in OZELGE_RE.findall(metin)}


def sayilar(metin: str) -> set[str]:
    govde = re.sub(r"https?://\S+", " ", metin)
    bulunan = {re.sub(r"\s", "", x) for x in SAYI_RE.findall(govde)} | set(TARIH_RE.findall(govde))
    return {x for x in bulunan if not re.fullmatch(r"(19|20)\d\d", x)}  # tek başına yıl anlamsız


def kaynak_alintilari(metin: str) -> list[str]:
    """'kaynak cevap' / 'komisyon cevabı' başlıklı bölümlerdeki > alıntı bloklarını döndürür."""
    bloklar, aktif, mevcut = [], False, []
    for satir in metin.splitlines():
        if re.match(r"^#{1,6}\s", satir):
            if mevcut:
                bloklar.append("\n".join(mevcut)); mevcut = []
            aktif = bool(re.search(r"KAYNAK CEVAP|KOMISYON CEVAB|RESMI CEVAP|TAM CEVAP", sade(satir)))
            continue
        if aktif and satir.startswith(">"):
            mevcut.append(satir.lstrip(">").strip())
        elif mevcut and not satir.strip().startswith(">"):
            if satir.strip():
                bloklar.append("\n".join(mevcut)); mevcut = []
    if mevcut:
        bloklar.append("\n".join(mevcut))
    return [b for b in bloklar if len(b) > 40]


def liste(on: dict, anahtar: str) -> list[str]:
    v = on.get(anahtar) or []
    return [str(x) for x in (v if isinstance(v, list) else [v])]


# ------------------------------------------------------------------- denetimler

def bas_sozcugu(baslik: str) -> str:
    """'10. CEVAP', 'C1. ÇÖZÜM', 'A. SORU' → numarasız, sadeleştirilmiş baş."""
    return re.sub(r"^[A-Z]?\d*[A-Z]?[.)]\s*", "", sade(baslik).strip())


def kaynak_bolumu_satirlari(govde: str) -> list[str]:
    """'Kaynak cevap / komisyon / resmî cevap / tam cevap' başlıklı bölümlerdeki > satırları (ham hâliyle)."""
    satirlar, aktif = [], None
    for satir in govde.splitlines():
        baslik = re.match(r"^(#{1,6})\s", satir)
        if baslik:
            seviye = len(baslik[1])
            if aktif is not None and seviye <= aktif:
                aktif = None
            if re.search(r"KAYNAK CEVAP|KOMISYON|RESMI CEVAP|TAM CEVAP", sade(satir)):
                aktif = seviye
            continue
        if aktif is not None and satir.startswith(">"):
            satirlar.append(satir)
    return satirlar


def cevap_bolumu_bayti(govde: str) -> int:
    """Tam komisyon cevabı başlığından sonraki eş/daha üst başlığa kadar ölçer."""
    aktif_seviye = None
    toplam = 0
    for satir in govde.splitlines(keepends=True):
        baslik = re.match(r"^(#{1,6})\s+(.*)", satir)
        if baslik:
            seviye = len(baslik[1])
            if aktif_seviye is not None and seviye <= aktif_seviye:
                aktif_seviye = None
            if re.search(r"TAM KOMISYON CEVABI|KAYNAK CEVAP|TAM CEVAP|RESMI CEVAP", sade(baslik[2])):
                aktif_seviye = seviye
        if aktif_seviye is not None:
            toplam += len(satir.encode("utf-8"))
    return toplam


def yazilan_metin_bayti(yol: Path) -> int:
    _, govde = oku(yol)
    cevap = cevap_bolumu_bayti(govde) if "VAKA" in sade(yol.name) else 0
    return len(yol.read_bytes()) - cevap


def bicim_denetle(yol: Path, hatalar: list, uyarilar: list) -> None:
    on, govde = oku(yol)
    ad = yol.name
    if "VARYASYON" in sade(ad):
        # EK-4 §3: Bu ekin gövdesi birebir taşınır; çalışma/vaka şeması aranmaz.
        for alan in ("id", "kaynak_bolum", "durum"):
            if not on.get(alan):
                hatalar.append(f"{ad}: frontmatter `{alan}` eksik")
        if sade(str(on.get("durum", ""))) not in GECERLI_DURUMLAR:
            hatalar.append(f"{ad}: varyasyon durumu geçersiz")
        return
    tur = "VAKA" if "VAKA" in sade(ad) else "CALISMA"
    for alan in ZORUNLU_ALANLAR:
        if alan not in on or on.get(alan) in (None, "", []):
            hatalar.append(f"{ad}: frontmatter `{alan}` eksik")
    durum = sade(str(on.get("durum", "")))
    if durum and durum not in GECERLI_DURUMLAR:
        hatalar.append(f"{ad}: durum `{on.get('durum')}` geçersiz — yalnız {', '.join(GECERLI_DURUMLAR)}")
    toplam = len(yol.read_bytes())
    boyut = yazilan_metin_bayti(yol)
    if boyut > BOYUT_TAVANI[tur]:
        hatalar.append(f"{ad}: yazılan metin {boyut:,} bayt — {tur} sınırı {BOYUT_TAVANI[tur]:,} bayt (toplam {toplam:,})".replace(",", "."))
    elif boyut > BOYUT_SINIRI[tur]:
        uyarilar.append(f"{ad}: alıntı hariç {boyut:,} bayt — {tur} önerilen sınırı {BOYUT_SINIRI[tur]:,} bayt aşıyor (okunurluk; içerik kısaltılmaz)".replace(",", "."))
    kacislar = KACIS_RE.findall(govde)
    if len(kacislar) > 3:
        hatalar.append(f"{ad}: {len(kacislar)} adet kaçış bozukluğu (\\# \\* vb.) — Google Docs dönüşümü kalıntısı")
    basliklar = [sade(b) for b in re.findall(r"^#{1,6}\s+(.*)$", govde, re.M)]
    alt_basliklar = [(i, bas_sozcugu(b)) for i, b in enumerate(basliklar)
                     if not re.match(r"^#\s", re.findall(r"^#{1,6}\s+.*$", govde, re.M)[i])]  # H1 başlık sayılmaz
    soru = next((i for i, b in alt_basliklar if re.search(r"\bSORU(LAR)?\b", b)), None)  # 'A. DÖRT SORU' de sayılır
    cevap = next((i for i, b in alt_basliklar if re.match(r"CEVAP|TAM KAYNAK CEVAP|KAYNAK CEVAP|COZUM(?!\s+(SIRASI|ALGORITMA|ADIMLARI|YOLU))", b)), None)
    if soru is None:
        hatalar.append(f"{ad}: 'SORU' başlıklı bölüm yok (cevabı kapalı çalışma için zorunlu)")
    if cevap is None:
        hatalar.append(f"{ad}: 'CEVAP' başlıklı bölüm yok")
    if soru is not None and cevap is not None and cevap < soru:
        hatalar.append(f"{ad}: CEVAP bölümü SORU'dan önce geliyor")
    if not any("KAYNAK" in b for b in basliklar) and not (tur == "VAKA" and on.get("kaynak")):
        hatalar.append(f"{ad}: 'Kaynak' bölümü yok (sınav dönemi + resmî dayanak listesi)")
    if re.search(r"mevzuat-mcp|yargi-mcp|erişimi bulunmadığından", govde, re.I):
        hatalar.append(f"{ad}: gövdede kalıp doğrulama uyarısı var — teyit durumu yalnız frontmatter `guncellik_teyidi:` alanına yazılır")
    if re.search(r"TASLAK_TEYIT_BEKLIYOR|dogrulama_durumu\s*:", govde):
        hatalar.append(f"{ad}: gövdede eski/bayat statü satırı var (TASLAK_TEYIT_BEKLIYOR / dogrulama_durumu) — statü yalnız frontmatter `durum:`")
    ters = len(re.findall(r"^\|\s*[—–]\s*\|\s*[—–]\s*\|\s*$", govde, re.M))
    if ters:
        hatalar.append(f"{ad}: {ters} adet '| — | — |' ayraçlı ters çevrilmiş tablo — tabloyu normal satır/sütun düzeninde yaz (sütun sınırı yok, telefonda kart görünümü otomatik)")
    hedge = len(re.findall(r"[Kk]aynak paket(?:e göre|te|teki|in)", govde))
    if hedge > 4:
        uyarilar.append(f"{ad}: {hedge} kez 'kaynak pakete göre/pakette' kalıbı — kuralı doğrudan yaz, aktarım olduğunu tekrar tekrar söyleme")
    if re.search(r"kurulmuş metin", govde):
        uyarilar.append(f"{ad}: SORU 'kurulmuş metin' — özgün soru KAYNAK (01_ham) dosyasında varsa oradan birebir alınmalı")
    isaret = govde.count("⚠")
    if isaret:
        uyarilar.append(f"{ad}: {isaret} adet ⚠ işareti — denetçinin özellikle bakacağı yerler")


MIKRO_SORU_RE = re.compile(r"^\s*(?:\*\*)?Soru\s*\d+\s*[:.)]", re.M | re.I)


def tekrar_karti_sayisi(govde: str) -> int:
    """'SRS / Tekrar kart' başlıklı bölümlerdeki tablo satırlarını sayar (başlık ve ayraç hariç)."""
    sayi, aktif = 0, False
    for satir in govde.splitlines():
        if re.match(r"^#{1,6}\s", satir):
            aktif = bool(re.search(r"SRS|TEKRAR KART|FLASH|KART", sade(satir)))
            continue
        if aktif and satir.startswith("|") and not re.match(r"^\|[\s:|-]+\|?\s*$", satir):
            sayi += 1
    return max(0, sayi - 1) if sayi else 0  # ilk satır tablo başlığı


def yeni_kaynak_alintilari(govde: str) -> list[str]:
    """Yeni dosyada 'Kaynak cevap / komisyon' başlıklı bölümlerdeki > satırları."""
    satirlar = []
    for satir in kaynak_bolumu_satirlari(govde):
        t = bosluk_normalize(satir.lstrip(">").strip())
        if len(t) > 25:
            satirlar.append(t)
    return satirlar


def karsilastir(eski: Path, yeniler: list[Path], hatalar: list, uyarilar: list,
                kaynaklar: list[Path] | None = None) -> dict:
    _, eski_govde = oku(eski)
    kaynak_metin = "\n".join(oku(k)[1] for k in (kaynaklar or []))
    izinli_govde = eski_govde + "\n" + kaynak_metin
    yeni_onler, yeni_govdeler = zip(*(oku(y) for y in yeniler))
    yeni_metin = "\n".join(yeni_govdeler)
    cikarilan = set(); izinli_atif = set()
    for on in yeni_onler:
        cikarilan |= {bosluk_normalize(x).split(" ")[0] for x in liste(on, "cikarilanlar")}
        izinli_atif |= {bosluk_normalize(x).split(" —")[0].split(" -")[0] for x in liste(on, "yeni_atiflar")}

    # 1) madde atıfları
    eski_m, yeni_m = madde_atiflari(eski_govde), madde_atiflari(yeni_metin)
    for a in sorted(yeni_m - madde_atiflari(izinli_govde)):
        if not any(a.startswith(sade(z).replace("C", "C")) or a == z for z in izinli_atif):
            hatalar.append(f"YENİ MADDE ATFI eski pakette/KAYNAK'ta yok: `{a}` — kaynağını göster ya da `yeni_atiflar:` alanına gerekçesiyle yaz")
    for a in sorted(eski_m - yeni_m):
        if a.split(" ")[-1] not in cikarilan and a not in cikarilan:
            uyarilar.append(f"Eski madde atfı yenide geçmiyor: `{a}`")

    # 2) özelge atıfları
    eski_o, yeni_o = ozelge_atiflari(eski_govde), ozelge_atiflari(yeni_metin)
    for o in sorted(yeni_o - ozelge_atiflari(izinli_govde)):
        hatalar.append(f"YENİ ÖZELGE ATFI eski pakette/KAYNAK'ta yok: `{o}`")
    for o in sorted(eski_o - yeni_o):
        hatalar.append(f"Özelge atfı kayboldu: `{o}` (özelge listesi için korunmalı)")

    # 3) kaynak cevap birebirliği
    yeni_norm = bosluk_normalize(yeni_metin.replace(">", " "))
    for i, blok in enumerate(kaynak_alintilari(eski_govde), 1):
        satirlar = [bosluk_normalize(s) for s in blok.splitlines() if len(bosluk_normalize(s)) > 25]
        eksik = [s for s in satirlar if s not in yeni_norm]
        if eksik:
            hatalar.append(f"Kaynak cevap #{i} birebir korunmamış: {len(eksik)}/{len(satirlar)} satır bulunamadı; ilk: «{eksik[0][:90]}»")

    # 3b) yenideki komisyon alıntıları eski pakette ya da KAYNAK'ta birebir var mı?
    izinli_norm = bosluk_normalize(izinli_govde.replace(">", " "))
    uydurma = [t for t in yeni_kaynak_alintilari(yeni_metin) if t not in izinli_norm]
    if uydurma:
        hatalar.append(f"Yenideki kaynak/komisyon alıntısının {len(uydurma)} satırı eski pakette ve KAYNAK'ta birebir yok; ilk: «{uydurma[0][:90]}»")

    # 3c) mikro sorular ve tekrar kartları kaybolmasın
    cikarilan_metin = " ".join(cikarilan).lower()
    eski_soru, yeni_soru = len(MIKRO_SORU_RE.findall(eski_govde)), len(MIKRO_SORU_RE.findall(yeni_metin))
    if yeni_soru < eski_soru and "mikro" not in cikarilan_metin:
        hatalar.append(f"Mikro sorular kayboldu: eskide {eski_soru}, yenide {yeni_soru} — 'Soru N:' biçiminde SORU bölümüne, cevapları CEVAP bölümüne taşı")
    eski_kart, yeni_kart = tekrar_karti_sayisi(eski_govde), tekrar_karti_sayisi(yeni_metin)
    if yeni_kart < eski_kart and "kart" not in cikarilan_metin:
        hatalar.append(f"Tekrar kartları kayboldu: eskide {eski_kart}, yenide {yeni_kart} — 'Tekrar kartları' başlıklı | Ön | Arka | tablosu olarak koru")

    # 4) sayılar ve tarihler
    eski_s, yeni_s = sayilar(eski_govde), sayilar(yeni_metin)
    kayip = sorted(x for x in eski_s - yeni_s if x not in cikarilan)
    yeni_eklenen = sorted(yeni_s - sayilar(izinli_govde))
    if kayip:
        uyarilar.append(f"Eskide olup yenide geçmeyen {len(kayip)} sayı/tarih/oran: {', '.join(kayip[:40])}" + (" …" if len(kayip) > 40 else ""))
    if yeni_eklenen:
        uyarilar.append(f"Yenide olup eskide olmayan {len(yeni_eklenen)} sayı/tarih/oran (yeni hesap ise verify.py'de olmalı): {', '.join(yeni_eklenen[:40])}" + (" …" if len(yeni_eklenen) > 40 else ""))

    return {"eski_madde": len(eski_m), "yeni_madde": len(yeni_m), "eski_ozelge": len(eski_o),
            "eski_sayi": len(eski_s), "kayip_sayi": len(kayip), "yeni_sayi": len(yeni_eklenen),
            "mikro_soru": f"{eski_soru}->{yeni_soru}", "tekrar_karti": f"{eski_kart}->{yeni_kart}"}


# ------------------------------------------------------------------------- ana

def main() -> int:
    ap = argparse.ArgumentParser(description="StudyPack biçim ve koruma denetimi")
    ap.add_argument("kip", choices=["bicim", "karsilastir"])
    ap.add_argument("dosyalar", nargs="+")
    ap.add_argument("--rapor")
    ap.add_argument("--kaynak", nargs="*", default=[], help="KAYNAK (01_ham) sınav dosyaları: soru ve komisyon cevabı buradan birebir alınabilir")
    a = ap.parse_args()

    hatalar: list[str] = []
    uyarilar: list[str] = []
    ozet = {}
    yollar = [Path(d) for d in a.dosyalar]
    if a.kip == "bicim":
        for y in yollar:
            bicim_denetle(y, hatalar, uyarilar)
    else:
        if len(yollar) < 2:
            sys.exit("karsilastir: ESKI.md ve en az bir YENI.md gerekir")
        for y in yollar[1:]:
            bicim_denetle(y, hatalar, uyarilar)
        ozet = karsilastir(yollar[0], yollar[1:], hatalar, uyarilar, [Path(k) for k in a.kaynak])

    satirlar = [f"# Denetim raporu — {a.kip}", "", "Dosyalar: " + ", ".join(y.name for y in yollar), ""]
    if ozet:
        satirlar += ["Özet: " + " · ".join(f"{k}={v}" for k, v in ozet.items()), ""]
    satirlar += [f"## HATA ({len(hatalar)})", *(f"- {h}" for h in hatalar or ["yok"]), "",
                 f"## UYARI ({len(uyarilar)})", *(f"- {u}" for u in uyarilar or ["yok"]), "",
                 f"SONUÇ: {'GEÇMEDİ' if hatalar else 'GEÇTİ'}"]
    rapor = "\n".join(satirlar)
    print(rapor)
    if a.rapor:
        Path(a.rapor).write_text(rapor + "\n", encoding="utf-8")
    return 1 if hatalar else 0


if __name__ == "__main__":
    raise SystemExit(main())
