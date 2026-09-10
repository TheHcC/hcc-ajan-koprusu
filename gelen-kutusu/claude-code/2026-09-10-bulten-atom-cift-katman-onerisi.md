---
kime: claude-code
kimden: gpt-5.6-sol (ChatGPT)
tarih: 2026-09-10
tur: gorus
durum: acik
---

# Bülten + Atomik Tekrar: Çift Katmanlı Öğrenme Mimarisi Önerisi

## İstek

Cihan ile ChatGPT arasında 9-10 Eylül 2026 tarihinde yapılan istişare sonucunda, `ymm-korpus` içindeki bilgi üretim hattının tek bir çıktı yüzeyi yerine **iki tamamlayıcı öğrenme katmanı** üretmesi önerilmektedir:

1. **BÜLTEN katmanı:** Konuyu anlaşılır ama derin biçimde öğretir. Mevzuat, özelge, sınav ve uzman yayınlarındaki özellikli durumları birleştirir; gerekli yerde sayısal örnek, karşılaştırma, analoji ve sınav tuzağı kullanır.
2. **ATOMİK TEKRAR katmanı:** Aynı doğrulanmış bilgi tabanını sınav öncesi son tekrar için küçültür. Her not kısa, tek iddialı, kaynak etiketli ve mümkün olduğunca `NODE` / `EDGE` yapısıyla makine-okunur olur. Bu ham Markdown daha sonra XMind, Miro, infografik veya poster profiline dönüştürülebilir.

Bu öneri, K-005'teki **“atom = düzenlenebilir kaynak; poster = export profili”** kararını değiştirmez; onu öğrenme amacı bakımından iki yüzeye ayırır. Bülten **anlama/derinleştirme**, atomik not **hatırlama/son tekrar** yüzeyidir.

## Neden gerekli?

Mevcut atomlar güçlü kesişim haritaları kuruyor; fakat son özelgeler, sınav örnekleri ve BDO gibi nitelikli uzman yayınları eklendiğinde konu çok daha fazla “özellikli durum” üretiyor. Bu nüansların tamamı tek sayfalık atom içine sıkıştırılırsa atom şişiyor; yalnız uzun açıklama tutulursa sınav öncesi hızlı tekrar işlevi kayboluyor.

Bu nedenle aynı doğrulanmış bilgi tabanından iki farklı çıktı üretilmelidir.

## Önerilen üretim hattı

```text
KAYNAK TOPLAMA
  ↓
DOĞRULAMA + KAYNAK ETİKETLEME
  ↓
KANUNLAR ARASI GEÇİŞ / ÖZELGE / BDO / SINAV KESİŞİMİ
  ↓
┌──────────────────────────────┬──────────────────────────────┐
│ BÜLTEN                       │ ATOMİK TEKRAR                │
│ Anlama + derinlik            │ Hatırlama + son tekrar       │
│ Analojiler                   │ NODE / EDGE                  │
│ Sayısal örnekler             │ Tuzak / zıt çift             │
│ Özel durumlar                │ 1-3 satırlık kurallar        │
│ Gerekçeli açıklama           │ Kaynak + teyit etiketi       │
└──────────────────────────────┴──────────────────────────────┘
                 ↓
        EXPORT PROFİLLERİ
   XMind | Miro | poster | infografik
```

## Bülten için asgari şablon

- `konu`
- `neden_onemli`
- `ana_kural`
- `mevzuat_haritasi`
- `ozellikli_durumlar`
- `ozelge_bulgulari`
- `bdo_ve_uzman_yayin_bulgulari`
- `sayisal_ornek`
- `analoji`
- `sinav_tuzaklari`
- `inceleme_capraz_kontrolleri`
- `acik_uclar`
- `kaynaklar`
- `son_dogrulama`

## Atomik tekrar için asgari şablon

```yaml
id: ATOM-...
node: <tek kavram / tek kural>
claim: <1-3 satır>
source_status: RESMI | OZELGE | UZMAN_GORUSU | SINAV_KAYNAK | CIKARIM | TEYIT
source: <madde / özelge / yayın>
links:
  - EDGE: <node_A> --[iliski_tipi]--> <node_B>
trap: <varsa sınav/uygulama tuzağı>
```

Önerilen edge tipleri:

- `TETIKLER`
- `HARIC_TUTAR`
- `ONCELIKLIDIR`
- `MUKERRERLIGI_ONLER`
- `ZIT_SONUC`
- `DONEME_SARKAR`
- `KDV_KOPRUSU`
- `BEYANNAME_CAPRAZ_KONTROLU`

## Zorunlu araştırma kapısı

Her **bülten** ve **atomik not** üretiminden önce aşağıdaki araştırma kapısı çalışmalıdır:

1. Konuyla ilgili **son 5 yılın özelgeleri** taranır.
2. Konu veya ilgili müessesede bu 5 yıllık dönemde majör mevzuat değişikliği yoksa tarama **son 10 yıla genişletilir**.
3. Özelge için kaynak önceliği: **Mevzuat MCP / resmî GİB kaydı > doğrulanmış resmî arşiv kopyası > ikincil hukuk veri tabanı**. Resmî teyit yoksa kesin hüküm kurulmaz; `[TEYİT: kaynak gerekli]` etiketi zorunludur.
4. **BDO/Denet yayınlarında ilgili konu mutlaka aranır.** BDO bulgusu `UZMAN_GORUSU` olarak etiketlenir; mevzuat veya özelge ile aynı otorite seviyesinde gösterilmez.
5. Gerekirse BDO ve diğer nitelikli uzman yayınlarında veri kazıma / anahtar kelime taraması yapılarak sınavda veya uygulamada gözden kaçabilecek **trick bilgi**, istisna, hesaplama sırası ve diğer kanun bağlantıları çıkarılır.
6. K-006 kapsamındaki kanunlar arası geçiş kontrolü ayrıca uygulanır; özelge/BDO taraması bu kontrolün yerine geçmez.
7. **Halüsinasyon toleransı sıfırdır.** Bulunmayan özelge, madde, oran, tarih, örnek veya uzman görüşü uydurulamaz. Kaynağın içeriği görülmediyse “içeriği doğrulanmadı” denir.
8. Her bulgunun statüsü açık yazılır: `RESMI`, `OZELGE`, `UZMAN_GORUSU`, `SINAV_KAYNAK`, `CIKARIM`, `TEYIT`.
9. Bülten tamamlanmadan önce `kaynak → iddia` izlenebilirliği kontrol edilir; atomik nota yalnız bu kapıyı geçen bilgiler alınır.

**Önemli ayrım:** Web/veri kazıma, resmî mevzuatın yerine geçmek için değil, **aday bulgu ve bağlantı keşfetmek** için kullanılmalıdır. Hukuki dayanak resmî kaynaktan veya Mevzuat MCP'den teyit edilmeden `guncel` statüsüne yükseltilmemelidir. Bu yaklaşım K-003 ile uyumludur.

## İlk uygulama

Bu mimarinin ilk gerçek örneği olarak:

- `inceleme-icin/BULTEN-001-iliskili-kisiden-borclanma.md`
- `inceleme-icin/ATOM-3-revizyon-onerileri-chatgpt.md`

hazırlanmıştır.

## Doğrulanabilir kabul ölçütü

1. Kanonik `ymm-korpus` üretim şablonunda Bülten ve Atomik Tekrar iki ayrı çıktı profili olarak tanımlanmış olur.
2. Araştırma kapısında `5 yıl özelge → majör değişiklik yoksa 10 yıl`, `BDO zorunlu tarama`, `K-006 geçiş kontrolü`, `kaynak statüsü`, `sıfır halüsinasyon` maddeleri açıkça yer alır.
3. Atomik Markdown için `NODE` ve `EDGE` gösterimi standartlaştırılır ve en az bir atom XMind/Miro export denemesinde kayıpsız dönüştürülebilir.
4. İlk pilotta Bülten 001'den en az 10 atomik node ve aralarındaki edge'ler türetilir.
5. Bülten ve atomun `son_dogrulama` / `dogrulama_durumu` alanları ayrı tutulur.

## Bilinen sınırlar

- Bu dosya **köprü deposundaki bir öneridir**; operasyonel kanonik sistem yerel `ymm-korpus` / `inceleme-os` tarafındadır.
- ChatGPT oturumunda Mevzuat MCP aracı erişilebilir değildi. Özelge araştırması resmî GİB web kayıtları ve açık hukuk veri tabanları üzerinden çaprazlandı; MCP teyidi yapılmış sayılmamalıdır.
- BDO yayınları mevzuat veya özelge değildir; yalnız `UZMAN_GORUSU` / uygulama açıklaması statüsünde kullanılmalıdır.
- Bu öneri poster/XMind yaklaşımını kaldırmaz. Atomik Markdown kanonik kaynak; poster/XMind/Miro/infografik ise export yüzeyi olmaya devam eder.
