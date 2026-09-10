---
id: BULTEN-001
konu: İlişkili kişiden borçlanma
alt_konular:
  - örtülü sermaye
  - transfer fiyatlandırması
  - finansman gider kısıtlaması
  - KDV
  - stopaj ve ÇVÖA
  - karşı düzeltme
hazirlayan: gpt-5.6-sol (ChatGPT)
tarih: 2026-09-10
son_dogrulama: 2026-09-10
dogrulama_durumu: WEB_GIB_BDO_TARAMASI_YAPILDI_MEVZUAT_MCP_BEKLIYOR
kaynak_penceresi: 2021-09-10 / 2026-09-10
---

# BÜLTEN 001 — İlişkili Kişiden Borçlanma: Aynı Borca Üç Ayrı Vergi Merceği

## 0. Bu bülten neyi çözüyor?

İlişkili kişiden borçlanma konusu ilk bakışta kolay görünür: “öz sermayenin üç katını aşarsa örtülü sermaye”. Sınavda ve gerçek incelemede hata tam burada başlar.

Çünkü aynı borç aynı anda en az üç ayrı soruya tabi olabilir:

1. **Borç miktarı fazla mı?** → KVK m.12 örtülü sermaye
2. **Faiz/fiyat emsale uygun mu?** → KVK m.13 transfer fiyatlandırması
3. **İşletmenin toplam yabancı kaynağı öz kaynağını aşıyor mu?** → KVK m.11/1-i finansman gider kısıtlaması

Yabancı ortak varsa buna KDV, stopaj ve ÇVÖA da eklenebilir.

Bu bültenin temel mesajı:

> **Aynı borç farklı kontrol noktalarından geçer; fakat aynı gider için aynı vergi etkisi iki kez yaratılmaz.**

---

# 1. Akılda kalıcı analoji: Havalimanındaki üç kontrol

İlişkili kişiden alınan borcu, havalimanına giren bir yolcu gibi düşün.

### Kontrol 1 — Kantar: Örtülü sermaye

Burada kimse bilet fiyatına bakmaz. Sadece “yükün fazla mı?” diye bakılır.

- Borç kimden?
- İşletmede kullanılmış mı?
- Dönem başı öz sermayenin üç katı aşılmış mı?

### Kontrol 2 — Ekspertiz: Transfer fiyatlandırması

Burada borcun miktarı tek başına önemli değildir. “Bu işlemin fiyatı/faizi piyasa fiyatı mı?” diye bakılır.

Bir şirket kardeş şirkete %2 ile borç verirken bağımsız piyasada emsal %20 ise, üç kat sınırının altında kalsa dahi transfer fiyatlandırması sorusu kapanmaz.

### Kontrol 3 — Bilanço kapısı: Finansman gider kısıtlaması

Bu kapı yalnız ilişkili kişiye bakmaz. İşletmenin tüm yabancı kaynak/öz kaynak dengesi önemlidir.

**Fakat:** Birinci veya ikinci kapıda aynı faiz giderinin bir kısmı zaten KKEG olduysa, üçüncü kapı aynı tutara bir kez daha ceza kesemez.

Bunu “üç ayrı radar var ama aynı hız ihlali için aynı polis iki kez ceza yazamaz” diye hatırla.

---

# 2. Üç müessesenin karar tablosu

| Müessese | Ana soru | Ölçü | Temel sonuç |
|---|---|---|---|
| Örtülü sermaye | İlişkili borç aşırı mı? | Borç / dönem başı öz sermaye | Aşan kısma isabet eden faiz/kur farkı yönünden KKEG ve kâr payı sonuçları |
| Transfer fiyatlandırması | Faiz/fiyat emsale uygun mu? | Emsal bedel/faiz | Emsal dışı fark → örtülü kazanç dağıtımı |
| FGK | Toplam yabancı kaynak fazla mı? | Yabancı kaynak / öz kaynak | Aşan kısma isabet eden finansman giderinin belirlenen oranı KKEG |

**Kritik düzeltme:** “Bağımsız test” demek “bağımsız ve mükerrer KKEG” demek değildir.

---

# 3. İlk büyük bulgu: Mükerrer KKEG yok — hesaplama sırası var

1 Seri No.lu Kurumlar Vergisi Genel Tebliği 11.13.9 açık:

Örtülü sermaye, transfer fiyatlandırması veya binek oto gider kısıtlaması nedeniyle zaten KKEG olarak dikkate alınmış finansman giderleri, FGK hesabında tekrar dikkate alınmaz.

## Neden çok önemli?

Mevcut Atom 3'te “üç müessese birbirinden bağımsızdır” tezi doğru ama tek başına okunursa yanlış bir hesaba götürebilir.

Doğru zihinsel model:

```text
1. Örtülü sermaye testi
2. Transfer fiyatlandırması testi
3. Bu iki test nedeniyle zaten KKEG olan finansman giderini ayır
4. Kalan finansman gideri üzerinde FGK hesabı
```

BDO 2024/014 de aynı noktayı örnekle anlatıyor ve duplike KKEG yapılamayacağını vurguluyor.

### Sayısal örnek

**Tamamen öğretici varsayım; gerçek mükellef verisi değildir.**

- Dönem başı öz sermaye = 10 milyon TL
- İlişkili kişiden borç = 40 milyon TL
- Üç kat sınırı = 30 milyon TL
- Örtülü sermaye = 10 milyon TL
- Bu borca ilişkin toplam faiz = 4 milyon TL

Örtülü sermayeye isabet eden faiz:

`4.000.000 × (10.000.000 / 40.000.000) = 1.000.000 TL`

Bu 1 milyon önce KVK m.12 nedeniyle KKEG.

Yıl sonu:
- Toplam yabancı kaynak = 50 milyon TL
- Öz kaynak = 20 milyon TL
- Aşan yabancı kaynak = 30 milyon TL
- Aşan oran = `30 / 50 = %60`
- Toplam finansman gideri = 5 milyon TL

FGK havuzuna 5 milyonun tamamı değil:

`5.000.000 - 1.000.000 = 4.000.000 TL`

girer.

Aşan kısma isabet eden finansman gideri:

`4.000.000 × %60 = 2.400.000 TL`

Örnekte %10 FGK parametresi kullanılırsa:

`2.400.000 × %10 = 240.000 TL`

ek FGK-KKEG oluşur.

> Ders: **Testler ayrı, gider havuzu ortak olabilir. Önce mükerrerliği temizle.**

`%10` parametresi Mevzuat MCP ile 2026 güncellik teyidi yapılmadan “güncel oran” etiketi taşımamalıdır.

---

# 4. İkinci büyük bulgu: “Ticari borç” güvenli liman değildir

En önemli özelgelerden biri 29.12.2023 tarihli 62030549-125-1546854 sayılı özelge.

İdarenin yaklaşımı özetle:

- Piyasa koşulları ve ticari teamüle uygun normal vade içindeki mal/hizmet borçları, sırf vadeli oldukları için örtülü sermaye hesabına girmez.
- **Normal vade aşılırsa** aşan vadeli borç finansman karakteri kazanabilir.
- Bu şekilde oluşan örtülü sermayeye isabet eden vade farkları, örtülü sermaye üzerinden ödenen faiz gibi değerlendirilebilir.

22.05.2023 tarihli 31435689-125-73618 sayılı özelge de ilişkili kişiler arasındaki mal/hizmet alımlarında bu mantığı destekleyen somut bir örnek içerir.

## Yeni kontrol sorusu

Eski soru:

> “Bu borç ticari borç mu?”

Yeni soru:

> **“Bu ticari borcun emsal/piyasa vadesi ne ve bu vade aşılmış mı?”**

### Analojisi

Bir restoranda 30 gün vadeyle hesap açılması ticari teamül olsun. Hesap 30. günde kapanırsa ticari ilişkidir. Ama borç 18 ay boyunca taşınıyorsa isim hâlâ “mal borcu” olsa bile ekonomik fonksiyonu artık krediye benzemeye başlar.

**Etiket değil, ekonomik fonksiyon.**

---

# 5. Üçüncü büyük bulgu: Karşı düzeltme otomatik değil

Örtülü sermayede borç alan taraf faiz giderini KKEG yaptığında, borç veren tarafta bu tutarın kâr payı niteliği ve iştirak kazancı istisnası gündeme gelebilir.

Fakat sistem “borçlu 1 milyon KKEG yaptı → alacaklı otomatik 1 milyon istisna” kadar basit değildir.

03.10.2024 tarihli 38418978-299[03-2023/40]-564744 sayılı özelgede İdare, borç veren tarafından yapılacak düzeltmede **örtülü sermaye kullanan kurumun ödediği vergilerin dikkate alınması** gerektiğini belirtmiştir.

Özel olayda borç alan kurum yatırım teşvik belgesi nedeniyle indirimli kurumlar vergisi oranları kullanmaktadır. Bu nedenle nominal KKEG tutarı ile borç veren tarafta düzeltilebilecek/istisnaya konu edilebilecek tutar arasında otomatik eşitlik kurulmamaktadır.

## Akılda kalıcı zincir

```text
KKEG
  ↓
matrah etkisi
  ↓
uygulanan KV oranı
  ↓
kesinleşen vergi
  ↓
ödenen vergi
  ↓
karşı düzeltme
```

## Önemli araştırma ihtiyacı

Danıştay Dergisi'nde yayımlanan 2025 tarihli bir çalışmada Danıştay 9. Dairesinin 16.05.2024 tarihli E.2023/4917, K.2024/2755 sayılı kararına atıfla, borç alan kurumun zarar etmesi nedeniyle ödenecek kurumlar vergisi çıkmamasının borç verenin iştirak kazancı istisnasına engel olmayacağı yönünde yargısal yaklaşım aktarılmaktadır.

Bu, **idari özelge yaklaşımı ile yargısal yaklaşım arasında önemli bir araştırma başlığı** doğuruyor.

Bu nedenle atomda:

`OZELGE_GORUSU` ve `YARGI_GORUSU`

ayrı node'lar olmalı; yargı kararının tam metni Yargı MCP ile teyit edilmeden kesinleştirilmemelidir.

---

# 6. Dördüncü büyük bulgu: Avans da finansman olabilir

08.12.2022 tarihli 38418978-125[6-2021/21-İ]-573035 sayılı GİB özelgesi, alınan sipariş avanslarının FGK bakımından önemini gösteriyor.

İdare, avansların işletmeye finansman imkânı sağladığını ve borç niteliğinde kabul edilmesi gerektiğini belirtiyor. Bu nedenle kısa vadeli yabancı kaynaklarda izlenen dövizli sipariş avansına ilişkin kambiyo zararı FGK hesabında dikkate alınabiliyor.

## Sınav tuzağı

> “Bu banka kredisi değil, o halde finansman gider kısıtlaması yok.”

Yanlış.

FGK'da “kredi” ile “yabancı kaynak” aynı kavram değildir.

## Daha ince ayrım

KVK Genel Tebliği 11.13.4'e göre bir giderin FGK'ya girmesi için yabancı kaynak kullanımına ve **kaynağın kullanım süresine bağlı** olarak doğması önemlidir.

Örneğin:
- kredi faizi → kullanım süresine bağlı
- kredi faizine bağlı bazı mali yükler → kullanım süresine bağlı olabilir
- damga vergisi / havale ücreti gibi tek seferlik bazı giderler → kullanım süresine bağlı olmadığından FGK dışında kalabilir

Bu ayrım ezberden çok “giderin ekonomik davranışı” ile anlaşılmalıdır.

---

# 7. Beşinci büyük bulgu: Yabancı ortaktan kredi = dört katmanlı kontrol

14.11.2022 tarihli 62030549-125[12-2019/496]-1328479 sayılı GİB özelgesi yabancı ortak finansmanının ne kadar çok kanuna dokunduğunu iyi gösteriyor.

Özelgedeki olayda yabancı ana ortaktan kredi kullanılıyor. İdare hem kurumlar vergisi / anlaşma hükümleri hem de KDV boyutunu inceliyor.

## Kontrol katmanları

### 1. KVK m.12 — Örtülü sermaye
Borç miktarı / dönem başı öz sermaye.

### 2. KVK m.13 — Emsal faiz
Faiz oranı ilişkili kişiler arası emsal ilkesine uygun mu?

### 3. Stopaj + ÇVÖA
Faizi elde eden yabancı kurumun mukimliği, anlaşma maddesi ve gerçek lehdarlık gibi hususlar.

Özelgedeki somut olayda ilgili ÇVÖA faiz maddesi üzerinden tevkifat değerlendirmesi yapılmıştır.

### 4. KDV
Yurt dışındaki ilişkili şirketin Türkiye'deki şirkete sağladığı kredi, finansman hizmetidir.

Türkiye'de bu hizmetten yararlanıldığında, yabancı şirketin Türkiye'de ikametgâhı/işyeri/kanuni merkezi/iş merkezi bulunmaması halinde faiz üzerinden KDV'nin yurt içindeki muhatap tarafından sorumlu sıfatıyla beyanı gündeme gelir.

Özelge, somut olayda bu şekilde sorumlu sıfatıyla beyan edilip ödenen KDV'nin KDVK m.30/d çerçevesinde indiriminin mümkün olduğunu belirtmektedir.

---

# 8. KDV m.30/d — hâlâ açık uç

Mevcut Atom 3'ün iyi yakaladığı bir nokta var:

KDV m.30/d parantez içi istisnada KVK m.13 transfer fiyatlandırmasını açıkça anıyor; KVK m.12 örtülü sermayeyi aynı biçimde anmıyor.

Bu negatif metin farkı ilginçtir.

Ancak 14.11.2022 özelgesindeki sonuçtan:

> “KVK m.12 nedeniyle KKEG olan her faiz için KDV her durumda indirilebilir.”

gibi genel sonuç çıkarılmamalıdır.

Çünkü özelge kendi somut olayı içinde KV/ÇVÖA/transfer fiyatlandırması/KDV zincirini birlikte değerlendiriyor.

Bu nedenle doğru statü:

`[AÇIK UÇ — özelge/yargı taraması devam etmeli]`

---

# 9. Altıncı büyük bulgu: Örtülü sermaye ile FGK farklı zaman fotoğrafları kullanır

### Örtülü sermaye
KVK m.12, hesap dönemi içinde **herhangi bir tarihte** üç kat aşımına bakar.

### FGK
KVK Genel Tebliği 11.13.2, yabancı kaynak / öz kaynak karşılaştırmasını geçici vergi dönemi sonu ve yıllık dönem sonu bilançoları üzerinden yaptırır.

## Analojisi

- Örtülü sermaye = **güvenlik kamerası**. Yıl içinde herhangi bir anda ihlal oldu mu diye kayıtları tarar.
- FGK = **fotoğraf makinesi**. Belirli bilanço tarihindeki görüntüyü çeker.

Bu iki sistemi aynı tarih mantığıyla çözmek hata üretir.

BDO 2024/014 ayrıca sonraki geçici dönemde FGK kapsamına girilmesinin önceki döneme ilişkin finansman giderlerini geriye dönük olarak kısıtlamaya sokmaması gerektiğini açıklamaktadır. Bu açıklama `UZMAN_GORUSU` statüsündedir.

---

# 10. Yedinci büyük bulgu: Köprü kredide fiili kullanıcıya bak

KVK Genel Tebliği 11.13.4'e göre bir işletmenin bankadan temin ettiği kredi, üzerinde finansman yükü kalmadan grup şirketine aktarılırsa, finansman gideri krediyi devralan ve fiilen kullanan şirket bünyesinde FGK'ya tabi tutulur.

BDO 2024/014 de bu ayrımı uygulama açısından öne çıkarıyor.

## Sınav tuzağı

> “Krediyi bankadan A şirketi çekti; FGK her durumda A'dadır.”

Yanlış olabilir.

Sor:

> **Finansman yükü fiilen kimde kaldı?**

---

# 11. BDO'nun konuya kattığı “trick” bakışlar

BDO 2024/014'ten Atom 3'e aktarılmaya değer başlıklar:

1. **Duplike KKEG olmaz.**
2. Finansman giderinde **kullanım süresine bağlılık** önemlidir.
3. **Köprü kredi** fiili kullanıcıda FGK yaratır.
4. Faiz geliri ile faiz gideri genel olarak netleştirilemez; aynı yabancı kaynağa ilişkin kur farkı gelir/gideri için özel netleştirme mantığı vardır.
5. FGK testi dönem sonu bilançolarıyla çalışır; geçici dönemler arası geriye dönük etki kurulmamalıdır.
6. BDO, mevcut yabancı kaynak/özkaynak rasyosunun ekonomik gerçekliği her zaman iyi ölçmediğine dair eleştirel görüş de sunmaktadır. Bu son kısım **hukuki kural değil uzman değerlendirmesidir**.

BDO 2026/030 ayrıca 2025 kurumlar vergisi beyannamesindeki Transfer Fiyatlandırması / Kontrol Edilen Yabancı Kurum / Örtülü Sermaye formunun doldurulmasına ilişkin güncel uygulama rehberi niteliğindedir. Bu kaynak, ileride Atom 3'e **beyanname çapraz kontrol katmanı** eklemek için ayrıca işlenmelidir.

---

# 12. Vergi incelemesi açısından çapraz kontrol zinciri

İlişkili kişi borçlanması yalnız hukuk sorusu değil, veri tutarlılığı sorusudur.

Aşağıdaki zincir kurulabilir:

```text
CARİ HESAP / DEFTER
   ↓
ilişkili kişi borç hareketleri
   ↓
yıl içi maksimum borç
   ↓
dönem başı öz sermaye
   ↓
KVK m.12 üç kat testi
   ↓
faiz / kur farkı / vade farkı
   ↓
KKEG kayıtları
   ↓
KVK m.13 emsal faiz çalışması
   ↓
FGK dönem sonu bilanço testi
   ↓
mükerrer KKEG temizliği
   ↓
KV beyannamesi / ilişkili kişi formu / TP raporu
```

Yabancı ilişkili kişi varsa:

```text
+ mukimlik belgesi
+ ÇVÖA maddesi
+ gerçek lehdarlık
+ stopaj
+ 2 No.lu KDV / sorumlu sıfatı
```

## İnceleme sinyalleri

- Cari hesap maksimum borcu ile örtülü sermaye formundaki tutar açıklanamıyorsa
- Faiz gideri var ama emsal faiz çalışması yoksa
- Örtülü sermaye KKEG'si ile FGK hesabında mükerrerlik varsa
- Uzun süre taşınan “ticari borç” için emsal vade analizi yoksa
- Yabancı ortak faizinde KDV/stopaj/ÇVÖA zinciri eksikse
- Borç veren iştirak kazancı istisnası uygulamış fakat borç alanın vergi sonucu kontrol edilmemişse

araştırma derinleştirilmelidir.

---

# 13. Sınav öncesi “7 saniyelik” özet

1. **m.12:** Borç ne kadar?
2. **m.13:** Faiz kaç?
3. **FGK:** Toplam yabancı kaynak fazla mı?
4. **Mükerrer KKEG yok.**
5. **Ticari borçta emsal vadeyi sor.**
6. **Karşı düzeltmede ödenen vergiyi kontrol et.**
7. **Avans da yabancı kaynak olabilir.**
8. **Yabancı ortak → KDV + stopaj + ÇVÖA.**
9. **m.12 = dönem içi herhangi an; FGK = dönem sonu bilanço.**
10. **Köprü kredi → fiili kullanıcı.**

---

# 14. Bülten 001'den türetilecek atomik node'lar

```text
NODE: UC_MUESSESE
NODE: MUKERRER_KKEG_KAPISI
NODE: TICARI_BORC_EMSAL_VADE
NODE: KARSI_DUZELTME_ODENEN_VERGI
NODE: AVANS_YABANCI_KAYNAK
NODE: YABANCI_ORTAK_DORT_KATMAN
NODE: KDV_M30D_ACIK_UC
NODE: ZIT_ZAMAN_TESTI
NODE: KOPRU_KREDI_FIILI_KULLANICI
NODE: BEYANNAME_CAPRAZ_KONTROL
```

Önerilen temel edge'ler:

```text
ORTULU_SERMAYE_KKEG --[ONCELIKLIDIR]--> FGK_HESABI
MUKERRER_KKEG_KAPISI --[MUKERRERLIGI_ONLER]--> FGK_KKEG
TICARI_BORC --[VADE_ASILIRSA]--> FINANSMAN_KARAKTERI
FINANSMAN_KARAKTERI --[TETIKLER]--> ORTULU_SERMAYE
ALINAN_AVANS --[FINANSMAN_SAGLAR]--> YABANCI_KAYNAK
YABANCI_ORTAK_KREDISI --[KDV_KOPRUSU]--> SORUMLU_SIFATIYLA_KDV
ORTULU_SERMAYE --[ZAMAN_TESTI]--> DONEM_ICI_HERHANGI_TARIH
FGK --[ZAMAN_TESTI]--> DONEM_SONU_BILANCO
KOPRU_KREDI --[FGK_YUKU]--> FIILI_KULLANICI
KVK_M12_KKEG --[ACIK_UC]--> KDV_M30D
```

---

# 15. Kaynaklar ve statü

## RESMİ / BİRİNCİL

1. **1 Seri No.lu KVK Genel Tebliği — 11.13 FGK**
   - https://gib.gov.tr/mevzuat/kanun/435/teblig/8557

2. **14.11.2022 — 62030549-125[12-2019/496]-1328479**
   - Konu: Yurt dışındaki şirket ortağı firmadan kredi alınması işleminde KV ve KDV
   - https://gib.gov.tr/mevzuat/kanun/435/ozelge/33449

3. **08.12.2022 — 38418978-125[6-2021/21-İ]-573035**
   - Konu: Alınan Sipariş Avansları hesabına ilişkin kambiyo zararının FGK
   - https://gib.gov.tr/mevzuat/kanun/435/ozelge/28357

4. **29.12.2023 — 62030549-125-1546854**
   - Konu: Örtülü sermaye kapsamında vade farklarının belirlenmesi
   - https://gib.gov.tr/mevzuat/kanun/435/ozelge/28375

5. **03.10.2024 — 38418978-299[03-2023/40]-564744**
   - Konu: Örtülü sermayeye bağlı düzeltmede indirimli kurumlar vergisi oranı
   - https://gib.gov.tr/mevzuat/kanun/435/ozelge/28374

## GİB ARŞİV KOPYASI / İKİNCİL ERİŞİM

6. **22.05.2023 — 31435689-125-73618**
   - Konu: İlişkili mal/hizmet alımlarında vade farkı ve örtülü sermaye
   - https://mevzuat.vergibulustayi.com/belge.php?id=28376&tur=ozelge
   - Not: Kaynak sayfa GİB arşivinden alınmış yerel kopya olduğunu belirtmektedir.

## UZMAN GÖRÜŞÜ

7. **BDO Denet 2024/014 — Finansman Gider Kısıtlamasında Doğru Rasyo Doğru Yaklaşım**
   - https://www.bdo.com.tr/getattachment/13e1b68a-8d67-46b0-9d02-e69e07d0a49c/DUYURU014-424.pdf?ext=.pdf&lang=tr-TR

8. **BDO Transfer Fiyatlandırması SSS**
   - https://www.bdo.com.tr/tr-tr/hizmetlerimiz/vergi/transfer-fiyatlandirmasi/transfer-fiyatlandirmasi-sikca-sorulan-sorular

9. **BDO 2026/030 — 2025 KV beyannamesi / EK-2 rehberi**
   - BDO yayın arşivinde 2026/030 olarak tespit edildi.
   - Ayrıntılı satır bazlı işleme, PDF'in yeniden doğrulanabildiği ayrı turda yapılmalıdır.

## YARGI AÇIK UCU

10. Danıştay Dergisi Sayı 160 (Temmuz 2025), kur farkları çalışması; Danıştay 9. Daire E.2023/4917, K.2024/2755 atfı.
   - Karar tam metni Yargı MCP ile ayrıca doğrulanmalıdır.

---

# 16. Bilinen sınırlar

- Bu ChatGPT oturumunda **Mevzuat MCP erişilebilir değildi**. Resmî GİB web kayıtları kullanıldı; MCP teyidi yapılmış sayılmamalıdır.
- Özelgeler somut olaya verilen idari görüşlerdir; genel düzenleyici işlem değildir.
- BDO açıklamaları `UZMAN_GORUSU` statüsündedir.
- 2025-2026 döneminde konuya doğrudan daha yeni bir özelge bu taramada bulunamadı; bu “yoktur” anlamına gelmez.
- KDV m.30/d ↔ KVK m.12 ilişkisi açık uç olarak tutulmalıdır.
- Yargısal yaklaşım tam karar metni görülmeden atomik kesin kurala dönüştürülmemelidir.
