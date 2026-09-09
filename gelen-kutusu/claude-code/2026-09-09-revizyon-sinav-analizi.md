---
kime: claude-code
kimden: claude-opus-5 (Claude.ai sohbeti)
tarih: 2026-09-09
tur: gorus
durum: acik
---

## İstek

Cihan'ın paylaştığı **2025/3. Dönem YMM Sınavı — Revizyon** sorularının (13 Aralık 2025,
resmi TÜRMOB cevap anahtarıyla) analizinden çıkan bulgular kayda geçirilsin. Bu belge
şu ana kadarki tüm kanıt tabanından niteliksel olarak farklı: Drive arşivindeki
posterler ve XMind'lar **üretim materyali** (Cihan'ın ne çalıştığı), bu sınav kağıdı ise
**doğrudan ölçüm** (sınavın gerçekte neyi sorduğu). Atom önceliklendirmesi ikincisine
göre yapılmalı, birincisine göre değil — 12. adımdaki "Poster atom şablonu — pilot
poster üretimi" bu belgedeki dört boşluktan biriyle başlamalı.

## Gerekçe

`[SINAV-KAYNAK]` Kaynak: TÜRMOB, 2025/3. Dönem YMM Sınavı, Revizyon, 13.12.2025,
10 soru, sınav komisyonu resmi cevaplarıyla birlikte. Born-digital PDF, OCR
gerekmedi — bu, 221 MB'lık taranmış `REVİZYON 2016-2022.1 SORU-CVP.pdf` dosyasından
önce işlenebilecek bir örnek oldu.

### 1. Sorular tek konu değil, konu **kombinasyonu** test ediyor

`[SINAV-KAYNAK]` 10 sorunun hiçbiri tek bir mevzuat maddesine dayanmıyor; her biri
2-4 farklı kanun/madde/tebliğ kesişiminde kuruluyor. Puan dağılımıyla:

| Soru | Puan | Konu kombinasyonu |
|---|---|---|
| 1 | 5 | Zarar mahsubu (KVK m.9) + serbest bölge istisnası + nakit sermaye faiz indirimi |
| 2 | 5 | Dava konusu vergi/ceza karşılığının KKEG'liği (KVK m.11, GVK m.90, KDVK m.58) |
| 3 | 10 | YK üyesi kâr payı ikramiyesi (GVK m.75) vs personel ikramiyesi (GVK m.61) — ücret/kâr payı ayrımı |
| 4 | 10 | Yurt dışı ortak borcu + kur farkı + faizsiz borçlanmada örtülü sermaye YOK ama emsal bedel üzerinden KDV VAR |
| 5 | **15** | Sat-kirala-geri al istisnası (KVK m.5/j) + amortismanın özel fon/kurum kazancı %25-%75 bölüştürülmesi |
| 6 | **15** | Bağışın 4 alt tipi: muafiyetsiz vakıf (KKEG) / üniversite (indirim) / Yeşilay iktisadi işletmesi (KKEG) / belediye (%5 sınırlı indirim) |
| 7 | 10 | Hizmet ihracı indirimi %80 (KVK m.10/ğ) + Türkiye'ye transfer şartı + KDV istisnası |
| 8 | 10 | Grup içi kredi aktarımı → örtülü sermaye sayılmaz (KVK m.12) ama gider kısıtlaması uygulanır |
| 9 | 10 | Opsiyon sözleşmesi — primin ve kazancın tahakkuk anı farklı tarihler |
| 10 | 10 | Değersiz alacak (VUK m.322) + KDV'nin ayrı indirim şartı (KDVK m.29/4) |

`[ÇIKARIM]` Bunun atom tasarımına sonucu: bir poster tek maddeyi anlatıyorsa
(örn. sadece "zarar mahsubu"), sınavın fiilen sorduğu şeyi karşılamaz. Atomun
künyesine `iliskili_maddeler: [liste]` alanı eklenmeli — tek `dayanak` alanı yetersiz.

### 2. Cevap mimarisi sabit bir kalıp izliyor

`[SINAV-KAYNAK]` 10 cevabın tamamı aynı iskeleti kullanıyor: (a) kanun maddesi tam
metin alıntı, (b) ilgili tebliğ paragrafı tam metin alıntı, (c) "Yukarıdaki madde
hükümleri ve tebliğ açıklamalarına göre:" geçiş cümlesi, (d) somut olaya uygulama +
sayısal hesap, (e) net sonuç cümlesi.

`[ÇIKARIM]` Poster/atom üretiminde bu kalıp şablon olarak kullanılabilir: her atom
"madde metni → tebliğ açıklaması → örnek hesap → sonuç" sırasını taşımalı. Bu,
09_bilgi ağacındaki atom şablonu tasarımına doğrudan girdi.

### 3. Drive arşiviyle çapraz kontrol — bir isabet, iki isim tuzağı

`[DRIVE-DOĞRULANDI]` Soru 6 (bağış, 15 puan — sınavın en yüksek puanlı ikinci sorusu)
ile `POSTER VERGİ/BAĞIŞ ve Yardımların vergiden indirimi Poster` dosya adı doğrudan
örtüşüyor. `[HİPOTEZ — içerik açılmadı]` Posterin sınavın sorduğu 4 alt tipin
(özellikle "Yeşilay'ın iktisadi işletmesine yapılan bağış KKEG'dir" inceliğinin)
tamamını içerip içermediği doğrulanmadı; bu, sistemin ilk gerçek pilot testi olabilir.

`[ÇIKARIM — isim benzerliği riski]` İki dosya adı yanıltıcı biçimde ilgili görünüyor
ama muhtemelen alakasız:
- `FİNANSAL YÖNETİM/MAPS/KAR DAĞITIM KURAMLARI.xmind` muhtemelen Modigliani-Miller
  kâr dağıtım teorisi (finans dersi) — Soru 3'teki **vergisel** kâr payı/ikramiye
  ayrımıyla (Revizyon dersi) konu olarak alakasız.
- `POSTER VERGİ/ZAYİ OLAN MAL-DEGERİ DÜŞEN MAL VUK DEĞERLEME POSTER` değersiz **mal**
  değerlemesidir (VUK m.278) — Soru 10'daki değersiz **alacak** (VUK m.322) farklı
  maddedir.

Bu iki dosyanın içeriği açılmadı; adlarından çıkarım yapıldı. **Sonuç:** ileride
yapılacak indekslemede dosya adı eşleştirmesi tek başına yeterli değil; her eşleşme
içerik düzeyinde teyit edilmeli. Öneri: atom şemasına `ad_icerik_riski: dusuk|orta|yuksek`
alanı.

### 4. Kapsam boşluğu — 45 puanlık dört konu hiçbir posterde yok

`[DRIVE-DOĞRULANDI]` `YMM Hcc Özel` arşivinde arattığım aşağıdaki dört konu için
poster, tablo veya XMind bulunamadı — hem Revizyon hem Finansal Yönetim/SPK
klasörlerinde arandı:

- Sat-kirala-geri al istisnası ve özel fon bölüştürme formülü (15 puan — sınavın en
  yüksek puanlı sorusu)
- Opsiyon sözleşmesi vergilendirmesi (10 puan)
- Grup içi kredi aktarımında örtülü sermaye istisnası + gider kısıtlaması (10 puan)
- Faizsiz borçlanmada transfer fiyatlandırması → emsal bedel üzerinden KDV sorumluluğu
  (Soru 4'ün 10 puanının bir kısmı)

`[ÇIKARIM]` Bu dört konu tek bir sınav döneminin toplam 100 puanının 45'ini
oluşturuyor. Örneklem büyütülmeden (yalnızca bu bir dönemden) kalıcı bir öncelik
sırası çıkarılamaz, ama **12. adımdaki ilk pilot posterin bu dört boşluktan biriyle,
tercihen en yüksek puanlı sat-kirala-geri al konusuyla başlaması** önerilir —
zaten var olan bir konuyu tekrar üretmek yerine.

## Doğrulanabilir kabul ölçütü

1. `DURUM.md`'deki 9. adım tanımına (Revizyon arşivi indeksi) bu dört konudan en az
   birinin "poster yok" olarak işaretlendiği bir satır eklenmiş olur.
2. 12. adımın pilot posteri, yukarıdaki dört konudan biri seçilerek üretilir ve
   üretilen posterin künyesinde `iliskili_maddeler` alanı en az iki madde numarası
   taşır (tek madde değil).
3. `BAĞIŞ ve Yardımların vergiden indirimi Poster` dosyası açılıp Soru 6'daki 4 alt
   tipin kaçını karşıladığı tek satırlık bir notla kayda geçirilir.
4. `KAR DAĞITIM KURAMLARI.xmind` ve `ZAYİ OLAN MAL... POSTER` dosyaları en az biri
   açılarak isim-içerik uyuşmazlığı hipotezi teyit veya çürütülür.

## Bilinen sınırlar

- **Tek sınav dönemi analiz edildi (2025/3).** Bu, 6-8 yıllık soru dağılımını temsil
  etmez; hangi konunun "sık sorulan" olduğuna dair genel bir iddia bu belgeden
  çıkarılamaz — yalnızca bu dönemde hangi konuların birlikte sorulduğu ve hangilerinin
  arşivde karşılığı olmadığı söylenebilir.
- **BAĞIŞ posterinin içeriği açılmadı.** "İsabet" tespiti yalnızca dosya adı
  eşleşmesine dayanıyor; posterin 4 alt tipi (özellikle Yeşilay iktisadi işletmesi
  inceliği) gerçekten içerip içermediği doğrulanmadı.
- **`KAR DAĞITIM KURAMLARI` ve `ZAYİ OLAN MAL` dosyalarının içeriği açılmadı.**
  İsim-içerik uyuşmazlığı tahmindir, dosya adlarından ve genel ders bilgisinden
  çıkarılmıştır; içerik gerçekten farklı olmayabilir.
- **Madde numaraları ve tebliğ referansları sınav PDF'inden birebir aktarıldı,
  bağımsız doğrulanmadı.** K-003 kararı gereği Mevzuat MCP bağlantı sorunu sürdüğü
  için bu numaraların hâlâ yürürlükte olup olmadığı, güncel tebliğ numaralarının
  bunlar olup olmadığı teyit edilmedi. Sınav belgesi resmi olduğu için maddeler
  büyük ihtimalle doğru aktarılmıştır, ama bu bir varsayımdır.
- **Diğer 41 dosyalık kalan Revizyon/Finansal Yönetim/SPK arşivi tam taranmadı** —
  yalnızca bu 10 sorunun anahtar kelimeleriyle arama yapıldı. Aranan dört konu için
  başka bir klasörde (örn. İleri Düzey, Vergi Tekniği) karşılık olabilir; bu belge
  onu dışlamaz, sadece bulunamadığını söyler.
- Bu okuma tek bir modelin (benim) tek geçişte yaptığı analizdir; ikinci bir
  gözden geçirme yapılmadı.
