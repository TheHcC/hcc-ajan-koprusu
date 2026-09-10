# Geçiş Haritası — kanunlar arası bağlantı sicili

> **Ne işe yarar:** Vergi mevzuatında asıl bilgi çoğu zaman tek bir kanunda değil,
> iki kanunun kesiştiği yerdedir. Bu dosya, atom üretilirken bulunan her geçişi
> **çift yönlü** kaydeder — böylece ileride ters yönden gelen bir çalışma bağlantıyı
> yeniden keşfetmek zorunda kalmaz.
>
> **Kim doldurur:** Her atom üretiminde, künyedeki `gecis_kontrolu` bloğundaki her
> `VAR` satırı buraya bir kayıt olarak düşer. `ŞÜPHELİ` satırları "Açık uçlar"a gider.

## Nasıl doldurulur — üç durumlu sonuç

Şerit boş bırakılamaz. Üç geçerli değer vardır:

| Değer | Ne zaman | Zorunlu ek |
|---|---|---|
| `VAR` | Geçiş bulundu | Madde numarası + tek cümle etki |
| `YOK` | Bakıldı, geçiş yok | **Gerekçe zorunlu** — "bakılmadı" ile "yok" karıştırılmasın |
| `ŞÜPHELİ` | Muhtemel ama doğrulanmadı | `[TEYİT: kaynak gerekli]` + açık uçlara yazılır |

**Zincir kuralı:** Komşu kanunda bir madde bulduğunda **ilk isabette durma** — o
maddenin istisna / hariç tutma zincirini de aç. Vergi mevzuatında asıl bilgi sık sık
ana kuralda değil, ona getirilen istisnanın istisnasındadır.

*Kanıt: KDV m.17/2-b tek başına okunursa "kısmi istisna, yüklenilen KDV indirilemez"
sonucu çıkar. m.30/a açılmadan bu sonuç yanlıştır.*

## Şeritler

`kdv` · `vuk` · `gvk` · `kvk` · `damga_harc` · `donem_sarkmasi` · `muhasebe_tms`

*(Şeritler `TEKNO AI HcC/vergi-incelemeler` vault taksonomisinden türetildi —
uydurulmuş bir liste değil, fiilen kullanılan kategoriler.)*

---

## Sicil

| # | Konu | Kaynak madde | Geçtiği madde | Etki | Atom |
|---|---|---|---|---|---|
| G-001 | Bağış ve yardımlar | KVK m.10/1-c | KDV m.17/2-b | Kamu idaresi/kamu yararına dernek/muafiyetli vakfa bedelsiz teslim KDV'den istisna | `10-poster/bagis-ve-yardimlar-kv-kdv.md` |
| G-002 | Bağış ve yardımlar | KDV m.17/2-b | **KDV m.30/a** | 17/2-b indirim iptalinin **dışında** — kısmi istisna olmasına rağmen yüklenilen KDV indirilir | aynı |
| G-003 | Tesis inşası bağışı | KVK m.10/1-ç | KDV m.13/1-k | Bağışçıya yapılan teslim/hizmetler tam istisna (7104 s.K., 1/6/2018'den); bağış protokolü + istisna belgesi şart | aynı |
| G-004 | Bağış — ayni | KVK m.10/1-c | VUK (takdir komisyonu) | Maliyet/kayıtlı değer yoksa takdir komisyonu değeri; fatura + arka yüz şerhi | aynı |
| G-005 | Bağış — kurum/gerçek kişi | KVK m.10/1-c | GVK m.89/4 | **ASİMETRİ (oran):** GVK'da kalkınmada öncelikli yörelerde %10; KVKUGT 10.3.2.1'de yöre ayrımı görülmedi | aynı |
| G-006 | Bağış — matrah tabanı | KVK m.10/1-c | GVK m.89/4 | **ASİMETRİ (taban):** GVK "beyan edilecek gelir"; KVK "ticari bilanço kârı − (iştirak kazancı istisnası + geçmiş yıl zararları)" | aynı |
| G-007 | Bağış — muhasebe | KVK m.11 | Beyanname düzeni | Önce KKEG, sonra beyannamede ayrıca indirim; ticari kâr ↔ mali kâr yapısal farkı | aynı |
| G-008 | Sat-kirala-geri al | KVK m.5/1-j | KDV m.17/4-y | Aynı işlem hem KV kazanç istisnası hem KDV istisnası doğurur | `10-poster/sat-kirala-geri-al.md` |
| G-009 | Sat-kirala-geri al | KDV m.17/4-y | **KDV m.30/a** | 17/4-y bu listede **YOK** → indirim iptali İŞLER; indirilemeyen kısım "İlave edilecek KDV" olarak beyan edilip gider yazılır | aynı |
| G-010 | Sat-kirala-geri al | KVK m.5/1-j | VUK mük. m.290 | Kiracıda kullanma hakkı rayiç bedel ile kira ödemelerinin bugünkü değerinden düşük olanı ile değerlenir; amortismana tabi | aynı |
| G-011 | Sat-kirala-geri al | KVK m.5/1-j | Amortisman / özel fon | Satış bedeli üzerinden amortisman ayrılır ama eski net bilanço aktif değerini aşan kısım yalnız fondan mahsup edilir — istisna af değil erteleme | aynı |
| G-012 | Sat-kirala-geri al | KVK m.5/1-j | Geçici vergi | Geçici vergi dönemlerinde de yararlanılır; süresinde fona alınmazsa geçici vergiden doğan vergi ziyaı cezası ve gecikme faizi ayrıca aranır | aynı |
| G-013 | İlişkili kişiden borçlanma | KVK m.12 · m.13 | **KVK m.11/1-i (FGK)** | G-022 |
| KVK m.12 | KVK m.11/1-b | Örtülü sermaye faizi **ve kur farkı gideri** KKEG — gider yazılamaz | `10-poster/iliskili-kisiden-borclanma.md` |
| G-014 | İlişkili kişiden borçlanma | KVK m.12 | GVK stopaj | Borç veren dar mükellef/gerçek kişi/muaf ise faiz **net kâr payı** sayılır, brüte tamamlanır, stopaja tabi. **Kur farkı bu kapsamda değil** | aynı |
| G-015 | Grup içi kredi aktarımı | KVK m.12 (muafiyet) | **KVK m.11/1-i** | Banka kredisi aynı şartlarla aktarılırsa örtülü sermaye **değil** — ama FGK'nın tetikleyicisi farklı (yabancı kaynak > öz kaynak), **FGK yine uygulanır.** Muafiyet zinciri kurulamaz | aynı |
| G-016 | Kur farkı | KVK m.12 | KVK m.11/1-i | **Aynı kalem, zıt muamele:** örtülü sermayede kur farkı kâr payı sayılmaz ve geliri de kazanca alınmaz; FGK'da kur farkı **kapsam içindedir** | aynı |
| G-017 | Örtülü kazanç | KVK m.13 | **KDV m.30/d** | 30/d parantezinde **yalnız m.13** anılıyor, **m.12 anılmıyor** — üçüncü zıt çift adayı `[ÇIKARIM]`, metne dayalı kural değil | aynı |
| G-018 | Faizsiz borçlanma | KVK m.12 | KDV m.27 + m.9 | KV'de faiz yok ama emsal bedel üzerinden KDV doğduğu iddia ediliyor — **dayanak korpusta bulunamadı** `[TEYİT]` | aynı |
| G-019 | Bağış — damga vergisi | KVK m.10/1-c · KDV m.13/1-k | **488 s.K. (2) sayılı tablo IV/55** | Kamu idareleri/il özel idareleri/YİKOB/belediye/köylere yapılacak bağışlara ilişkin, ilgili idare ile bağışlayan arasında düzenlenen kâğıtlar **damga vergisinden istisna** *(Ek: 14/10/2021-7338/54)*. Ayrıca DVK m.8: resmî daireler muaf | `10-poster/bagis-ve-yardimlar-kv-kdv.md` |
| G-020 | Sat-kirala — damga ve harç | KVK m.5/1-j | **6361 s.K. m.37** | Finansal kiralama sözleşmeleri, devir/tadil kâğıtları, kiralayan-satıcı sözleşmeleri ve teminat kâğıtları **damga vergisinden**, ilgili işlemler **harçtan** müstesna (kiralayanlarca devralmaya ilişkin tapu işlemleri hariç). m.37/2: süre sonunda kiracı adına tescil tapu harcından müstesna | `10-poster/sat-kirala-geri-al.md` |
| G-021 | Sat-kirala — kurum/gerçek kişi | KVK m.5/1-j | GVK (paralel **YOK**) | **ASİMETRİ:** GVK'da sat-kirala-geri al istisnasının karşılığı yoktur; istisna yalnız kurumlar vergisi mükelleflerine özgüdür | aynı |
| G-022 | Mükerrer KKEG engeli | KVK m.12 / m.13 KKEG | **KVKUGT 11.13.9** | Örtülü sermaye veya transfer fiyatlandırması nedeniyle zaten KKEG sayılan finansman gideri, FGK (m.11/1-i) hesabına bir daha girmez — üç müessese bağımsız test edilir ama mükerrer cezalandırılmaz. Resmî örnekle doğrulandı (Python, 9/9 PASS) | `10-poster/iliskili-kisiden-borclanma.md` §6b |
| G-023 | Ticari borç → finansman | KVK m.12 | KVKUGT 12.1.6 | "Ticari borç" etiketi korumaz — piyasa/teamül vadesi aşılırsa örtülü sermaye testine girer. RESMİ, özelge değil | `10-poster/iliskili-kisiden-borclanma.md` §3b, `15-atomik-tekrar/ATOM3-nodes.md` N-03 |
| G-024 | Sipariş avansı → yabancı kaynak | KVK m.12 | KVKUGT 12.1.6 | Alınan avanslar örtülü sermaye hesabında borç sayılır (inşaat istihkakı hariç). RESMİ | aynı, N-04 |
| G-025 | Köprü kredi → FGK yükü | KVK m.11/1-i | KVKUGT 11.13 | Yüksüz aktarılan kredide FGK yükü fiilen kullanan şirkette kalır, ilk alanda değil. RESMİ | aynı, N-05 |

## Ters dizin — hangi maddeden nereye gidilir

| Maddeden | Şuraya bak | Kayıt |
|---|---|---|
| KDV m.17/2-b | KDV m.30/a · KVK m.10/1-c | G-001, G-002 |
| KDV m.30/a | KDV m.17/2-b,c,d ve m.17/4-ı,ö | G-002 |
| KDV m.13/1-k | KVK m.10/1-ç · KDVUGT II/B-15 | G-003 |
| GVK m.89/4-5 | KVK m.10/1-c,ç | G-005, G-006 |
| KVK m.11 | KVK m.10 (indirim sırası) | G-007 |

## ⚠️ Zıt çiftler — benzer görünüp ters çalışanlar

İki atom sonunda beliren en değerli yapı bu. Aynı kanunun aynı maddesinde, aynı
"istisna" adı altında, **birbirinin tersi** sonuç doğuran hükümler var. Tek başına
okunduğunda ikisi de "KDV istisnası" görünür.

| Konu | Bağış — KDV m.17/2-b | Sat-kirala-geri al — KDV m.17/4-y |
|---|---|---|
| m.30/a listesinde | ✅ **VAR** | ⛔ **YOK** |
| Yüklenilen KDV | **İndirilir** | **İndirilemez** |
| Telafi | gerekmez | "İlave edilecek KDV" → **gider** yazılır |
| Kayıt | G-002 | G-009 |

**Üçüncü aday `[ÇIKARIM — doğrulanmadı]`:** KDV m.30/d parantezinde KVK **m.13** (transfer
fiyatlandırması) açıkça anılıyor, **m.12** (örtülü sermaye) anılmıyor. Aynı olumsuz-delil
deseni ama bu kez metinde örtülü sermayeye özgü bir KDV hükmü **hiç yok** — bu yüzden
kural değil, açık uç (A-007). Doğrulanmadan kullanılmamalı.

**Teşhis yöntemi — her KDV istisnasında sor:**

1. Bu bent m.30/a'nın parantez içi listesinde sayılıyor mu?
2. Sayılmıyorsa, **bendin kendi metninde** "30 uncu maddenin birinci fıkrasının (a)
   bendi hükmü uygulanmaz" benzeri açık bir cümle var mı?
3. İkisi de yoksa → **indirim iptali işler.** Bendin sunduğu telafi (varsa) indirim
   hakkı değil, gider yazma imkânıdır.

*Olumsuz delil kuralı:* (i) ve (z) bentlerinde bu açık cümle **vardır**, (y) bendinde
**yoktur**. Kardeş bentlerdeki bir hükmün yokluğu, tesadüf değil bilinçli tercihtir.

## Açık uçlar — ŞÜPHELİ kalanlar

| # | Soru | Neden açık | Nereden bakılmalı |
|---|---|---|---|
| ~~A-001~~ | ✅ **KAPANDI** (teyit turu 01) — bağış protokolü damga vergisinden **istisna**; 488 s.K. (2) sayılı tablo IV/55 → G-019 |
| ~~A-002~~ | ✅ **KAPANDI** (teyit turu 01) — KVK m.10/1-c'de yöre ayrımı **YOK**, oran Türkiye genelinde %5. GVK m.89/4'teki %10 farkı **kanun düzeyinde kesinleşmiş asimetri** → G-005 doğrulandı |
| ~~A-003~~ | ✅ **KAPANDI** (teyit turu 01) — 6361 s.K. m.37 damga ve harç istisnası → G-020 |
| ~~A-004~~ | ✅ **KAPANDI** (teyit turu 01) — GVK'da paralel hüküm **yok** → G-021 |
| ~~A-005~~ | ✅ **KAPANDI** (teyit turu 01) — bent **kesinlikle (j)** *(Ek: 15/7/2016-6728/56)*. Kök neden: güncel kanunda (ı)=eğitim, (i)=risturn, (j)=sat-kirala; yerel dosyada **Türkçe ı/i ASCII çakışması** sıralamayı kaydırmış |
| A-006 | Faizsiz borçlanmada emsal bedel üzerinden KDV doğduğunun mevzuat dayanağı nedir? | KDV m.27 ve m.9 metinleri var ama faizsiz borç vermeye özgü KDVUGT açıklaması bulunamadı | KDVUGT tam tarama · sınav cevap anahtarı `[TEYİT]` |
| A-007 | Örtülü sermaye (m.12) kaynaklı KKEG dolayısıyla ödenen KDV, m.30/d karşısında ne olur? | 30/d parantezi yalnız m.13'ü anıyor; m.12'ye özgü hüküm korpusta yok | KDV m.30/d + özelge/içtihat `[TEYİT]` |
| A-008 | Grup içi kredi aktarım sözleşmeleri damga vergisine tabi mi? | Taranmadı | 488 s.K. `[TEYİT: kaynak gerekli]` |
| A-009 | Özelge numaralarının (5 adet, BULTEN-001'de) gerçekliği | GİB sitesi JS-render, WebFetch içini göremedi — ölçüm sınırı, uydurma kanıtı değil | Mevzuat MCP veya browserclaw `[TEYİT]` |
| A-010 | Danıştay 9. Daire E.2023/4917, K.2024/2755 — gerçek içerik | Yargı MCP CONNECT_TIMEOUT | Yargı MCP `[TEYİT: MCP bağlantısı başarısız]` |
| A-011 | Dar mükellefe faiz stopajının 2026 güncel oranı ve ÇVÖA indirimi | Genel oran (%15) doğrulandı, ÇVÖA istisnası/indirim güncelliği doğrulanmadı | Mevzuat MCP `[TEYİT]` |

---

## Korpus sağlığı — yerel mevzuat dosyalarında tespit edilen boşluklar

| Dosya | Sorun | Etki |
|---|---|---|
| `vtr-vir/mevzuat/KVK.md` | **Türkçe ı/i harfleri ASCII dönüşümünde çakışıyor** — m.5/1'de (ı) eğitim, (i) risturn bentleri ayırt edilemiyor, bent sıralaması bir harf kaymış görünüyor. | Bent harfi bu dosyadan okunamaz. *(teyit turu 01'de tespit edildi)* |
| `vtr-vir/mevzuat/KVKUGT.md` | **"Bakanlar Kurulunca vergi muafiyeti tanınan vakıflar"** ifadesi 15 yerde geçiyor; güncel kanun **"Cumhurbaşkanınca"** diyor (2018 sonrası). | Tebliğ metni bu yönden bayat; kurum adları kanun metninden alınmalı. |
| `vtr-vir/mevzuat/KVK.md` | **Madde 12 metni dosyada İKİ KEZ geçiyor ve ölçüler farklı:** birinci nüsha "öz sermayenin **iki katı**", ikinci nüsha "**üç katı**". KVKUGT üç katıyı teyit ediyor. | Tek nüshaya bakarak oran alınamaz; hangi nüshanın okunduğu belirtilmeli. |
| `vtr-vir/mevzuat/KVK.md` | **5520 s.K.'nin 2006 tarihli orijinal gerekçe metnidir**, güncel kanun metni değildir. 2016'da 6728 s.K. ile eklenen sat-kirala-geri al istisnası bu dosyada yoktur; madde 5/1 bent harfleri güncel kanunla uyuşmuyor. | Bu dosyadan bent harfi veya sonradan eklenmiş hüküm doğrulanamaz. KVKUGT daha güncel. |

*Bu tablo, atom üretirken kaynağın kendisinde bulunan boşlukları kaydeder. Mevzuat MCP
bağlandığında ilk iş buradaki satırların kapatılmasıdır.*

---

## Bakım notu

Bu dosya elle değil, **atom üretiminin yan ürünü olarak** büyür. Bir atom yazılırken
`gecis_kontrolu` bloğu doldurulur; `VAR` satırları sicile, `ŞÜPHELİ` satırları açık
uçlara düşer. Sicil şişip elle yönetilemez hâle gelirse (kabaca 100+ kayıt) bir
`.base` görünümüne veya betikle üretilen tabloya taşınır — **o noktaya gelmeden
otomasyon kurulmaz.**
