---
kime: chatgpt
kimden: claude-opus-5-5 (Claude.ai / Cowork oturumu)
tarih: 2026-10-15
tur: gorev
durum: acik — Cihan G0 oturumunu açınca başlar
onceki: gorevler/2026-10-15-studypack-temizlik.md (Codex sürümü — bunun yerine geçti)
---

# StudyPack temizliği — ChatGPT sürümü

## A. İş bölümü (Cihan için)

| Kim | Ne yapar |
|---|---|
| **ChatGPT** (tek model, alt ajan / agent / deep research yok) | Envanter, sınıflandırma, paketleri yeni formata çevirme, denetimi kendi Python sandbox'ında çalıştırma, her oturum sonunda **tek bir çıktı ZIP'i** |
| **Bilgisayarındaki script** (`temizlik_uygula.py`) | Yedek ZIP; ChatGPT çıktısını **yeniden denetleyip** kasaya yazma; eskileri silme; okunur PDF/HTML üretme |
| **Claude** | G1 pilotunu ve kapanışı kontrol eder (az kota) |
| **Sen** | Kapılarda "devam"; pilot PDF'ini telefonda okumak |

ChatGPT kasaya ve Drive'a **yazmaz**. Drive bağlayıcısıyla Google Doc da oluşturmaz, çünkü kaçışlı/bozuk aynalar (`_arsiv_bozuk_kacisli_aynalar`) böyle oluşmuştu. Her şey ZIP olarak iner, kasaya yalnız script yazar. Script ChatGPT'nin "geçti" demesine bakmaz, denetimi kendisi yeniden koşar.

## B. Kurulum (bir kez, ~10 dk)

1. Araçları indir: `github.com/TheHcC/hcc-ajan-koprusu` → `araclar/ymm-studypack/` (5 dosya) → bir klasöre koy, ör. `claude-practice\ymm-araclar\`.
   Sonra bir kez: `pip install markdown-it-py pyyaml`
2. Yedek al (bu ZIP aynı zamanda ChatGPT'ye yükleyeceğin dosya):
   ```
   python temizlik_uygula.py yedek "<...>\HcC Kasa Obsidian\40-YMM-Sinav" "<...>\HcC Kasa Arsiv"
   ```
3. Özelge atıflarını çıkar (ChatGPT özel repoyu göremez, bunu yerelde yapıyoruz):
   ```
   python ozelge_atif_cikar.py "<...>\claude-practice\ymm-korpus\01_ham" --cikti ozelge_atiflari.csv
   ```
4. ChatGPT'de **"YMM Temizlik"** adlı bir Proje aç:
   - Proje talimatına aşağıdaki **C** bölümünü yapıştır.
   - Proje dosyalarına `paket_denetle.py`, `ozelge_atif_cikar.py` ve bu belgeyi ekle.
   - Modeli tek seç ve iş boyunca değiştirme: senin seçimin olan Luna/medium; pilot oturumunda bir üst düşünme seviyesi.
5. Her oturum = yeni sohbet. Oturum başında yükle:
   - yedek ZIP,
   - `paket_denetle.py`,
   - varsa bir önceki oturumun `TEMIZLIK_RAPORU.md`'si.

   Sandbox dosyaları sohbetler arasında kalmaz; sürekliliği rapor dosyası sağlar.

## C. Proje talimatı (ChatGPT Project → Instructions'a aynen yapıştır)

```
ROLE: You are the single worker on a file-migration job for Cihan's YMM exam study packs.
OUTPUT LANGUAGE: Write ALL files, reports, frontmatter values and chat messages in Turkish.

HARD RULES
1. Do all file work in Python (code interpreter). Unzip the uploaded snapshot and work on the
   files there. Never retype text from memory: read it from the files with Python.
2. The verbatim commission answer (the ">" blockquote under "Tam kaynak cevap" / "Kaynak cevap")
   must be COPIED WITH PYTHON from the old file into the new file, byte for byte. Never type it.
3. No new legal content. You restructure and shorten. Never add an article reference, rate, date,
   özelge or example that is not in the old pack. If you think the old pack is wrong, keep the
   statement and mark it "(⚠)" with one line explaining why. Do not "fix" law. Do not browse the web.
4. The judge is paket_denetle.py, not you. A pack is done only when
   `python paket_denetle.py karsilastir OLD.md NEW_*.md` exits 0. Never edit the checker.
5. Anti-loop: if the checker fails, ONE repair attempt. If it fails again, mark the pack BLOKE in
   the report with the checker output and move on. Never a third attempt, never a full rewrite.
6. No Google Docs, no writing to Drive or any connector. Deliver everything as ONE downloadable ZIP.
7. Do not use agent mode, deep research or sub-tasks. One model, this chat only.
8. Stop at the gate named in the session prompt. Do not start the next gate.

TARGET FORMAT (every pack)
Files: <ID>_CALISMA.md (≤15 KB) + optional <ID>_VAKA_<n>_<dönem>_<konu>.md (≤20 KB each, only real
exam questions, one question family per file). Reference style: VT_SP_05_CALISMA.md and
VT_SP_05_VAKA_1..4 inside the snapshot (Vergi Tekniği/StudyPack/).
Frontmatter keys exactly:
  id, aliases (old ID), ders, konu, durum (TASLAK|KONTROLLU|CALISILDI), kaynak (list of exam
  period-question IDs), tarih, uretici ("chatgpt/<model>-<effort>"), eski_dosya,
  cikarilanlar (deliberately dropped numbers/refs, 3-word reason each), yeni_atiflar (must stay []),
  calisma_kaydi ([] — Cihan fills).
CALISMA headings in this order: 1. Kapılar · 2. Ezber (≤12 sentences) · 3. Karar akışı · 4. Hesap
(if numeric) · 5. Güncel hukuk (source period vs today, date lock) · 6. Tuzaklar (≤10) · 7. SORU ·
8. CEVAP · 9. Parametre değişirse · 10. Kaynak (exam period; verbatim commission answer as ">"
blockquote unless it is in a VAKA file; official sources; özelge citations exactly as written).
Style: paragraphs ≤4 lines; tables ≤3 columns; "(Yorum)" = interpretation, "(⚠)" = unsure,
unmarked = law or commission. Missing original question text → label the SORU
"(kurulmuş metin — özgün soru dosyada yok)" and use only numbers that are in the commission answer.
Status: KONTROLLU only if the old pack was accepted (KABUL / RELEASED / "Cihan kabul etti") AND
the checker shows 0 HATA AND no "yenide olup eskide olmayan sayı" warning. Otherwise TASLAK.

OUTPUT ZIP STRUCTURE (always exactly this, file names exact)
  ENVANTER_ONAYLI.csv   columns: yol,tur,paket_id,boyut,durum_eski,oneri,gerekce
                        yol = path relative to the 40-YMM-Sinav folder
                        tur ∈ PAKET | KOPYA | SISTEM | DENEY | KAYNAK ; oneri ∈ DONUSTUR | SIL | TUT
  YENI_DOSYALAR.csv     columns: paket_id,yeni_yol,eski_yol   (relative paths; this session only)
  yeni/<yeni_yol>       the new pack files
  denetim/<ID>_DENETIM.md   checker output per pack
  TEMIZLIK_RAPORU.md    cumulative: previous report + this session's block
Classification: PAKET = a study pack's content · KOPYA = Google-Docs mirror, _arsiv*, 99-Arsiv,
older version of a pack, escape-corrupted mirror · SISTEM = protocols, handoffs, logs, authority
notes, dashboards, status cards, Cloud-Credit-Lab · DENEY = Muhakeme-Motoru, VT-VERGI-INCELEMESI,
BBN pilot, Konu Pilotları v2 · KAYNAK = raw exam question/answer sources and PDFs (never SIL).
```

## D. Oturum açılış mesajları (her biri yeni sohbet)

**G0 — Envanter** (yükle: yedek ZIP + paket_denetle.py)
```
Session G0. Unzip the snapshot. Inventory every file. Produce ENVANTER_ONAYLI.csv with your
oneri for each row, an empty YENI_DOSYALAR.csv (header only), and TEMIZLIK_RAPORU.md with: counts
per tur, every DENEY row listed for my decision, and the list of PAKET groups (old file → planned
new ID). Ask me about the DENEY rows, apply my answers, then give me the ZIP. Stop. Turkish output.
```
→ G0 ZIP'ini **uygulama**. Sadece rapordaki listeye göz at.

**G1 — Pilot** (yükle: yedek ZIP + paket_denetle.py + G0 TEMIZLIK_RAPORU.md + ENVANTER_ONAYLI.csv)
```
Session G1 (pilot). Convert exactly two packs: SP-VR-E-003 (Vergi-Revizyon) and VT-SP-01
(Vergi Tekniği). Use the higher reasoning effort. Run the checker for each, include its output,
give me the ZIP. Stop. Turkish output.
```
Sonra yerelde:
```
python temizlik_uygula.py uygula G1.zip "<40-YMM-Sinav>" --yedek "<yedek.zip>" --gercek --silme-yok
```
Pilot dosyaları kasaya yazılır, hiçbir şey silinmez. `_okuma/` altındaki PDF'i telefonda oku. Claude'a "G1 hazır" de; o, kasadaki yeni ve eski dosyaları karşılaştırır.

**PARTİ n** (G1 onaylanınca; her parti yeni sohbet; yükle: yedek ZIP + paket_denetle.py + son TEMIZLIK_RAPORU.md + ENVANTER_ONAYLI.csv)
```
Session PARTİ <n>. Convert the next packs from the report's PAKET list, at most 4 packs or
150 KB of old text, whichever comes first. Order: Vergi-Revizyon E-001…E-010 → VT-SP-02…04 →
VT-SP-05…08 (already new style: only frontmatter schema + Kaynak section, content untouched) →
Denetim packs → YM01, YM03, YM04. Checker per pack, anti-loop rule, then the ZIP. Stop. Turkish output.
```
Sonra yerelde önce prova, sonra gerçek:
```
python temizlik_uygula.py uygula PARTI_n.zip "<40-YMM-Sinav>" --yedek "<yedek.zip>"
python temizlik_uygula.py uygula PARTI_n.zip "<40-YMM-Sinav>" --yedek "<yedek.zip>" --gercek
```
Bir partide 2 veya daha fazla BLOKE varsa dur ve Claude'a göster.

**KAPANIŞ** (son parti bittikten sonra; yükle: son rapor + ENVANTER_ONAYLI.csv)
```
Session KAPANIŞ. Write 00-BASLA.md for the 40-YMM-Sinav root: "Bugün çalış" (Dataview: durum =
KONTROLLU and empty calisma_kaydi), "Tekrar" (packs with a wrong answer in calisma_kaydi), one link
per course. No hand-maintained status tables. Put it in yeni/ with a YENI_DOSYALAR.csv row
(paket_id=NAV, eski_yol empty), mark every remaining SISTEM row SIL, give me the ZIP. Turkish output.
```
Yerelde önce prova, sonra `--gercek` çalıştır. Script `NAV` satırını paket denetiminden muaf tutar ama yalnız kökteki `00-BASLA.md`'ye izin verir; kalan SİSTEM dosyalarını da siler. Ardından Claude'a "kapanış" de; o, rastgele %20'yi yeniden denetler.

## E. Doğrulanabilir kabul ölçütü
- Kasada yalnız şunlar kalır: `00-BASLA.md`, ders klasörlerinde `<ID>_CALISMA/VAKA` dosyaları, `_okuma/`, KAYNAK dosyaları.
- Her paket için yerel `TEMIZLIK_UYGULAMA_GERCEK_*.md` günlüğünde "✓ geçti" satırı bulunur.
- Yedek ZIP ve `.sha256` dosyası `HcC Kasa Arsiv/` altındadır.

## F. Bilinen sınırlar (Claude)
- ChatGPT sandbox'ında `yaml` kurulu olmayabilir. Checker bu durumda kendi basit okuyucusuna düşer, sonuç değişmez.
- Checker madde, özelge, sayı ve alıntı değişikliğini yakalar; bir cümlenin anlamındaki kaymayı yakalamaz. Pilot kapısı bunun için var.
- Sandbox dosyaları sohbet bitince kaybolur. Her oturumun ZIP'ini indirmeyi unutma.
- "Luna/medium" senin seçimin; ChatGPT'deki tam model adını ve sandbox süre sınırını doğrulamadım.
