---
konu: Sat-kirala-geri al — kazanç istisnası, özel fon ve amortismanın bölüştürülmesi
ders: [Revizyon, Vergi Tekniği]
yuzey_profili: poster-tablo
dayanak:
  - KVK m.5/1-j        # 6728 s.K. m.56 (15/7/2016) ile eklendi — bent harfi TEYİT EDİLDİ (teyit turu 01)
  - KDV m.17/4-y       # 6728 s.K. ile değişik
iliskili_maddeler:
  - KVK m.5/1-e        # ⚠️ 7456 s.K. (15/7/2023) ile TAŞINMAZ bu bentten ÇIKARILDI; bent artık
                       # iştirak hissesi vb. için %75. Taşınmazda Geçici m.16 ile %25 (sadece
                       # 15/7/2023 öncesi iktisap). Fon disiplini benzetmesi ARTIK GEÇERSİZ.
  - KDV m.30/a         # indirim iptali — 17/4-y bu listede YOK
  - VUK mük. m.290     # finansal kiralama işlemlerinde değerleme
  - VUK mük. m.298     # kullanma hakkının yeniden değerlemesi
  - 6361 s.K.          # Finansal Kiralama, Faktoring ve Finansman Şirketleri Kanunu
  - KVKUGT 5.15        # tebliğ açıklaması
  - KDVUGT II/4.21     # tebliğ açıklaması
gecis_kontrolu:
  kdv: "VAR + ZIT SONUC — m.17/4-y istisna, ANCAK m.30/a'nin parantez ici listesinde YOK (listede yalniz 17/2-b,c,d ve 17/4-i,o sayili). Indirim iptali ISLER. Telafi: devre kadar indirilemeyen KDV 'Ilave edilecek KDV' olarak beyan edilir ve gider yazilir. Bagis atomunun (17/2-b) tam TERSI."
  vuk: "VAR — muk. m.290 finansal kiralama degerlemesi: kiracida kullanma hakki ve borc, rayic bedel ile kira odemelerinin bugunku degerinden DUSUK olani ile degerlenir; kullanma hakki amortismana tabi. Ayrica finansal kiralama testi (dort olcutten biri yeterli)."
  gvk: "YOK (teyit turu 01, 09.09.2026) — GVK'da paralel hukum YOKTUR. KVK m.5/1-j istisnayi yalnizca 'kurumlar tarafindan' yapilan satislara taniyor; GVK m.38, m.40, m.81 ve muk. m.80'de ferdi isletmeler icin sat-kirala-geri al kazanc istisnasi bulunmuyor. Istisna kurumlar vergisi mukelleflerine ozgudur."
  kvk: "VAR — m.5/1-j istisnasi %100; kazanc ozel fona alinir; fonun amac disi kullanimi vergi ziyai cezasi dogurur."
  damga_harc: "VAR (teyit turu 01, 09.09.2026) — 6361 s.K. m.37/1: finansal kiralama sozlesmeleri, devir/tadil kagitlari, kiralayan-satici sozlesmeleri ve teminat kagitlari DAMGA VERGISINDEN, bu kagitlarla ilgili islemler HARCTAN mustesnadir (finansal kiralama konusu gayrimenkullerin kiralayanlarca devir alinmasina iliskin tapu islemleri haric). m.37/2: sat-kirala-geri al taşinmazlarinin sure sonunda kiraci adina tescili de tapu harcindan mustesna."
  donem_sarkmasi: "VAR — GUCLU. (a) Istisna satisin yapildigi donemde uygulanir, pesin/vadeli fark etmez. (b) Fona alma suresi: satisi izleyen hesap donemi basindan, kazancin beyan edildigi doneme ait KV beyannamesinin verildigi tarihe kadar. (c) Gecici vergi donemlerinde de yararlanilir; suresinde fona alinmazsa gecici vergiden dogan vergi ziyai cezasi ve gecikme faizi AYRICA aranir. (d) Amortisman farki kira suresi boyunca ve geri alim sonrasina sarkar."
  muhasebe_tms: "VAR — ozel fon hesabi acilir; geri alim sonrasi amortisman IKIYE BOLUNUR (bir kismi kurum kazancindan gider, kalani yalniz fondan mahsup); KDV tarafinda 'Ilave edilecek KDV' beyani."
gecerlilik_donemi: 2026
son_dogrulama: 2026-09-09
dogrulama_durumu: TEYITLI
teyit_kapsami: "Kanun metni duzeyinde teyit edildi (Gorev S / teyit-turu-01, bedesten.adalet.gov.tr). TEBLIG duzeyi (KVKUGT 5.15, KDVUGT II/4.21) TARANMADI."
kaynak: vtr-vir/mevzuat/{KVKUGT,KDV,KDVUGT,VUK}.md — yerel korpus, birebir okundu
---

# Sat-Kirala-Geri Al — KV × KDV × VUK

> Üç aşamalı **tek** bir işlemdir: kiracı varlığı satar → geri kiralar → süre sonunda
> geri alır. Aynı sözleşme kapsamındaki işlemler ayrıştırılıp farklı rejimlere tabi
> tutulamaz.

## 1. Kim, neyi, kime

| | |
|---|---|
| **Kiracı** | Varlığını geri kiralama amacıyla ve **sözleşme sonunda geri alınması şartıyla** devreden kurumlar vergisi mükellefi |
| **Kiralayan** | Finansal kiralama şirketleri · katılım bankaları · kalkınma ve yatırım bankaları — **bu üçü dışında kimse yok** |
| **Konu** | Her türlü **taşınır ve taşınmaz** (taşınırlar 9/8/2016'dan sonraki sözleşmelerde) |
| **İstisna oranı** | **%100** — kazancın tamamı |

Tam/dar mükellefiyet ayrımı istisna açısından önemsizdir.

## 2. Üç şart — biri eksikse istisna yok

1. **Sözleşmede iki hüküm bulunacak:** varlık kiracıya *geri kiralanacak* **ve** süre
   sonunda kiracı tarafından *geri alınacak*. Hükmün bulunması yetmez — **fiilen
   uyulacak.**
2. **Kazanç özel fon hesabına alınacak.** Süre: satışı izleyen hesap döneminin başından,
   kazancın beyan edildiği döneme ait KV beyannamesinin verildiği tarihe kadar.
3. **Fon işletmeden çekilmeyecek.**

## 3. Çekirdek mekanik — amortismanın ikiye bölünmesi

Konunun sınavda sayısal sorulduğu yer burasıdır. Kural: **satış bedeli üzerinden
amortisman ayrılır, ama vergi avantajı eski değerle sınırlıdır.**

KVKUGT 5.15.3.3'teki resmî örnek:

| Adım | Tutar |
|---|---|
| İktisap (13/5/2014) | 2.500.000 |
| Ayrılan amortisman | (500.000) |
| **Devir tarihinde net bilanço aktif değeri** | **2.000.000** |
| Satış (8/9/2016, katılım bankasına) | 3.000.000 |
| **İstisna kazanç → özel fona** | **1.000.000** |

Geri alındıktan sonra amortisman **3.000.000** üzerinden ayrılır. Ama:

```
Amortismanın 2.000.000'e isabet eden kısmı → kurum kazancının tespitinde GİDER
Amortismanın 1.000.000'e isabet eden kısmı → YALNIZCA özel fondan mahsup
```

**Okunuşu:** İstisna bir vergi affı değil, **ertelemedir.** Satışta vergilenmeyen
1.000.000, amortisman yoluyla ikinci kez kazanılmaz — fondan eritilir. Fon başka
hiçbir amaçla kullanılamaz.

### 3b. Yıllara yayılmış hesap (TÜRETİLMİŞ, doğrulandı)

> KVKUGT'nin resmî örneği tek yıllık toplamı verir. Aşağıdaki, 5 yıllık faydalı ömür
> varsayımıyla **yıl yıl** dağılımı gösterir — `scripts/dogrula_09bilgi_sayisal.py`
> ile doğrulanmıştır (09.09.2026). Sınavda "yıllık amortisman kaydını yapınız"
> istenirse aritmetik budur.

Varsayım: 3.000.000 üzerinden, 5 yıl faydalı ömürle **doğrusal amortisman**.

```
Gider payı  = 2.000.000 / 3.000.000  (net bilanço aktif değeri / satış bedeli)
Fon payı    = 1.000.000 / 3.000.000  (istisna kazanç / satış bedeli)
Yıllık amortisman = 3.000.000 / 5 = 600.000
```

| Yıl | Toplam amortisman | → Kurum kazancından gider | → Yalnız fondan mahsup |
|---|---|---|---|
| 1 | 600.000 | 400.000 | 200.000 |
| 2 | 600.000 | 400.000 | 200.000 |
| 3 | 600.000 | 400.000 | 200.000 |
| 4 | 600.000 | 400.000 | 200.000 |
| 5 | 600.000 | 400.000 | 200.000 |
| **Toplam** | **3.000.000** | **2.000.000** | **1.000.000** |

**Sağlama:** 5 yılın sonunda "yalnız fondan mahsup" sütunu tam olarak özel fonu
(1.000.000) eritir; "gider" sütunu tam olarak eski net bilanço aktif değerini
(2.000.000) karşılar. Fon bir kuruş fazla veya eksik erimemeli — eridiyse hesap
yanlıştır.

## 4. KDV köprüsü — bağış atomunun tam tersi

İki KDV istisnası, aynı maddenin iki fıkrası, **zıt sonuç**:

| | Bağış (m.17/2-b) | Sat-kirala-geri al (m.17/4-y) |
|---|---|---|
| İstisna var mı? | ✅ | ✅ |
| **m.30/a listesinde mi?** | ✅ **VAR** | ⛔ **YOK** |
| Yüklenilen KDV | **İndirilir** | **İndirilemez** — iptal işler |
| Telafi | gerekmez | İndirilemeyen kısım **"İlave edilecek KDV"** olarak beyan → **gider** yazılır |

**Kanıt — olumsuz delil.** m.30/a'nın parantezi yalnız `17/2-(b,c,d)` ve `17/4-(ı,ö)`
sayar; **(y) yoktur.** Üstelik kardeş bentlerde 30/a'yı devre dışı bırakan **açık cümle
var**, (y)'de yok:

> *(i) bendi:* "Bu bent kapsamında istisna edilen işlemler bakımından, 30 uncu maddenin
> birinci fıkrasının (a) bendi hükmü uygulanmaz."
>
> *KDVUGT 4.22, (z) bendi:* "…Kanunun (30/a) maddesi hükmü uygulanmayacağından… indirim
> hesaplarından çıkarılmak suretiyle düzeltilmesi gerekmez."

Bu cümlenin (y) bendinde **bulunmaması**, indirim iptalinin işlediğinin kanıtıdır.
Bendin kendi metnindeki tek telafi "gider olarak dikkate alınır"dır — indirim hakkı değil.

**Ayrıntı:** Devre kadar zaten indirilmiş kısım için **düzeltme yapılmaz**; yalnızca
indirilmemiş bakiye "İlave edilecek KDV" olur.

## 5. VUK tarafı — mükerrer m.290

- **Kiracıda:** kullanma hakkı ve borç, *rayiç bedel* ile *kira ödemelerinin bugünkü
  değerinden* **düşük olanı** ile değerlenir. Kullanma hakkı amortismana ve yeniden
  değerlemeye tabidir.
- **Kira ödemeleri** anapara ve faiz olarak ayrıştırılır; her dönem sonu kalan borca
  **sabit dönemsel faiz oranı** uygulanacak şekilde.
- Bu madde kapsamındaki borç ve alacaklar **reeskonta tabi tutulmaz.**
- **Finansal kiralama testi** — şu dördünden **biri** yeterli: mülkiyet devri ·
  düşük bedelle satın alma hakkı · sürenin ekonomik ömrün **%80**'ini aşması ·
  kira ödemelerinin bugünkü değerinin rayiç bedelin **%90**'ını aşması.

## 6. İhlal — iki farklı yaptırım, karıştırma

| Ne olursa | Yaptırım |
|---|---|
| Fon başka hesaba nakledilir / işletmeden çekilir / ana merkeze aktarılır / tasfiye | Zamanında tahakkuk ettirilmeyen vergiler **+ vergi ziyaı cezası + gecikme faizi** |
| Sözleşmeden kaynaklanan **yükümlülüklerin yerine getirilememesi** nedeniyle süreç tamamlanamaz | Vergiler **+ gecikme faizi** — **vergi ziyaı cezası UYGULANMAKSIZIN** |
| Kiralayan, süreç tamamlanmadan varlığı **üçüncü kişiye** satar | Kiralayan istisnadan yararlanamaz; vergileme, kiracıdaki ilk net bilanço aktif değeri ve toplam amortisman dikkate alınarak **kiralayan nezdinde** yapılır |

Ceza farkı bir kusur ayrımıdır: fonu çekmek iradi, sözleşmenin çökmesi değil.

**Bildirim yükümlülüğü:** Kiracı, ilk devir tarihindeki net bilanço aktif değerini — ve
tekrarlanan işlemlerde o tarihten itibaren ayrılan toplam amortismanı — kiralayana
**yazı ile** bildirir.

## Sınırlar

- ~~**Bent harfi çelişkisi**~~ → ✅ **ÇÖZÜLDÜ (teyit turu 01, 09.09.2026).** Bent
  **kesinlikle (j)**'dir *(Ek: 15/7/2016-6728/56 md.)*. Çelişkinin kök nedeni ilginç:
  güncel kanunda **(ı)** bendi eğitim/kreş-rehabilitasyon istisnası, **(i)** bendi
  kooperatif risturn istisnasıdır — yerel `KVK.md` dosyasında Türkçe **ı/i harflerinin
  ASCII dönüşümü** iki bendi çakıştırmış ve sıralama bir harf kaymış görünmüştür.
  Ayrıca o dosya 2006 gerekçe metni olduğu için 2016 eklemesini zaten içermiyor.
  → **Korpus bulgusu olarak kayıtlı:** yerel `KVK.md` güncel kanun metni değildir *ve*
  Türkçe harf dönüşümü bent sıralamasını bozmaktadır.
- **Güncellik teyidi yok** — Mevzuat MCP bağlanamadı; 2026 yürürlüğü doğrulanmadı.
- ~~Damga vergisi şeridi~~ → ✅ **ÇÖZÜLDÜ:** 6361 s.K. m.37/1 damga vergisi ve harç
  istisnası getiriyor (tapu işlemlerinde bir istisna hariç). Künyede tam metin.
- ~~GVK paraleli~~ → ✅ **ÇÖZÜLDÜ:** GVK'da paralel hüküm **yok**; istisna yalnız
  kurumlar vergisi mükelleflerine özgü.
- **Tebliğ düzeyi doğrulanmadı** — teyit turu 01 yalnız **kanun metinlerini** taradı.
  KVKUGT 5.15 ve KDVUGT II/4.21 açıklamalarının güncelliği ayrıca kontrol edilmeli.
- Sayısal örnek **KVKUGT'nin kendi resmî örneğidir**, tarafımdan üretilmemiştir.
