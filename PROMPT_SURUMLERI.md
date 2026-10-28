# Prompt sürüm defteri

Ajanlara verilen görev emirleri, sistem prompt'ları ve bunları denetleyen araçlar için tek satırlık sürüm kaydı.
Ayrıntılı fark her zaman `git log -p <dosya>` ile görülür; bu defter yalnızca **ne, neden, sonuç**.

**Durum etiketleri:** Taslak · Test · Stabil · Sorunlu · İptal

**Kural:** Bir prompt ya da görev emri değiştiğinde buraya bir satır eklenir. Sonuç sütunu, değişikliğin
denendiği ilk çıktıdan sonra doldurulur.

## YMM StudyPack temizliği (Codex görev emri + paket_denetle.py)

Dosyalar: `gorevler/2026-10-15-studypack-temizlik.md` · `araclar/ymm-studypack/paket_denetle.py`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-14 | İlk görev emri: tek işçi, kapılar G0–G3, tek format, 3 statü; denetim/okunurluk/özelge araçları (43dade6) | Çok taşeronlu patinaj, 9 statü, 3 format kuşağı | G0 temiz geçti (462 dosya, yedek ZIP, 413 özelge çifti) | Stabil |
| v1.0-c | 2026-10-14 | ChatGPT'ye uyarlanmış sürüm + yerel `temizlik_uygula.py` (3e4dfa3) | ChatGPT'ye verme seçeneği | Cihan Codex'te kalmaya karar verdi; geri alındı (3b0f497) | İptal |
| v1.1 | 2026-10-15 | EK-1: gövdede kalıp uyarı yok, ters tablo yasağı ve sütun sınırı kaldırıldı, mikro soru/tekrar kartı korunur, VAKA ham kaynaktan birebir (`--kaynak`), ezber = hukuk kuralı (95f2031) | G1'de içerik kaybı ve okunamaz tablolar; denetim geçmesine rağmen | G1b: VR-E-003 mikro soru 6→6, kart 12→12; VT-SP-01 tam komisyon cevabı | Stabil |
| v1.2 | 2026-10-15 | EK-2: soru kendi başına çözülebilir, eski bölüm numarasına atıf yok, mikro sorular doğrudan (7a0eda4) | G1b'de küçük kusurlar | Parti 01–02: 4 paket geçti, 4 BLOKE | Stabil |
| v1.3 | 2026-10-15 | EK-3: boyut sınırı birebir komisyon alıntısını saymaz (ÇALIŞMA 20 KB / VAKA 12 KB); tek soru = tek VAKA; BLOKE 4 pakete bir yeni deneme (50596ee) | 3 BLOKE'nin nedeni kuraldı: alıntı 20–60 KB | 4 eski BLOKE geçti; parti 03–04'te 4 yeni BLOKE (hepsi boyut/başlık kuralı) | Sorunlu |
| v1.4 | 2026-10-15 | EK-4: boyut yalnız uyarı, tavan ÇALIŞMA 30 KB / VAKA 40 KB; H1 başlık SORU/CEVAP sırasına sayılmaz; BLOKE adaylar yeniden yazılmadan yeniden denetlenir | Hazır işlenmiş vakalar (VT-SP-06/07/08) 12 KB'a sığmıyordu; başlık okuma hatası | Yeniden denetim: 4/4 BLOKE geçti (bir başlık hatası daha düzeltildi) | Stabil |

## HCC-Beyin (Hermes yakalama/düzenleme/bülten prompt'ları)

Dosyalar: Drive `HcC Kasa Obsidian/HCC-Beyin/_sistem/hermes-kurallari.md` (3 blok) · anayasa: `HCC-Beyin/00_Claude-Gorus-1_Yalin-Sistem.md`
Değişiklik kuralı: 4. bültene (2026-11-15) kadar yalnız hata düzeltmesi; yeni alan/bölüm/klasör eklenmez.

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v0.1 | 2026-10-18 | İlk sürüm, Cihan onaylı. Blok 1: Telegram yakalama kuralı (yalnız link/iletilen içerik ya da `b:` = kart; mükellef verisi reddedilir). Blok 2: günlük 07:30 inbox hijyeni + Hermes karşı görüşü + `derin_qc` bayrağı. Blok 3: Pazar 20:00 bülten (maks. 5 dk, boşsa alarm) + `onay N` / `red N` komutu. Ek: CLAUDE.md/AGENTS.md'ye tek satırlık kart yazma kuralı | ChatGPT'nin v0 tasarımı (7 faz kapısı, 6 durum, 5 hafıza türü) tek kişilik kullanım için fazla ağırdı; darboğaz kayıttı, QC değil | Bekleniyor — Hermes'e yüklenmedi; ilk bülten 2026-10-25 | Taslak |

## PCH — prompts.chat kişisel hasat (Hermes görev emri)

Dosyalar: Drive `HcC Kasa Obsidian/20-Araclar/prompts.chat/HERMES_GOREV_PCH_HASAT_2026-10-23_v1.2.md` (güncel) · sevk: `VPS-KUTUSU/GIRIS/` · çıktı: `VPS-KUTUSU/CIKTI/PROMPTS-CHAT/HERMES-PCH-HASAT-2026-10-23/`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-23 | İlk direktif (Claude): profil merceği, 8 küme, 5 ölçütlü puanlama, ≤15 Hazine, desen kütüphanesi; çıktıyı rclone ile doğrudan kasaya yazıyordu | — | Sevk edilmedi | İptal |
| v1.1 | 2026-10-23 | **VPS-KUTUSU uyumlu** (Claude): `HERMES_GOREV` biçimi; yazma yalnız `CIKTI/PROMPTS-CHAT/<görev>`; kasa notları `04_OBSIDIAN_IMPORT_BUNDLE` olarak önerilir, kasaya alımı Claude QC sonrası yapar; tek seferlik icra + kopya savunması + Drive geri-okuma; MCP ekleme yasak | Hermes Drive'da yalnız VPS-KUTUSU'yu kullanabiliyor; v1.0 bu kuralı çiğniyordu | Sevk edilmedi; v1.2 yerine geçti | İptal |
| v1.2 | 2026-10-23 | ChatGPT revizyonu: doğrulanmamış profil varsayımları çıkarıldı; 22.10 yönetici raporu kuralının `_YONETICI` dar yazma istisnası; tek 0–10 puanlama, gizli bonus yok; CSV eksikse HTML/MCP alternatifi; gerçek test / masa başı / statik inceleme ayrımı | v1.1'de profil varsayımları ve bonus/ceza karmaşası | BITTI 2026-10-24 02:44 TR: 534 aday, 15 not (2 Hazine, 10 Pilot, 3 Beklet); Claude QC: puan formülü 15/15 tutarlı; Cihan 2026-10-24 KABUL: 6 not kasada (`prompts.chat/hasat/2026-10-23/`: H-01, 02, 03, 05, 09, 10) | Stabil |

## PCH-K — prompts.chat kişisel alan tasnifi (Hermes görev emri)

Dosyalar: Drive `HcC Kasa Obsidian/20-Araclar/prompts.chat/HERMES_GOREV_PCH_KISISEL_TASNIF_2026-10-24_v1.0.md` · sevk: `VPS-KUTUSU/GIRIS/` · çıktı: `VPS-KUTUSU/CIKTI/PROMPTS-CHAT/HERMES-PCH-KISISEL-2026-10-24/`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-24 | İki eksenli taksonomi (alan EGT/SIT/OKU/DIS/KIS + işlev F01–F11, yüz: seviye, kullanıcı, çocuğa doğrudan, TR uyarlama); 534 eski adayın yeniden tasnifi + kişisel alan araması; kapılar: akademik dürüstlük, çocuk verisi, fetva yasağı, uydurma kaynak yasağı; kişisel rubrik U/H/A/G/B (0,35/0,20/0,15/0,20/0,10); alan başına ≤4 Hazine, toplam ≤18; 30 örneklik kör uyum kontrolü; Obsidian import bundle `kisisel-katalog/` | PCH v1.2'nin şeritleri mesleki; kişisel alanlar kapsam matrisinde yoktu | BITTI 2026-10-24 16:15 TR: 1.674 aday tarandı, yalnız 21'i tam okundu, 4 Hazine (EGT 2, SIT 1, OKU 1; DIS/KIS 0). Kör uyum %33 (hedef %80) → 1.653 satırlık katalog güvenilir tasnif değil, aday havuzu. Claude QC: puan 20/20 tutarlı, kapılar uygulanmış; K-EGT-02 = H-10 tekrarı ("NEW" diye işaretli), EGT.VAR tanımsız kod, 1 notta katkıcı e-postası. Kabul Cihan'da | Sorunlu |

## PCH-CGPT — ChatGPT prompts.chat çalışması (ChatGPT görev emri)

Dosyalar: Drive `HcC Kasa Obsidian/20-Araclar/prompts.chat/ChatGPT Calisma/` (ChatGPT'nin master planı ve kartları) · devam direktifi: `prompts.chat/CHATGPT_GOREV_PCH_CGPT_DEVAM_2026-10-24_v1.0.md`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-24 | ChatGPT'nin kendi master planı: 6 grup (MES, YMM, EGT, HUK, OKU, KIS), PCH-CGPT-1 puanlama (ağırlıkları PCH-K ile aynı), not standardı; ilk parti MES-001…003 | Cihan doğrudan ChatGPT'den istedi | 18 not; 3 kart H-03/H-01/H-05'in geliştirilmiş sürümleri; H-09'da kaynağa yanlış atfedilmiş adım tespit etti | Test |
| DEVAM v1.0 | 2026-10-24 | Claude: önce üç üreticinin işini kaynak kimliğine göre uzlaştıran kayıt; iş sırası boşluk öncelikli (YMM → HUK → EGT boşlukları → MES M4–M5 → OKU boşlukları; KIS ertelendi); aday havuzu olarak Hermes CSV'leri; temiz oturumda model denemesi; her karta hedef Claude Projesi; kullanım kapısı; Hermes'e yalnız HERMES_TALEP ile ulaşma | ChatGPT'nin planı kasaya alınan ve Hermes'in yeni bitirdiği işlerle çakışıyordu | 2026-10-24: uzlaştırma kaydı (33 kaynak), H-09 düzeltme önerisi, YMM-001…003. Claude QC: statik GEÇTİ, 2 küçük düzeltme. Model denemesi 0, kullanım 0 → kullanım kapısı devrede | Test |

## AJAN-TAHTASI — üç ajanlı iş tahtası ve döngü

Dosyalar: Drive `HcC Kasa Obsidian/00-Ajan-Tahtasi/` (`KURALLAR.md`, `TAHTA.md`, `gorevler/`, `olaylar/`) · Claude saatlik zamanlanmış kontrol (08–24 TR)

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-24 | Tahta kuralları: kart/adım/tek sahip, durum akışı, tek yazar (Claude), ChatGPT olay notu, Hermes GIRIS/SON_DURUM. Claude QC GEÇTİ → kasaya (Cihan'ın ayrıca kabulü gerekmez, ret hakkı saklı). Claude'un saatlik kontrol görevi (değişiklik yoksa sessiz). İlk kartlar: eğitim kartı (Hermes kaynak → ChatGPT föy → Claude QC/şekil/PDF → kullanım → tekrar föyü), PCH-K kasa alımı, H-09 düzeltmesi | Cihan en az insan müdahalesiyle döngü istedi | Kuruldu; Hermes kaynak görevi GIRIS'te | Test |

## CGPT-TEK-STIL — YMM StudyPack tek stil, 4 dosya (ChatGPT görev emri)

Dosyalar: Drive `HcC Kasa Obsidian/40-YMM-Sinav/00-YENI-DUZEN/03_DIREKTIF_CHATGPT_STUDYPACK_TEK_STIL_v1.md` · bağlam: aynı klasörde `01_SPK_KAPSAMA_HARITASI_2023-2026.md`, `02_YENI_DUZEN_KARAR.md`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-28 | İlk görev emri (Claude): konu başına 4 dosya (1-KART, 2-VAKA, 3-COZUM, 4-TEST); yalnız 4 frontmatter alanı; süreç verisi yasak; iki kapı (kaynak + Python hesap); ikili karar KABUL/DÜZELT; pilot 2 paket: VR-E-004 dönüşümü + SPK-A1 yeni üretim | Kasa süreç dosyalarıyla doldu; Cihan çalışacağı dosyayı bulamıyor. Cihan 28.10'da 4 dosya formatını onayladı; ders bazında ayrı stil şablonu isteyebileceğini bildirdi | 29.10 teslim: 2 paket, 8 dosya. Claude QC Q1–Q8 iki pakette GEÇTİ → KABUL; Python 11/11 blok birebir; ChatGPT kaynak paketteki süre hatasını yakaladı (9,0 M → 9,6 M); SPK-A1'e Claude 3 kart ekledi. Açık: SPKn m.22 metni [EKSİK] | Stabil |

## SADE-v1 — ymm-korpus + kasa sadeleştirme (Codex görev emri)

Dosyalar: `ymm-korpus/direktifler/codex/SADE-v1_GITHUB_KASA.md` (private) · tek plan: `ymm-korpus/00_strateji/PLAN.md`

| Sürüm | Tarih | Değişiklik | Neden | Sonuç | Durum |
|---|---|---|---|---|---|
| v1.0 | 2026-10-28 | İlk görev emri (Claude): yalnız taşıma (git mv), içerik değişmez; strateji belgeleri, eski dış model görevleri ve eski raporlar arşive; kasa kopyaları (dagitim/kasa_*) çıkarılır; DURUM.md tek blok; `cikti/` ağacı; kasada `00-CALIS/00-PANO.md` ve eski klasörler `_ARSIV/2026-10-28_eski-duzen/`; kanıt: dosya sayısı mutabakatı, yalnız-rename diff, link kontrolü | K11 KARAR-5 (Cihan onayı 28.10) | Codex'e sevk bekliyor | Taslak |

## Eski tracker'dan devreden, kaydı yapılmamış sürümler

| Prompt | Sürüm | Tarih | Not |
|---|---|---|---|
| Müzakere ve davranış bilimi iletişim sistem prompt'u | v1.0 | 2026-03-30 | 8 çerçeve; Claude Project'te kullanılıyor |
| İnceleme harness (Claude Code yürütme çerçevesi, vergi uyarlaması) | v1.0 | 2026-10-08 | Kasada `20-Araclar/Prompt-Kutuphanesi/Prompt-Inceleme-Harness.md` |
