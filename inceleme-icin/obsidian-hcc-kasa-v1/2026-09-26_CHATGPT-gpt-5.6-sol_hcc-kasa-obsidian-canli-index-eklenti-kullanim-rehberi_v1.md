---
tip: sistem-rehberi
baslik: HcC Kasa Obsidian — Canlı İndeks ve Eklenti Kullanım Rehberi
alan: obsidian
durum: aktif
tarih: 2026-09-26
guncelleme: 2026-09-26
surum: v1
model: gpt-5.6-sol
kaynak: "HcC Kasa mevcut yapı denetimi + eklentilerin resmi GitHub dokümantasyonu"
karantina: false
mimaride-onaylandi: true
etiketler: [obsidian, ikinci-beyin, master-index, eklenti, hcc-kasa]
---

# HcC Kasa Obsidian — Canlı İndeks ve Eklenti Kullanım Rehberi v1

> [!success] Karar
> İlk fazda **Paket A + dört çekirdek eklenti** uygulanır: Folder Overview, QuickAdd, Linter ve Homepage. Meta Bind, Omnisearch ve Breadcrumbs kurulu kalabilir; fakat ikinci faza kadar sistemin veri modelini değiştiren otomasyonları devreye alınmaz.

← [[MASTER-INDEX|HcC Kasa Master Index]] · → [[20-Araclar/_index|20-Araclar Canlı İndeks]] · ← [[ANA-HARITA]]

---

## 1. Mimari: MOC ile canlı indeks birbirinin rakibi değil

HcC Kasa'da iki farklı navigasyon katmanı kullanılacaktır:

1. **MOC — anlam haritası:** İnsan/AI kürasyonu içerir. “Hangi not neden önemli, önce ne okunmalı, hangi fikir hangisine bağlı?” sorusunu cevaplar. Örnek: [[MOC-Kavramlar]], [[MOC-AI-Araclari]].
2. **Canlı `_index` / Base — envanter katmanı:** Klasörde veya kasada ne olduğunu otomatik gösterir. Yeni bilgi geldiğinde manuel liste bakımını ortadan kaldırır. Örnek: [[20-Araclar/_index]] ve [[MASTER-INDEX]].

Hedef akış:

```text
ANA-HARITA  →  anlam / yön bulma
     ↓
MASTER-INDEX  →  canlı kontrol paneli
     ↓
klasör _index sayfaları  →  otomatik envanter
     ↓
MOC'lar  →  editoryal/kavramsal bağlam
     ↓
atomik notlar / proje notları / kaynak notları
```

Bu ayrım sayesinde MOC'lar hiçbir zaman dev dosya listelerine dönüşmez; otomatik indeksler de “akıllı kürasyon” rolünü üstlenmeye çalışmaz.

---

# 2. İlk fazda oluşturulan dosyalar

- [[MASTER-INDEX]] — kasanın canlı giriş paneli.
- `00-panolar/KASA-MASTER.base` — tüm kasayı tarayan Obsidian Base.
- [[20-Araclar/_index]] — Folder Overview pilotu.
- `00-panolar/_SABLONLAR/QuickAdd-Hizli-Yakala.md` — güvenli Raw yakalama şablonu.

> [!warning] Pilot sınırı
> Bu fazda hiçbir mevcut dosya taşınmaz veya silinmez. Önce sistem kullanılarak davranışı gözlenir.

---

# 3. Eklentileri topluca kurmuş olman sorun mu?

Genel olarak **hayır**. Eklenti kurulu olması dosyaları kendi başına bozmaz. Risk, otomatik yazma/yeniden biçimlendirme yapan özelliklerin kontrolsüz açılmasından gelir.

Özel dikkat:

- **Folder Overview + Folder Notes** aynı anda etkin olmamalı. Folder Overview geliştiricisi iki eklentinin birlikte kullanılamayacağını açıkça belirtiyor. Eğer ayrıca Folder Notes kurduysan şimdilik **Folder Notes'u kapat**, Folder Overview açık kalsın.
- **Linter:** “lint on save” ve toplu vault lint işlemleri ilk hafta kapalı olsun. Önce tek dosyada dene.
- **QuickAdd:** yalnız tanımladığımız `Raw/` yakalama akışını kullan. Şimdilik otomatik taşıma/sınıflandırma yapmasın.
- **Meta Bind:** ikinci faza kadar sadece test notunda kullan; frontmatter'ı tıklamayla değiştirebildiği için yanlış bağlanan bir kontrol gerçek property'yi değiştirebilir.
- **Omnisearch:** ağırlıklı olarak okuma/indeksleme yapar; düşük riskli.
- **Breadcrumbs:** ilişki şemanı değiştirmeden tek başına mevcut notları bozmaz; fakat `up/down/next/prev` standardına geçmeden önce taksonomi kararı verilmelidir.

---

# 4. Folder Overview — “Bu klasörde şu an ne var?”

## Ne iş yapar?

Belirlediğin klasörün içeriğini dinamik bir liste/grid/explorer olarak gösterir. Dosya eklendiğinde, silindiğinde veya taşındığında görünüm güncellenebilir. HcC Kasa'daki ilk kullanım yeri [[20-Araclar/_index]].

## Ben senin yerinde nasıl kullanırdım?

**Kural:** Her ana klasörün bir `_index.md` dosyası olur; ama bunu hemen tüm kasaya yaymam. Önce `20-Araclar` pilotunu bir hafta kullanırım.

### Senaryo A — Yeni bir GitHub reposu keşfettin

Bugün “context memory” ile ilgili yeni bir repo notu `20-Araclar`a geldi. Eskiden `MOC-AI-Araclari`na ayrıca satır eklemezsen not görünmez olabiliyordu. Şimdi:

1. Dosya `20-Araclar`a gelir.
2. [[20-Araclar/_index]] içindeki Folder Overview onu otomatik gösterir.
3. Not gerçekten stratejikse daha sonra [[MOC-AI-Araclari]] içine **kürate edilmiş** bir bağlantı eklenir.

Yani “dosyanın varlığını hatırlama” işini makine, “önemini belirleme” işini sen/ajan yapar.

### Senaryo B — Jev alt klasörüne yeni analiz geldi

`20-Araclar/Jev/` içine yeni bir çalışma eklendiğinde `depth: 2` nedeniyle üst canlı indeks içinden görünür. MOC'u manuel güncellemek zorunda değilsin.

## Pilot ayarı

[[20-Araclar/_index]] içinde şu güvenlik tercihleri var:

- `autoSync: true` — görünüm canlı kalsın.
- `useActualLinks: true` — liste sadece görsel olmasın; Obsidian gerçek iç link olarak algılasın.
- `hideLinkList: true` — teknik link listesi ekranda gereksiz kalabalık yapmasın.
- `allowDragAndDrop: false` — pilotta yanlışlıkla dosya taşımayı önle.
- `depth: 2` — 20-Araclar ve bir alt seviyesini göster; tüm derin ağaçla ekranı boğma.

### İlk kontrol

[[20-Araclar/_index]] aç. Kod bloğu yerine gerçek dosya listesi görüyorsan çalışıyor. Liste görünmüyorsa Settings → Community plugins altında **Folder Overview etkin mi** kontrol et.

Pilot düzgün çalıştıktan sonra Settings → Folder Overview → **Auto-update links without opening the overview** seçeneğini açabilirsin. Böylece sayfayı açmasan bile graph/backlink ilişkilerinin güncel tutulması hedeflenir.

---

# 5. QuickAdd — “Aklıma geldi, iki dokunuşla kasaya at”

## Ne iş yapar?

Tek komutla not oluşturma, bir nota içerik ekleme veya birden fazla adımı ardışık çalıştırma aracıdır. Template, Capture, Macro ve Multi olmak üzere dört ana Choice tipi vardır.

## İlk fazda neden yalnız Raw?

Senin sisteminde yanlış klasöre otomatik bilgi atmak, birkaç saniye kazanmaktan daha pahalıdır. Bu yüzden ilk QuickAdd akışı **sınıflandırma yapmayacak**.

### Kuracağımız Choice

**Adı:** `HcC — Hızlı Yakala`  
**Tip:** Template  
**Template:** `00-panolar/_SABLONLAR/QuickAdd-Hizli-Yakala.md`  
**Hedef klasör:** `Raw`  
**Dosya adı:** `{{DATE:YYYY-MM-DD_HHmm}}-{{VALUE:baslik}}`

### Adım adım kurulum

1. Settings → QuickAdd.
2. `HcC — Hızlı Yakala` adında **Template Choice** oluştur.
3. Template path olarak `00-panolar/_SABLONLAR/QuickAdd-Hizli-Yakala.md` seç.
4. “Create in folder” / hedef klasör olarak `Raw` seç.
5. File Name Format'ı etkinleştir ve `{{DATE:YYYY-MM-DD_HHmm}}-{{VALUE:baslik}}` yaz.
6. Choice'un yanındaki ⚡ işaretini aç; böylece Command Palette'te görünür.
7. Mobilde istersen Obsidian mobil toolbar'a `QuickAdd: HcC — Hızlı Yakala` komutunu ekle.

Şablon sana `baslik`, `kaynak`, `ozet` ve `not` sorar. Aynı isimli `{{VALUE:...}}` alanları QuickAdd tarafından bir kez sorulup tekrar kullanılabilir.

### Senaryo A — X'te bir repo gördün

Telefondasın, uzun analiz yapmayacaksın:

- Başlık: `Agent-Reach repo`
- Kaynak: X/GitHub linki
- Özet: `Web araştırması için çoklu kaynak erişimi sağlayabilir`
- Not: `Claude Code / HCC Ajan Köprüsü açısından incele`

Dosya `Raw/`a düşer. [[MASTER-INDEX]] → **Raw Kuyruğu** görünümünde hemen belirir.

### Senaryo B — Vergiyle ilgili aklına bir kontrol fikri geldi

İnceleme dosyasına doğrudan yazmak yerine QuickAdd ile Raw'a kısa fikir bırak. Sonra uygun mahremiyet/alan kontrolünden geçirip `60-Vergi-Incelemeler` veya başka çalışma alanına aktar. Bu, “aklımdan çıktı” ile “yanlış yere yazdım” arasında güvenli orta yoldur.

## Sonraki faz

Bir haftalık kullanım sonrası ayrı choice'lar eklenebilir:

- `Yeni AI/Repo Notu` → `20-Araclar`
- `Yeni Kavram` → `10-Kavramlar`
- `Yeni Proje Notu` → `30-Projeler`

Ama önce Raw yakalama alışkanlığının çalıştığını görelim.

---

# 6. Linter — “Notların yazım ve YAML standardını koru”

## Ne iş yapar?

Markdown/YAML biçimini kurallara göre düzenler. En büyük faydası notların yıllar içinde farklı yazım biçimlerine kaymasını engellemektir.

## En büyük risk

Linter kötü değildir; **fazla kuralı aynı anda açmak** risklidir. Bazı kurallar birbirini etkileyebilir. Eski HcC notlarındaki frontmatter zaten farklı dönemlerden geldiği için tüm kasayı tek seferde lint etmek istemiyoruz.

## İlk hafta önerdiğim güvenli profil

**Aç:**

- Add blank line after YAML
- Dedupe YAML array values
- Heading blank lines
- Empty line around code fences
- Empty line around tables
- Consecutive blank lines
- Trailing spaces
- Line break at document end

**Şimdilik kapalı tut:**

- YAML key sort
- Insert YAML attributes
- Remove YAML keys
- Move tags to YAML
- Dosya adını/başlığı otomatik değiştiren agresif kurallar
- **Lint on save**
- Vault-wide bulk lint

### Senaryo

QuickAdd ile yeni Raw notunu oluşturdun. Önce notu açıp Command Palette → `Linter: Lint the current file` çalıştır. Öncesi/sonrası makulse o profil güvenlidir. 20–30 yeni notta sorun çıkmazsa yeni dosyalarda “lint on save” değerlendirilir.

**Ben olsam:** Eski kasayı geçmişe dönük güzelleştirmeye çalışmazdım. Linter'ı öncelikle **bundan sonra üretilen notların kalite kapısı** yapardım.

---

# 7. Homepage — “Obsidian açılınca nereden başlayacağım?”

## Ne iş yapar?

Belirlediğin bir note, Canvas, Base veya workspace'i açılış sayfası yapar.

## Senin için tek doğru ilk kullanım

Settings → Homepage:

- Homepage file: `00-panolar/MASTER-INDEX.md`
- Open on startup: **ON**
- View: **Reading** veya **Live Preview** (hangisi daha rahat gelirse)
- Eski sekmeleri ilk etapta kapatmak yerine **koru**; çalışma bağlamını kaybetme.

### Senaryo

Bir hafta sonra “Jev nerede kalmıştı?” diye Obsidian'ı açıyorsun. Klasör ağacında gezmek yerine ilk ekranda:

1. `20 — Araçlar` bağlantısına bas.
2. [[20-Araclar/_index]] canlı içeriğini gör.
3. Jev veya HCC Sistem Analizi'ne in.

Veya “dün telefondan ne kaydetmiştim?” diyorsun → Master Index → Raw Kuyruğu.

Homepage'in görevi bilgi üretmek değil; **nereden başlayacağını unutturmamak**.

---

# 8. Meta Bind — ikinci faz: “Notu küçük bir uygulamaya dönüştür”

Meta Bind, frontmatter property'lerini not içinde checkbox, seçim alanı veya buton gibi kullanmanı sağlar.

Resmî örneğin en basit hali:

```text
INPUT[toggle:done]
```

Bu kontrol `done` property’sini doğrudan `true/false` değiştirir.

## Senin senaryon

Bir HCC analizinde:

```yaml
karantina: true
mimaride-onaylandi: false
```

ileride not içinde görünür kontrollerle “onaylandı / bekliyor” yönetebiliriz. Ancak property isim standardımızı netleştirmeden Meta Bind'i bütün kasaya yaymayacağız.

**Ben olsam:** önce sadece `30-Projeler` ve HCC sistem belgelerinde dener, YMM/vergi bilgi tabanına sonradan taşırdım.

---

# 9. Omnisearch — ikinci faz: “Dosya adını değil anlamını hatırlıyorum”

Omnisearch, hızlı ve relevans ağırlıklı bir vault aramasıdır. Dosya adı, başlık ve içerik sinyallerini kullanır; yazım hatalarına da tolerans gösterir. Arama sonucundan doğrudan `[[wikilink]]` ekleyebilir.

## Senaryolar

### “O repo vardı, context'i oturumlar arasında koruyordu…”

Dosya adını hatırlamıyorsun. Omnisearch'e `oturum context hafıza claude` yaz. İlgili notları önem sırasına göre getirir.

### İç link eklerken

Yeni Jev notunda “HCC Ajan Köprüsü” ile bağlantı kuracaksın. Omnisearch sonucu üzerinden doğrudan link ekleyerek `[[HCC Ajan Köprüsü]]` bağlantısını üretirsin.

### Arama dili

- `"nakdi sermaye"` → tam ifadeyi ara
- `nakdi sermaye -Raw` → Raw benzeri istenmeyen eşleşmeyi azaltmak için dışlama mantığını kullan
- `.md jev router` → Markdown sonuçlarına odaklan

**Ben olsam:** Quick Switcher'ın yerine değil, “hangi notta olduğunu bilmiyorum” durumunda ana arama motoru yapardım.

---

# 10. Breadcrumbs — ikinci faz: “Bağlantı var ama ilişkinin türü ne?”

Normal Obsidian linki yalnızca A'nın B'ye bağlı olduğunu söyler. Breadcrumbs ise ilişkinin türünü tanımlar: `up/down`, `next/prev` veya kendi tanımladığın ilişki.

## Senin için güçlü olduğu yer: YMM

Örneğin:

```yaml
up: "[[Denetim/_index]]"
```

bir notun Denetim ağacının altında olduğunu açıkça söyler. Böylece:

`YMM → Denetim → Tasdik → Tasdikten Doğan Sorumluluk`

gibi gerçek bir hiyerarşi gezilebilir.

Ayrıca Tree/Matrix/trail görünümleri ile bulunduğun notun üst ve alt bağlamını gösterebilir.

## Neden ikinci faz?

Çünkü önce ilişki sözlüğüne karar vermeliyiz. `up/down` dışında `dayanak`, `karsit`, `benzer`, `uygular`, `istisna` gibi ilişkiler çok değerli olabilir ama bunları rastgele üretirsek yeni bir taksonomi dağınıklığı doğar.

> [!warning] Sürüm notu
> Breadcrumbs 4.15+ Obsidian 1.13 veya daha yenisini ister. Eski Obsidian 1.12 kullanılıyorsa 4.14.2 uyumluluk sürümü gerekir.

---

# 11. Ben senin yerinde olsam günlük nasıl kullanırdım?

## Sabah / işe başlarken

1. Obsidian açılır → Homepage otomatik [[MASTER-INDEX]] açar.
2. “Son 30 Gün” ve “Raw Kuyruğu”na bakarım.
3. Çalışacağım alan belliyse ilgili canlı `_index` veya MOC'a inerim.

## Gün içinde telefonda

Bir fikir/link/not geldi:

1. QuickAdd → `HcC — Hızlı Yakala`.
2. 20–40 saniyede başlık/kaynak/özet/not.
3. Kapat. Klasör seçmekle uğraşmam.

## Masaüstünde işleme seansı

Raw'daki 3–5 notu işlerim:

1. Mevcut nota mı eklenmeli, yeni not mu açılmalı?
2. Uygun klasöre taşı.
3. En az 1–2 gerçek `[[wikilink]]` ekle.
4. Stratejikse ilgili MOC'a kürate edilmiş bağlantı ekle.
5. Linter'ı **yalnız o dosyada** çalıştır.

## Bir şeyi bulamadığımda

- Dosya adını biliyorsam Quick Switcher.
- Konuyu/hatırladığım kelimeleri biliyorsam Omnisearch.
- Benzer fikir arıyorsam Smart Lookup / Smart Connections.
- “Bu notun üst/alt bağlamı ne?” diyorsam ileride Breadcrumbs.

Bu dört arama/navigasyon katmanını birbirine karıştırmazdım.

---

# 12. İç linkleme kuralları

HcC Kasa için basit ve sürdürülebilir kural:

1. Her kalıcı not en az **bir üst navigasyon noktasına** bağlanır: MOC, `_index`, proje panosu veya Master Index.
2. Yalnız konu benzer diye 10 link eklenmez; **anlamlı ilişki** varsa link verilir.
3. MOC manuel kürasyondur; her yeni dosyayı MOC'a eklemek zorunlu değildir.
4. `_index` eksiksizlik içindir; Folder Overview bunu otomatik sağlar.
5. Raw notları kalıcı bilgi ağı sayılmaz; işlenene kadar `karantina: true` kalır.
6. Dosya adı değişirse Obsidian'ın “Automatically update internal links” davranışı açık tutulur.
7. HCC Sistem Analizi gibi denetim/versiyon belgelerinde dosya adlandırması korunur: `YYYY-MM-DD_MODEL_kisa-konu_vN.md`.

---

# 13. Bir haftalık pilot başarı kriterleri

Pilot başarılı sayılırsa:

- [ ] `20-Araclar/_index` yeni dosyaları manuel bakım olmadan gösteriyor.
- [ ] Master Index günlük başlangıç noktası haline geliyor.
- [ ] QuickAdd ile en az 5 gerçek Raw kaydı alındı.
- [ ] Raw'a atılan notlarda “nereye koyacağım?” sürtünmesi azaldı.
- [ ] Linter tekil kullanımda istenmeyen içerik değişikliği yapmadı.
- [ ] Homepage çalışma bağlamını kolaylaştırdı.
- [ ] Kasa performansında hissedilir yavaşlama oluşmadı.

Bu kontrol geçerse sonraki faz: diğer ana klasörlere `_index` yayılımı + Meta Bind/Omnisearch/Breadcrumbs'in kontrollü yapılandırılması.

---

## Bağlantılar

- [[MASTER-INDEX]]
- [[ANA-HARITA]]
- [[20-Araclar/_index]]
- [[MOC-AI-Araclari]]
- [[PROJELER-DURUM]]
