---
baslik: HCC Sistem Darbogazlari — Normalizasyon Analizi
yazar: Claude (Claude.ai sohbet, model: Claude Opus 5.5)
tur: sistem-analizi / mimari oneri
tarih: 2026-09-25
versiyon: v1
girdi: "[[2026-09-25_GROK_ai-radar-pilot-raporu_v1]]"
cikti: "[[2026-09-25_DIREKTIF_CLAUDE-Opus-5.5-to-CLAUDE-CODE_N1-N3-uygulama_v1]]"
durum: ONERI (Cihan onayi bekliyor)
etiketler: [hcc-sistem-analizi, claude, normalizasyon, kanit-defteri]
---

# HCC Sistem Darboğazları — Normalizasyon Analizi (v1)

Grok'un raporu iyi bir teşhis, ama darboğazları tek tek ele alırsak her birine yeni bir araç eklemiş oluruz. 10 darboğaz aslında 4 kök nedenden çıkıyor. "Normalize etmek" de veritabanındaki anlamıyla okunabilir: her bilgi tek yerde yaşar, geri kalan her şey oradan otomatik türetilen bir görünümdür.

## Kök neden haritası

- **Durum dağınık** (#1 gelen kutusu, #6 bayat köprü, #9 dağınık bellek): Aynı gerçek 3–4 yerde elle tutuluyor.
- **Kanonik kaynak var, türetim yok** (#5 üç hedef): Otorite sırası tanımlanmış, ama kopyalar elle eşitleniyor.
- **Doğrulama tek noktaya kilitli** (#3 ADR-9, #4 GİB, #8 bayatlama): Doğrulama sonucu kayda geçmiyor, bu yüzden her seferinde yeniden yapılıyor.
- **Cihan iki işi birden yapıyor** (#2 router, #7 onay): Mekanik yönlendirme ile hukuki yargı aynı kişide toplanmış.

## Dört normalizasyon

**N1 — Tek durum makinesi.** Klasörler durum olmaktan çıksın, durumun görünümü olsun. Her paketin tek bir kuyruk kaydı olur: `TASLAK → URETILDI → MEKANIK_PASS → MEVZUAT_PASS → KABUL → ARSIV`. `02_ISLENDI_ARSIV`'in boş olması, son geçişin bir sahibi olmadığını gösteriyor. KABUL verildiği anda taşıma işi bir script'e bağlanmalı, akla bırakılmamalı. Public `DURUM.md` de bu kayıttan üretilsin ve 3 günden eskiyse başlığına otomatik "BAYAT — gerçek durum Drive'da" yazsın. Böylece #6 bir hijyen sorunu olmaktan çıkar, kendi kendini ilan eden bir durum olur.

**N2 — Tek yönlü türetim.** Üç hedef senkronu ikiye iner. Obsidian vault'u doğrudan `ymm-korpus` git çalışma ağacını, yani `09_bilgi/` klasörünü göstersin. O zaman Obsidian'daki md dosyası zaten git'teki dosyanın kendisi olur. Obsidian MCP'nin yanlış dizine bakma sorunu da aynı anda çözülür. Drive Google Doc'u da git'ten tek yönlü üretilen, "düzenleme git'te yapılır" başlıklı salt-okunur bir kopya olsun. Kural basit: Drive'ın gelen kutusu yalnız girdi kanalıdır, türetilmiş Doc'lar yalnız çıktıdır. İki yön asla aynı klasörde buluşmaz.

> Not (v1 sonrası tespit): "HcC Kasa Obsidian" vault'u zaten Google Drive ile senkronize bir klasör. Yani vault içindeki `.md` dosyaları Drive'da da duruyor. N2 tasarımında bu gerçek dikkate alınmalı: pratikte hedefler "git ↔ vault(Drive)" olarak ikiye inebilir.

**N3 — Kanıt Defteri.** En yüksek kaldıraç bu. Her mevzuat veya özelge atfı bir kez doğrulandığında bir kayıt oluşur: `atıf_id`, kaynak/madde, metin hash'i, tarih, araç, güven düzeyi (`RESMI` / `ADAY`) ve `bağımlı_atomlar[]`. Bu tek yapı üç darboğazı birden çözer:
- **#3:** Bir atomun tüm atıfları defterde `RESMI` ve güncel ise Codex mevzuat PASS'ı defterden verebilir. Claude'un toplu turu yalnızca defterde olmayan yeni atıfları görür. Hem kota tasarrufu sağlar hem de tek ajana kilitlenmeyi kırar.
- **#8:** Bayatlama motoru küçük bir iş hâline gelir. Haftalık zamanlı bir görev atıfları yeniden çeker, hash değiştiyse bağımlı atomları `BAYAT` olarak işaretler.
- **#4 ve MCP kırılganlığı:** Bir devre kesici konur. Üst üste iki timeout gelince atıf `TEYIT_BEKLIYOR` kuyruğuna düşer ve toplu tur durmaz. Chrome DevTools MCP bu deftere yalnızca `ADAY` üreten bir kaynak olarak girer, böylece K-003 kendiliğinden korunur.

**N4 — Yönlendirme ≠ yargı.** KABUL kapısı Cihan'da kalmalı, ona dokunulmaz. Ama kopyala-yapıştır ve "şimdi Claude'a ver" işi deterministik bir script'in işi, ajanın değil. İzin istemlerine gelince, Happy'den önce istem sayısını düşürmek gerekir. Claude Code izin kurallarıyla (allow/deny) yalnız `ymm-korpus/03_taslak/**` gibi dar yollara yazma izni vermek sandbox'ı kapatmaz ve 14.09 kararına aykırı değildir. Codex tarafında workspace-write sandbox'ı aynı rolü görür. İstemlerin çoğu bu şekilde yok olur. Geriye kalanlar hâlâ can sıkıyorsa Happy o zaman anlam kazanır.

**#10 için:** Üç bölgeli hafif bir tablo yeterli: 0 = mükellef/VDK, 1 = ymm-korpus, 2 = public/Drive. Her aracın bir bölge tavanı olur; örneğin Happy ve DevTools MCP'nin tavanı 1. Tek satırlık bir kural, ağır bir yönetişim gerektirmez.

## Asıl meta-darboğaz

Grok'un "hatırlattığı" şeyler de bir desen gösteriyor: Herdr, Kaku ve Jev önerilmiş ama hiçbirinin PASS'i yok. Rapor şimdi iki yeni pilot daha öneriyor. Kurucu Paradoksu'nun sistem düzeyindeki hâli bu. Öneri: **aynı anda tek aktif pilot, 14 günde PASS/FAIL, yoksa otomatik kapanır.**

Düzeltme: Grok, Jev'i "Kaku auto-tag, ertelendi" diye sınıflamış. Oysa Jev, Claude Code ve Codex için kurulmakta olan model/effort yönlendiricisi HCC Adaptive Router'ın temeli (notlar: Drive `20-Araclar/Jev`). Bu kayıt düzeltilmezse bir sonraki model de yanlış okur.

Grok'un iki adayı arasında sıralama net: **önce DevTools MCP.** A-009 bir doğruluk tıkanıklığı. Happy ise bir konfor meselesi, N4'teki izin kuralları çoğu ihtiyacı zaten karşılayabilir.

## Sıralama

1. **Faz 0 — bu hafta, sıfır yeni araç:** Gelen kutusunu arşivle, DURUM'a bayatlık başlığını ekle, Herdr/Kaku için karar ver, Jev kaydını düzelt, bölge tablosunu yaz.
2. **Faz 1 — N1 + N2:** Kuyruk kaydı, Obsidian'ı git ağacına bağlama, Drive'a tek yönlü üretim.
3. **Faz 2 — N3:** Kanıt Defteri ile birlikte DevTools MCP pilotu, defterin `ADAY` kaynağı olarak.
4. **Faz 3 — Bayatlama görevi ve dar izin kuralları.** Happy ancak bundan sonra, gerekirse.

## Ölçüm

Ölçmeden optimize edilmez. VR11–VR20 taban çizgisi olarak kullanılır ve şunlar sayılır: paket başına Cihan'ın araya girme sayısı, tur başına izin istemi sayısı, 01'den KABUL'e geçen süre, açık `[TEYİT]` sayısı. N3'ten sonra defterden karşılanan atıf oranı eklenir.
