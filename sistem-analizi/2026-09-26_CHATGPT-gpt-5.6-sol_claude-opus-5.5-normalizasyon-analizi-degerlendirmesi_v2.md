---
baslik: Claude Opus 5.5 Darbogaz Normalizasyon Analizi — ChatGPT Degerlendirmesi
yazar: ChatGPT (GPT-5.6 Sol)
tur: sistem-analizi / mimari-capraz-denetim
tarih: 2026-09-26
versiyon: v2
onceki_versiyon: "[[2026-09-25_CHATGPT-gpt-5.6-sol_claude-opus-5.5-normalizasyon-analizi-degerlendirmesi_v1]]"
durum: DEGERLENDIRME_REVIZE
girdi: "[[2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1]]"
iliskili:
  - "[[2026-09-25_GROK_ai-radar-pilot-raporu_v1]]"
  - "[[2026-09-25_CHATGPT-gpt-5.6-sol_grok-ai-radar-pilot-capraz-denetimi_v1]]"
revizyon_nedeni:
  - "Cihan'in kurum bilgisayarinda eski Chrome surumu kullanmak zorunda oldugunu bildirmesi"
  - "Chrome DevTools MCP resmi gereksinimlerinin yeniden dogrulanmasi"
  - "Faz siralamasinin N1 -> N3 -> tarayici adaptoru -> N2 olarak netlestirilmesi"
etiketler: [hcc-sistem-analizi, chatgpt, claude, normalizasyon, kanit-defteri, mimari, chrome-devtools, revizyon]
---

# Claude Opus 5.5 Darboğaz Normalizasyon Analizi — ChatGPT Değerlendirmesi (v2)

## Yönetici özeti

Claude'un analizi Grok raporunun üzerine doğru seviyede çıkıyor: tek tek semptomlara yeni araç eklemek yerine bunları birkaç kök mimari nedene indiriyor. Bu yaklaşım HCC'nin “araç ekleyerek çözme” eğilimini frenlediği için güçlü.

v2'de ana görüşüm şudur:

- **N1 Tek durum makinesi:** hemen uygulanabilir ve yüksek öncelikli.
- **N3 Kanıt Defteri:** en yüksek stratejik kaldıraç; N1'den hemen sonra gelmeli.
- **Chrome DevTools MCP:** kurum bilgisayarındaki eski Chrome nedeniyle artık ilk pilot değildir; bu makinede resmi olarak desteklenmeyebilir.
- **N2 Tek yönlü türetim:** doğru hedef ama küçük topoloji pilotu olmadan uygulanmamalı.
- **N4 Yönlendirme ≠ yargı:** doğru; Cihan final karar kapısı olarak kalmalı, mekanik routing otomatikleşmeli.
- **GrokBot Radar:** çekirdek üretim hattının içine değil, dış teknoloji/radar katmanına yerleştirilmeli.

## 1. Kök neden normalizasyonu — isabetli

Claude'un görünen darboğazları dört kök nedene indirmesi sistem tasarımı açısından doğrudur:

1. durum dağınık,
2. kanonik kaynak var ama türetim yok,
3. doğrulama tek noktaya kilitli,
4. Cihan mekanik router + hukuki karar verici işlerini birlikte yapıyor.

Bu çerçeve korunmalı.

## 2. N1 — Tek durum makinesi

En doğru kısa vadeli müdahale budur.

Klasör, Drive konumu veya ajan hafızası state değildir. Kanonik state tek ledger'da yaşamalıdır:

`TASLAK -> URETILDI -> MEKANIK_PASS -> MEVZUAT_KANIT_PASS -> HUKUKI_MUHAKEME_PASS -> KABUL -> ARSIV`

### 2.1. Neden iki ayrı PASS öneriyorum?

Claude'un tek `MEVZUAT_PASS` durumu kaynak doğrulama ile hukuki sonucu birbirine fazla yaklaştırıyor.

- `MEVZUAT_KANIT_PASS`: atıf gerçekten var mı, resmi mi, güncel mi, hash uyuşuyor mu?
- `HUKUKI_MUHAKEME_PASS`: bu kaynak gerçekten paketteki sonuca götürüyor mu, istisna zinciri/kanunlar arası geçiş doğru mu?

Bu ayrım özellikle YMM/vergisel çalışma için önemlidir.

### 2.2. Her geçiş kanıtlı ve idempotent olmalı

Her transition şu alanları taşımalıdır:

- kim,
- tarih/saat,
- önceki state,
- yeni state,
- kanıt bağlantısı/hash'i,
- yorum/not.

Aksi hâlde ledger yeni bir paralel gerçeklik olur.

## 3. N3 — Kanıt Defteri: en yüksek kaldıraç

Claude'un en güçlü önerisi budur ve **N2'den önce değer üretmeye başlayabilir**.

Her atıf bir kez doğrulandığında şu bilgiler yeniden kullanılabilir olmalıdır:

- canonical kaynak,
- belge/madde kimliği,
- resmi metin hash'i,
- doğrulama tarihi,
- effective date / yürürlük dönemi,
- kaynak origin,
- erişim aracı,
- doğrulama sonucu,
- bağımlı atom / Study Pack listesi.

### 3.1. Origin ile transport ayrılmalı

`chrome-devtools-mcp` gibi erişim araçlarına otomatik `ADAY` vermek doğru değildir.

Önerilen model:

```text
kaynak_statu: RESMI | UZMAN | IKINCIL | BILINMIYOR
origin: gib.gov.tr | mevzuat.gov.tr | resmigazete.gov.tr | ...
erisim_araci: mevzuat-mcp | chrome-devtools-mcp | browser | manuel | api
dogrulama: DOGRULANDI | ADAY | TEYIT_BEKLIYOR
```

Örneğin GİB'in kendi alanındaki resmi özelge Chrome üzerinden okunuyorsa kaynak hâlâ `RESMI` olabilir; Chrome yalnız erişim yöntemidir.

### 3.2. Hash tek başına yeterli değildir

Şunlar da tutulmalıdır:

- canonical URL,
- retrieval timestamp,
- source version / ETag / Last-Modified varsa,
- hash normalization version,
- yürürlük başlangıç/bitiş bilgisi varsa.

## 4. Ledger'dan otomatik PASS sınırı

Codex veya başka bir ajan ledger üzerinden yalnız **kanıt katmanı PASS'i** verebilir.

Şartlar:

- tüm atıflar ledger'da mevcut,
- `kaynak_statu=RESMI`,
- `dogrulama=DOGRULANDI`,
- freshness SLA içinde,
- pakette yeni analoji/yorum yok.

Yeni yorum, K-006 kanunlar arası geçiş, istisna zinciri veya özelgeden genel kurala genişletme varsa bağımsız hukuki reviewer gerekir.

## 5. Circuit breaker

İki timeout sonrası tüm batch'i durdurmamak doğru.

Ancak devre kesici global değil şu anahtarla tutulmalı:

```text
source_id + endpoint/query + task_type
```

Alanlar:

```text
failure_count
last_failure
next_retry
state: CLOSED | OPEN | HALF_OPEN
```

## 6. N2 — Tek yönlü türetim

Prensip doğru fakat uygulama öncesi fiziksel topoloji pilotu gerektirir.

`HcC Kasa Obsidian` Google Drive ile senkronize bir fiziksel klasör. Aynı dosya ağacını git working tree ile birleştirmek şu riskleri doğurabilir:

- conflict copy,
- rename çakışması,
- CRLF/LF gürültüsü,
- Drive stream/mirror davranışı,
- Obsidian metadata/frontmatter bozulması,
- mobil Drive edit'i ile git diff çatışması.

Bu nedenle önce 3–5 test Markdown dosyasıyla küçük pilot yapılmalıdır.

Güvenli varsayılan:

**git = canonical**

**vault/Drive = tek yönlü türetilmiş read/edit policy'si açıkça tanımlı yüzey**

Yerel topoloji PASS olmadan bu kesinleştirilmemelidir.

## 7. N4 — Yönlendirme ≠ yargı

Claude'un bu ayrımı doğru.

Cihan'ın yapması gereken:

- KABUL / RED,
- önemli kapsam değişikliği,
- hukuki risk kararı,
- mimari politika kararı.

Cihan'ın yapmaması gereken:

- “VR11 geldi, Claude'a söyle”,
- “bunu Codex'e ver”,
- “çıktıyı 01'e taşı”,
- kota bitince hangi ajana geçileceğini tekrar tekrar seçmek,
- üç hedefi elle eşitlemek.

Hedef: Cihan'ı mekanik **human-in-the-loop** olmaktan çıkarıp **human-on-the-loop + final acceptance authority** konumuna taşımaktır.

## 8. Pilot yaşam döngüsü

Tek aktif pilot ilkesi yerinde.

Önerilen lifecycle:

`ADAY -> PILOT -> PASS | FAIL | EXPIRED | DONDURULDU | REDDEDILDI | EMEKLI`

`DONDURULDU` ve `EXPIRED` ayrımı önemlidir:

- FAIL = test edildi ve başarısız oldu.
- DONDURULDU = bağımlılık/zaman/öncelik nedeniyle bilinçli bekletildi.
- EXPIRED = 14 gün içinde karar çıkmadı; yeniden insan onayı olmadan devam edemez.

Aynı anda **maksimum 1 ACTIVE PILOT** kuralını destekliyorum.

## 9. Chrome DevTools MCP — kurum eski Chrome kısıtı nedeniyle revizyon

### 9.1. Yeni gerçek

Cihan'ın kurum bilgisayarında kurum politikası nedeniyle eski bir Chrome sürümü kullanılmak zorunda.

Chrome DevTools MCP'nin resmi güncel gereksinimi:

- Node.js LTS,
- **Chrome current stable veya daha yeni**,
- resmi destek yalnız Google Chrome ve Chrome for Testing için.

Ayrıca `--autoConnect` özelliğinin güncel troubleshooting dokümanında **Chrome 144+** gerektirdiği belirtiliyor.

### 9.2. Sonuç

Bu nedenle önceki kararımı değiştiriyorum:

> **Kurum bilgisayarında Chrome DevTools MCP artık ilk pilot olmamalı.**

Eski Chrome ile bazı CDP işlemleri tesadüfen çalışabilir; ancak bu resmi destek sınırının dışındadır ve protokol/feature uyumsuzluğu nedeniyle güvenilir bir HCC bileşeni sayılmamalıdır.

Özellikle `--autoConnect` Chrome 144'ten eski sürümde kullanılmamalıdır.

### 9.3. Alternatifler

Aşağıdaki seçenekler kurum politikası ve güvenlik onayı çerçevesinde değerlendirilebilir:

**A. Ayrı güncel Chrome for Testing / güncel Chrome**

Yalnız public GİB/mevzuat araştırması için, kurum politikası izin veriyorsa. Kurumun zorunlu eski Chrome profilinden tamamen ayrı olmalıdır.

**B. Kişisel/ayrı güvenli makine veya izole ortam**

Public GİB özelgeleri üzerinde browser adapter burada çalışır; sonuç Kanıt Defteri'ne provenance ile girer. Kurum/VDK oturumları taşınmaz.

**C. Mevcut MCP/API hattını güçlendirmek**

`turk-hukuku-mevzuat-mcp`, özelge MCP ve resmi endpoint'ler öncelikli kalır. Browser yalnız boşluğu dolduran adapter olur.

**D. GrokBot cloud browser veya başka cloud browser**

Sadece public kaynak için düşünülebilir. Kurumsal login, VDK, mükellef verisi veya authenticated kurum oturumu kesinlikle verilmez. Bu seçenek resmi kaynak origin'ini koruyabilir ama güvenlik/kanıt zinciri ayrıca değerlendirilmelidir.

### 9.4. Pilot koşulu revize

Chrome DevTools pilotu ancak şu şartlardan biri sağlanırsa aktifleşsin:

1. kurum dışında güncel desteklenen Chrome/Chrome for Testing mevcut,
2. kurum BT politikası ayrı desteklenen tarayıcıya açıkça izin veriyor,
3. sadece public veri kullanılan izole test makinesi/VM var.

Aksi hâlde pilot statüsü:

`BLOCKED_BY_ENVIRONMENT`

olmalı; FAIL sayılmamalıdır.

## 10. Faz sıralaması — revize

Önceki önerimi netleştiriyorum:

1. **Faz 0 — hijyen / gerçek durum tespiti**
2. **Faz 1 — N1 tek state ledger**
3. **Faz 2 — N3 Kanıt Defteri temeli**
4. **Faz 3 — Kanıt Defteri adapter'ları**
   - mevcut resmi MCP/API kaynakları önce,
   - Chrome DevTools yalnız desteklenen ayrı ortam varsa,
   - aksi hâlde browser adapter ertelenir.
5. **Faz 4 — N2 küçük topoloji pilotu**
6. **Faz 5 — bayatlama motoru + dar izin/routing otomasyonu**
7. **Happy** ancak hâlâ gerçek bir insan-müdahale darboğazı ölçülüyorsa.

Bu sıralamada epistemik kalite ve kanıt tekrar kullanımı dosya topolojisi optimizasyonundan önce gelir.

## 11. GrokBot Radar'ın yeri

GrokBot çekirdek Study Pack üretim hattının bir parçası olmamalıdır.

Önerilen yerleşim:

```text
X + GitHub + Web
       ↓
GROKBOT RADAR
       ↓
Mevcut HCC kabiliyet matrisiyle delta karşılaştırması
       ↓
YENI + UYGUN / PILOT ADAYI
       ↓
PILOT-KAYDI
```

Radar ayrıca **CAPABILITY DRIFT** kontrolü yapmalıdır: mevcut ChatGPT/Claude/Codex/Grok bağlantılarının eskiden yapamadığı ama artık yapabildiği yetenekleri tespit etmelidir. Yeni ürün almak yerine mevcut sistem kabiliyetiyle çözülmüş ihtiyaçlar böylece görülür.

## 12. Claude Code direktifine revizyon önerileri

Claude'un mevcut direktifinde şu değişiklikleri öneriyorum:

1. T3 state'lerinde `MEVZUAT_PASS` ikiye ayrılmalı:
   - `MEVZUAT_KANIT_PASS`
   - `HUKUKI_MUHAKEME_PASS`
2. T5 Kanıt Defteri şemasında:
   - `kaynak_statu`,
   - `origin`,
   - `erisim_araci`,
   - `dogrulama`
   ayrı alanlar olmalı.
3. Chrome DevTools MCP pilotu koşulsuz Faz 2 aracı olmaktan çıkarılmalı; `BLOCKED_BY_ENVIRONMENT` gate'i eklenmeli.
4. `chrome-devtools-mcp` ile gelen resmi-origin içerik otomatik `ADAY` yapılmamalı; erişim aracı ile kaynak otoritesi ayrılmalı.
5. N2 uygulaması design-only kalmalı ve önce 3–5 dosyalık topoloji testi istenmeli.
6. Pilot registry lifecycle'ına `DONDURULDU`, `EXPIRED`, `BLOCKED_BY_ENVIRONMENT` eklenmeli.
7. Public GitHub'a aynalanan direktif/raporlarda local kullanıcı yolu, private Drive ID ve benzeri gereksiz tanımlayıcılar sanitise edilmelidir.

## 13. Önerilen hedef mimari

```text
                         CİHAN
                 KABUL / RED / KARAR
                           ▲
                           │
                    HCC STATE LEDGER
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
      ÜRETİCİLER        REVIEWER        KANIT DEFTERİ
   ChatGPT / Codex      Claude Code           │
                                             │
                              ┌──────────────┼──────────────┐
                              │              │              │
                         Mevzuat MCP     Resmi API      Browser Adapter
                                                       (ortam uygunsa)
```

GrokBot Radar bu çekirdeğin dışında dış teknoloji/sinyal katmanı olarak kalmalıdır.

## Sonuç

Claude'un normalizasyon yaklaşımı güçlüdür ve uygulanmaya değerdir. v2 itibarıyla ana kararlarım:

1. **N1 hemen.**
2. **N3 hemen ardından.**
3. Chrome DevTools MCP kurum bilgisayarındaki eski Chrome nedeniyle **öncelikli pilot değil; environment-gated adapter**.
4. N2 ancak küçük topoloji pilotundan sonra.
5. Kanıt PASS ile hukuki muhakeme PASS ayrılmalı.
6. Origin / erişim aracı / doğrulama statüsü ayrı tutulmalı.
7. GrokBot çekirdek ajan değil, delta-radar ve capability-drift gözcüsü olmalı.
8. Tek aktif pilot ilkesi korunmalı; başarısızlık ile ertelenme/ortam engeli birbirinden ayrılmalı.
