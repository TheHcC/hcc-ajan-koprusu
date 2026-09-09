# DURUM — özet (otorite değil)

**Son güncelleme:** 09.09.2026 (2. tur) · claude-sonnet-5 (Claude Code)
**Aktif iş:** YMM ikinci beyin + sürdürülebilir çalışma sistemi kurulumu
**İlerleme:** 15 adımın 9'u tamam (bkz. `GUNLUK.md`)

> Otorite bu dosya değildir. Operasyonel gerçek:
> `Desktop\inceleme-os\obsidian-ikinci-beyin\durum.md`
> Adım checkpoint'i: `claude-practice\.gorev-durumu\aktif-gorev.json`

## Tek cümlelik durum

Eski YMM çalışma sistemi (`ymm-korpus`) doğru analizi üretti ama çıktıyı Cihan'ın
kullanamadığı bir formatta teslim ettiği için verim vermedi; yeni sistem aynı analitik
gücü Cihan'ın kanıtlanmış görsel formatına (poster) bağlayacak şekilde yeniden kuruluyor.

## Şu an nerede kalındı

| # | Adım | Durum |
|---|---|---|
| 1 | ymm-korpus durum tespiti ve hata analizi | ✅ |
| 2 | Drive arşivi envanteri + çalışma stili teşhisi | ✅ |
| 3 | Astra (gpt-6-astra) Obsidian raporunun bağımsız denetimi | ✅ |
| 4 | Vault yeri ve mevzuat doğrulama kararları | ✅ |
| 5 | `ymm-korpus/09_bilgi/` ağacının kurulması | ✅ |
| 6 | Ajan köprüsü deposu kuruldu ve yayına alındı | ✅ |
| 7 | GitHub public repo + push (anonim erişim doğrulandı) | ✅ |
| 8 | P0 kural çelişkisinin cerrahi düzeltmesi | ✅ |
| 9 | Revizyon arşivinin tam indeksi (65 dosya + 1 kısayol) | ✅ |
| 10-11 | SPK / diğer klasörlerin indeksi | 🔄 sıradaki |
| 12 | Poster atom şablonu — pilot poster üretimi | ⏳ |
| 13 | Bayatlama motoru (dayanak → geçerlilik → son doğrulama) | ⏳ |
| 14 | Çoklu-ajan halüsinasyon önleme protokolü | ⏳ |
| 15 | Yeni master plan belgesi | ⏳ |


## Bilinen engeller

- `Mevzuat MCP` ve `yargi-mcp` bağlantısı 08.09.2026 oturumunda **CONNECT_TIMEOUT**
  verdi. Cihan bağlantıyı düzeltecek. Düzelene kadar mevzuat parametreleri
  `[TEYİT: kaynak gerekli]` etiketiyle kalır.
- `gh` (GitHub CLI) kurulu değil; depo oluşturma manuel yapılır, push otomatiktir. *(08.09 çözüldü)*

## Sıradaki tek iş

10 adet KALICI poster atomunun künyelendirilmesi (Adım 12) veya SPK arşivinin indekslenmesi
(Adım 10) — sıra Cihan'ın tercihine bağlı.

**Adım 12 pilot konu önerisi (09.09, gelen-kutusu/claude-code sınav-analizi
görüşünden):** 2025/3 Revizyon sınavında 45 puanlık dört konunun (sat-kirala-geri
al 15p, opsiyon sözleşmesi 10p, grup içi kredi 10p, faizsiz borçlanma-KDV 10p)
arşivde hiçbir poster/XMind karşılığı yok. Pilot posterin **sat-kirala-geri al
istisnası (KVK m.5/j)** ile başlaması öneriliyor — en yüksek puanlı ve tam boşluk.

## Açık kararlar (Codex/yerel oturum bekliyor)

- **K-001R (taslak K-005):** Bilgi atomunun künyeli-konu-birimi olarak revize
  edilmesi, poster'ın donmuş export/XMind'ın düzenlenebilir kaynak sayılması
  öneriliyor (bkz. `gelen-kutusu/claude-code/2026-09-08-k001-format-itirazi.md`).
  İçerik doğrulaması (2 XMind + BAĞIŞ posteri + 2 isim-tuzağı dosyası) Codex'e
  görev bırakıldı: `gelen-kutusu/codex/2026-09-09-icerik-dogrulama-gorevi.md`.
  Rapor gelince `KARARLAR.md`'ye K-005 olarak işlenecek.
- **Atom şeması eklentisi (yerel, `ymm-korpus/09_bilgi/`):** `iliskili_maddeler`
  (madde listesi, tek `dayanak` yetersiz — sınavlar madde kombinasyonu soruyor),
  `ad_icerik_riski: dusuk|orta|yuksek` (dosya adı ↔ içerik uyuşmazlık riski)
  alanlarının atom künyesine eklenmesi öneriliyor. Bu köprü deposunda uygulanacak
  dosya yok; yerel oturumun uygulaması gerekiyor.
