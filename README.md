# Ajan Köprüsü — HcC

Bu depo bir **köprüdür**. İçinde iş yapılmaz; işin *nerede kaldığı, ne konuşulduğu
ve ne kararlaştırıldığı* burada tutulur ki farklı ortamlardaki modeller aynı
gerçekliği okusun.

**Neden public:** Claude.ai sohbeti ve ChatGPT, private depoları okuyamaz. Bu deponun
tek amacı onların da okuyabilmesi olduğu için public'tir.

## ⛔ Bu depoya ASLA girmeyecek şeyler

- Mükellef adı, VKN, tutar, beyanname, defter, tutanak — **hiçbir inceleme verisi**
- Kişisel belge, sınav sonucu, itiraz dosyası, sağlık/mali özel bilgi
- Kurum içi yazışma, özelge/rapor tam metni

Bu depo fiziksel olarak `claude-practice` ağacının **dışındadır**; mükellef verisi
oraya bakan hiçbir komutla buraya karışamaz. Bu sınır tartışmaya kapalıdır.

## Kim, neyi okur

| Dosya | Ne verir | Kim okumalı |
|---|---|---|
| `DURUM.md` | Şu anki durum özeti + otorite defterlere işaretçi | Herkes, ilk olarak |
| `GUNLUK.md` | Baştan sona anlatı: ne konuşuldu, hangi aşamalardan geçildi | Sohbete yeni katılan model |
| `KARARLAR.md` | Verilen kararlar ve **gerekçeleri** | Karar tartışacak olan |
| `gelen-kutusu/` | Bir ajana bırakılmış görev/görüş dosyaları | Adı geçen ajan |

## Otorite sırası — çelişkide ne esas alınır

Bu depo **ikinci kopyadır, otorite değildir.** Çelişki olursa:

1. `Desktop\inceleme-os\<slug>\durum.md` — operasyonel gerçek (kilit, faz, işlem defteri)
2. `claude-practice\.gorev-durumu\aktif-gorev.json` — adım adım checkpoint
3. Bu depo — anlatı ve karar geçmişi

Buradaki `DURUM.md` bayat olabilir. Sayısal/operasyonel bir iddiayı buradan alıp
kesin diye sunma; yukarıdaki otoriteye bak.

## Halüsinasyon önleme — her modelin uyacağı 7 kural

Bu depoyu okuyan **her model** (Claude, GPT, Gemini, hangisi olursa) şunlara uyar:

1. **Bilmiyorsan "bilmiyorum" yaz.** Boşluğu doldurma. Eksik bilgi, uydurulmuş
   bilgiden her zaman iyidir.
2. **Her sayısal/hukuki iddia kaynak gösterir.** Kaynak yoksa
   `[TEYİT: kaynak gerekli]` etiketiyle yaz — etiketsiz kesin ifade kullanma.
3. **Mevzuat parametresi (oran, tutar, süre, eşik) doğrulanmadan "güncel" denmez.**
   Yıl belirt: "2026 için X" — "X'tir" değil.
4. **Başka modelin çıktısını denetlemeden devralma.** Devraldığında hangi iddiayı
   doğruladığını, hangisini doğrulayamadığını yaz.
5. **Dosya/klasör/fonksiyon adı uydurma.** Var olduğunu görmediğin bir yolu
   referans verme.
6. **Kendi işini "tamamlandı" ilan etmeden önce kanıt göster.** Hangi komut koştu,
   çıktısı ne oldu.
7. **Bülten/atom araştırma kapısı zorunludur.** Her bülten ve atomik not üretiminden önce ilgili konudaki son **5 yılın özelgeleri** taranır. İlgili müessese veya konu alanında bu dönemde majör mevzuat değişikliği yoksa tarama **10 yıla** genişletilir.

   - Özelge kaynak önceliği: `Mevzuat MCP / resmî GİB > doğrulanmış resmî arşiv
     kopyası > ikincil hukuk veri tabanı`.
   - Resmî teyit olmayan hukuki iddia `[TEYİT: kaynak gerekli]` etiketi taşır.
   - **BDO/Denet yayınlarında ilgili konu mutlaka taranır.** BDO bulguları
     `UZMAN_GORUSU` statüsündedir; mevzuat veya özelge gibi sunulmaz.
   - Gerekirse nitelikli uzman yayınlarında veri kazıma/anahtar kelime taramasıyla
     trick bilgi, istisna, hesaplama sırası ve diğer kanun bağlantıları çıkarılır.
   - K-006 kanunlar arası geçiş kontrolü ayrıca uygulanır.
   - Halüsinasyon toleransı sıfırdır: görülmeyen özelge, madde, oran, tarih,
     BDO görüşü veya örnek uydurulamaz.
   - Bülten tamamlanmadan `kaynak → iddia` izlenebilirliği kontrol edilir;
     atomik nota yalnız doğrulama kapısını geçen bilgi alınır.
   - Web/veri kazıma resmî mevzuatın yerine geçmez; yalnız aday bulgu ve bağlantı
     keşfi için kullanılır. Hukuki dayanak resmî kaynak/Mevzuat MCP ile teyit
     edilmeden `guncel` statüsüne yükseltilmez.

## Bir ajana iş bırakmak

**18.09.2026'dan itibaren gelen kutusu GitHub'da DEĞİL, Google Drive'da:**
[HCC Ajan Köprüsü — Gelen Kutusu](https://drive.google.com/drive/folders/1MfpWVE8ubUO47018BuZ6uJCAVGkybRbJ)
(şablon ve kurallar o klasördeki `OKUBEN` dokümanında). Sebep: Claude.ai ve
ChatGPT web sohbetleri GitHub'a yazamıyor ama Drive'a kendi bağlayıcılarıyla
doğrudan yazabiliyor. `DURUM.md`/`GUNLUK.md`/`KARARLAR.md` değişmedi, hâlâ burada
— yalnız istek/öneri bırakma taşındı.

Eski `gelen-kutusu/claude-code/` ve `gelen-kutusu/codex/` klasörleri GitHub'da
arşiv olarak duruyor, silinmedi.

Cihan onaylamadan hiçbir ajan gelen kutusundaki isteği uygulamaz — gelen kutusu
bir **öneri kanalıdır**, emir kanalı değil (Drive'da da aynı kural geçerli).
