# YMM StudyPack araçları

Bu klasör yalnız **taşıma** içindir: araçlar buradan byte-birebir `ymm-korpus/tools/` altına kopyalanır.
Köprüde iş yapılmaz kuralı geçerlidir; burada çalıştırma çıktısı tutulmaz.

| Dosya | Görev |
|---|---|
| `paket_denetle.py` | Yeni paketin biçimini ve eski→yeni içerik korunmasını denetler (madde/özelge atfı, birebir komisyon cevabı, sayı/tarih, boyut). Çıkış 0 = geçti. |
| `okunur_yap.py` | Paketleri telefonda/bilgisayarda okunur A5 PDF + HTML'e çevirir (`_okuma/`). Cevaplar kapalı gelir. |
| `ozelge_atif_cikar.py` | Komisyon cevaplarındaki özelge atıflarını CSV'ye çıkarır. |
| `temizlik_uygula.py` | **Yerelde** çalışır: yedek ZIP alır; ChatGPT'nin çıktı ZIP'ini yeniden denetler, geçenleri kasaya yazar, onaylı envantere göre siler, `_okuma/` üretir. Varsayılan kip provadır. |
| `obsidian-okunur-tablolar.css` | Obsidian için tablo sarma snippet'i. |

Kurulum: `pip install markdown-it-py pyyaml` · PDF için Edge/Chrome yeterli.
Görev emri: `gorevler/2026-10-15-studypack-temizlik-chatgpt.md` (Codex sürümü iptal)
