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

## Eski tracker'dan devreden, kaydı yapılmamış sürümler

| Prompt | Sürüm | Tarih | Not |
|---|---|---|---|
| Müzakere ve davranış bilimi iletişim sistem prompt'u | v1.0 | 2026-03-30 | 8 çerçeve; Claude Project'te kullanılıyor |
| İnceleme harness (Claude Code yürütme çerçevesi, vergi uyarlaması) | v1.0 | 2026-10-08 | Kasada `20-Araclar/Prompt-Kutuphanesi/Prompt-Inceleme-Harness.md` |
