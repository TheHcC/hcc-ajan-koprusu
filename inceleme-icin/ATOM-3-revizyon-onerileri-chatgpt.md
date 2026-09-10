---
konu: ATOM-3 revizyon önerileri
kaynak_atom: inceleme-icin/ATOM-3-iliskili-kisiden-borclanma.md
hazirlayan: gpt-5.6-sol (ChatGPT)
tarih: 2026-09-10
durum: ONERI
---

# ATOM-3 Revizyon Önerileri — İlişkili Kişiden Borçlanma

Bu not, mevcut Atom 3'ü doğrudan değiştirmez. Son özelge ve BDO taramasından çıkan eklemeleri, düzeltmeleri ve yeni node/edge önerilerini kanonik dosyada uygulanmak üzere ayrı tutar.

## 1. Ana tezi hassaslaştır

Mevcut tez:

> Üç müessese aynı anda ve birbirinden bağımsız bakar.

Önerilen yeni tez:

> **Örtülü sermaye, transfer fiyatlandırması ve finansman gider kısıtlamasının tetikleyicileri birbirinden bağımsızdır; ancak aynı finansman giderinin vergisel sonuçları hesaplanırken sıra ve mükerrer KKEG yasağı gözetilir.**

Gerekçe: 1 Seri No.lu KVK Genel Tebliği 11.13.9, örtülü sermaye / transfer fiyatlandırması / binek oto kısıtlaması nedeniyle zaten KKEG yapılmış finansman giderlerinin FGK hesabında yeniden dikkate alınmayacağını açıkça düzenler.

Kaynak:
- GİB KVK Genel Tebliği 11.13.9: https://gib.gov.tr/mevzuat/kanun/435/teblig/8557
- BDO 2024/014: https://www.bdo.com.tr/getattachment/13e1b68a-8d67-46b0-9d02-e69e07d0a49c/DUYURU014-424.pdf?ext=.pdf&lang=tr-TR

## 2. Yeni node: `MUKERRER_KKEG_KAPISI`

```yaml
id: ATOM3-N01
node: MUKERRER_KKEG_KAPISI
claim: Örtülü sermaye veya transfer fiyatlandırması nedeniyle zaten KKEG yapılan finansman gideri FGK hesabına ikinci kez girmez.
source_status: RESMI
source: KVK Genel Tebliği 11.13.9
links:
  - EDGE: ORTULU_SERMAYE_KKEG --[ONCELIKLIDIR]--> FGK_HESABI
  - EDGE: TRANSFER_FIYATLANDIRMASI_KKEG --[ONCELIKLIDIR]--> FGK_HESABI
  - EDGE: MUKERRER_KKEG_KAPISI --[MUKERRERLIGI_ONLER]--> FGK_KKEG
trap: Üç müessese bağımsızdır = aynı gider üç kez KKEG yapılır değildir.
```

## 3. Yeni node: `TICARI_BORC_EMSAL_VADE`

29.12.2023 tarihli 62030549-125-1546854 sayılı özelge ve 22.05.2023 tarihli 31435689-125-73618 sayılı özelge, ilişkili kişiler arası ticari borçlarda kritik sorunun yalnız “borç ticari mi?” olmadığını gösterir.

Yeni kontrol:

> **Piyasa koşulları ve ticari teamüle uygun normal vade aşılmış mı?**

Normal vade aşılmışsa, aşan vadeli borç örtülü sermaye testine girebilir ve ilgili vade farkı örtülü sermaye üzerinden ödenen faiz gibi değerlendirilebilir.

```yaml
id: ATOM3-N02
node: TICARI_BORC_EMSAL_VADE
claim: İlişkili ticari borç, piyasa/teamül vadesini aşınca finansman karakteri kazanabilir ve KVK m.12 testine girebilir.
source_status: OZELGE
source:
  - GIB 29.12.2023, 62030549-125-1546854
  - GIB 22.05.2023, 31435689-125-73618
links:
  - EDGE: TICARI_BORC --[VADE_ASILIRSA]--> FINANSMAN_KARAKTERI
  - EDGE: FINANSMAN_KARAKTERI --[TETIKLER]--> ORTULU_SERMAYE_TESTI
trap: “Ticari borçtur, örtülü sermayeye girmez” otomatik sonucu yanlıştır.
```

## 4. Yeni node: `KARSI_DUZELTME_VERGI_ODENMIS`

03.10.2024 tarihli 38418978-299[03-2023/40]-564744 sayılı özelge, borç veren taraftaki düzeltmenin nominal KKEG tutarına mekanik biçimde eşit olmadığını gösterir.

Özelgede düzeltmede dikkate alınacak tutarın, örtülü sermaye kullanan kurumun **ödediği vergiler dikkate alınarak** hesaplanması gerektiği belirtilmiştir.

```yaml
id: ATOM3-N03
node: KARSI_DUZELTME_VERGI_ODENMIS
claim: Borç veren taraftaki düzeltmede yalnız KKEG tutarına değil, borç alan tarafta kesinleşen/ödenen vergi sonucuna bakılır.
source_status: OZELGE
source: GIB 03.10.2024, 38418978-299[03-2023/40]-564744
links:
  - EDGE: BORCLU_KKEG --[TEK_BASINA_YETMEZ]--> BORC_VEREN_ISTISNA
  - EDGE: ODENEN_VERGI --[SINIRLAR]--> KARSI_DUZELTME
trap: Borçlu 1 milyon KKEG yaptıysa borç veren otomatik 1 milyon iştirak kazancı istisnası uygular varsayımı.
```

### Çelişki / araştırma uyarısı

Danıştay Dergisi'nin 2025 tarihli bir çalışmasında, Danıştay 9. Dairesinin 16.05.2024 tarihli E.2023/4917, K.2024/2755 sayılı kararına atıfla, borç alanın zarar nedeniyle ödenecek KV'si çıkmamasının borç verenin istisnasına engel olmadığı yönünde yargısal yaklaşım aktarılmaktadır.

Bu nedenle bu node yalnız özelge görüşü olarak yazılmalı; **idari görüş ≠ kesin yargısal sonuç** ayrımı kurulmalı ve Yargı MCP / karar tam metni ile ayrıca teyit edilmelidir.

## 5. Yeni node: `AVANS_DA_YABANCI_KAYNAK`

08.12.2022 tarihli 38418978-125[6-2021/21-İ]-573035 sayılı özelgeye göre alınan sipariş avansı işletmeye finansman imkânı sağlar ve borç niteliğindedir; buna ilişkin kambiyo zararı FGK hesabında dikkate alınabilir.

```yaml
id: ATOM3-N04
node: AVANS_DA_YABANCI_KAYNAK
claim: Klasik banka kredisi olmayan alınan sipariş avansı da işletmeye finansman sağladığı için FGK bakımından yabancı kaynak/borç niteliği doğurabilir.
source_status: OZELGE
source: GIB 08.12.2022, 38418978-125[6-2021/21-İ]-573035
links:
  - EDGE: ALINAN_SIPARIS_AVANSI --[FINANSMAN_SAGLAR]--> YABANCI_KAYNAK
  - EDGE: AVANS_KUR_ZARARI --[TETIKLEYEBILIR]--> FGK
trap: “Kredi hesabında değilse FGK yok” varsayımı.
```

## 6. Yeni node: `YABANCI_ORTAK_KREDISI_DORT_KATMAN`

14.11.2022 tarihli 62030549-125[12-2019/496]-1328479 sayılı özelge, yabancı ortaktan finansmanın yalnız KVK m.12 ile bitmediğini gösterir. Kredi/faiz ilişkisi için KV/ÇVÖA ve KDV boyutları birlikte açılır.

Özelge, yurt dışındaki ana ortak tarafından sağlanan finansman hizmetinden Türkiye'de yararlanılması halinde faiz üzerinden sorumlu sıfatıyla KDV beyanını; ayrıca özelgedeki somut olayda faiz ödemesi için ÇVÖA/tevkifat değerlendirmesini ele almaktadır.

```yaml
id: ATOM3-N05
node: YABANCI_ORTAK_KREDISI_DORT_KATMAN
claim: Yabancı ortak kredisi; KVK m.12, KVK m.13/emsal, stopaj-ÇVÖA ve KDV sorumluluğu katmanlarıyla birlikte incelenmelidir.
source_status: OZELGE
source: GIB 14.11.2022, 62030549-125[12-2019/496]-1328479
links:
  - EDGE: YABANCI_ORTAK_KREDISI --[TETIKLER]--> ORTULU_SERMAYE
  - EDGE: YABANCI_ORTAK_KREDISI --[TETIKLER]--> EMSAL_FAIZ
  - EDGE: FAIZ_ODEMESI --[TETIKLER]--> STOPAJ_CVOA
  - EDGE: YURTDISI_FINANSMAN_HIZMETI --[KDV_KOPRUSU]--> SORUMLU_SIFATIYLA_KDV
```

## 7. KDV m.30/d açık ucunu koru; ama özelge ile zenginleştir

Mevcut atomda KDV m.30/d'nin parantez içi istisnasının KVK m.13'ü açıkça sayıp KVK m.12'yi saymaması bir `[CIKARIM]` olarak işaretlenmişti. Bu statü korunmalıdır.

14.11.2022 özelgesi, somut olayda yurt dışı finansman hizmetine ilişkin sorumlu sıfatıyla beyan edilen KDV'nin m.30/d çerçevesinde indiriminin mümkün olduğunu ifade etmektedir; ancak bu özelge, **yalnız KVK m.12 nedeniyle KKEG olan faize ait KDV** problemini soyut ve bağımsız şekilde çözmüş sayılmamalıdır.

Yeni edge:

`KVK_M12_KKEG --[ACIK_UC]--> KDV_M30D`

Statü: `TEYIT / YARGI-ÖZELGE TARAMASI GEREKLİ`

## 8. Yeni node: `FGK_ZAMAN_TESTI`

KVK Genel Tebliği 11.13.2'ye göre FGK yabancı kaynak/öz kaynak testi her geçici vergi dönemi sonu ve yıllık dönem sonu bilançosu üzerinden yapılır.

Örtülü sermayede ise KVK m.12 “hesap dönemi içinde herhangi bir tarihte” üç kat aşımına bakar.

```yaml
id: ATOM3-N06
node: ZIT_ZAMAN_TESTI
claim: Örtülü sermaye dönem içindeki herhangi bir aşımı ararken, FGK ilgili beyan dönemi sonu bilançosuna bakar.
source_status: RESMI
source:
  - KVK m.12
  - KVK Genel Tebliği 11.13.2
links:
  - EDGE: ORTULU_SERMAYE --[ZAMAN_TESTI]--> DONEM_ICI_HERHANGI_TARIH
  - EDGE: FGK --[ZAMAN_TESTI]--> DONEM_SONU_BILANCO
trap: İki müessesede aynı tarih/bakiye mantığını kullanmak.
```

BDO 2024/014 ayrıca bir sonraki geçici dönemde FGK kapsamına girmenin önceki dönemin finansman giderlerini geriye dönük olarak kısıtlamaya sokmaması gerektiğini açıklamaktadır. Bu kısım `UZMAN_GORUSU` olarak tutulmalıdır.

## 9. Yeni node: `KOPRU_KREDI_FIILI_KULLANICI`

KVK Genel Tebliği 11.13.4 ve BDO 2024/014: Bankadan alınan kredi, aracı şirket üzerinde finansman yükü kalmadan grup şirketine aktarılıyorsa FGK fiilen kullanan şirket bünyesinde değerlendirilir.

```yaml
id: ATOM3-N07
node: KOPRU_KREDI_FIILI_KULLANICI
claim: Köprü kredide FGK açısından kredi maliyeti aracı üzerinde kalmıyorsa fiili kullanıcıya gider.
source_status: RESMI
source: KVK Genel Tebliği 11.13.4
links:
  - EDGE: KOPRU_KREDI --[FGK_YUKU]--> FIILI_KULLANICI
trap: Krediyi ilk alan şirket her durumda FGK yükünü taşır varsayımı.
```

## 10. Hesaplama sırası için mini örnek

**Öğretici varsayım — gerçek mükellef verisi değildir.**

- Dönem başı öz sermaye: 10 milyon TL
- İlişkili kişiden borç: 40 milyon TL
- Üç kat sınırı: 30 milyon TL
- Örtülü sermaye kısmı: 10 milyon TL
- İlişkili borca ait toplam faiz: 4 milyon TL

Oransal olarak örtülü sermayeye isabet eden faiz:

`4.000.000 × (10.000.000 / 40.000.000) = 1.000.000 TL`

Bu 1 milyon TL önce KVK m.12 nedeniyle KKEG'dir.

Varsayalım yıl sonu:
- Toplam yabancı kaynak: 50 milyon TL
- Öz kaynak: 20 milyon TL
- Aşan yabancı kaynak: 30 milyon TL
- Aşan oran: `30/50 = %60`
- Toplam finansman gideri: 5 milyon TL

FGK hesabına **5 milyonun tamamı** değil, daha önce KKEG olan 1 milyon çıkarıldıktan sonra kalan 4 milyon girer.

`4.000.000 × %60 = 2.400.000 TL`

Mevcut %10 kısıtlama parametresi varsayımıyla:

`2.400.000 × %10 = 240.000 TL FGK-KKEG`

**Ana ders:** Üç müessese farklı testtir; fakat aynı gider iki kez KKEG yapılmaz.

`%10` parametresi Mevzuat MCP ile 2026 güncellik teyidi yapılmadan “güncel oran” olarak etiketlenmemelidir.

## 11. Atomik node/edge özeti

```text
[TICARI_BORC]
   --VADE_ASILIRSA--> [FINANSMAN_KARAKTERI]
   --TETIKLER-------> [ORTULU_SERMAYE]

[ORTULU_SERMAYE_KKEG]
   --ONCELIKLIDIR--> [FGK_HESABI]
   --MUKERRERLIGI_ONLER--> [IKINCI_KKEG]

[ALINAN_SIPARIS_AVANSI]
   --FINANSMAN_SAGLAR--> [YABANCI_KAYNAK]
   --KUR_ZARARI--------> [FGK]

[YABANCI_ORTAK_KREDISI]
   --> [KVK_M12]
   --> [KVK_M13_EMSAL]
   --> [STOPAJ_CVOA]
   --> [KDV_SORUMLULUK]

[ORTULU_SERMAYE]
   --ZAMAN_TESTI--> [DONEM_ICI_HERHANGI_TARIH]

[FGK]
   --ZAMAN_TESTI--> [DONEM_SONU_BILANCO]

[KOPRU_KREDI]
   --FGK_YUKU--> [FIILI_KULLANICI]

[KVK_M12_KKEG]
   --ACIK_UC--> [KDV_M30D]
```

## 12. Kaynak listesi

### Resmî / birincil
- KVK Genel Tebliği 11.13: https://gib.gov.tr/mevzuat/kanun/435/teblig/8557
- GİB 14.11.2022 özelgesi: https://gib.gov.tr/mevzuat/kanun/435/ozelge/33449
- GİB 08.12.2022 özelgesi: https://gib.gov.tr/mevzuat/kanun/435/ozelge/28357
- GİB 29.12.2023 özelgesi: https://gib.gov.tr/mevzuat/kanun/435/ozelge/28375
- GİB 03.10.2024 özelgesi: https://gib.gov.tr/mevzuat/kanun/435/ozelge/28374

### GİB arşiv kopyası / ikincil erişim
- 22.05.2023 özelgesi: https://mevzuat.vergibulustayi.com/belge.php?id=28376&tur=ozelge

### Uzman görüşü
- BDO 2024/014: https://www.bdo.com.tr/getattachment/13e1b68a-8d67-46b0-9d02-e69e07d0a49c/DUYURU014-424.pdf?ext=.pdf&lang=tr-TR
- BDO Transfer Fiyatlandırması SSS: https://www.bdo.com.tr/tr-tr/hizmetlerimiz/vergi/transfer-fiyatlandirmasi/transfer-fiyatlandirmasi-sikca-sorulan-sorular

## Sınırlar

- Mevzuat MCP bu ChatGPT oturumunda erişilebilir değildi; 2026 güncellik teyidi MCP üzerinden yapılmadı.
- Özelgeler somut olaylara verilen idari görüşlerdir; genel düzenleyici işlem gibi sunulmamalıdır.
- BDO yorumları uzman görüşüdür.
- Borç veren düzeltmesinde idari görüş ile yargısal yaklaşım arasında potansiyel ayrışma bulunduğundan Yargı MCP ile ayrı doğrulama önerilir.
