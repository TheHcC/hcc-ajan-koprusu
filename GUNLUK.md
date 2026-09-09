# GÜNLÜK — baştan sona anlatı

En yeni kayıt en üstte. Bu dosya "ne konuşuldu, hangi aşamalardan geçildi"
sorusunun cevabıdır. Sohbete yeni katılan bir model önce burayı okur.

---

## 2026-09-09 (2. tur) · claude-sonnet-5 (Claude Code) — İki inbox item işlendi, Codex'e görev bırakıldı

### Yapılan

Cihan'ın dün gece Claude Code dışında (Claude.ai sohbetinden, elle) pushladığı
iki `gelen-kutusu/claude-code/` dosyası (K-001 format itirazı, 2025/3 revizyon
sınav analizi) değerlendirildi. İkisi de metodolojik olarak aynı sınırı taşıyor:
tüm bulgular Drive dosya listesi metadata'sından (ad, boyut, tarih), **hiçbir
dosya içeriği açılmadı.**

- Sınav analizinin somut, doğrulanabilir kısmı (45 puanlık dört konunun arşivde
  boşluk olduğu) kabul edildi ve adım 12'nin pilot konusu "sat-kirala-geri al
  istisnası"na sabitlendi (DURUM.md).
- İtirazın K-001 revizyonu (poster donmuş export, XMind/Markdown düzenlenebilir
  kaynak olmalı) prensipte kabul edildi ama **resmi karara (K-005) çevrilmedi** —
  itirazın kendisi de içerik doğrulamadığını itiraf ediyor; kör onaylamak K-001'in
  düştüğü hatayı (biçim ≠ kullanılabilirlik) tekrarlardı.
- Kalan doğrulama işi (BAĞIŞ posterinin sınavdaki 4 alt tipi karşılayıp
  karşılamadığı, 2 XMind'ın gerçek yapısı, 2 "isim tuzağı" dosyasının içeriği)
  `gelen-kutusu/codex/2026-09-09-icerik-dogrulama-gorevi.md` olarak Codex'e
  görev bırakıldı — bu köprü deposundan Drive'a erişim yok.
- İki inbox dosyası `## Yanıt` ile kapatıldı; atom şemasına önerilen
  `iliskili_maddeler` / `ad_icerik_riski` alanları not edildi ama uygulanacak
  dosya bu depoda değil (`ymm-korpus/09_bilgi/`, yerel).

### Paralel oturum notu

Bu değerlendirme sürerken **aynı anda başka bir Claude Code oturumu** (yerel
terminal, `bjxyjg3-vivid-frog`) adım 9'u tamamlayıp pushladı (aşağıdaki giriş).
Cross-session mesajlaşma bu ortamdan o oturuma ulaşamadı (farklı makine, kanal
açık değil); çakışma `git fetch` ile pull edilip güncel DURUM.md/GUNLUK.md
üzerine ekleme yapılarak yönetildi, üzerine yazılmadı.

### Sıradaki

Codex'in içerik doğrulama raporu bekleniyor. Rapor gelince: (1) K-005 kararı
`KARARLAR.md`'ye işlenir, (2) BAĞIŞ posteri sonucu kaydedilir, (3) atom şeması
önerisi yerel oturumda uygulanır.

---

## 2026-09-09 · claude-opus-5 + claude-sonnet-5 (Claude Code) — Revizyon arşivi indekslendi

### Yapılan

Geçmiş çalışma arşivinin en kalabalık klasörü (Revizyon) tam olarak tasnif edildi:
**65 dosya + 1 kısayol.** İş bir Sonnet alt-agent'ına verildi; ham PDF'ler ana modelin
bağlamına hiç girmedi. Alt-agent'a verilen maliyet freni işe yaradı — dosya gövdesi
okuma hakkı (en fazla 5 dosya) hiç kullanılmadı, sınıflandırma başlık, tarih ve
boyuttan yapıldı.

Sonuç: ÖLÜ 10 · RİSKLİ 24 · KALICI 23 · BELİRSİZ 9

### Kalite kapısı — alt-agent çıktısı denetlendi

Bu, çok-ajanlı çalışmanın denetim katmanının ikinci canlı örneği.

**Bağımsız doğrulananlar:** dosya sayımı (tablo satır sayısıyla tutarlı), mükerrer çift
tespiti (aynı ad + aynı bayt boyutu, ayrı ayrı teyit edildi), en büyük dosya, bütün
dayanak atıflarının tahmin etiketi taşıması.

**Düzeltilen — sınıflandırma hatası:** Enflasyon düzeltmesi konulu **9 dosyanın 8'i
"ÖLÜ" işaretlenmişti.** Bu yanlış: ilgili düzenleme süreli bir tedbir değil, kalıcı
mevzuattır; yalnızca *geçiş* belgeleri tek seferliktir. Sekiz dosya "RİSKLİ"ye alındı,
geçiş belgesi ÖLÜ bırakıldı.

Gerekçe kayda değer çünkü genel bir kural: **hata asimetrik.** Yanlışlıkla "ölü" demek
kullanılabilir malzemeyi çöpe atar; yanlışlıkla "riskli" demek yalnızca bir doğrulama
turu maliyetidir. Belirsizlikte daha az yıkıcı olan tarafa yaslanılır.

**Eklenen — kaçırılmış değer:** Alt-agent "poster adayı" olarak 5 PDF önermişti. Oysa
arşivde **16 dosya zaten poster/tablo formatında** — yani dönüştürülecek aday değil,
hazır atom. Bunların 10'u kalıcı nitelikte ve bugün kullanılabilir durumda. Ayrı bir
bölüm olarak indekse eklendi.

Bir yan bulgu: 16 dosya ancak yaklaşık 10 ayrı konu — dört konuda hem "poster" hem
"tablo" versiyonu var. Tekilleştirilmeden kütüphaneye alınırlarsa "hangisi güncel"
sorusu doğar.

### Sıradaki

İki seçenek var ve sıra kullanıcının tercihine bağlı: kalıcı poster atomlarının
künyelendirilmesi (sistemin ilk gerçek çıktısı, mevzuat doğrulaması beklemez) ya da
SPK arşivinin indekslenmesi.

---

## 2026-09-08 (2. tur) · claude-opus-5 (Claude Code) — Köprü kuruldu, P0 düzeltildi

### Köprü deposu yayına alındı

Bu depo oluşturuldu ve public olarak yayımlandı. Anonim okunabilirlik fiilen
doğrulandı (kimlik doğrulaması olmadan HTTP 200). Artık Claude.ai sohbeti ve ChatGPT
bu depoyu okuyup `gelen-kutusu/` üzerinden katkı sunabilir.

### P0 kural çelişkisi giderildi

Üç değişiklik yapıldı:

1. **`inceleme-os\SISTEM.md` §2** — Antigravity atölye satırı ölü bir yolu
   (`Desktop\Anti\...`) gösteriyordu; kanonik ağaca çekildi. Önceki hâliyle, kurala
   *tam uyan* bir ajan var olmayan klasöre yönleniyordu.
2. **`AGENTS.md` §7** — "Diğer ajanlar kuyruğa nasıl yazar" alt bölümü ve JSONL satır
   şeması eklendi. Tespit şuydu: `/save-bulgu` bir Claude Code slash komutu, diğer
   CLI'lar onu çağıramıyor. Çözüm ikinci bir kuyruk açmak değil — kuyruk zaten düz bir
   JSONL dosyası, şeması belgelendi. Vault'a yazma yetkisi (onay kapısı) tek elde kaldı.
3. **Bayat iddia düzeltildi** — aynı bölümde "kuyruk 28.07'den beri işlenmedi, vault
   24 Haziran'da beslenmeyi bıraktı" yazıyordu. Doğrulandı ve **yanlış** çıktı: arşiv
   dosyasında 2026-09-03 tarihli işlenmiş bir kayıt ve hedef notu mevcut.

Üçüncüsü öngörülen iş değildi; aynı bölümü düzenlerken bulundu ve kanıtla doğrulandığı
için düzeltildi. **Ders:** kural dosyalarındaki tarihli iddialar da bayatlıyor. Bu,
poster künyesindeki `son_dogrulama` alanının neden zorunlu olduğunun kural-dosyası
düzeyindeki karşılığıdır.

### Bir hata ve düzeltilmesi

SISTEM.md'ye ilk yazma denemesinde kaçış dizisi hatası satırı bozdu
(ters bölü + v ve ters bölü + a dizileri kontrol karakterine dönüştü). Yazımdan hemen sonraki doğrulama bunu
yakaladı, satır ham dizgeyle yeniden yazıldı ve `cat -v` ile kontrol karakteri
kalmadığı teyit edildi. Kayda geçiriliyor çünkü sistemin kuralı bu: **yazdıktan sonra
doğrula, doğrulamadan "oldu" deme.**

### Sıradaki

Revizyon arşivinin indekslenmesi (68 dosya): her dosya için konu, tür, tarih,
bayatlama riski (ÖLÜ / RİSKLİ / KALICI) ve dayanak tahmini.

---

## 2026-09-08 · claude-opus-5 (Claude Code) — Teşhis oturumu

### Başlangıç noktası

Cihan, `ymm-korpus` projesinden verim alamadığını, strateji değiştirmek istediğini
söyledi. Şikâyeti üç başlıktı: (a) sistem çok şey üretti ama fiilen çalışılamadı,
(b) her oturumda nereden başlanacağı belirsiz, (c) üretilen flash kartlar ve zihin
haritası sınav gerçekliğiyle bağdaşmıyor.

### Ölçüm: sistem ne üretmişti

`ymm-korpus`: 715 dosya, 183 MB, 4 dersin ham korpusu, 296 kayıtlık envanter,
Tier haritaları, 30 Python scripti, 17 dış-model direktifi, 5 strateji belgesi.

Buna karşılık öğrenme katmanına düşen: 5 monograf, 120 SRS kartı, 1 zihin haritası
bloğu, 0 adet elle yazılmış süreli cevap, hata sicili yok, KPI paneli yok.

**Teşhis:** Proje bir korpus-mühendisliği projesine dönüşmüştü. Kendi master planının
1 numaralı ilkesi — "her çalışma bloğu yazılı çıktıyla biter" — hiçbir yerde
uygulanmamıştı.

### Kartların neden kullanılamaz olduğu (kanıtlı)

İlk ~12 kart iyi: gerçek analojiler taşıyor. Sonrası çöküyor. Örnek bir kartın
hafıza çengeli, cevap anahtarı metnindeki kelime frekansından türetilmişti — yani
"şu soruda şu kelimeleri hatırla" diyordu; sınavda karşılığı yok. Başka kartlarda ön
yüz X soruyor, arka yüz Y cevaplıyor.

**Kök sebep:** Kart doğrulama raporunda K1'den K10'a bütün denetimler %100 geçmişti.
Tip dağılımı hedefin birebir aynısı çıkmıştı. Yani üretici bir kotayı tutturmak için
kart üretmiş, denetim ise yalnız **biçimi** ölçmüştü. "Bu kart bir insanın işine
yarar mı" diye soran hiçbir kapı yoktu.

> Bu, projenin tek cümlelik hastalığı: **sistem kendi ürettiği çıktıyı kendi
> ölçütleriyle denetledi ve ölçütlerin hiçbiri kullanılabilirlik değildi.**

### Dönüm noktası: geçmiş arşivin incelenmesi

Cihan, farklı bir Google hesabındaki kişisel çalışma arşivini paylaşıma açtı
(paylaşım yoluyla erişildi; hesap değiştirmeye gerek kalmadı).

Arşiv tek bir şey gösterdi: **çalışma stili zaten var, kanıtlı ve görsel.**
2022'de sermaye piyasası mevzuatı madde bloklarına bölünüp on iki ayrı zihin
haritası ve PNG çıktısı üretilmiş; 2023'te muhasebe/vergi konularında tablo-poster
serisi; 2025'te güncel vergi konularında sekiz poster daha. Üç yıl, dört ders,
tek format.

Karşılaştırma çarpıcıydı: aynı konuda Cihan'ın 2022'de kendi ürettiği zihin haritası
866 KB, sistemin 2026'da ürettiği 3 KB'lık boş iskeletti. Sistem, Cihan'ın dört yıl
önce çok daha derin yaptığı şeyin kabuğunu üretip "sen doldur" demişti.

**Sonuç:** Eski sistemin analitik gücü (hangi maddenin gerçekten sorulduğu ölçümü)
değerli ve korunur. Yanlış olan, aynı sistemin **format kararını da vermeye
kalkmasıydı.** Format kararı zaten Cihan'da, kanıtlı.

### Hedefin genişlemesi

Cihan hedefi netleştirdi: zaman baskısı yok, amaç yalnız sınavı geçmek değil.
İstenen, mevzuat değiştikçe kendini güncelleyen, kendi öğrenme stiline oturan,
çok-ajanlı ve halüsinasyona kapalı bir ikinci beyin altyapısı. YMM sınavı bu
sistemin ilk yükü.

### Paralel iş: Obsidian dağınıklığı

Cihan aynı konuyu OpenCode/Astra'ya (gpt-6-astra) da sormuş, o da bir analiz raporu
üretmişti. Rapor devralınmadan önce **bağımsız denetlendi** — sistemin ilk
halüsinasyon kontrolü:

- 8 kayıtlı vault iddiası: doğrulandı
- Bulgu kuyruğuna yalnız tek ajanın yazabildiği: doğrulandı
- İki kural dosyası arasındaki konum çelişkisi: doğrulandı
- Bulgu hattının tamamen durmadığı: doğrulandı
- **Raporun kaçırdığı bulgu:** Obsidian MCP sunucusunun izinli dizini yanlış yere
  bakıyor; asıl bilgi merkezi vault'una hiç erişemiyor. "Obsidian MCP'si var" ile
  "Obsidian vault'una erişiyor" aynı şey değilmiş.

Astra'nın raporu sağlam çıktı: iddialarını abartmamış, sınırlarını dürüstçe yazmıştı.

### Alınan kararlar

Ayrıntı ve gerekçeler `KARARLAR.md` dosyasında. Özet: bilgi atomu poster olacak;
yeni vault açılmayacak, bilgi ağacı `ymm-korpus/09_bilgi/` altına kuruldu; mevzuat
teyitleri MCP bağlantısı düzelene kadar etiketle bekleyecek; bu köprü deposu public
olacak.

### Yapılanlar

- `.gorev-durumu/aktif-gorev.json` kuruldu — 14 adımlık plan diske yazıldı,
  kesinti hâlinde buradan devam edilir
- `ymm-korpus/09_bilgi/` ağacı açıldı (`00-index`, `10-poster`, `20-mevzuat-izleme`)
- Bu köprü deposu kuruldu

### Sıradaki

P0 kural çelişkisinin iki satırlık düzeltmesi (Cihan onayı bekliyor), ardından
geçmiş arşivin indekslenmesi — hangi dosya ölü, hangisi güncellenmeli, hangisi
kalıcı poster adayı.
