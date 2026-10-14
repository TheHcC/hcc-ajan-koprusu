---
tur: proje-notu
tarih: 2026-10-15
durum: bekliyor — StudyPack temizliği (G3) kapandıktan sonra açılacak
---
# Özelge projesi — not

**Karar (Cihan, 14.10.2026):** Özelge araştırması **sınav cevaplarında geçen özelgelerden** başlar
(hızlı ve isabetli). Ayrıca StudyPack konuları için **yeni çıkan özelgeleri izleyen ayrı bir proje**
kurulacak; yeni özelgeler sınavlara konu olabiliyor.

## Aşama A — Sınavın işaret ettiği özelgeler (temizlik FAZ 0'da başlar)
- `araclar/ymm-studypack/ozelge_atif_cikar.py` → `ymm-korpus/ozelge_atiflari.csv`
  (tarih, sayı, ders, dönem, satır). Komisyon metnindeki atıf olduğu gibi alınır.
- Önceliklendirme: birden çok sınavda geçen > son 5 yıl > kalan.

## Aşama B — Metinlerin toplanması
- GİB sitesi otomatik erişimi engelliyor (robots); toplu kazıma yapılmaz.
  Metin; Cihan'ın tarayıcısı / Claude'un tarayıcı aracı / ChatGPT web araması ile tek tek açılır.
- Kayıt: `ozelge/<kanun>/<madde>/<tarih>_<sayı>.md` — frontmatter: tarih, sayı, idare,
  kanun_madde, konu, gecen_sinavlar, ilgili_paketler, metin_kaynagi (URL), dogrulama.
- Arama: SQLite FTS5 veya ripgrep. Vektör veritabanı gerekmez.

## Aşama C — Yeni özelge radarı (ayrı proje)
- Her paketin `1. Kapılar` bölümündeki kanun/madde listesi = izleme listesi.
- Ayda bir: GİB'de kanun bazlı özelge sayfalarında son ayın özelgeleri taranır (ucuz model +
  tarayıcı; Claude/Claude Code kullanılmaz). Bulgu → `ozelge/yeni/YYYY-MM.md`.
- Etkilenen pakete frontmatter `guncellik_uyarisi: <özelge kimliği>` eklenir; paket TASLAK'a
  düşmez, yalnız bir sonraki çalışmada "yeni özelge var" diye görünür.
- Özelge kanun değildir: pakete "özelge" etiketiyle girer, kural cümlesinin yerine geçmez.
