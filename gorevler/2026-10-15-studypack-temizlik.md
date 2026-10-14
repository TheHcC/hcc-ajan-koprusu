---
kime: codex
kimden: claude-opus-5-5 (Claude.ai / Cowork oturumu)
tarih: 2026-10-15
tur: gorev
durum: acik — Cihan onayı ile başlar
---

> **Cihan için 4 satır özet:** Codex tek işçi, tek model, alt ajan yok. Önce envanter ve tek
> bir yedek ZIP çıkarır, sonra **durur**. Senin "tamam"ınla 2 pilot paketi yeni formata çevirir,
> sonra yine **durur**. Claude pilotları kontrol eder. Ardından kalan paketleri 4'erli partiler
> hâlinde çevirir, eski sürümleri ve kopyaları kasadan siler. Her adımı model değil script
> (`paket_denetle.py`) doğrular. Okunacak her paket `_okuma/` klasörüne A5 PDF + HTML olarak düşer.

# DIRECTIVE — YMM StudyPack cleanup and migration to one format

**Output language: ALL files, reports, frontmatter values, log entries and messages you produce
must be in Turkish.** This directive is written in English for precision only.

## 0. Ground rules (read twice)

1. **One worker, one model.** You (Codex) do everything yourself with the single model Cihan
   selected for this job (suggested: GPT-6 Luna, effort `medium`; use `high` only for the two
   pilot packs). **Do not spawn sub-agents, do not delegate to other models, do not switch model
   mid-run.**
2. **No new legal content.** You restructure and shorten existing packs. You never add a legal
   claim, article reference, rate, date, özelge or example that is not already in the old pack.
   If you believe the old pack is wrong, **keep the statement and mark it `(⚠)`** with one line
   saying why. Do not "fix" law.
3. **The script is the judge, not you.** A pack is done only when
   `python paket_denetle.py karsilastir OLD.md NEW_*.md` exits 0. Never edit the checker.
4. **Anti-loop rule.** If the checker fails, you get **one** repair attempt. If it fails again,
   mark the pack `BLOKE` in the batch report with the checker output, leave its old files
   untouched, and move to the next pack. Never retry a third time. Never rewrite a pack from
   scratch to "make it pass".
5. **Stop gates are hard stops.** At a STOP, write the report, post it (see §6) and end the
   session. Do not continue until Cihan writes "devam" for that gate.
6. Bridge rules apply (github.com/TheHcC/hcc-ajan-koprusu README, 7 anti-hallucination rules).
   No taxpayer data anywhere.

## 1. Tools (bridge repo `araclar/ymm-studypack/`; copy them to `ymm-korpus/tools/` — byte-exact, do not retype)

| File | Purpose |
|---|---|
| `paket_denetle.py` | `bicim` = format check of a new pack; `karsilastir` = old→new preservation check (article refs, özelge refs, verbatim commission answer, numbers, dates, size limits, Google-Docs escape corruption) |
| `okunur_yap.py` | Renders packs to readable A5 PDF + responsive HTML in a sibling `_okuma/` folder. Answers are collapsed in HTML and start on a new page in the PDF. |
| `ozelge_atif_cikar.py` | Extracts every özelge citation (date + number) from raw commission answers into a CSV |
| `obsidian-okunur-tablolar.css` | Obsidian CSS snippet for wrapped tables |

Setup: `pip install markdown-it-py pyyaml`. PDF uses Edge/Chrome automatically on Windows.

## 2. The one format (applies to every pack)

Per pack: `<ID>_CALISMA.md` (≤ 15 KB) + optional `<ID>_VAKA_<n>_<dönem>_<konu>.md` (≤ 20 KB each,
**only** for real exam questions; one question family per file). Model: the existing
`VT_SP_05_CALISMA.md` + `VT_SP_05_VAKA_1..4` are the reference style.

Frontmatter (exact keys):

```yaml
id: VR-E-003            # ders kısaltması + numara; eski ID alias olarak kalır
aliases: [SP-VR-E-003]
ders: Vergi Revizyonu
konu: <tek satır>
durum: TASLAK           # yalnız TASLAK | KONTROLLU | CALISILDI
kaynak: [RV-2024/1-S5]  # sınav dönemi-soru kimlikleri
tarih: 2026-10-15
uretici: codex/<model>-<effort>
eski_dosya: <old file name>          # migration trace, nothing else
cikarilanlar: []        # numbers/refs you deliberately dropped, each with 3-word reason
yeni_atiflar: []        # must stay empty (rule 0.2); checker fails otherwise
calisma_kaydi: []       # Cihan fills: "2026-10-20 · §SORU çözüldü · doğru/yanlış"
```

CALISMA sections, in this order (headings must contain these words so the tools find them):
`1. Kapılar` (which article decides, one sentence each) · `2. Ezber` (≤ 12 sentences) ·
`3. Karar akışı` · `4. Hesap` (if numeric) · `5. Güncel hukuk` (source-period rule vs. today, with
date lock) · `6. Tuzaklar` (≤ 10) · `7. SORU` · `8. CEVAP` · `9. Parametre değişirse` ·
`10. Kaynak` (exam period, **verbatim commission answer in a `>` blockquote** if it is not in a
VAKA file, official sources, özelge citations exactly as in the commission answer).

Writing rules: paragraphs ≤ 4 lines; tables **≤ 3 columns** (phone width); no section numbers
inside sentences; `(Yorum)` = our interpretation, `(⚠)` = unsure; unmarked = law or commission.
If the original question text is missing, the SORU is labelled `(kurulmuş metin — özgün soru
dosyada yok)`; never invent numbers that are not in the commission answer.

**Status carry-over:** a converted pack gets `KONTROLLU` only if the old pack was accepted
(KABUL / RELEASED / "Cihan kabul etti") **and** the checker reports 0 HATA and 0 "yenide olup
eskide olmayan sayı" warnings. Everything else becomes `TASLAK`. `CALISILDI` is set only by Cihan.

## 3. Phases

### FAZ 0 — Inventory + one snapshot (no edits)
1. Inventory every file under Drive `HcC Kasa Obsidian/40-YMM-Sinav/` (all subfolders) and
   `ymm-korpus/12_study_pack/`. Write `ENVANTER.csv`: `yol, tür, paket_id, boyut, durum_eski,
   öneri, gerekçe`. `tür` ∈ PAKET (a study pack's content) · KOPYA (Google Docs mirror,
   `_arsiv*`, `99-Arsiv`, older version of a pack, escape-corrupted mirror) · SİSTEM (protocols,
   handoffs, logs, authority notes, dashboards, Cloud-Credit-Lab, metadata cards) ·
   DENEY (Muhakeme-Motoru, VT-VERGI-INCELEMESI, BBN pilot, Konu Pilotları v2) · KAYNAK (raw exam
   PDFs/question-answer sources — **never deleted**). `öneri` ∈ DÖNÜŞTÜR / SİL / TUT.
2. Create **one** snapshot ZIP of `40-YMM-Sinav/` and put it in Drive `HcC Kasa Arsiv/`
   as `40-YMM-Sinav_TEMIZLIK_ONCESI_2026-10-15.zip`, with its SHA-256 in the report. This is the
   only backup; it lives outside the vault.
3. Run `ozelge_atif_cikar.py ymm-korpus/01_ham --cikti ozelge_atiflari.csv`.
4. **STOP — gate G0.** Report: counts per `tür`, the DENEY rows listed one by one (Cihan decides
   keep/delete), the snapshot hash, the özelge count.

### FAZ 1 — Pilot (2 packs, effort high)
Convert `SP-VR-E-003` (Revizyon, long format) and `VT-SP-01` (Vergi Tekniği, long format).
For each: write new files → `paket_denetle.py karsilastir` → `okunur_yap.py` → save checker
report as `<ID>_DENETIM.md` next to the pack. Do **not** delete anything yet.
**STOP — gate G1.** Claude reviews the two packs; Cihan reads one PDF on the phone.

### FAZ 2 — Batches of 4
Order: Vergi-Revizyon E-001…E-010 → VT-SP-02…04 → VT-SP-05…08 (already new style: only
frontmatter schema + `Kaynak` section; content untouched) → Denetim packs → YM01, YM03, YM04.
Per pack the same loop as the pilot, with rule 0.4. After each batch append one block to
`TEMIZLIK_RAPORU.md`: pack, checker result, status given, warnings count, BLOKE reason.
No stop between batches unless a batch has ≥ 2 BLOKE packs → then **STOP — gate G2**.

### FAZ 3 — Delete old material
Only for packs whose new version passed: delete the old long file, its Google Docs mirror and
any archived variants. Delete all rows marked SİL in the approved inventory, plus empty
folders. Use Drive trash (recoverable 30 days); in git, delete normally (history keeps them).
Never delete KAYNAK rows or the snapshot ZIP. Then rebuild navigation:
- `40-YMM-Sinav/00-BASLA.md` — one page: "Bugün çalış" (Dataview: `durum = KONTROLLU` and no
  `calisma_kaydi`), "Tekrar" (packs with a wrong answer in `calisma_kaydi`), per-course links.
- One registry generated by Dataview from frontmatter. **No hand-maintained status tables
  anywhere** (StudyPack Kaydı, Durum-Verileri cards, authority notes go).
- Run `okunur_yap.py 40-YMM-Sinav` (renders KONTROLLU packs into each course's `_okuma/`).

### FAZ 4 — Close
Update `DURUM.md` + `GUNLUK.md` in the bridge repo (git). Post the final report (§6).
**STOP — gate G3** (Claude final check: re-runs the checker on a random 20 % sample).

## 4. Doğrulanabilir kabul ölçütü
- Every converted pack: `paket_denetle.py karsilastir` exit 0, report file present.
- `40-YMM-Sinav/` contains only: `00-BASLA.md`, course folders with `<ID>_CALISMA/VAKA` files,
  `_okuma/` folders, KAYNAK files and the tools — no `_arsiv*`, `99-Arsiv`, Docs mirrors,
  protocol/handoff/authority files.
- Snapshot ZIP exists in `HcC Kasa Arsiv/` with the reported hash.
- `ozelge_atiflari.csv` exists in `ymm-korpus/`.

## 5. Bilinen sınırlar (Claude)
- I could read Drive but not the private `ymm-korpus` repo or the local vault; the folder list
  in Faz 0 is therefore yours to establish. I have not seen the Denetim packs' files.
- The checker catches added/lost article refs, özelge refs, numbers, dates and verbatim-quote
  changes. It cannot judge whether a *paraphrased sentence* changed legal meaning — that is why
  the pilot gate and the KONTROLLU rule exist.
- I do not know the exact model names available in Codex on Cihan's plan; "GPT-6 Luna medium"
  is Cihan's choice, not a verified name.

## 6. How to report (so the others see it)
At every STOP: put the report in the Drive inbox subfolder `01_CIKTI_DENETIM_BEKLIYOR/` named
`2026-10-xx-temizlik-G<n>-rapor.md`, and add one line at the top of `DURUM.md` in the bridge repo
(`Sıradaki kapı: G<n> — Cihan/Claude onayı bekleniyor`). When this directive is finished, add
`## Yanıt` at the bottom of this file and prefix the title with `[KAPANDI]`.
