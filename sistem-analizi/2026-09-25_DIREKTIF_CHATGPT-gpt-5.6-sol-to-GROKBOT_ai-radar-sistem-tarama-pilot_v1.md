---
baslik: DIREKTIF — GrokBot AI Radar Sistem Tarama Pilotu
yazar: ChatGPT (GPT-5.6 Sol)
kimden: ChatGPT (GPT-5.6 Sol)
kime: GrokBot
tur: direktif / sistem-tarama / ai-radar
tarih: 2026-09-25
versiyon: v1
durum: UYGULANDI
cikti: "[[2026-09-25_GROK_ai-radar-pilot-raporu_v1]]"
etiketler: [hcc-sistem-analizi, direktif, grokbot, ai-radar, read-only]
---

# GROKBOT AI RADAR — SİSTEM TARAMA VE KİŞİSEL TEKNOLOJİ FİLTRESİ

**Mod:** PILOT / READ-ONLY  
**Kullanıcı:** Cihan  
**Amaç:** Kullanıcının mevcut AI çalışma sistemini gerçek kaynaklardan anlayıp, X + GitHub + Web üzerinden keşfedilen yeni AI araçlarını bu sisteme sağlayabilecekleri **marjinal faydaya** göre filtrelemek.

## 0. ANA PRENSİP

Sen genel bir “AI haber botu” değilsin.

Görevin:

> İnternette ilginç görünen araçları listelemek değil; Cihan'ın mevcut sisteminde gerçekten yeni bir kabiliyet oluşturabilecek araçları bulmaktır.

Bir araç popüler olduğu, X'te viral olduğu veya güçlü göründüğü için önerilmemelidir.

Temel soru:

> “Cihan bunu mevcut ChatGPT + Claude Code + Codex + OpenCode/Hermes + GitHub/Drive/Obsidian sistemine eklediğinde, bugün yapamadığı veya gereksiz emekle yaptığı hangi işi daha iyi yapabilecek?”

Bu soruya somut cevap yoksa aracı kullanıcıya gösterme.

## 1. BU PİLOTTA YETKİ SINIRI

Bu çalışma **READ-ONLY** olacaktır.

Şunları YAPMA:

- repository değiştirme
- commit oluşturma
- push yapma
- branch açma
- Google Drive dosyalarını değiştirme
- dosya silme/taşıma
- program/skill/plugin/MCP kurma
- hesap açma
- ücretli servis başlatma
- API key isteme veya kaydetme
- mevcut workflow'u değiştirme

Sadece:

1. oku,
2. haritala,
3. araştır,
4. karşılaştır,
5. öner.

Herhangi bir uygulama/pilot önerisi ayrıca kullanıcı onayına sunulacaktır.

## 2. BİLİNEN BAŞLANGIÇ NOKTALARI

Aşağıdaki bilgiler **kanıt değil, keşif ipucudur**.

Gerçek mevcut durumu dosyalardan teyit et.

### GitHub

Öncelikle şunları ara:

- `TheHcC/hcc-ajan-koprusu`
- `TheHcC/ymm-korpus`

Bulabiliyorsan ayrıca kullanıcının diğer ilgili repo ve çalışma alanlarını tespit et.

### Google Drive

Özellikle şu yapı/adları ara:

- `HCC Ajan Köprüsü — Gelen Kutusu`
- `GitHub/ymm-korpus`
- `HcC Kasa Obsidian`
- YMM çalışma alanları
- GitHub / AI araç analiz notları
- Grok / Jev / Kaku / Herdr / agent sistemleriyle ilgili önceki değerlendirmeler

### Dosya ve yapı sinyalleri

Bulunduğunda özellikle oku:

- `CLAUDE.md`
- `Claude.md`
- `AGENTS.md`
- `BASLA.md`
- `DURUM.md`
- `GUNLUK.md`
- `KARARLAR.md`
- `GECIS-HARITASI.md`
- `STATUS.md`
- `MEMORY.md`
- `_kuyruk.json`

ve benzeri:

- direktif dosyaları
- agent handoff dosyaları
- değerlendirme notları
- study-pack yapıları
- `12_study_pack`
- `gelen-kutusu`
- `gelen-kutusu/claude-code`
- `inceleme-icin`
- session passport / handoff / checkpoint kayıtları

Dosya isimlerinden sistem hakkında sonuç çıkarma.

İçeriği oku ve mümkünse birden fazla kaynaktan doğrula.

## 3. AŞAMA A — MEVCUT SİSTEMİ HARİTALA

Araştırmaya başlamadan önce kullanıcının mevcut sistemini çıkar.

### A. Bilgi katmanı

Hangileri kullanılıyor?

- Google Drive
- Obsidian
- GitHub
- Markdown
- Google Docs
- başka yapılar

Hangisi hangi tür bilginin otoriter/kanonik kaynağı?

Otorite çatışması varsa ayrıca belirt.

### B. Ajanlar ve modeller

Gerçek kullanımda hangi ajanlar bulunuyor?

Örneğin:

- ChatGPT
- Claude / Claude Code
- Codex
- OpenCode
- Hermes
- Grok
- Jev
- diğerleri

Her biri için:

| Ajan | Gerçek rolü | Güçlü olduğu iş | Başka ajanla çakışıyor mu? |
|---|---|---|---|

Kullanıcının daha önce bir aracı sadece **incelemiş olması**, aktif kullandığı anlamına gelmez.

`aktif / pilot / düşünülüyor / reddedildi / bilinmiyor`

durumlarını ayır.

## 4. AŞAMA B — WORKFLOW HARİTASI

Gerçek iş akışını çıkar.

Örneğin sistem buna benziyor olabilir:

```text
Kaynak
  ↓
Araştırma
  ↓
Gelen kutusu / direktif
  ↓
Ana uygulayıcı ajan
  ↓
Bağımsız reviewer
  ↓
Test / doğrulama
  ↓
Kanonik repo
  ↓
DURUM / GUNLUK / KARARLAR
  ↓
İnsan onayı
```

Ancak bunu doğru kabul etme.

Gerçek dosyalardan mevcut akışı çıkar.

Özellikle şunları belirle:

1. İş kim tarafından başlatılıyor?
2. Hangi ajan ana uygulayıcı?
3. Hangi ajan bağımsız reviewer?
4. Claude Code ile Codex nasıl ayrılmış?
5. ChatGPT hangi aşamada kullanılıyor?
6. GitHub neyin kayıt sistemi?
7. Drive neyin kayıt sistemi?
8. Obsidian neyin kayıt sistemi?
9. Aynı bilgi birden fazla yerde tutuluyor mu?
10. Kullanıcının halen manuel yaptığı işler hangileri?

## 5. AŞAMA C — DARBOĞAZ ANALİZİ

Sistemi inceledikten sonra **5–10 gerçek darboğaz** çıkar.

Genel ifadeler kullanma.

Kötü örnek:

> “Araştırma daha iyi otomatikleştirilebilir.”

İyi örnek:

> “Drive gelen kutusuna yeni bir `VRxx` veya `DIS_MODEL_GOREVI_*.md` geldiğinde kullanıcı halen ajanı manuel olarak haberdar ediyor. Bu nedenle olay-temelli bir watcher/handoff katmanı potansiyel fayda yaratabilir.”

Her darboğaz için:

```text
DARBOĞAZ:
MEVCUT ÇÖZÜM:
MANUEL ADIM:
KULLANILAN ARAÇ:
SORUN:
YENİ BİR ARAÇ NEYİ DEĞİŞTİREBİLİR:
```

yaz.

## 6. AŞAMA D — MEVCUT KABİLİYET MATRİSİ

Yeni araç aramadan önce şu matrisi üret:

| Kabiliyet | Mevcut çözüm | Olgunluk | Açık var mı? |
|---|---|---:|---|
| Derin muhakeme | | | |
| Kodlama | | | |
| Code review | | | |
| Browser automation | | | |
| Web research | | | |
| X araştırması | | | |
| GitHub araştırması | | | |
| Agent memory | | | |
| Session continuity | | | |
| Agent handoff | | | |
| Multi-agent orchestration | | | |
| Background execution | | | |
| Event/watch automation | | | |
| Mobile approval | | | |
| Document ingestion | | | |
| Knowledge graph | | | |
| Obsidian integration | | | |
| Drive integration | | | |
| Source verification | | | |
| Testing/evaluation | | | |

Amaç:

**Yeni aracın hangi gerçek boşluğu doldurduğunu belirlemek.**

## 7. AŞAMA E — ÖNCE MÜKERRERLERİ ÖĞREN

Drive/GitHub/Obsidian içerisinde daha önce değerlendirilmiş araçları bul.

Örneğin aşağıdaki isimler mevcut kayıtlarda geçebilir:

- Agent-Reach
- Defuddle
- youtube-full
- Browser Harness
- Composio
- codebase-memory-mcp
- Claude-Mem
- Loopy
- Humanizer
- i-have-adhd
- Kaku
- Jev
- Herdr
- OpenRouter
- OpenCode
- Hermes
- Obsidian Skills
- Serena/Serai türü agent sistemleri

Listeyi genişlet.

Her biri için durum oluştur:

```text
KNOWN
ACTIVE
PILOT
EVALUATED
REJECTED
UNKNOWN
```

Daha önce incelenmiş bir aracı yeni keşifmiş gibi kullanıcıya sunma.

## 8. AŞAMA F — DIŞ DÜNYAYI TARA

Sistem haritası tamamlandıktan sonra araştırmaya başla.

### X

Öncelikli alanlar:

- Claude Code
- Codex
- coding agents
- agent orchestration
- multi-agent
- agent memory
- context engineering
- browser agents
- computer use
- MCP
- agent skills
- persistent agents
- background agents
- mobile agent control
- agent handoff
- GitHub automation
- Obsidian AI
- knowledge management
- evaluation/evals
- context compression
- session continuity

Özellikle son dönemde ciddi teknik tartışma veya açık kaynak proje üreten hesaplara öncelik ver.

Viral post ≠ kaliteli araç.

### GitHub

Aday repo için kontrol et:

- son commit
- release sıklığı
- issue durumu
- README
- documentation
- lisans
- contributor yapısı
- açık kaynak mı?
- Windows uyumluluğu
- Claude Code/Codex uyumluluğu
- MCP/CLI/API desteği
- mevcut sistemle entegrasyon maliyeti

Star sayısını sadece yardımcı sinyal olarak kullan.

### Web

Mümkün olduğunca:

1. resmi dokümantasyon
2. GitHub
3. geliştiricinin açıklaması
4. teknik kullanıcı deneyimi
5. X/Reddit topluluk sinyali

sırasıyla doğrula.

Sadece X paylaşımına dayanarak öneri üretme.

## 9. HER ADAY İÇİN MARJİNAL FAYDA TESTİ

### TEST 1 — Mevcut araç bunu zaten yapıyor mu?

EVET → büyük ihtimalle ele.

### TEST 2 — Yeni bir kabiliyet getiriyor mu?

Örneğin:

- bugün olmayan persistent execution
- daha iyi agent handoff
- gerçek event watcher
- anlamlı memory
- daha güçlü browser automation
- mobil approval
- cross-agent context
- otomatik eval
- daha iyi provenance

### TEST 3 — Mevcut sistemi değiştirme maliyeti nedir?

- Düşük
- Orta
- Yüksek

### TEST 4 — Lock-in yaratıyor mu?

Özellikle değerlendir:

- proprietary format
- cloud dependency
- veri dışarı aktarma
- API bağımlılığı
- kapalı memory
- vendor-specific workflow

### TEST 5 — Kullanıcının mevcut Markdown/Git/Drive sistemine uyuyor mu?

Tercihen mevcut kanonik yapıyı değiştirmeden eklenebilmelidir.

### TEST 6 — İnsan denetimini azaltıyor mu, yoksa ortadan mı kaldırıyor?

Amaç:

**Human-in-the-loop → Human-on-the-loop**

olabilir.

Ancak kritik kararları sessizce otomatikleştiren sistemleri düşük değerlendir.

## 10. SINIFLANDIRMA

Her adayı aşağıdaki dört kategoriden yalnızca birine koy.

### 🟢 1 — YENİ + DOĞRUDAN UYGUN

Şartlar:

- sistemde gerçek bir boşluk dolduruyor;
- mevcut araçlarla kolayca karşılanamıyor;
- entegrasyon maliyeti makul;
- kullanıcının gerçek workflow'una açıkça bağlanabiliyor.

**Kullanıcıya göster.**

### 🟢 2 — SİSTEME UYGUN / PİLOT ADAYI

Faydalı olabilir fakat küçük bir pilotla doğrulanmalıdır.

**Kullanıcıya göster.**

### 🟡 3 — İNCELENMELİ AMA ŞİMDİLİK DEĞMEZ

İlginç ama:

- mevcut araçlarla fazla örtüşüyor,
- erken aşamada,
- entegrasyon maliyeti yüksek,
- faydası henüz belirsiz.

Kayıtlara al fakat normal raporda kullanıcıya gösterme.

### ⚫ 4 — GEREKSİZ / MÜKERRER / HYPE

Mevcut sistemde yeni değer oluşturmuyor.

Kullanıcıya gösterme.

## 11. KRİTİK FİLTRE

Bir araç yalnızca şu nedenle önerilemez:

- yeni çıktı,
- viral,
- çok yıldız aldı,
- herkes X'te konuşuyor,
- “Claude killer” deniyor,
- “Codex killer” deniyor,
- yeni bir model kullanıyor.

Asıl kriter:

> **Cihan'ın mevcut sisteminde hangi işi ölçülebilir biçimde daha iyi hale getiriyor?**

Bunun cevabı yoksa ELE.

## 12. ÖZELLİKLE ARADIĞIM ŞEY

Yeni bir LLM aramıyorum.

Öncelik sırası:

1. mevcut ajanlar arasında orkestrasyon
2. event/watch mekanizmaları
3. persistent/background execution
4. context ve memory altyapısı
5. cross-agent handoff
6. araştırma ve provenance
7. browser/computer automation
8. eval/test altyapısı
9. Drive/GitHub/Obsidian entegrasyonu
10. mobil kontrol/onay

Yeni coding agent ancak Claude Code/Codex'e göre **belirgin ve benzersiz bir fayda** sağlıyorsa gösterilmelidir.

## 13. İLK ÇALIŞMANIN ÇIKTISI

İlk pilotta maksimum **5 öneri** getir.

Ancak kaliteli aday yoksa:

> “Bu taramada kullanıcıya göstermeye değer yeni araç bulunamadı.”

yaz.

Boşluğu doldurmak için zayıf öneri üretme.

## 14. ÇIKTI FORMATI

# GROKBOT AI RADAR — PILOT RAPORU

## 1. Sistemi Nasıl Anladım?

Maksimum 15 madde.

## 2. Tespit Ettiğim Ana Darboğazlar

Maksimum 10.

## 3. Yeni Araçlar

Sadece kategori **1 ve 2**.

Her araç için:

- kategori,
- ne olduğu,
- Cihan'ın sistemindeki karşılığı,
- bugün ne kullanıldığı,
- ne eklediği,
- neden mevcut araçlardan farklı olduğu,
- gerçek HCC örneği,
- entegrasyon maliyeti,
- risk/eksiler,
- küçük ve geri döndürülebilir pilot,
- resmi kaynaklar / GitHub / X doğrulaması.

## 15. BUNLARI BİLEREK GÖSTERMEDİM

Rapor sonunda yalnızca sayıları ver ve en fazla 5 önemli elenmiş örneği gerekçesiyle yaz.

## 16. SON BÖLÜM — TEK SORU

Raporu şu soruyla bitir:

> “Bu adaylardan hangisini derinleştireyim?”

Henüz hiçbirini kurma.

## 17. BAŞARI KRİTERİ

Pilot başarılı sayılacaktır eğer:

- mevcut sistemi doğru haritalarsan,
- aktif/pilot/yalnızca değerlendirilmiş araçları ayırırsan,
- mükerrer araçları yeniden önermezsen,
- en fazla birkaç yüksek değerli aday getirirsen,
- her adayın mevcut workflow'da nereye oturduğunu gösterirsen,
- popülerlik yerine marjinal faydayı ölçersen,
- bilmediğin şeyi varsaymak yerine `UNKNOWN` olarak işaretlersen.

**Şimdi önce sistem taramasını yap. Dış araştırmaya, sistem haritasını tamamladıktan sonra geç.**
