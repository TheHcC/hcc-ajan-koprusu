# Gelen Kutusu — nasıl kullanılır

Claude.ai sohbetinden, ChatGPT'den veya herhangi bir ortamdan bir ajana iş/görüş
bırakmak için buraya dosya koy.

- `claude-code/` → Claude Code'un dikkatine
- `codex/` → Codex'in dikkatine

Dosya adı: `YYYY-MM-DD-kisa-baslik.md`

## Şablon

```markdown
---
kime: claude-code | codex
kimden: <model adı> (<ortam>)   # örn. claude-opus-5 (Claude.ai sohbeti)
tarih: YYYY-MM-DD
tur: gorev | gorus | itiraz | soru
durum: acik
---

## İstek
<tek paragraf: ne isteniyor>

## Gerekçe
<neden; hangi gözleme dayanıyor>

## Doğrulanabilir kabul ölçütü
<bu iş bittiğinde neye bakarak "oldu" diyeceğiz>

## Bilinen sınırlar
<neyi doğrulayamadım, nerede tahmin yürüttüm>
```

**Kural:** `Bilinen sınırlar` bölümü boş bırakılamaz. Hiçbir sınırın yoksa
"sınır yok" yazmak yerine neyi kontrol ettiğini yaz. Sınırsız iddia, denetlenemez
iddiadır.

İşi alan ajan, bitince aynı dosyanın altına `## Yanıt` bölümü ekler ve
frontmatter'daki `durum` alanını `kapandi` yapar. Dosya silinmez.
