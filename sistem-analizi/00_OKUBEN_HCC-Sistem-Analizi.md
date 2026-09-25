---
baslik: HCC Sistem Analizi — Okuben
yazar: Claude (Claude.ai, Opus 5.5)
tarih: 2026-09-25
versiyon: v1
etiketler: [hcc-sistem-analizi, okuben]
---

# HCC Sistem Analizi — Okuben

Bu klasör, HCC çok-ajanlı sisteminin darboğaz analizlerini, model bazında versiyonlu olarak tutar.

## İsimlendirme kuralı

`YYYY-MM-DD_YAZAR_konu_vN.md`

- **YYYY-MM-DD** — belgenin yazıldığı tarih
- **YAZAR** — belgeyi yazan model/ajan, model adıyla: `GROK`, `CLAUDE-Opus-5.5`, `CLAUDE-CODE`, `CODEX`, `CHATGPT-gpt-5.6-sol` …
- **konu** — kısa, tireli
- **vN** — aynı yazarın aynı konudaki versiyonu. Revizyon yeni dosya açar (v2, v3); eski versiyon silinmez.

Direktifler: `YYYY-MM-DD_DIREKTIF_KIMDEN-to-KIME_konu_vN.md`
Örnek: `DIREKTIF_CLAUDE-Opus-5.5-to-CLAUDE-CODE` = Claude.ai'ın Claude Code'a verdiği direktif.

## Dizin

| Dosya | Yazar | Tür | Durum |
|---|---|---|---|
| `2026-09-25_GROK_ai-radar-pilot-raporu_v1.md` | Grok | radar / darboğaz tespiti | girdi |
| `2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1.md` | Claude.ai (Opus 5.5) | normalizasyon analizi | öneri |
| `2026-09-25_DIREKTIF_CLAUDE-Opus-5.5-to-CLAUDE-CODE_N1-N3-uygulama_v1.md` | Claude.ai → Claude Code | direktif | aktif, 28.09.2026 14:18 |

## Konumlar

- Drive / Obsidian (aynı klasör, vault Drive ile senkron): `HcC Kasa Obsidian/20-Araclar/HCC-Sistem-Analizi/`
- GitHub (Claude Code direktif T1 ile aynalar): `TheHcC/hcc-ajan-koprusu/sistem-analizi/`
