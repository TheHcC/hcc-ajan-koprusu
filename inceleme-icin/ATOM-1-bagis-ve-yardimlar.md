---
konu: Bağış ve yardımlar — KV indirimi ile KDV boyutunun birlikte değerlendirilmesi
ders: [Revizyon, Vergi Tekniği]
yuzey_profili: poster-tablo   # koşullu/karşılaştırmalı kural kümesi (K-005)
dayanak:
  - KVK m.10/1-c        # %5 sınırlı bağış
  - KVK m.10/1-ç        # eğitim-sağlık-dini tesis, sınırsız
iliskili_maddeler:
  - KVK m.11            # KKEG
  - KDV m.17/1          # istisnadan yararlanan kuruluş listesi
  - KDV m.17/2-b        # bu kuruluşlara bedelsiz teslim istisnası
  - KDV m.30/a          # indirim iptalinin 17/2-b istisnası
  - KDV m.13/1-k        # bağışlanacak tesis inşasında tam istisna
  - VUK m.267           # ayni bağışta takdir komisyonu değeri
  - KVKUGT 10.3, 10.3.2 # tebliğ açıklamaları
  - KDVUGT II/B-15      # tesis inşası istisnasının usulü
gecis_kontrolu:   # ZORUNLU — her şerit ya bulgu ya gerekçeli YOK taşır, boş bırakılamaz
  kdv: "VAR — m.17/2-b bedelsiz teslim istisnası; m.30/a bu istisnayı indirim iptalinin DIŞINDA bırakır (yüklenilen KDV indirilir); m.13/1-k tesis inşasında bağışçıya yapılan teslimler ayrı ve tam istisna"
  vuk: "VAR — ayni bağışta maliyet bedeli/kayıtlı değer, yoksa takdir komisyonu değeri; işletmeden çekilende fatura + arka yüz şerhi (belge düzeni)"
  gvk: "VAR + ASİMETRİ — m.89/4-5 gerçek kişi paraleli mevcut. (a) Oran: GVK'da kalkınmada öncelikli yörelerde %10, KVKUGT 10.3.2.1'de yöre ayrımı görülmedi [TEYİT: KVK m.10/1-c kanun metni ayrıca okunmalı]. (b) Taban: GVK'da 'beyan edilecek gelir', KVK'da 'ticari bilanço kârı − (iştirak kazançları istisnası + geçmiş yıl zararları)'"
  kvk: "VAR — m.11 gereği bağış önce KKEG'e eklenir, sonra beyannamede ayrıca indirilir"
  damga_harc: "VAR (teyit turu 01, 09.09.2026) — 488 s.K. (2) sayili tablo IV/55 (Ek: 14/10/2021-7338/54): genel/ozel butceli idarelere, il ozel idarelerine, YIKOB'lara, belediyelere ve koylere yapilacak bagislara iliskin olarak ilgili idare ile bagislayanlar arasinda duzenlenen kagitlar damga vergisinden ISTISNADIR. Ayrica DVK m.8 uyarinca resmi daireler muaftir."
  donem_sarkmasi: "YOK — kanun açık: indirilemeyen kısım sonraki yıla devretmez (KVKUGT 10.3.2.1). Sarkma imkânı bilinçli kapatılmış"
  muhasebe_tms: "VAR — bağış kayıtlarda gider yazılır, KKEG olarak matraha eklenir, beyannamede ayrıca indirilir; ticari kâr ile mali kâr arasında yapısal fark doğurur"
gecerlilik_donemi: 2026
son_dogrulama: 2026-09-09
dogrulama_durumu: TEYITLI
teyit_kapsami: "Kanun metni duzeyinde teyit edildi (Gorev S / teyit-turu-01, bedesten.adalet.gov.tr). TEBLIG duzeyi (KVKUGT 10.3, KDVUGT II/B-15) TARANMADI. NOT: yerel KVKUGT hala 'Bakanlar Kurulunca' diyor, guncel kanun 'Cumhurbaskaninca' — atom guncel metne gore yazilmisti."
kaynak: vtr-vir/mevzuat/{KVKUGT,KDVUGT,KDV}.md — yerel korpus, birebir okundu
---

# Bağış ve Yardımlar — KV × KDV

> **Sınavın test ettiği şey tek bir madde değil, geçiş.** Aynı bağış KV'de indirim,
> KDV'de istisna, muhasebede KKEG olabilir; ve alıcı bir harf değişince üçü de değişir.

## 1. Karar tablosu — kime bağışlandığı her şeyi belirler

| Kime / ne için | KV tarafı | KDV tarafı |
|---|---|---|
| **Kamu idaresi** (genel/özel bütçeli), il özel idaresi, belediye, köy — genel bağış | **%5 sınırlı indirim** (m.10/1-c) | Bedelsiz teslim **istisna** (17/2-b) · yüklenilen KDV **indirilir** (30/a) |
| Aynı kuruluşlara **okul / sağlık tesisi / ≥100 yatak öğrenci yurdu / çocuk yuvası / yetiştirme yurdu / huzurevi / bakım-rehabilitasyon / ibadethane / yaygın din eğitimi tesisi** inşası | **Tamamı indirilir** (m.10/1-ç) | Bağışçıya yapılan teslim/hizmetler **istisna** (13/1-k) — istisna belgesi + bağış protokolü şart |
| **Kamu yararına dernek** / Cumhurbaşkanınca vergi muafiyeti tanınan **vakıf** | **%5 sınırlı** — *tesis inşası için olsa bile* | Bedelsiz teslim **istisna** (17/2-b, 17/1'de sayılıyorlar) |
| Bu kuruluşların **iktisadi işletmesine** | ⛔ **İndirim yok → KKEG** | ⛔ 17/2-b **uygulanmaz** — normal KDV |
| Muafiyeti olmayan vakıf / sıradan dernek | ⛔ **KKEG** | ⛔ İstisna yok |

**Tuzak:** Dördüncü satır. Kuruluşun *kendisi* listede olsa da **iktisadi işletmesi ayrı
bir kurumlar vergisi mükellefidir** ve 17/1 listesinde yer almaz. KVKUGT 10.3.2.2.3 bunu
şöyle kapatır: *"kamu idare ve kuruluşları dışında kalan kurum veya kuruluşlara yapılacak
bağış ve yardımların... genel hükümler çerçevesinde değerlendirilecektir."*

## 2. Sıralama kuralı — en çok atlanan adım

Bağış **önce KKEG yazılır, sonra beyannamede indirilir.** KVKUGT 10.3 birebir:

> *"...bağış ve yardımın yapıldığı tarihte kayıtlarda gider olarak dikkate alındığından,
> söz konusu harcamalar ile bağış ve yardımların kurum kazancının tespitinde kanunen
> kabul edilmeyen gider olarak dikkate alınması ve kurum kazancının yeterli olması
> halinde... beyanname üzerinde ayrıca gösterilmek şartıyla kurumlar vergisi matrahından
> indirilmesi gerekmektedir."*

**%5'in matrahı normal kurum kazancı değildir** (KVKUGT 10.3.2.1):

```
%5 tabanı = Ticari bilanço kârı − (iştirak kazançları istisnası + geçmiş yıl zararları)
```

İndirim ve istisnalar **düşülmeden önceki** tutardır. **İndirilemeyen kısım sonraki yıla
devretmez.**

Diğer şartlar: makbuz karşılığı · karşılıksız · sadece ilgili dönem kazancından ·
beyannamede ayrıca gösterilmiş.

## 2b. Sayısal örnek — %5 limiti ve iktisadi işletme tuzağı (TÜRETİLMİŞ, doğrulandı)

> Bu örnek tebliğde birebir yoktur; §2'deki formülden **türetilmiştir** ve
> `scripts/dogrula_09bilgi_sayisal.py` ile Python'da doğrulanmıştır (12/12 PASS,
> 09.09.2026). Sınavda aynı desenle karşına çıkabilir — sayılar değişir, mantık değişmez.

**Veriler:**

| Kalem | Tutar |
|---|---|
| Ticari bilanço kârı | 1.000.000 |
| İştirak kazançları istisnası | 200.000 |
| Geçmiş yıl zararları | 100.000 |
| Belediyeye makbuz karşılığı bağış | 50.000 |
| Kuruluşun **iktisadi işletmesine** bağış | 20.000 |

**Çözüm:**

```
%5 tabanı  = 1.000.000 − (200.000 + 100.000) = 700.000
%5 limiti  = 700.000 × %5                     =  35.000
```

⚠️ **Tuzak burada işliyor:** iktisadi işletmeye yapılan 20.000, kuruluşun kendisine
yapılmadığı için **%5 testine hiç girmez** — havuza yalnız belediye bağışı (50.000) girer.

```
%5 testine giren bağış         = 50.000
İndirilebilecek (limitle sınırlı) = min(50.000, 35.000) = 35.000
Limit aşımı (devretmez → KKEG)  = 50.000 − 35.000        = 15.000
İktisadi işletme bağışı (baştan kapsam dışı → KKEG)       = 20.000
──────────────────────────────────────────────────────────────
TOPLAM KKEG                                               = 35.000
```

**Sağlama:** İndirilen (35.000) + KKEG (35.000) = yapılan toplam bağış (70.000). ✓

**Puan öldüren hata:** 20.000'i de %5 havuzuna dahil edip "70.000'in %5'i" diye
limit hesaplamak — bu, iktisadi işletme tuzağını (§1, satır 4) atlamak demektir.

## 3. Ayni bağış — değerleme ve belge

| Soru | Cevap |
|---|---|
| Hangi değer? | Maliyet bedeli **veya** kayıtlı değer; yoksa **VUK'a göre takdir komisyonu** değeri |
| İşletmeden çekilerek bağışlandıysa | **Fatura düzenlenir**; faturanın **arka yüzüne** kurumca teslim alındığına dair şerh + yetkili imza |
| Dışarıdan alınıp bağışlandıysa | Bağış alan kurumun düzenleyeceği teslim belgesi |

## 4. KDV köprüsü — sınavın en sevdiği ince nokta

KDV m.17/2-b bir **kısmi istisna**dır; kural olarak kısmi istisnada yüklenilen KDV
indirilemez. **Ama m.30/a onu açıkça dışarıda bırakır** (birebir):

> *"a) Vergiye tabi olmayan veya vergiden istisna edilmiş bulunan malların teslimi ve
> hizmet ifası **(Bu Kanunun 17 nci maddesinin (2) numaralı fıkrasının (b), (c) ve (d)
> bentleri ile (4) numaralı fıkrasının (ı) ve (ö) bentleri uyarınca katma değer
> vergisinden istisna edilen işlemler hariç)** ile ilgili alış vesikalarında gösterilen
> ...katma değer vergisi [indirilemez]"*

**Sonuç:** Kamu idaresine / kamu yararına derneğe / muafiyetli vakfa yapılan bedelsiz
teslimde **KDV hesaplanmaz ama yüklenilen KDV indirim hakkı korunur.** Kısmi istisna
kılığında çalışan bir tam istisna — KDV'de nadir bir durum ve tam da bu yüzden sorulur.

**13/1-k ile karıştırma:** O ayrı bir istisnadır ve **bağışçıya yapılan** teslimleri
kapsar (7104 sayılı Kanun, 1/6/2018'den itibaren). Yani müteahhidin bağışçıya kestiği
fatura KDV'siz olur. Usulü ağırdır: onaylı proje + inşaat ruhsatı + ilgili idareyle
**bağış protokolü** + vergi dairesinden **istisna belgesi** (KDVUGT II/B-15).

## 5. Bu atomun sınav karşılığı

`[SINAV-KAYNAK]` 2025/3. Dönem YMM Revizyon sınavı, **Soru 6, 15 puan** — bağışın dört
alt tipi birlikte soruldu: muafiyetsiz vakıf (KKEG) / üniversite (indirim) / Yeşilay'ın
**iktisadi işletmesi** (KKEG) / belediye (%5 sınırlı). Yani tablodaki 1., 3., 4. ve 5.
satırlar tek soruda test edilmiş.

## Sınırlar

- **Güncellik teyidi yapılmadı.** Bütün metinler yerel mevzuat korpusundan birebir
  okundu, ancak Mevzuat MCP bu oturumda bağlanamadığı için **2026 yürürlük durumu
  doğrulanmamıştır.** Özellikle KVK m.10 ve KDV m.17/30 üzerinde sonradan değişiklik
  olup olmadığı kontrol edilmelidir.
- **Sınav sorusunun cevap anahtarını kendim görmedim.** 5. bölümdeki dört alt tip
  bilgisi Claude.ai sohbetinin gelen-kutusu belgesinden alındı; sınav PDF'i bu ortamda
  açılmadı.
- **Üniversite satırı tabloda ayrı gösterilmedi** — üniversiteler KDV 17/1'de açıkça
  sayılıyor, KV tarafında ise "özel bütçeli kamu idaresi" kapsamında değerlendirilir;
  bu eşleme tebliğden birebir alıntıyla değil, yapıdan çıkarıldı. `[ÇIKARIM]`
- Bu atom **oran/tutar içermez** (%5 hariç, o kanunun kendisinde). Dolayısıyla yıllık
  parametre güncellemesine görece dayanıklıdır — bayatlama riski **RİSKLİ değil, KALICI**
  sınıfına yakındır.
