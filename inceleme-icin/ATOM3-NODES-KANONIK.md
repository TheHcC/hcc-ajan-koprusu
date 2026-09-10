# Atomik Tekrar — İlişkili Kişiden Borçlanma (Atom 3 / Bülten 001)

> **Kaynak:** `25-bulten/BULTEN-001-iliskili-kisiden-borclanma.md` ve
> `10-poster/iliskili-kisiden-borclanma.md` — aynı doğrulanmış araştırma
> tabanından türetilmiştir, bağımsız araştırma yapılmamıştır.
>
> **Kullanım:** Sınav öncesi hızlı tekrar. Her NODE tek iddia taşır. EXPORT'a
> (XMind/Miro/infografik) hazır — bu şu an **veri modelidir**, otomatik
> dönüştürücü henüz yazılmadı (K-006 kararı: skill/exporter terfisi 10 atom
> sonrasına bırakıldı).
>
> **Şema:** `id · node · claim · source_status · source · trap? · links`
> `source_status ∈ {RESMI, OZELGE, UZMAN_GORUSU, SINAV_KAYNAK, YARGI, CIKARIM, TEYIT}`

---

```yaml
id: N-01
node: UC_MUESSESE
claim: >
  İlişkili kişiden borçlanma üç ayrı vergi merceğinden geçer — örtülü
  sermaye (miktar), transfer fiyatlandırması (fiyat), FGK (toplam yabancı
  kaynak dengesi). Tetikleyicileri bağımsızdır.
source_status: RESMI
source: KVK m.12, m.13, m.11/1-i
links:
  - EDGE: N-01 --[ONCELIKLIDIR]--> N-02

id: N-02
node: MUKERRER_KKEG_KAPISI
claim: >
  Örtülü sermaye veya transfer fiyatlandırması nedeniyle zaten KKEG sayılan
  finansman gideri, FGK hesabına bir daha girmez.
source_status: RESMI
source: KVKUGT 11.13.9 (satır 11756) — resmî örnekle Python'da doğrulandı, 9/9 PASS
trap: >
  KKEG-1 düşülmeden toplam gider üzerinden FGK hesaplamak — resmî örnekte
  1.000 TL fazla KKEG çıkarır.
links:
  - EDGE: N-01 --[MUKERRERLIGI_ONLER]--> N-02

id: N-03
node: TICARI_BORC_EMSAL_VADE
claim: >
  "Ticari borç mu?" yanlış sorudur. Doğru soru: piyasa/teamül vadesi
  aşıldı mı? Aşılmışsa örtülü sermaye testine girer.
source_status: RESMI
source: KVKUGT 12.1.6 (satır 12311) — doğrudan tebliğ metni, özelgeye gerek kalmadı
trap: "Vadeli mal/hizmet borcunu otomatik 'ticari, güvenli' sayıp örtülü sermaye testinden muaf tutmak."
links:
  - EDGE: N-03 --[VADE_ASILIRSA]--> N-01

id: N-04
node: AVANS_YABANCI_KAYNAK
claim: >
  Alınan sipariş avansları da işletmeye finansman sağladığı için örtülü
  sermaye hesabında borç olarak dikkate alınır. İstisna: inşaat istihkak
  bedelleri avans sayılmaz.
source_status: RESMI
source: KVKUGT 12.1.6 (satır 12311)
trap: "'Kredi almadım, avans aldım' savunması örtülü sermaye testini durdurmaz."
links:
  - EDGE: N-04 --[FINANSMAN_SAGLAR]--> N-01

id: N-05
node: KOPRU_KREDI_FIILI_KULLANICI
claim: >
  Banka kredisi finansman yükü kalmaksızın grup şirketine aktarılırsa, FGK
  yükü krediyi ilk alan değil, fiilen kullanan şirkette kalır.
source_status: RESMI
source: KVKUGT 11.13 (satır ~11199)
trap: "'Krediyi bankadan ilk alan şirket FGK yükünü her zaman taşır' ezberi."
links:
  - EDGE: N-05 --[ONCELIKLIDIR]--> N-01

id: N-06
node: ZIT_ZAMAN_TESTI
claim: >
  Örtülü sermaye "hesap dönemi içinde herhangi bir tarihte" ölçülür; FGK
  "dönem sonu bilançosu" ile ölçülür. Aynı yıl içindeki geçici aşım ikisini
  farklı etkileyebilir.
source_status: RESMI
source: KVKUGT 12.1.1 (herhangi bir tarih) + KVKUGT 11.13 Örnek 1 ("dönem sonu itibarıyla")
links:
  - EDGE: N-06 --[ZAMAN_TESTI]--> N-01
  - EDGE: N-06 --[ZAMAN_TESTI]--> N-07

id: N-07
node: KUR_FARKI_UC_YONLU
claim: >
  Örtülü sermayede kur farkı gideri KKEG, geliri kazanca alınmaz, kâr payı
  da sayılmaz (stopajsız). FGK'da ise kur farkı kapsam içindedir — aynı
  kalem, iki müessesede zıt.
source_status: RESMI
source: KVKUGT 12.3, 12.4 (satır 12410-12444) + KVKUGT 11.13.1 (kapsam)
links:
  - EDGE: N-07 --[ZIT_SONUC]--> N-06

id: N-08
node: KARSI_DUZELTME_KESINLESME
claim: >
  Borç veren tarafta düzeltme yapılabilmesi için, örtülü sermaye kullanan
  kurum adına tarh edilen verginin kesinleşmiş VE ödenmiş olması şarttır —
  düzeltme yıllar sonraya sarkabilir.
source_status: RESMI
source: KVKUGT 12.4 (satır 12425)
links:
  - EDGE: N-08 --[DONEME_SARKAR]--> N-01

id: N-09
node: IDARI_YARGI_CARPISMASI
claim: >
  Borç veren tarafta zarar/vergi ödenmemesi durumunda düzeltmenin akıbeti
  konusunda idari ve yargısal görüş çarpışabilir — bu oturumda tam teyit
  edilemedi.
source_status: TEYIT
source: "[TEYİT: MCP bağlantısı başarısız — Yargı MCP CONNECT_TIMEOUT verdi]"
trap: "Danıştay 9. Daire E.2023/4917, K.2024/2755 atfı ChatGPT taslağında var; tam metin görülmeden kesin kural yazılmaz."
links:
  - EDGE: N-08 --[ACIK_UC]--> N-09

id: N-10
node: KDV_M30D_ACIK_UC
claim: >
  KDV m.30/d parantezinde yalnız KVK m.13 (transfer fiyatlandırması)
  anılıyor, m.12 (örtülü sermaye) anılmıyor — üçüncü zıt-çift adayı, ama
  metinde örtülü sermayeye özgü hüküm yok; bu bir çıkarımdır.
source_status: CIKARIM
source: KDV m.30/d metni (olumsuz delil) — bkz. G-017, gecis-haritasi.md
trap: "Örtülü sermaye KKEG'i için KDV indirim iptalinin de otomatik işlediğini varsaymak — bu metinde yazılı değil."
links:
  - EDGE: N-01 --[KDV_KOPRUSU]--> N-10

id: N-11
node: YABANCI_ORTAK_DORT_KATMAN
claim: >
  Yabancı ortaktan borçlanma dört ayrı katmanı aynı anda tetikleyebilir —
  örtülü sermaye, emsal faiz (TF), stopaj/ÇVÖA, sorumlu sıfatıyla KDV.
source_status: TEYIT
source: "KVK m.12/m.13 RESMI; KVK m.30 stopaj genel oranı (%15) RESMI (satır 2699); güncel ÇVÖA indirimi ve KDV sorumluluğunun kesin dayanağı [TEYİT: kaynak gerekli]"
links:
  - EDGE: N-11 --[TETIKLER]--> N-01
  - EDGE: N-11 --[TETIKLER]--> N-10
```

---

## Beyanname çapraz kontrolü (BEYANNAME_CAPRAZ_KONTROLU)

```yaml
id: N-12
node: BEYANNAME_CAPRAZ_KONTROLU
claim: >
  KV beyannamesinde KKEG-1 (örtülü sermaye/TF) ve KKEG-2 (FGK) ayrı
  satırlarda, çakışmadan gösterilmelidir; inceleme sinyali budur.
source_status: SINAV_KAYNAK
source: "BULTEN-001 §12 (inceleme çapraz kontrolü) — sınav ve uygulama pratiğinden çıkarım"
links:
  - EDGE: N-02 --[BEYANNAME_CAPRAZ_KONTROLU]--> N-12
```

## İlişki tipleri sözlüğü (bu setle sınırlı, genişletilebilir)

| Tip | Anlamı |
|---|---|
| `TETIKLER` | A gerçekleşirse B devreye girer |
| `ONCELIKLIDIR` | A, B'den önce hesaplanır |
| `MUKERRERLIGI_ONLER` | A, B'nin aynı tutarı iki kez saymasını engeller |
| `ZIT_SONUC` | Aynı olgu A'da ve B'de ters sonuç doğurur |
| `DONEME_SARKAR` | A'nın sonucu ileri bir döneme taşınabilir |
| `ZAMAN_TESTI` | A ve B farklı zaman ölçütleriyle test edilir |
| `KDV_KOPRUSU` | A'nın KV sonucu, KDV'de ayrı bir soru doğurur |
| `VADE_ASILIRSA` | A yalnız belirli bir eşik aşıldığında B'ye dönüşür |
| `FINANSMAN_SAGLAR` | A, B'nin tanımına giren bir finansman kaynağıdır |
| `ACIK_UC` | A'nın B üzerindeki etkisi doğrulanmadı |
| `BEYANNAME_CAPRAZ_KONTROLU` | A'nın doğru işlendiği B'de görülür |
