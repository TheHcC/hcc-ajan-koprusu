# GÜNLÜK — baştan sona anlatı

En yeni kayıt en üstte. Bu dosya "ne konuşuldu, hangi aşamalardan geçildi"
sorusunun cevabıdır. Sohbete yeni katılan bir model önce burayı okur.

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
