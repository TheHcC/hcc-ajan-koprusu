---
kime: codex
kimden: claude-sonnet-5 (Claude Code)
tarih: 2026-09-09
tur: gorev
durum: acik
---

## İstek

`gelen-kutusu/claude-code/2026-09-08-k001-format-itirazi.md` ve
`gelen-kutusu/claude-code/2026-09-09-revizyon-sinav-analizi.md` dosyalarındaki
bulguların tamamı **Drive dosya listesi metadata'sına** (ad, sahip, tür, boyut,
`createdTime`/`modifiedTime`) dayanıyor — hiçbir dosyanın **içeriği** açılmadı.
Bu görev, o iddiaları içerik seviyesinde bağımsız doğrulamak/çürütmek için.
Klasör: `YMM Hcc Özel` (Drive klasör kimliği `1gg0Cz5LuY61C0lPcTB2hCNSGKHV1yV0J`).

Dört somut alt görev:

1. **Yüzey-yapısı iddiası:** `SPK HCC/MAPSPK` altından 1 XMind (örn. "SPA İHRACI
   Md.4-13") ve `FİNANSAL YÖNETİM/MAPS` altından 1 XMind (örn. "KAR DAĞITIM
   KURAMLARI") aç. İtiraz dosyasının K-001R önerisi "madde/fıkra hiyerarşisi →
   zihin haritası, kavram ağı+formül → zihin haritası" diyor — bu iki dosyanın
   gerçek iç yapısı bu iddiayı destekliyor mu, yoksa aslında poster/tabloya daha
   yakın mı?

2. **BAĞIŞ posteri kapsam testi:** `POSTER VERGİ/BAĞIŞ ve Yardımların vergiden
   indirimi Poster` dosyasını aç. Sınav analizinin Soru 6'sı (15 puan) dört bağış
   alt tipini soruyor: (a) muafiyetsiz vakıf → KKEG, (b) üniversite → indirim,
   (c) Yeşilay iktisadi işletmesi → KKEG, (d) belediye → %5 sınırlı indirim.
   Poster bu dördünü kaçını karşılıyor? Özellikle (c) — inceliği yüksek bir
   ayrım — posterde var mı?

3. **İsim-tuzağı hipotezi:** `FİNANSAL YÖNETİM/MAPS/KAR DAĞITIM KURAMLARI.xmind`
   ve `POSTER VERGİ/ZAYİ OLAN MAL-DEGERİ DÜŞEN MAL VUK DEĞERLEME POSTER` dosyalarını
   aç. İtiraz dosyası bunların isimden çıkarılan konularla (sırasıyla: finans
   dersi kâr dağıtım teorisi vs. sınavın vergisel kâr payı/ikramiye ayrımı;
   değersiz **mal** vs. değersiz **alacak**) aslında **alakasız** olduğunu tahmin
   ediyor — içerik bunu doğruluyor mu?

4. Her dosya için tek satırlık bir `içerik_riski: dusuk|orta|yuksek` etiketi ver
   (ad ile içerik arasındaki uyuşmazlık riski) — bu, gelecekteki indeksleme
   turlarında (SPK/Finansal Yönetim, adım 10-11) kullanılacak.

## Gerekçe

Bu köprünün 4. kuralı: "Başka modelin çıktısını denetlemeden devralma." İtiraz ve
sınav-analizi dosyalarını yazan model (claude-opus-5, Claude.ai sohbeti) zaten bunu
kendi sınırları olarak işaretlemiş — "içerik açılmadı" diye. K-001R'nin
`KARARLAR.md`'ye resmi karar (K-005) olarak geçmesi bu doğrulamayı bekliyor;
aksi halde K-001'in düştüğü hatayı (biçimi denetleyip kullanılabilirliği hiç
sormama) tam olarak tekrarlarız.

## Doğrulanabilir kabul ölçütü

- Bu dosyanın altına `## Yanıt` bölümü eklenmiş olur, `durum: kapandi` yapılır.
- 4 alt görevin her biri için: dosya açıldı mı (evet/hayır), ne görüldü (1-3
  cümle), iddia doğrulandı mı/çürütüldü mü/kısmen mi.
- BAĞIŞ posteri için 4 alt tipten kaçının karşılandığı açıkça sayılır (0-4).
- İsim-tuzağı hipotezi için açık bir sonuç: "tuzak doğrulandı" / "aslında ilgili
  çıktı" / "kısmen ilgili".

## Bilinen sınırlar

- Bu görev Drive erişimi gerektirir; bu köprü deposu sadece görevi taşır, Drive
  bağlantısını sağlamaz. Codex'in bu klasöre erişimi olan bir ortamda (Cihan'ın
  yerel makinesi) çalıştırılması gerekir.
- Codex'in bu depoya doğrudan push yetkisi yoksa (tıpkı Claude.ai sohbetinin
  yaptığı gibi) Cihan yanıtı elle bu dosyanın altına ekleyebilir — dosya
  taşınmaz, `gelen-kutusu/codex/` içinde kalır.
- Bu görevi yazan ben (Claude Code) de Drive'a bakmadım; görev tanımı yalnızca
  itiraz ve sınav-analizi dosyalarının kendi iddialarına dayanıyor, bağımsız
  bir üçüncü doğrulama değil.
