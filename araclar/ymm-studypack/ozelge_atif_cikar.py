#!/usr/bin/env python3
"""
ozelge_atif_cikar.py — Komisyon cevaplarında (ham sınav metinleri) ve StudyPack'lerde
geçen özelge atıflarını tek listeye çıkarır. Özelge projesinin 1. adımı:
"sınavın kendisi hangi özelgeleri işaret ediyor?"

Kullanım:
  python ozelge_atif_cikar.py ymm-korpus/01_ham  [başka klasör/dosya ...]  --cikti ozelge_atiflari.csv

Çıktı CSV sütunları:
  tarih, sayi_ham, sayi_sade, kaynak_dosya, ders, donem, satir, baglam
Aynı (tarih, sayı) birden çok yerde geçiyorsa her geçiş ayrı satırdır; özet sayım ekrana basılır.
Sınav dönemi ve ders, dosya yolundan tahmin edilir (örn. 01_ham/revizyon/2024_1.md → revizyon, 2024/1).
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

TARIH = r"(\d{1,2}[./]\d{1,2}[./]\d{4})"
# 1) "05.07.2010 tarih ve ..... KVK-8-1-470 sayılı"   2) "... 1234 sayılı ve 05.07.2010 tarihli"
DESEN_1 = re.compile(TARIH + r"\s*tarih(?:li)?\s*(?:ve|,)?\s*(.{1,90}?)\s*sayılı", re.I)
DESEN_2 = re.compile(r"([\w\[\]().\-/]{3,60})\s*sayılı\s*(?:ve|,)\s*" + TARIH + r"\s*tarihli", re.I)
OZELGE_IPUCU = re.compile(r"özelge|ozelge|muktezа|mukteza|görüş yazısı", re.I)


def sayi_sadelestir(ham: str) -> str:
    s = re.sub(r"[.…]{2,}|…", " ", ham)          # '.....' ve '…' boşluklarını at
    s = re.sub(r"\b(tarih|ve|sayılı|nolu|no)\b", " ", s, flags=re.I)
    s = re.sub(r"\s+", "", s).strip(" ,;:-")
    return s


def ders_donem(yol: Path) -> tuple[str, str]:
    parcalar = [p.lower() for p in yol.parts]
    ders = next((p for p in parcalar if p in {"revizyon", "vergiteknigi", "vergi-teknigi", "vergi_teknigi",
                                                "denetim", "spk", "dis-ticaret", "yonetim-muhasebesi"}), "")
    m = re.search(r"(20\d\d)[_/-](\d)", yol.stem) or re.search(r"(20\d\d)[_/-](\d)", str(yol))
    return ders, (f"{m.group(1)}/{m.group(2)}" if m else "")


def tara(dosya: Path) -> list[dict]:
    metin = dosya.read_text(encoding="utf-8", errors="replace")
    satirlar = metin.splitlines()
    ders, donem = ders_donem(dosya)
    bulunan = []
    for no, satir in enumerate(satirlar, 1):
        # komisyon metinlerinde atıf iki satıra bölünebilir → bir sonraki satırla birlikte bak
        pencere = satir + " " + (satirlar[no] if no < len(satirlar) else "")
        for desen, tarih_grubu, sayi_grubu in ((DESEN_1, 1, 2), (DESEN_2, 2, 1)):
            for m in desen.finditer(pencere):
                if m.start() >= len(satir):  # yalnız bir sonraki satırda başlayan eşleşme oraya ait
                    continue
                tarih = m.group(tarih_grubu).replace("/", ".")
                ham = m.group(sayi_grubu).strip()
                if re.search(r"Cumhurbaşkanı|Resm[iî] Gazete|Kanun|Karar", ham, re.I):
                    continue  # CBK / kanun atfı, özelge değil
                baglam = " ".join(satirlar[max(0, no - 3):no + 1])
                if not OZELGE_IPUCU.search(baglam + " " + " ".join(satirlar[no:no + 8])):
                    continue
                bulunan.append({"tarih": tarih, "sayi_ham": ham, "sayi_sade": sayi_sadelestir(ham),
                                "kaynak_dosya": str(dosya), "ders": ders, "donem": donem,
                                "satir": no, "baglam": re.sub(r"\s+", " ", satir.strip())[:200]})
    return bulunan


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("girdiler", nargs="+")
    ap.add_argument("--cikti", default="ozelge_atiflari.csv")
    a = ap.parse_args()
    dosyalar: list[Path] = []
    for g in a.girdiler:
        p = Path(g)
        dosyalar += sorted(p.rglob("*.md")) + sorted(p.rglob("*.txt")) if p.is_dir() else [p]
    kayitlar = [k for d in dosyalar for k in tara(d)]
    with open(a.cikti, "w", newline="", encoding="utf-8-sig") as f:  # utf-8-sig: Excel Türkçe karakteri doğru açar
        w = csv.DictWriter(f, fieldnames=["tarih", "sayi_ham", "sayi_sade", "kaynak_dosya", "ders", "donem", "satir", "baglam"])
        w.writeheader()
        w.writerows(kayitlar)
    tekil = Counter((k["tarih"], k["sayi_sade"]) for k in kayitlar)
    print(f"{len(dosyalar)} dosya tarandı · {len(kayitlar)} atıf · {len(tekil)} tekil özelge → {a.cikti}")
    for (t, s), n in tekil.most_common(10):
        print(f"  {n}×  {t}  {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
