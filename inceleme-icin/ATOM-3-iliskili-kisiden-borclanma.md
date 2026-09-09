---
konu: İlişkili kişiden borçlanma — örtülü sermaye, transfer fiyatlandırması ve finansman gider kısıtlamasının kesişimi
ders: [Revizyon, Vergi Tekniği]
yuzey_profili: poster-tablo
dayanak:
  - KVK m.12          # örtülü sermaye
  - KVK m.13          # transfer fiyatlandırması yoluyla örtülü kazanç dağıtımı
  - KVK m.11/1-i      # finansman gider kısıtlaması
iliskili_maddeler:
  - KVK m.11/1-b      # örtülü sermaye faiz/kur farkının KKEG'liği
  - KDV m.27          # emsal bedel
  - KDV m.9           # vergi sorumlusu
  - KDV m.30/d        # KKEG dolayısıyla ödenen KDV — m.13 anılıyor, m.12 anılmıyor
  - GVK m.41/1-5      # işletme aleyhine oluşan farklar (30/d parantezinde)
  - KVKUGT 11.13, 12, 13
gecis_kontrolu:
  kdv: "VAR + ACIK UC — (a) Faizsiz borclanmada emsal bedel (m.27) ve sorumlu sifatiyla KDV (m.9) gundeme gelebilir; ANCAK korpusta 'iliskili kisiye faizsiz borc verme' icin ozel KDVUGT aciklamasi BULUNAMADI. (b) KDV m.30/d parantezi acikca yalniz KVK m.13'u (transfer fiyatlandirmasi) aniyor, m.12'yi (ortulu sermaye) ANMIYOR — ucuncu zit cift adayi, ancak [CIKARIM], metinde yazili degil."
  vuk: "VAR — oz sermaye VUK'a gore tespit edilmis HESAP DONEMI BASINDAKI oz sermayedir (donem sonu degil). Emsal bedel icin VUK m.267 mantigi KDV m.27'ye baglanir."
  gvk: "VAR — borc veren dar mukellef/gercek kisi/vergiden muaf ise ortulu sermaye faizi NET kar payi sayilir, brute tamamlanir ve stopaja tabi tutulur. Kur farki bu kapsamda DEGIL."
  kvk: "VAR — uc muessese ayni olayda ayri tetikleyicilerle calisir; birinden muafiyet digerini kapatmaz."
  damga_harc: "SUPHELI — grup ici kredi aktarim sozlesmelerinin damga vergisi durumu bu cikarimda taranmadi [TEYIT: kaynak gerekli]."
  donem_sarkmasi: "VAR — GUCLU. (a) Ortulu sermaye olcusu 'hesap donemi icinde HERHANGI BIR TARIHTE' asilmasina baglidir; tek gunluk asim yil boyu sonuc dogurur. (b) Kar payi sayilma ani hesap doneminin SON GUNUdur. (c) Gecici vergi doneminde sartlar gerceklesirse duzeltme o donemde yapilabilir. (d) Karsi tarafta duzeltme icin tarh edilen vergilerin KESINLESMIS VE ODENMIS olmasi sart — duzeltme yillar sonraya sarkabilir."
  muhasebe_tms: "VAR — ortulu sermaye faizi gider yazilamaz (KKEG), kur farki GELIRI de kurum kazancina alinmaz (simetri); FGK'da asan kisma isabet eden giderin %10'u KKEG."
gecerlilik_donemi: "[TEYİT: 2026 yürürlük doğrulanmadı — Görev S teyit turunda]"
son_dogrulama: 2026-09-09
dogrulama_durumu: KAYNAKTAN_OKUNDU_GUNCELLIK_TEYIT_BEKLIYOR
kaynak: vtr-vir/mevzuat/{KVK,KVKUGT,KDV,KDVUGT}.md — yerel korpus, birebir okundu
---

# İlişkili Kişiden Borçlanma — Üç Müessesenin Kesişimi

> **Atomun tezi:** Bir şirket ilişkili kişiden borçlandığında üç müessese **aynı anda ve
> birbirinden bağımsız** bakar. Birinden muaf olmak diğerinden muaf kılmaz. Sınavın
> tuzağı tam olarak bu varsayımdır.

## 1. Karar tablosu — üç ayrı tetikleyici

| Müessese | Tetikleyici | Sonuç |
|---|---|---|
| **Örtülü sermaye** (m.12) | Borç, hesap dönemi içinde **herhangi bir tarihte** öz sermayenin **üç katını** aşarsa | Aşan kısma isabet eden faiz → dönemin **son günü** itibarıyla **dağıtılmış kâr payı** |
| **Transfer fiyatlandırması** (m.13) | Bedel emsale aykırıysa (ödünç para alma/verme dâhil) | Emsal farkı → **örtülü kazanç dağıtımı** |
| **Finansman gider kısıtlaması** (m.11/1-i) | **Yabancı kaynak > öz kaynak** | Aşan kısma isabet eden finansman giderlerinin **%10'u → KKEG** |

Üçünün ölçüsü farklıdır: biri **borç/öz sermaye** oranına, biri **fiyata**, biri
**yabancı kaynak/öz kaynak** dengesine bakar.

## 2. Örtülü sermaye — ölçünün ayrıntıları

- **Üç şart birlikte:** ortak/ortakla ilişkili kişiden temin + **işletmede kullanım** +
  öz sermayenin üç katını aşma.
- **Öz sermaye hangi tarih?** VUK'a göre tespit edilmiş **hesap dönemi başındaki** öz
  sermaye. *Dönem sonu değil* — sık yapılan hata.
- **Aşım hangi tarih?** "Hesap dönemi içinde **herhangi bir tarihte**". Yılın tek bir
  gününde aşılması, **ilgili hesap döneminin tamamı** için sonuç doğurur.
- **Ortaklık payı sınırı yok.** Tebliğin örneği: **%5** iştirak bile yeterli. Tek istisna:
  borsada işlem gören hisselerin elde bulundurulmasında **en az %10** ortaklık payı aranır.

### Kapsam dışı haller

| Hâl | Not |
|---|---|
| **Banka/finans kurumundan veya sermaye piyasasından temin edilip *aynı şartlarla* grup şirketine aktarılan borç** | ⚠️ **En kritik bent.** "Aynı şartlar" = kredi sözleşmesindeki **vade, faiz oranı ve benzeri** kullandırılma şartlarında **hiçbir değişiklik olmaması**. Kredibilitesi olan grup şirketinin krediyi aynı faiz ve vadeyle birden fazla şirkete paylaştırması hâlinde örtülü sermayeden söz edilemez. |
| Bankaların kendi faaliyetleri çerçevesinde yaptığı borçlanmalar | Herhangi bir şarta bağlı değil |
| Finansal kiralama / faktoring / finansman / ipotek finansman kuruluşlarının **ortak sayılan bankalardan** borçlanmaları | Banka ortak değilse zaten madde kapsamına girmez |

## 3. ⚠️ Tuzak 1 — muafiyet zinciri kurma

> **Grup içi kredi aktarımı örtülü sermaye sayılmaz → o hâlde bir şey yapmaya gerek yok.**

**Yanlış.** Örtülü sermaye muafiyeti **yalnızca m.12'yi** kapatır. Finansman gider
kısıtlamasının tetikleyicisi bambaşkadır (**yabancı kaynak > öz kaynak**) ve grup içi
kredi de bir yabancı kaynaktır. **FGK uygulanmaya devam eder.**

`[SINAV-KAYNAK]` 2025/3 Revizyon S8 (10 puan) tam olarak bunu sormuş.

## 4. Kur farkının özel rejimi — üç yönlü

Örtülü sermayede kur farkı **ayrı muamele** görür ve üç ayrı yerde karşımıza çıkar:

| Yön | Sonuç |
|---|---|
| Kur farkı **gideri** | Gider yazılamaz — KKEG (m.11/1-b) |
| Kur farkı **geliri** | **Kurum kazancına gelir olarak da alınmaz.** Borç örtülü sermaye sayıldığı için simetrik davranılır |
| Kur farkının **kâr payı** sayılması | ⛔ **Sayılmaz.** Kanun metni: *"kur farkı hariç, faiz ve benzeri ödemeler… dağıtılmış kâr payı… sayılır"* → dar mükellef/gerçek kişide **stopaja tabi değildir** |

**Karşılaştır:** Finansman gider kısıtlamasında kur farkı **kapsam içindedir** (faiz,
komisyon, vade farkı, kâr payı, kur farkı ve benzeri). Aynı kalem, iki müessesede zıt.

## 5. Düzeltme mekanizması — ve sarkması

Faiz, **hesap döneminin son günü** itibarıyla, **hem borç alan hem borç veren** nezdinde
dağıtılmış kâr payı sayılır. Karşı tarafta düzeltme yapılabilmesi için:

> *"…bu düzeltmenin yapılması için örtülü sermaye kullanan kurum adına tarh edilen
> vergilerin **kesinleşmiş ve ödenmiş** olması şarttır."*

Yani düzeltme, tarhiyatın kesinleşip ödenmesine bağlıdır — **yıllar sonraya sarkabilir.**

**Borç veren kim?**

| Borç veren | Sonuç |
|---|---|
| Tam mükellef kurum | Karşılıklı düzeltme; geçici vergi döneminde de yapılabilir |
| **Dar mükellef kurum / gerçek kişi / vergiden muaf kişi** | Faiz **net kâr payı** sayılır → **brüte tamamlanır** → stopaj. Kur farkı bu kapsamda değil |

## 6. Finansman gider kısıtlaması — parametreler

- **Oran:** gider ve maliyet unsurları toplamının **%10**'u (Cumhurbaşkanı Kararı 3490,
  **1/1/2021**'den itibaren başlayan vergilendirme dönemi kazançlarına)
- **Kapsam:** faiz, komisyon, vade farkı, kâr payı, **kur farkı** ve benzeri adlar altındaki
  gider ve maliyet unsurları
- **Hariç:** **yatırımın maliyetine eklenmiş** olan yabancı kaynaklardan doğanlar
- **Kapsam dışı mükellefler:** kredi kuruluşları, finansal kuruluşlar, finansal kiralama,
  faktoring ve finansman şirketleri
- Kısıtlama **yalnız aşan kısma münhasırdır**

## 7. ⚠️ Tuzak 2 — KV'de sonuç yoksa KDV'de de yoktur varsayımı

`[SINAV-KAYNAK]` 2025/3 Revizyon S4: faizsiz borçlanmada **örtülü sermaye faizi yok**
(faiz hesaplanmamış), ama **emsal bedel üzerinden KDV** doğduğu sorulmuş.

`[TEYİT: kaynak gerekli]` Bu sonucun mevzuat dayanağı bu çıkarımda **doğrulanamadı** —
KDV m.27 (emsal bedel) ve m.9 (sorumlu sıfatıyla KDV) metinleri mevcut, ancak **ilişkili
kişiye faizsiz borç verilmesine özgü bir KDVUGT açıklaması korpusta bulunamadı.** Sınav
cevap anahtarını da bu ortamda görmedim. **Bu satır Görev S teyit turunda kapatılmalıdır.**

Yine de atomun tezi ayakta: KV tarafında bir müessesenin işlememesi, KDV tarafının da
işlemeyeceği anlamına gelmez.

## 8. Üçüncü zıt çift adayı `[ÇIKARIM]`

KDV m.30/d, KKEG dolayısıyla ödenen KDV'nin indirilemeyeceğini söyler. Parantez içi
istisnada **açıkça** şunlar sayılır:

> *"…5520 sayılı Kanunun **13 üncü maddesine** göre transfer fiyatlandırması yoluyla
> örtülü olarak dağıtılan kazançlar ile Gelir Vergisi Kanununun 41 inci maddesinin
> birinci fıkrasının (5) numaralı bendine göre işletme aleyhine oluşan farklara ilişkin…
> katma değer vergisi **hariç**"*

**12 nci madde (örtülü sermaye) bu istisnada anılmıyor.** Bağış ve sat-kirala
atomlarındaki olumsuz-delil deseninin aynısı.

⚠️ **Ama bu bir `[ÇIKARIM]`dır, kural değildir.** Metinde örtülü sermayeye özgü bir KDV
hükmü **yok**; sonuç madde numaralarının farkından çıkarılmıştır. Doğrulanmadan
kullanılmamalıdır — açık uç olarak kaydedildi.

## Sınırlar

- **Güncellik teyidi yok** — Görev S teyit turunda kapatılacak.
- **§7'nin mevzuat dayanağı doğrulanamadı** (faizsiz borçlanma → KDV). Korpusta özel
  açıklama bulunamadı; sınav cevap anahtarı görülmedi.
- **§8 çıkarımdır**, metne dayalı kural değildir.
- **Faizsiz borç vermeye özgü transfer fiyatlandırması açıklaması korpusta yok** —
  KVKUGT yalnızca genel "ödünç para alınması ve verilmesi" ifadesini kullanıyor.
- **Damga vergisi şeridi taranmadı** (ŞÜPHELİ).
- **Korpus uyarısı:** `KVK.md` içinde madde 12 metni **iki kez** geçiyor ve ölçüler
  farklı — birinci nüsha "iki katı", ikinci nüsha "üç katı". KVKUGT **üç katı**yı teyit
  ediyor; güncel ölçü budur. Bu dosyadan tek nüshaya bakarak oran alınmamalıdır.
