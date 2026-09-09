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
| A-001 | KDV m.13/1-k için zorunlu **bağış protokolü** damga vergisine tabi mi? | İncelenmedi | 488 s. Damga Vergisi Kanunu (1) sayılı tablo `[TEYİT: kaynak gerekli]` |
| A-002 | KVK m.10/1-c'de kalkınmada öncelikli yöre ayrımı gerçekten yok mu? | Tebliğ okundu, **kanun metni okunmadı** | KVK m.10/1-c kanun metni |
| A-003 | 6361 s.K. kapsamındaki finansal kiralama sözleşmeleri damga vergisinden istisna mı? | Taranmadı | 488 s.K. (2) sayılı tablo · 6361 s.K. m.37 `[TEYİT: kaynak gerekli]` |
| A-004 | Sat-kirala-geri al istisnasının gerçek kişi/ferdi işletme karşılığı var mı? | İstisna KV mükelleflerine tanınmış; GVK tarafı incelenmedi | GVK m.40 / m.89 `[TEYİT: kaynak gerekli]` |
| A-005 | KVK'da sat-kirala-geri al istisnasının **gerçek bent harfi** nedir? | KVKUGT "(j)" diyor; yerel KVK.md'de (j) risturn istisnası | Güncel KVK m.5/1 kanun metni |

---

## Korpus sağlığı — yerel mevzuat dosyalarında tespit edilen boşluklar

| Dosya | Sorun | Etki |
|---|---|---|
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
