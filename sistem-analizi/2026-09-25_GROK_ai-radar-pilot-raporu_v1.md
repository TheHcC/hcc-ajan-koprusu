---
baslik: GrokBot AI Radar — Pilot Raporu
yazar: Grok (GrokBot)
tur: sistem-analizi / darbogaz + arac radari
tarih: 2026-09-25
versiyon: v1
durum: GIRDI (degerlendirildi — bkz. Claude analizi v1)
kaynak: Cihan tarafindan Claude.ai sohbetine yapistirildi; metin degistirilmeden aktarildi
iliskili:
  - "[[2026-09-25_CLAUDE-Opus-5.5_darbogaz-normalizasyon-analizi_v1]]"
  - "[[2026-09-25_DIREKTIF_CLAUDE-Opus-5.5-to-CLAUDE-CODE_N1-N3-uygulama_v1]]"
bilinen_duzeltme: "Jev bu raporda 'Kaku auto-tag, ertelendi' olarak siniflanmis; gercekte HCC Adaptive Router'in (Claude Code + Codex model/effort yonlendiricisi) temelidir."
etiketler: [hcc-sistem-analizi, grok, radar, darbogaz]
---

# GROKBOT AI RADAR — PILOT RAPORU

Mod: READ-ONLY. Hiçbir şey kurulmadı, repo/Drive değiştirilmedi.

Kanıt tabanı: public [TheHcC/hcc-ajan-koprusu](https://github.com/TheHcC/hcc-ajan-koprusu) (son commit 18.09.2026); Drive **HCC Ajan Köprüsü — Gelen Kutusu** (18–25.09, bugün VR01–VR10 toplu denetim direktifi); Drive `GitHub/` altındaki önceki araç değerlendirmeleri; `ymm-korpus` Drive aynası (10.09 kopyası). `TheHcC/ymm-korpus` private — GitHub bağlayıcısı bu oturumda bağlanmadı. Yerel `claude-practice` / `inceleme-os` diskine erişilemedi.

---

## 1. Sistemi Nasıl Anladım?

1. Bu bir “çok model, tek Markdown gerçeği” sistemi. Yeni LLM aranmıyor; üretici ile bağımsız denetçi ayrılıyor, Cihan onay kapısı.
2. **Bilgi otoritesi (çelişkide):** (1) yerel `inceleme-os\<slug>\durum.md` — inceleme operasyonu; (2) `claude-practice\.gorev-durumu\aktif-gorev.json` — adım checkpoint; (3) **git `ymm-korpus`** — Study Pack kanonik Markdown; (4) public köprü `DURUM.md` / `GUNLUK.md` / `KARARLAR.md` — anlatı, **otorite değil**. Drive gelen kutusu öneri kanalı, emir değil.
3. **Otorite çatışması (kanıtlı):** Public köprü DURUM son güncelleme **10.09.2026**. Drive’da 18–25.09 VR/SP hattı canlı. Köprü DURUM’u “şu an” diye okuyan model **bayat** kalır. Drive `GitHub/ymm-korpus` kopyası da 10.09; kanonik git değil.
4. 18.09’da gelen kutu GitHub’dan Drive’a taşındı: Claude.ai / ChatGPT GitHub’a yazamıyor, Drive’a yazabiliyor. CLI ajanlar (Claude Code, Codex, OpenCode) hâlâ git’e commit ediyor.
5. İş iki paralel kol: **Denetim** (Hat E/M, SP-DENETIM-E-001…; kuyruk `_kuyruk_denetim.json`, son 19.09) ve **Vergi-Revizyon** (VR01–VR10, 25.09’da toplu Claude eşiği doldu).
6. Üretim hattı: Claude Code aday seçer + kendi-yeten direktif yazar → Cihan ChatGPT/Codex’e verir → çıktı Drive `01_CIKTI_DENETIM_BEKLIYOR` ve/veya git TASLAK → **Claude Code bağımsız denetim** (ADR-9 canlı mevzuat) → Cihan `KABUL_EDILDI`. Üretici = denetçi yasak.
7. 24–25.09 kuralı: her paketten sonra Claude değil; **~10 pakette bir toplu tur**. VR01–VR10 ilk dilim. Codex VR10’da mekanik PASS verdi, mevzuat PASS vermedi (MCP’si yok).
8. Üç hedef eşitlemesi zorunlu: GitHub `.md` + Drive Google Doc + Obsidian `40-YMM-Sinav/...md`. Codex bunu VR10’da karakter-karakter yaptı. Otomatik değil.
9. Kota kademesi (14.09 AGENTS.md, güvenlik notunda): Claude Code → Codex → **agy/OpenCode**. Hermes = VPS’e bırakılmış, **düşünülüyor**. OpenRouter, OpenCode üzerinden ucuz worker.
10. Mevzuat: `turk-hukuku-mevzuat-mcp` (aydincan) **aktif**; `yargi-mcp` (surucu.dev) **ölü** (Bedesten API hâlâ canlı, paket bypass ile bir Danıştay kararı çekildi); `gib-ozelge-mcp` / `tr-eli-mcp` var, sık `CONNECT_TIMEOUT`; claude.ai Mevzuat MCP **CONNECT_TIMEOUT**; WebFetch GİB’de JS-render yüzünden kör. K-003: kazıma resmî mevzuatın yerine geçmez.
11. Eski `ymm-korpus` hastalığı teşhis edilmiş: kota-güdümlü hacim, biçim denetimi, kullanılabilirlik yok. Yeni birim K-005 atom (düzenlenebilir MD/XMind) + K-006 geçiş kontrolü + K-008 üç katman zorunlu (poster/bülten/node). Study Pack bu üçlünün sınav yüzeyi.
12. Obsidian: 8 vault, yeni vault yasak (K-002). Bilgi ağacı `ymm-korpus/09_bilgi/`. `TEKNO AI HcC` inceleme için ayrı. 08.09’da Obsidian MCP’nin izinli dizini **yanlış yere** bakıyordu — “MCP var” ≠ “kasa vault’una erişiyor”. Bugünkü durum **UNKNOWN**.
13. Köprü 7 halüsinasyon kuralı + `Bilinen sınırlar` boş bırakılamaz. Cihan onaylamadan gelen kutu uygulanmaz.
14. Windows. Hassas mükellef/VDK verisi köprüye ve public git’e **giremez**. `hcc-harness` Drive’da şifreli yedek olarak duruyor; içi bu taramada **UNKNOWN** (parola dosyasına dokunulmadı).
15. Grok bu oturumda Drive’ı okuyabildi. Grok’un fiilî rolü şimdiye kadar kayıtlarda yoktu; bu radar **PILOT**.

| Ajan | Gerçek rolü | Güçlü olduğu iş | Çakışma | Durum |
|---|---|---|---|---|
| ChatGPT (gpt-5.6-sol) | Üretici + mimari öneri | Study Pack, Bülten/Atom önerisi | Claude denetçi | **aktif** |
| Claude Code (opus/sonnet 5) | Ana icracı + bağımsız denetçi | ADR-9, git, alt-agent denetimi | ChatGPT üretim | **aktif** |
| Codex | Üretici (devralıyor) + mekanik ilk kontrol + Drive klasör aynası | üç hedef parite, commit | Claude review | **aktif** |
| OpenCode / Astra | Kota 3. kademe | ucuz bulk, Obsidian tarama (08.09 raporu denetlendi) | CC/Codex | **aktif** (kademe) |
| Antigravity (agy) | Kota kademesi | Gemini CLI | OpenCode | **aktif** (kademe) |
| Claude.ai sohbet | Köprü okuma, itiraz (K-005) | muhakeme | Claude Code | **aktif** |
| Hermes | VPS persistent adayı | — | OpenCode | **düşünülüyor** |
| Grok | X/web/Drive radar | dış tarama | ChatGPT araştırma | **pilot** (bu iş) |
| Kaku | AI diff / linked-context editör | ajan yazısı ↔ canonical MD arası review | Obsidian | **pilot önerildi** (23.09); kurulum PASS’i yok |
| Jev | Kaku auto-tag | — | — | **ertelendi** (Kaku Faz 6) |
| Herdr | CLI ajan runtime / pane orkestrasyonu | `agent.wait`, session restore | — | **pilot önerildi** (18.09); kurulum PASS’i yok |
| GitHub Copilot Chat | — | — | CC/Codex | **evaluated** (13.09) |
| Serai | kapalı control plane | shared memory iddiası | köprü | **evaluated / izle** (3,5/10) |
| suede-codex-fleet | Claude judges, Codex generates | paralel worker | mevcut hat zaten bu kalıp | **evaluated**; paket kurulmadı, desen alındı |
| vlln/subagents-skill, climux | otomatik multi-CLI | — | sandbox/onay bypass | **reddedildi** (14.09) |

---

## 2. Tespit Ettiğim Ana Darboğazlar

**1. Drive gelen kutusu olay değil, kuyruk.**
- MEVCUT: Cihan direktifi yapıştırır / Drive’a koyar; Claude Code “periyodik kontrol” eder (OKUBEN).
- MANUEL: VR/DIS_MODEL_GOREVI düşince ajanı haberdar etmek.
- ARAÇ: Drive + insan.
- SORUN: 25.09’da `00_AKTIF_DIREKTIF` ve `01_CIKTI_DENETIM_BEKLIYOR` dolu; `02_ISLENDI_ARSIV` boş; kökte hâlâ 25+ eski dosya.
- YENİ ARAÇ: watcher ancak **onayı/sandbox’ı kapatmadan** bildirim üretirse değerli. Grok+Drive ile zamanlı tarama mevcut stack’te mümkün — bu yüzden ayrı bir “Drive watcher ürünü” önermiyorum.

**2. Cihan hâlâ router.**
- MEVCUT: direktif yaz → ChatGPT/Codex → Drive/git → Claude toplu denetim.
- MANUEL: kopyala-yapıştır, “şimdi Claude’a ver”, üç hedefi eşitle.
- ARAÇ: köprü protokolü + BAŞUCU REHBERİ.
- SORUN: protokol olgun, runtime yok. Herdr tam bu boşluk için değerlendirildi; kurulumu teyitsiz.
- YENİ ARAÇ: sandbox bypass eden orkestrasyon **reddedilmiş kural**. Aynı sınıfı tekrar önermiyorum.

**3. ADR-9 tek ajana kilitli ve MCP kırılgan.**
- MEVCUT: canlı mevzuat yalnız MCP’li Claude Code.
- MANUEL: timeout olunca iş durur; Codex “mevzuat PASS yok” demek zorunda.
- ARAÇ: turk-hukuku-mevzuat-mcp, gib-ozelge-mcp, tr-eli-mcp.
- SORUN: VR10’un kabulü TCMB ham satırı + özelge MCP’sine bağlı. Kota bitince denetim de biter.
- YENİ ARAÇ: yeni coding agent bunu çözmez. Yeni LLM de değil.

**4. GİB JS-render — A-009 hâlâ açık.**
- MEVCUT: WebFetch boş; GECIS-HARITASI “Mevzuat MCP veya browserclaw”.
- MANUEL: özelge numarası doğrulanamıyor, `[TEYİT]`.
- ARAÇ: WebFetch (yetersiz).
- SORUN: araştırma kapısı (K-008) fiilen özelgede kör.
- YENİ ARAÇ: **canlı, JS’li tarayıcı** (aşağıda).

**5. Üç hedef senkronu elle.**
- MEVCUT: Codex/Claude karakter karşılaştırması.
- MANUEL: git / Drive Doc / Obsidian md.
- SORUN: VR08 üç parça dosya; “hangisi kanonik” BAŞUCU’da ayrıca kural.
- YENİ ARAÇ: Obsidian Drive Sync eklentisi Git otoritesiyle **çatışır** — önermiyorum.

**6. Public köprü anlatısı 15 gündür duruyor.**
- MEVCUT: DURUM/GUNLUK GitHub’da, iş Drive+private git’te.
- SORUN: ChatGPT/Claude.ai köprüyü okuyunca 10.09 dünyasında kalır.
- YENİ ARAÇ: ürün değil, hijyen. Yeni araçla çözülmez.

**7. İzin bekleyen ajan masada donuyor.**
- MEVCUT: terminalde `y`. 14.09 kararı: onay/sandbox kapatan multi-CLI **yasak**.
- MANUEL: Cihan klavyede olmalı.
- SORUN: Human-in-the-loop korunuyor, Human-on-the-loop yok.
- YENİ ARAÇ: izinleri **kapatmayan** mobil onay (aşağıda).

**8. Bayatlama motoru (adım 13) yok.**
- MEVCUT: `son_dogrulama` künye alanı + ADR-9 elle.
- SORUN: atom/SP kabul edildikten sonra mevzuat değişince kim uyarır?
- YENİ ARAÇ: hazır “Türk mevzuat bayatlama” ürünü yok. Uydurma ürün önermiyorum.

**9. Session/memory dağınık, ama dosya tabanı güçlü.**
- MEVCUT: DURUM, GUNLUK, KARARLAR, `_kuyruk.json`, Study Pack frontmatter.
- SORUN: Serai bu boşluğu vaat etti, kapalı/Web3 profili yüzünden elendi. Claude-Mem / codebase-memory, Herdr analizinde “ayrı katman, Herdr’ın işi değil” denmiş; kurulum kaydı Drive’da yok (**UNKNOWN**).
- YENİ ARAÇ: Beads/Gas Town `_kuyruk.json`’u değiştirir, maliyet yüksek — göstermiyorum.

**10. Hassas veri sınırı ile ajan özerkliği gerilimi.**
- MEVCUT: köprü arındırılmış; VDK/mükellef ayrı ağaç.
- SORUN: tarayıcı/mobil/runtime bağlandığında oturum sızıntısı (GİB login, inceleme Chrome profili) yeni risk yüzeyi.
- YENİ ARAÇ: her adayda bu sınır test edildi; aşanlar elendi.

---

## 3. Yeni Araçlar

Bu taramada **kategori 1 (yeni + doğrudan uygun) aday yok.** Windows deneysellik, tarayıcı-oturum sızıntısı ve “kurulum teyidi olmadan production” riski yüzünden ikisi de pilot.

### Happy (slopus/happy)

Kategori: **sisteme uygun / pilot adayı**

Ne bu?
Claude Code ve Codex’in (ayrıca `happy agy`, OpenCode ACP) üzerine binen açık kaynak mobil/web istemci. Bilgisayardaki aynı oturumu telefonda görüp, izin/hata olunca bildirim alıp, sandbox’ı kapatmadan onay vermeyi hedefliyor. MIT, ~23,9k yıldız, CLI v1.2.5 (22.09.2026), E2E şifreleme, self-host iddiası.

Cihan’ın sistemindeki karşılığı
Kota kademesi CC → Codex → agy/OpenCode. Ajan izin isteyince iş duruyor. 14.09’da tam da bu yüzden `dangerously-bypass` orkestrasyon reddedildi. Happy o reddi delmeden “masadan kalkınca iş ölmesin” katmanı.

Şu anda ne kullanılıyor?
Claude Code + Codex + terminalde insan onayı. Herdr (runtime) ve Kaku (diff review) önerilmiş, kurulumu teyitsiz. Mobil katman yok.

Bu araç ne ekliyor?
İzin/hata anında telefona bildirim ve aynı oturuma dönüş — onay kapısını kapatmadan Human-on-the-loop.

Neden mevcut araçlardan farklı?
Herdr pane/SSH runtime; Kaku Markdown review; ntfy-approve yalnız Claude PermissionRequest ve zayıf bakım. Happy, Cihan’ın **üç gerçek CLI’sini** (claude / codex / agy) sarmalıyor. Yeni coding agent değil.

Örnek kullanım

```text
Cihan VR01–VR10 toplu denetimi başlatır (Claude Code)
        ↓
MCP timeout / dosya yazma izni
        ↓
Happy bildirimi telefona
        ↓
Cihan: Allow / Deny  (sandbox hâlâ açık)
        ↓
ADR-9 devam; KABUL_EDILDI yine yalnız Cihan
```

Entegrasyon maliyeti: **Orta** (wrapper: `happy claude` / `happy codex`; Windows “experimental”, bazı özellikler WSL2).

Risk / eksiler
- Windows resmen deneysel.
- Relay sunucusu (self-host mümkün; varsayılan onların backend’i). Mükellef ağacında **çalıştırılmamalı**.
- `happy-desktop` ayrı, zayıf (84 yıldız) ve Herdr ile örtüşür — **onu kurma**.
- Wrapper, session restore bug’ları (1.2.5’te tam da bunu yamıyorlar).

Önerilen deney (30–45 dk, geri alınır)
1. Yalnız `ymm-korpus` (mükellef yok) içinde `npm i -g happy` → `happy claude`.
2. Android/iOS veya web’den QR.
3. Kasıtlı bir izin isteği (tek dosya Write) → telefonda onay/red.
4. `happy` kapat, normal `claude` ile aynı iş. Checkpoint: git temiz.
PASS: bildirim + onay çalışıyor, sandbox flag yok, git diff yalnızca o dosya.

Kaynaklar
- [happy.engineering](https://happy.engineering/)
- [github.com/slopus/happy](https://github.com/slopus/happy)
- [X: CLI sarmalayıcı özeti, 25.09](https://x.com/rosehexon/status/2103486469646262605)

---

### Chrome DevTools MCP (ChromeDevTools/chrome-devtools-mcp)

Kategori: **sisteme uygun / pilot adayı**

Ne bu?
Google Chrome ekibinin resmi MCP’si: ajan canlı Chrome’u sürer, JS-render sayfayı görür, ağ yanıtını okur. Apache-2.0, v1.10.1 (23.09.2026), Windows için `cmd /c npx` belgelenmiş. `autoConnect` ile **zaten açık Chrome oturumuna** bağlanabilir.

Cihan’ın sistemindeki karşılığı
A-009: beş özelge WebFetch ile doğrulanamadı (GİB JS-render). K-008 araştırma kapısı “fiilen çalıştırılır” diyor; özelgede kapı kapalı. Codex ADR-9 yapamıyor; Claude da GİB HTML’ini göremiyor.

Şu anda ne kullanılıyor?
WebFetch + mevzuat/özelge MCP. GECIS-HARITASI zaten “browserclaw” demiş — **ürün olarak değerlendirilmemiş, kurulmamış**. Chrome DevTools MCP, o boşluğu resmi/bakımlı yoldan doldurur; BrowserClaw’ı yeni keşif diye sunmuyorum.

Bu araç ne ekliyor?
GİB/özelge sayfasının JS sonrası metnini, insan GİB’e girmişken, `[TEYİT]` kapatmak için okumak.

Neden mevcut araçlardan farklı?
MCP’ler API/statik HTML. Playwright MCP benzer ama “logged-in Chrome’a bağlan” işi DevTools MCP’nin işi. Yeni tarayıcı-ajan (BrowserClaw/browser-use) ikinci beyin kurmaz; mevcut Claude Code’a göz ekler.

Örnek kullanım

```text
VR10 / A-009: İstanbul VDB 30.01.2018 özelgesi
        ↓
Cihan ayrı bir Chrome profilinde yalnız GİB (inceleme profili DEĞİL)
        ↓
Claude Code + chrome-devtools-mcp autoConnect
        ↓
sayfa metni + ağ yanıtı kayda geçer
        ↓
doğrulandıysa atom/SP; değilse [TEYİT] kalır
        ↓
Cihan KABUL_EDILDI
```

Entegrasyon maliyeti: **Düşük** (`claude mcp add chrome-devtools ...`; Windows’ta `cmd /c`).

Risk / eksiler
- Ajan, bağlı Chrome’da **ne açıksa** onu görür. İnceleme/VDK/banka profili **yasak**. Ayrı Windows kullanıcısı veya ayrı Chrome profili şart.
- GİB bot koruması MCP’yi de kesebilir — o zaman hâlâ `[TEYİT]`, uydurma yok.
- Web kazıma K-003’ü delmemeli: bu araç aday metin üretir; `RESMI` yine MCP/resmî metin.

Önerilen deney (30 dk)
1. Temiz Chrome profili, bir **public** JS-render sayfa (GİB özelge değil, önce duman testi).
2. Claude Code’dan “bu sayfadaki başlık ve ilk paragraf nedir?” — WebFetch vs DevTools MCP.
3. PASS ise A-009’daki **tek** özelge. İnceleme vault’u kapalı.
4. İş bitince MCP’yi kapat / profili kapat.

Kaynaklar
- [github.com/ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- [Chrome for Developers: DevTools for agents](https://developer.chrome.com/docs/devtools/agents/get-started)
- [X tartışması: Claude extension vs in-app vs DevTools MCP, 15.09](https://x.com/hot_town/status/2099820292445020277)

---

## 4. Bunları bilerek göstermedim

| | Sayı |
|---|---|
| Taranan aday | 42 |
| Yeni + doğrudan uygun | 0 |
| Pilot adayı | 2 |
| İncelendi fakat elendi (kategori 3) | 16 |
| Mükerrer / gereksiz / zaten kayıtlı (kategori 4) | 24 |

Önemli elenenler:

- **Kaku / Jev / Herdr** → 18–23.09 Drive’da zaten pilot önerisi; yeni keşif değil. Kurulum PASS’i yok.
- **vlln/subagents-skill, climux** → 14.09 **red**: `--dangerously-bypass-approvals-and-sandbox` / `--full-auto`. Aynı sınıftaki Gas Town / happy-desktop / suede’nin hazır kurulum paketi de bu yüzden yok.
- **Serai** → 14.09, 3,5/10; public repo yok, Web3 profili, lock-in.
- **suede-codex-fleet** → kalıp zaten VR hattında (ChatGPT/Codex üretir, Claude yargılar). Paketi kurmak mükerrer.
- **Beads / Gas Town** → `_kuyruk.json` + DURUM/GUNLUK ile aynı iş; Gastown tmux/opinionated, Windows/Cihan köprüsünü değiştirir.
- **Claude-Mem, codebase-memory-mcp, Mem0, projectmem** → dosya tabanlı bellek zaten kanonik; Herdr notu bunları ayrı katman saymış. Drive’da kurulum yok = UNKNOWN, “yeni memory ürünü” diye satılmadı.
- **Playwright MCP, BrowserClaw, browser-use, Stagehand** → A-009 için rakip; BrowserClaw dosyalarınızda zaten aday. Resmi bakımlı olanı (DevTools MCP) seçtim, diğerlerini göstermedim.
- **ntfy-approve / AgentNotifier** → mobil onayun ince hali; Codex tarafı macOS, bakım zayıf. Happy aynı boşluğu CC+Codex+agy ile kapsıyor.
- **Obsidian Google Drive Sync** → üç hedefte Git otoritesini bozar.
- **GitHub Copilot, Devin, Cursor background, “Codex killer” ajanlar** → mevcut CC/Codex ayrımına marjinal fayda yok.
- **Agent-Reach, Defuddle, youtube-full, Composio, Loopy, Humanizer, i-have-adhd, Serena** → Drive’da değerlendirme dosyası **bulunamadı** (UNKNOWN). X bookmark indeksinde de yok. Boşluğu doldurmak için önermedim.

Drive olay izleme için ayrı ürün yok: Grok+Drive veya mevcut Drive MCP poll’u yeterli; n8n/Make lock-in.

---

## 5. UNKNOWN (varsaymadım)

- `ymm-korpus` git HEAD (private; 10.09 Drive aynası bayat olabilir)
- Herdr / Kaku fiilen kurulu mu
- Obsidian MCP hâlâ yanlış vault’a mı bakıyor
- `claude-mem` / harness içi memory kurulu mu
- `hcc-harness` yedeğinin içeriği
- Yerel `claude-practice/AGENTS.md` §11–12’nin 14.09 sonrası hali

---

**Bu adaylardan hangisini derinleştireyim?**

Henüz hiçbirini kurmuyorum. İki net yol: **Happy** (mobil onay, Windows deneysel) veya **Chrome DevTools MCP** (A-009/GİB, ayrı Chrome profili şart). İkisi de mevcut Claude Code + Codex hattına ek; köprü protokolünü değiştirmiyor.
