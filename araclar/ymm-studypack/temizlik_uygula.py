#!/usr/bin/env python3
"""
temizlik_uygula.py — ChatGPT'nin hazırladığı temizlik çıktısını kasaya UYGULAYAN yerel script.
ChatGPT'nin "geçti" demesine güvenmez: her yeni paketi paket_denetle.py ile burada
yeniden denetler; geçmeyeni kasaya koymaz, eskisini de silmez.

Üç komut (Windows'ta PowerShell / cmd'de, araçların olduğu klasörde):

  1) Yedek + ChatGPT girdisi (kasaya dokunmaz):
     python temizlik_uygula.py yedek "G:\\Drive'ım\\HcC Kasa Obsidian\\40-YMM-Sinav" "G:\\Drive'ım\\HcC Kasa Arsiv"
       → HcC Kasa Arsiv\\40-YMM-Sinav_TEMIZLIK_ONCESI_<tarih>.zip + .sha256
       Bu ZIP hem tek yedektir hem de ChatGPT'ye yükleyeceğin dosyadır.

  2) Prova (hiçbir şey değişmez, ne yapılacağını listeler):
     python temizlik_uygula.py uygula CHATGPT_CIKTI.zip "<40-YMM-Sinav yolu>" --yedek "<yedek .zip yolu>"

  3) Pilot (G1) için: yeni dosyaları yaz ama hiçbir şey silme → sona --silme-yok ekle.

  4) Gerçek uygulama:
     python temizlik_uygula.py uygula CHATGPT_CIKTI.zip "<40-YMM-Sinav yolu>" --yedek "<yedek .zip yolu>" --gercek

ChatGPT çıktı ZIP'inin beklenen yapısı (görev emrinde ChatGPT'ye aynen verildi):
  ENVANTER_ONAYLI.csv   yol,tur,paket_id,boyut,durum_eski,oneri,gerekce   (yol = 40-YMM-Sinav'a göre göreli)
  YENI_DOSYALAR.csv     paket_id,yeni_yol,eski_yol                          (göreli yollar)
  yeni/<yeni_yol>       yeni paket dosyaları
  TEMIZLIK_RAPORU.md

Güvenlik kuralları (kodda sabit, ChatGPT değiştiremez):
  * tur = KAYNAK olan satır asla silinmez.
  * tur = PAKET olan eski dosya yalnız o paketin yeni dosyaları burada denetimden GEÇİP
    kasaya yazıldıysa (veya önceki bir çalıştırmada yazılmışsa) silinir.
  * --gercek için --yedek ZIP'i var olmalı ve .sha256 dosyasıyla eşleşmeli.
  * Var olan bir dosyanın üzerine yazılmaz (aynı içerikse atlanır).
  * Silme = işletim sistemi silmesi; Google Drive masaüstü uygulaması bunu Drive Çöp Kutusu'na
    taşır (30 gün geri alınabilir). İlk gerçek çalıştırmadan sonra Drive çöpünü bir kez kontrol et.
Günlük, yedek ZIP'in yanına yazılır (kasaya değil).
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

BURASI = Path(__file__).resolve().parent
sys.path.insert(0, str(BURASI))
import paket_denetle  # noqa: E402

SILINEBILIR_TURLER = {"KOPYA", "SISTEM", "SİSTEM", "DENEY", "PAKET"}


def sha256(yol: Path) -> str:
    h = hashlib.sha256()
    with open(yol, "rb") as f:
        for parca in iter(lambda: f.read(1 << 20), b""):
            h.update(parca)
    return h.hexdigest()


# ---------------------------------------------------------------------- yedek

def yedek(kaynak: Path, hedef_klasor: Path) -> int:
    if not kaynak.is_dir():
        sys.exit(f"Klasör yok: {kaynak}")
    hedef_klasor.mkdir(parents=True, exist_ok=True)
    zip_yol = hedef_klasor / f"{kaynak.name}_TEMIZLIK_ONCESI_{dt.date.today():%Y-%m-%d}.zip"
    if zip_yol.exists():
        sys.exit(f"Zaten var, üzerine yazmıyorum: {zip_yol}")
    sayi = 0
    with zipfile.ZipFile(zip_yol, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(kaynak.rglob("*")):
            if p.is_file() and ".smart-env" not in p.parts:
                z.write(p, p.relative_to(kaynak.parent))
                sayi += 1
    ozet = sha256(zip_yol)
    zip_yol.with_suffix(".zip.sha256").write_text(f"{ozet}  {zip_yol.name}\n", encoding="utf-8")
    print(f"✓ {sayi} dosya → {zip_yol}\n  SHA-256: {ozet}\n  Bu ZIP'i ChatGPT'ye yükle.")
    return 0


# --------------------------------------------------------------------- uygula

def csv_oku(z: zipfile.ZipFile, ad: str) -> list[dict]:
    try:
        ham = z.read(ad).decode("utf-8-sig")
    except KeyError:
        sys.exit(f"ChatGPT çıktısında {ad} yok.")
    return list(csv.DictReader(io.StringIO(ham)))


def norm(s: str) -> str:
    return (s or "").strip().upper().replace("İ", "I")


def guvenli_yol(kok: Path, goreli: str) -> Path:
    hedef = (kok / goreli.replace("\\", "/").lstrip("/")).resolve()
    if kok.resolve() not in hedef.parents and hedef != kok.resolve():
        raise ValueError(f"Kasa dışına çıkan yol reddedildi: {goreli}")
    return hedef


def uygula(cikti_zip: Path, kasa: Path, yedek_zip: Path | None, gercek: bool, silme_yok: bool = False) -> int:
    kasa = kasa.resolve()
    if gercek:
        if not yedek_zip or not yedek_zip.exists():
            sys.exit("--gercek için var olan bir --yedek ZIP'i gerekli.")
        sha_dosya = yedek_zip.with_suffix(".zip.sha256")
        if not sha_dosya.exists() or sha_dosya.read_text().split()[0] != sha256(yedek_zip):
            sys.exit("Yedek ZIP'in SHA-256'sı .sha256 dosyasıyla eşleşmiyor — durdum.")
    gunluk: list[str] = [f"# Temizlik uygulama günlüğü — {dt.datetime.now():%Y-%m-%d %H:%M}",
                         f"Kip: {'GERÇEK' if gercek else 'PROVA (hiçbir şey değişmedi)'}", ""]

    with zipfile.ZipFile(cikti_zip) as z, tempfile.TemporaryDirectory() as gecici:
        envanter = csv_oku(z, "ENVANTER_ONAYLI.csv")
        yeniler = csv_oku(z, "YENI_DOSYALAR.csv")
        z.extractall(gecici)
        cikti_kok = Path(gecici)

        # 1) Yeni paketleri burada yeniden denetle
        paketler: dict[str, list[dict]] = {}
        for r in yeniler:
            paketler.setdefault(r["paket_id"].strip(), []).append(r)
        gecen_paketler: set[str] = set()
        gunluk += ["## 1. Yeni paketler — yerel yeniden denetim", ""]
        for pid, satirlar in sorted(paketler.items()):
            eski_yollar = {s["eski_yol"].strip() for s in satirlar if s.get("eski_yol", "").strip()}
            yeni_dosyalar = [cikti_kok / "yeni" / s["yeni_yol"].replace("\\", "/") for s in satirlar]
            eksik = [str(y) for y in yeni_dosyalar if not y.exists()]
            if eksik:
                gunluk.append(f"- ✗ {pid}: ZIP'te dosya yok: {eksik}")
                continue
            hatalar: list[str] = []
            uyarilar: list[str] = []
            if pid.upper() == "NAV":  # gezinme sayfası: paket değil, yalnız kökteki 00-BASLA.md'ye izin var
                if [s["yeni_yol"].strip() for s in satirlar] != ["00-BASLA.md"]:
                    gunluk.append(f"- ✗ NAV: yalnız '00-BASLA.md' kabul edilir")
                    continue
                gecen_paketler.add(pid)
                gunluk.append("- ✓ NAV: 00-BASLA.md (gezinme sayfası, paket denetimi uygulanmaz)")
                continue
            for y in yeni_dosyalar:
                paket_denetle.bicim_denetle(y, hatalar, uyarilar)
            for e in eski_yollar:  # eski dosya ChatGPT'den değil, KASADAN okunur
                eski = guvenli_yol(kasa, e)
                if not eski.exists():
                    hatalar.append(f"eski dosya kasada yok: {e}")
                    continue
                paket_denetle.karsilastir(eski, yeni_dosyalar, hatalar, uyarilar)
            if hatalar:
                gunluk.append(f"- ✗ {pid}: GEÇMEDİ — kasaya yazılmayacak, eskisi silinmeyecek")
                gunluk += [f"    - {h}" for h in hatalar]
                continue
            gecen_paketler.add(pid)
            gunluk.append(f"- ✓ {pid}: geçti ({len(uyarilar)} uyarı)")

        # 2) Geçenleri kasaya yaz
        gunluk += ["", "## 2. Kasaya yazılacak dosyalar", ""]
        yazilan = 0
        for r in yeniler:
            pid = r["paket_id"].strip()
            if pid not in gecen_paketler:
                continue
            kaynak = cikti_kok / "yeni" / r["yeni_yol"].replace("\\", "/")
            hedef = guvenli_yol(kasa, r["yeni_yol"])
            if hedef.exists():
                if hedef.read_bytes() == kaynak.read_bytes():
                    gunluk.append(f"- = {r['yeni_yol']} (zaten aynı)")
                    continue
                gunluk.append(f"- ✗ {r['yeni_yol']} kasada FARKLI içerikle var — üzerine yazmıyorum; {pid} durduruldu")
                gecen_paketler.discard(pid)
                continue
            gunluk.append(f"- + {r['yeni_yol']}")
            yazilan += 1
            if gercek:
                hedef.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(kaynak, hedef)

        # 3) Silme
        yazilmis_paketler = {r["paket_id"].strip() for r in yeniler
                             if guvenli_yol(kasa, r["yeni_yol"]).exists()} | gecen_paketler
        gunluk += ["", "## 3. Silinecekler" + (" — ATLANDI (--silme-yok)" if silme_yok else ""), ""]
        silinen = atlanan = 0
        for r in ([] if silme_yok else envanter):
            if norm(r.get("oneri")) != "SIL":
                continue
            tur, yol, pid = norm(r.get("tur")), r["yol"].strip(), (r.get("paket_id") or "").strip()
            if tur == "KAYNAK" or tur not in {norm(t) for t in SILINEBILIR_TURLER}:
                gunluk.append(f"- ⛔ {yol} — tür {tur or '?'} silinemez, atlandı")
                atlanan += 1
                continue
            if tur == "PAKET" and pid not in yazilmis_paketler:
                gunluk.append(f"- … {yol} — {pid} yeni sürümü kasada değil, eski korunuyor")
                atlanan += 1
                continue
            hedef = guvenli_yol(kasa, yol)
            if not hedef.exists():
                continue
            gunluk.append(f"- − {yol}")
            silinen += 1
            if gercek:
                if hedef.is_dir():
                    shutil.rmtree(hedef)
                else:
                    hedef.unlink()
        if gercek:  # boş klasörleri temizle
            for d in sorted((p for p in kasa.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
                if not any(d.iterdir()):
                    d.rmdir()

        rapor = cikti_kok / "TEMIZLIK_RAPORU.md"
        gunluk += ["", f"Özet: {len(gecen_paketler)}/{len(paketler)} paket geçti · {yazilan} dosya yazılacak · "
                       f"{silinen} öğe silinecek · {atlanan} öğe korundu",
                   "", "ChatGPT raporu: " + ("TEMIZLIK_RAPORU.md ZIP içinde" if rapor.exists() else "yok")]

    # 4) Okunur çıktılar
    if gercek:
        sonuc = subprocess.run([sys.executable, str(BURASI / "okunur_yap.py"), str(kasa)],
                               capture_output=True, text=True)
        gunluk += ["", "## 4. Okunur çıktılar", "```", sonuc.stdout.strip() or sonuc.stderr.strip(), "```"]

    metin = "\n".join(gunluk) + "\n"
    print(metin)
    gunluk_yeri = (yedek_zip.parent if yedek_zip else cikti_zip.parent)
    ad = f"TEMIZLIK_UYGULAMA_{'GERCEK' if gercek else 'PROVA'}_{dt.datetime.now():%Y%m%d_%H%M}.md"
    (gunluk_yeri / ad).write_text(metin, encoding="utf-8")
    print(f"Günlük: {gunluk_yeri / ad}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="ChatGPT temizlik çıktısını kasaya uygula")
    alt = ap.add_subparsers(dest="komut", required=True)
    y = alt.add_parser("yedek"); y.add_argument("kaynak"); y.add_argument("hedef_klasor")
    u = alt.add_parser("uygula"); u.add_argument("cikti_zip"); u.add_argument("kasa")
    u.add_argument("--yedek"); u.add_argument("--gercek", action="store_true")
    u.add_argument("--silme-yok", action="store_true", help="yalnız yeni dosyaları yaz, hiçbir şey silme (pilot için)")
    a = ap.parse_args()
    if a.komut == "yedek":
        return yedek(Path(a.kaynak), Path(a.hedef_klasor))
    return uygula(Path(a.cikti_zip), Path(a.kasa), Path(a.yedek) if a.yedek else None, a.gercek, a.silme_yok)


if __name__ == "__main__":
    raise SystemExit(main())
