---
konu: Sat-kirala-geri al — kazanç istisnası, özel fon ve amortismanın bölüştürülmesi
ders: [Revizyon, Vergi Tekniği]
yuzey_profili: poster-tablo
dayanak:
  - KVK m.5/1-j        # 6728 s.K. (2016) ile eklendi — [TEYİT: bent harfi, Sınırlar'a bak]
  - KDV m.17/4-y       # 6728 s.K. ile değişik
iliskili_maddeler:
  - KVK m.5/1-e        # taşınmaz satış kazancı istisnası — benzer fon disiplini
  - KDV m.30/a         # indirim iptali — 17/4-y bu listede YOK
  - VUK mük. m.290     # finansal kiralama işlemlerinde değerleme
  - VUK mük. m.298     # kullanma hakkının yeniden değerlemesi
  - 6361 s.K.          # Finansal Kiralama, Faktoring ve Finansman Şirketleri Kanunu
  - KVKUGT 5.15        # tebliğ açıklaması
  - KDVUGT II/4.21     # tebliğ açıklaması
gecis_kontrolu:
  kdv: "VAR + ZIT SONUC — m.17/4-y istisna, ANCAK m.30/a'nin parantez ici listesinde YOK (listede yalniz 17/2-b,c,d ve 17/4-i,o sayili). Indirim iptali ISLER. Telafi: devre kadar indirilemeyen KDV 'Ilave edilecek KDV' olarak beyan edilir ve gider yazilir. Bagis atomunun (17/2-b) tam TERSI."
  vuk: "VAR — muk. m.290 finansal kiralama degerlemesi: kiracida kullanma hakki ve borc, rayic bedel ile kira odemelerinin bugunku degerinden DUSUK olani ile degerlenir; kullanma hakki amortismana tabi. Ayrica finansal kiralama testi (dort olcutten biri yeterli)."
  gvk: "SUPHELI — istisna kiraci tarafinda 'kurumlar vergisi mukellefleri' ile sinirli (KVKUGT 5.15.1). Gercek kisi/ferdi isletme icin GVK'da paralel hukum olup olmadigi incelenmedi [TEYIT: kaynak gerekli]."
  kvk: "VAR — m.5/1-j istisnasi %100; kazanc ozel fona alinir; fonun amac disi kullanimi vergi ziyai cezasi dogurur."
  damga_harc: "SUPHELI — 6361 sayili Kanun kapsamindaki finansal kiralama sozlesmelerinin damga vergisi karsiligi bu cikarimda taranmadi [TEYIT: 488 s.K. ve 6361 s.K. m.37 kontrol edilmeli]."
  donem_sarkmasi: "VAR — GUCLU. (a) Istisna satisin yapildigi donemde uygulanir, pesin/vadeli fark etmez. (b) Fona alma suresi: satisi izleyen hesap donemi basindan, kazancin beyan edildigi doneme ait KV beyannamesinin verildigi tarihe kadar. (c) Gecici vergi donemlerinde de yararlanilir; suresinde fona alinmazsa gecici vergiden dogan vergi ziyai cezasi ve gecikme faizi AYRICA aranir. (d) Amortisman farki kira suresi boyunca ve geri alim sonrasina sarkar."
  muhasebe_tms: "VAR — ozel fon hesabi acilir; geri alim sonrasi amortisman IKIYE BOLUNUR (bir kismi kurum kazancindan gider, kalani yalniz fondan mahsup); KDV tarafinda 'Ilave edilecek KDV' beyani."
gecerlilik_donemi: "[TEYİT: 2026 yürürlük doğrulanmadı]"
son_dogrulama: 2026-09-09
dogrulama_durumu: KAYNAKTAN_OKUNDU_GUNCELLIK_TEYIT_BEKLIYOR
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

- **Bent harfi çelişkisi `[TEYİT]`:** KVKUGT istisnayı "(j) bendi" diye anıyor; ancak
  yerel `KVK.md` dosyasındaki m.5/1 listesinde **(j) bendi kooperatif risturn
  istisnasıdır.** Sebebi: `KVK.md`, 5520 sayılı Kanunun **2006 tarihli orijinal gerekçe
  metnidir**; sat-kirala-geri al 2016'da (6728 s.K.) eklendiği için o dosyada yer almaz.
  **Kesin bent harfi güncel kanun metninden doğrulanmalıdır.**
  → Bu aynı zamanda bir **korpus bulgusudur:** yerel `KVK.md` güncel kanun metni değildir.
- **Güncellik teyidi yok** — Mevzuat MCP bağlanamadı; 2026 yürürlüğü doğrulanmadı.
- **Damga vergisi şeridi taranmadı** (ŞÜPHELİ) — 6361 s.K. kapsamındaki sözleşmelerin
  damga vergisi durumu bu çıkarımda aranmadı.
- **GVK paraleli araştırılmadı** (ŞÜPHELİ) — istisna kurumlar vergisi mükelleflerine
  tanınmış; gerçek kişi tarafı incelenmedi.
- Sayısal örnek **KVKUGT'nin kendi resmî örneğidir**, tarafımdan üretilmemiştir.
