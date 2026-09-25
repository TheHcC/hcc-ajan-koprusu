---
baslik: HCC Sistem Analizi — Okuben
yazar: Claude (Claude.ai, Opus 5.5) + ChatGPT (GPT-5.6 Sol) dizin güncellemesi
tarih: 2026-09-26
versiyon: v3
etiketler: [hcc-sistem-analizi, okuben]
---

# HCC Sistem Analizi — Okuben

Bu klasör, HCC çok-ajanlı sisteminin sistem analizlerini, darboğaz değerlendirmelerini, karşı-denetimleri ve uygulama direktiflerini **yazar/model ve versiyon bilgisi korunarak** tutar.

## İsimlendirme kuralı

`YYYY-MM-DD_YAZAR_konu_vN.md`

- **YYYY-MM-DD** — belgenin yazıldığı tarih
- **YAZAR** — belgeyi yazan model/ajan: `GROK`, `CLAUDE-Opus-5.5`, `CLAUDE-CODE`, `CODEX`, `CHATGPT-gpt-5.6-sol` …
- **konu** — kısa, tireli
- **vN** — aynı yazarın aynı konudaki versiyonu. Revizyon yeni dosya açar; eski versiyon silinmez.

Direktifler: `YYYY-MM-DD_DIREKTIF_KIMDEN-to-KIME_konu_vN.md`

## Dizin

| Dosya | Yazar | Tür | Durum |
|---|---|---|---|
| `2026-09-25_GROK_ai-radar-pilot-raporu_v1.md` | Grok / GrokBot | radar / sistem tarama | girdi |
| `2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1.md` | Claude.ai (Opus 5.5) | normalizasyon / mimari analiz | öneri |
| `2026-09-25_DIREKTIF_CLAUDE-Opus-5.5-to-CLAUDE-CODE_N1-N3-uygulama_v1.md` | Claude.ai → Claude Code | uygulama direktifi | Drive/Obsidian'da mevcut; public GitHub aynası sanitizasyon bekliyor |
| `2026-09-25_CHATGPT-gpt-5.6-sol_grokbot-sistem-rolu-degerlendirmesi_v1.md` | ChatGPT (GPT-5.6 Sol) | GrokBot rol / uyum değerlendirmesi | değerlendirme |
| `2026-09-25_DIREKTIF_CHATGPT-gpt-5.6-sol-to-GROKBOT_ai-radar-sistem-tarama-pilot_v1.md` | ChatGPT → GrokBot | AI Radar pilot direktifi | uygulandı |
| `2026-09-25_CHATGPT-gpt-5.6-sol_grok-ai-radar-pilot-capraz-denetimi_v1.md` | ChatGPT (GPT-5.6 Sol) | Grok çıktısı çapraz-denetim | değerlendirme |
| `2026-09-25_CHATGPT-gpt-5.6-sol_claude-opus-5.5-normalizasyon-analizi-degerlendirmesi_v1.md` | ChatGPT (GPT-5.6 Sol) | Claude analizinin karşı-değerlendirmesi | v1 |
| `2026-09-26_CHATGPT-gpt-5.6-sol_claude-opus-5.5-normalizasyon-analizi-degerlendirmesi_v2.md` | ChatGPT (GPT-5.6 Sol) | Claude analizinin revize karşı-değerlendirmesi | **güncel; eski Chrome kısıtı işlendi** |

## Güncel okuma sırası

Claude Code veya başka bir reviewer bu konuya dönerken sırasıyla:

1. `2026-09-25_GROK_ai-radar-pilot-raporu_v1.md`
2. `2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1.md`
3. `2026-09-25_CHATGPT-gpt-5.6-sol_claude-opus-5.5-normalizasyon-analizi-degerlendirmesi_v1.md`
4. **`2026-09-26_CHATGPT-gpt-5.6-sol_claude-opus-5.5-normalizasyon-analizi-degerlendirmesi_v2.md`**
5. gerekiyorsa Claude Code uygulama direktifi

v2, v1'i silmez; **Chrome DevTools MCP'nin kurum bilgisayarındaki eski Chrome nedeniyle environment-gated hâle gelmesi başta olmak üzere güncel ChatGPT görüşünü taşır.**

## Konumlar

### Drive / Obsidian

`HcC Kasa Obsidian/20-Araclar/HCC-Sistem-Analizi/`

Drive klasörü:
`https://drive.google.com/drive/folders/1eyJ7eUsh6bDD1xThn4K_Icg5myt-ijCj`

Bu klasör Obsidian kasasının Drive ile senkronize edilen alanıdır; ayrı Obsidian kopyası tutulmaz.

### GitHub

Repo: `TheHcC/hcc-ajan-koprusu`

Branch: `sistem-analizi/n1-n3`

Klasör: `sistem-analizi/`

Public mirror kuralı: hassas veya gereksiz kişisel/yerel tanımlayıcı içeren dosya sanitise edilmeden public repo'ya konulmaz.

## Sürüm ilkesi

- İçerik revizyonunda `v2`, `v3` şeklinde yeni sürüm açılır.
- Eski model çıktısı silinmez.
- Bir modelin başka model çıktısına yaptığı değerlendirme ayrı dosyadır; kaynak metnin üzerine yazılmaz.
- Yeni maddi kısıt önceki analizin sonucunu etkiliyorsa yeni versiyon açılır ve `revizyon_nedeni` yazılır.
- Public GitHub aynası Drive/Obsidian kaynağının güvenli paylaşım sınırına uyar.
