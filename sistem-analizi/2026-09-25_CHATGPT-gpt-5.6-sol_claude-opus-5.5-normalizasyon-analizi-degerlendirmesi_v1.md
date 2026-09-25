---
baslik: Claude Opus 5.5 Darbogaz Normalizasyon Analizi — ChatGPT Degerlendirmesi
yazar: ChatGPT (GPT-5.6 Sol)
tur: sistem-analizi / mimari-capraz-denetim
tarih: 2026-09-25
versiyon: v1
durum: DEGERLENDIRME
girdi: "[[2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1]]"
iliskili:
  - "[[2026-09-25_GROK_ai-radar-pilot-raporu_v1]]"
  - "[[2026-09-25_CHATGPT-gpt-5.6-sol_grok-ai-radar-pilot-capraz-denetimi_v1]]"
etiketler: [hcc-sistem-analizi, chatgpt, claude, normalizasyon, kanit-defteri, mimari]
---

# Claude Opus 5.5 Darboğaz Normalizasyon Analizi — ChatGPT Değerlendirmesi (v1)

## Yönetici özeti

Claude'un analizi Grok raporunun üzerine doğru seviyede çıkıyor: tek tek 10 semptoma 10 yeni ürün önermek yerine bunları **4 kök neden** altında normalize ediyor. Bu yaklaşım HCC'nin mevcut “araç ekleyerek çözme” eğilimini frenlediği için mimari açıdan güçlü.

Benim değerlendirmemde:

- **N1 Tek durum makinesi:** doğru ve yüksek öncelikli.
- **N2 Tek yönlü türetim:** doğru problem, fakat uygulanmadan önce canonical-path ve Drive/Obsidian senkron topolojisi test edilmeli.
- **N3 Kanıt Defteri:** en yüksek stratejik kaldıraç; fakat `RESMI` statüsü erişim aracından değil kaynağın origin/provenance zincirinden türetilmeli.
- **N4 Yönlendirme ≠ yargı:** çok doğru; Happy'den önce izin ve router mekanizmasını sadeleştirmek mantıklı.
- **Tek aktif pilot / 14 gün:** güçlü yönetişim ilkesi; otomatik kapama yerine `EXPIRED / yeniden onay gerekli` statüsü daha güvenli.

## 1. Kök neden normalizasyonu — isabetli

Claude'un 10 darboğazı 4 kök nedene indirmesi sistem tasarımı açısından doğru:

1. durum dağınık,
2. kanonik kaynak var ama türetim yok,
3. doğrulama tek noktaya kilitli,
4. Cihan mekanik router + hukuki karar verici işlerini birlikte yapıyor.

Bu, yeni araç bağımlılığını azaltır ve sistemin “her problem için yeni agent” yönünde şişmesini engeller.

## 2. N1 — Tek durum makinesi

En doğru kısa vadeli müdahale budur.

Şu an klasörler, kuyruk JSON'ları, Drive dizinleri ve insan hafızası kısmen durum taşıyor. `TASLAK -> URETILDI -> MEKANIK_PASS -> MEVZUAT_PASS -> KABUL -> ARSIV` gibi tek bir state machine bunu açık hâle getirir.

Ancak iki ilave kural öneriyorum:

### 2.1. State ledger kanonik olmalı, klasörler yalnız view

Drive'da bir dosyanın `01_CIKTI_DENETIM_BEKLIYOR` içinde bulunması state değildir; ledger state'in görünümüdür.

### 2.2. Her geçiş idempotent ve kanıtlı olmalı

Her state transition:

- `kim`,
- `ne zaman`,
- `hangi kanıtla`,
- `hangi önceki state'ten`

alanlarını taşımalıdır.

Aksi hâlde yeni ledger yalnız yeni bir paralel gerçeklik olur.

## 3. N2 — Tek yönlü türetim

Prensip doğru: kanonik kaynak bir yerde yaşamalı, diğer yüzeyler üretilmelidir.

Fakat burada Claude'un önerisinde uygulanmadan önce cevaplanması gereken kritik topoloji sorusu vardır:

> `HcC Kasa Obsidian` Drive tarafından senkronize edilen fiziksel klasör ise, `ymm-korpus` git working tree ile aynı fiziksel dosya ağacını paylaşmak Drive sync + git + Obsidian üçlüsünde yarış koşulu yaratır mı?

Bu nedenle doğrudan “Obsidian git working tree'yi okusun” uygulanmamalı; önce küçük bir test repo/vault ile:

- dosya lock,
- rename,
- conflict copy,
- line ending,
- hidden `.git` davranışı,
- Google Drive stream/mirror modu

test edilmelidir.

Benim güvenli varsayılanım:

**git = canonical**  
**vault = tek yönlü export/read surface**

şeklindedir; ancak yerel topoloji doğrulanmadan kesinleştirilmemelidir.

## 4. N3 — Kanıt Defteri: en yüksek kaldıraç

Claude'un en güçlü önerisi budur.

Bir atıf bir kez doğrulandığında şu bilgi yeniden kullanılabilir hâle gelir:

- kaynak,
- normalize edilmiş resmi metin hash'i,
- doğrulama tarihi,
- kaynak origin,
- erişim aracı,
- güven seviyesi,
- bağımlı atom/SP'ler.

Bu üç problemi aynı anda azaltır:

1. her pakette aynı mevzuatın yeniden doğrulanması,
2. Claude Code / tek MCP'ye bağımlılık,
3. mevzuat değiştiğinde hangi bilgi atomlarının etkilendiğinin bilinmemesi.

### 4.1. `RESMI` statüsü için düzeltme

Claude direktifinde `chrome-devtools-mcp` üzerinden gelen her şeyin `ADAY` olması öneriliyor. Bu fazla kaba bir sınıflandırmadır.

Daha doğru model iki eksenlidir:

```text
kaynak_statu: RESMI | UZMAN | IKINCIL | BILINMIYOR
erisim_araci: mevzuat-mcp | chrome-devtools-mcp | browser | manuel | api
```

Örneğin GİB'in kendi alanından Chrome DevTools ile alınan içerik:

`kaynak_statu = RESMI`

`erisim_araci = chrome-devtools-mcp`

olabilir.

Buna ek olarak doğrulama sonucu ayrı alan olmalıdır:

`dogrulama = DOGRULANDI | ADAY | TEYIT_BEKLIYOR`

Bu ayrım, kaynak otoritesi ile erişim kanalını karıştırmaz.

### 4.2. Hash tek başına yeterli değil

Normalize edilmiş metin hash'i faydalı ama şu metadata da tutulmalıdır:

- canonical URL / belge no,
- retrieval timestamp,
- effective date / yürürlük dönemi,
- source version veya ETag/Last-Modified varsa,
- hash normalizasyon sürümü.

Aksi hâlde normalizasyon algoritması değiştiğinde bütün kayıtlar sahte “değişmiş” görünebilir.

## 5. “Codex ledger'dan mevzuat PASS verebilir” önerisi

Bu fikir doğru yönde ama otomatik PASS konusunda dikkat gerekir.

Ben bunu şöyle sınırlandırırım:

Codex ancak:

- paketteki bütün atıflar ledger'da mevcut,
- her kayıt `kaynak_statu=RESMI`,
- `dogrulama=DOGRULANDI`,
- freshness SLA içinde,
- pakette yeni yorum/analojik genişleme yok

ise **`MEVZUAT_KANIT_PASS`** verebilir.

Bu, nihai hukuki değerlendirme PASS'i değildir.

Yeni hukuki yorum, istisna zinciri veya kanunlar arası geçiş varsa Claude/ChatGPT bağımsız inceleme kapısı devam etmelidir.

## 6. Circuit breaker

İki timeout sonrası tüm batch'in durmaması doğru.

Ancak “iki timeout” global değil **source + endpoint + task** bazında tutulmalıdır. Aksi hâlde tek problemli GİB endpoint'i bütün kaynağı gereksiz yere devre dışı bırakabilir.

Önerilen alanlar:

```text
source_id
endpoint_or_query
failure_count
last_failure
next_retry
state: CLOSED | OPEN | HALF_OPEN
```

## 7. N4 — yönlendirme ≠ yargı

Claude'un burada yaptığı ayrım çok doğru.

Cihan'ın yapması gereken:

- KABUL / RED,
- riskli scope değişikliği,
- hukukî yorum ve politika kararı.

Cihan'ın yapmaması gereken:

- dosyayı hangi ajana vereceğini tekrar tekrar seçmek,
- klasör taşımak,
- “şimdi Claude'a ver” demek,
- zaten izin verilmiş dar çalışma alanında sürekli aynı file write prompt'una cevap vermek.

Dolayısıyla Happy'den önce deterministik router + dar izinler denenmelidir.

## 8. Üç bölgeli veri modeli

Zone 0/1/2 fikri yararlı ve sade.

Ancak bunu sadece araç listesine bağlamamak gerekir. Her **iş yükü** de zone taşımalıdır.

Örneğin:

```text
workload_zone: 0 | 1 | 2
tool_zone_ceiling: 0 | 1 | 2
```

Kural:

`workload_zone <= tool_zone_ceiling`

olmalıdır.

Bu, yeni araç geldiğinde karar vermeyi otomatikleştirir.

## 9. Tek aktif pilot / 14 gün kuralı

Çok değerli. HCC sisteminde “önerildi ama hiçbir zaman PASS/FAIL olmadı” birikimini engeller.

Ancak 14 gün sonunda otomatik `FAIL` veya “kapatıldı” yerine:

`EXPIRED — yeniden insan onayı olmadan devam edemez`

statüsü daha doğru olur.

Çünkü başarısızlık ile ilgilenilmemiş olmak aynı şey değildir.

Önerilen pilot lifecycle:

`ADAY -> PILOT -> PASS | FAIL | EXPIRED | REDDEDILDI | EMEKLI`

## 10. Faz sıralaması

Claude'un sıralaması genel olarak doğru:

1. Faz 0 hijyen,
2. N1 + N2 tasarımı,
3. N3 + Chrome DevTools pilotu,
4. bayatlama + izin optimizasyonu,
5. Happy ancak hâlâ gerçek ihtiyaç varsa.

Ben tek değişiklik yaparım:

**N2'nin uygulamasını N3'ten önce zorunlu kılmam.**

N2 topoloji riski taşıyor; N3 ise mevcut yapıya paralel, düşük riskli bir ledger olarak değer üretmeye başlayabilir. Dolayısıyla:

`Faz 1: N1`

`Faz 2A: N3 temel`

`Faz 2B: N2 küçük topoloji pilotu`

şeklinde paralel ama kontrollü ilerleme daha güvenlidir.

## 11. Claude Code direktifine ilişkin kritik not

Claude'un uygulama direktifi kapsamlı ve iyi korumalı; fakat T1 public GitHub mirror görevi kendi içinde bir güvenlik sorunu taşıyor: direktif dosyasının kendisinde yerel kullanıcı yolu ve private Drive klasör ID'si bulunuyor.

Bu nedenle public repo'ya **byte-level aynı direktif kopyası** atılmamalıdır. Public mirror için:

- yerel kullanıcı yolu genelleştirilmeli,
- private Drive folder ID kaldırılmalı,
- private bağlantılar sanitise edilmelidir.

Bu, direktifin kendi “hassas veri bulursan commit etme” kuralıyla da uyumludur.

## Sonuç

Claude'un analizi mimari olarak güçlü ve Grok raporundan daha yüksek seviyede. Benim ana düzeltmelerim:

1. N1 hemen uygulanabilir.
2. N3 en yüksek kaldıraç; kaynak statüsü / erişim aracı / doğrulama statüsü ayrılmalı.
3. N2 uygulanmadan önce Drive + git + Obsidian fiziksel topolojisi küçük pilotla test edilmeli.
4. Ledger'dan otomatik PASS yalnız kanıt katmanında olmalı; hukuki yorum kapısı korunmalı.
5. Circuit breaker endpoint bazlı olmalı.
6. Pilot 14 gün sonunda `EXPIRED` olmalı, otomatik FAIL değil.
7. Claude direktifinin public GitHub kopyası sanitise edilmeden paylaşılmamalı.
