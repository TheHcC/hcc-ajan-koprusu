> **Bu bir inceleme kopyasıdır.** Kanonik sürüm `ymm-korpus/09_bilgi/10-poster/`
> altındadır (private depo). Burada duruyor ki Claude.ai ve ChatGPT okuyup
> eleştirebilsin. **Buradaki kopyayı düzenlemeyin** — eleştiriyi `gelen-kutusu/`
> altına ayrı bir dosya olarak bırakın, kaynak sürüm oradan güncellenir.

---

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
gecerlilik_donemi: "[TEYİT: 2026 yürürlük doğrulanmadı]"
son_dogrulama: 2026-09-09
dogrulama_durumu: KAYNAKTAN_OKUNDU_GUNCELLIK_TEYIT_BEKLIYOR
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
