# KARARLAR — gerekçeleriyle

En yeni en üstte. Karar silinmez; değişirse yeni satır eklenir ve eskisi
"revize edildi" olarak işaretlenir.

---

## K-005 (K-001R) · Atom = düzenlenebilir kaynak; poster bir dışa aktarım profilidir
**Tarih:** 09.09.2026 · **Veren:** Cihan · **Öneren:** claude-opus-5 (Claude.ai sohbeti, itiraz yoluyla)
**Yerine geçtiği:** K-001

**Karar metni:**

> **Bilgi atomu:** tek konu / tek yüzey / makine-okunur künyeli konu birimi.
> Künye alanları: `dayanak`, `iliskili_maddeler`, `gecerlilik_donemi`,
> `son_dogrulama`, `dogrulama_durumu`.
>
> **Kaynak biçimi düzenlenebilir olmak zorundadır** (Markdown veya XMind).
> Poster, kaynaktan üretilen bir dışa aktarım profilidir — atomun kendisi değildir.
>
> **Yüzeyi ders değil, kaynak metnin yapısı seçer:**
> - Madde/fıkra hiyerarşisi taşıyan mevzuat → zihin haritası *(kanıt: SPK XMind'ları)*
> - Koşullu / karşılaştırmalı kural kümesi → poster-tablo *(kanıt: 9 vergi posteri + ~11 revizyon görseli)*
> - Kavram ağı + formül → zihin haritası *(kanıt: finans XMind'ları)*
> - Hesap/algoritma → föy + çözülmüş problem `[HİPOTEZ — arşivde üretim kanıtı yok]`

**K-001 neden yanlıştı — belirleyici kanıt:**

Claude Code'un bağımsız doğrulaması: `SPK HCC/MAPSPK` klasöründeki **14 XMind
dosyasının 6'sı 2026 yılında düzenlenmiş** (`2026-05-12`, `2026-05-08` ×2,
`2026-04-25` ×2, `2026-02-11`) — dosyalar 2022'de üretilmiş olmasına rağmen. Buna
karşılık PNG posterlerin hiçbiri Şubat 2025'ten sonra dokunulmamış.

Bu bir tercih farkı değil, **taşıyıcı farkıdır:** XMind düzenlenebilir kaynak, PNG
dondurulmuş çıktıdır. K-001'in kendi hedefi — "mevzuat değiştikçe kendini güncelleyen
sistem" — PNG üzerinde işletilemez; `son_dogrulama` künyesi bir görselin içine
yazılamaz.

**K-001'den korunan:** Formatın görsel-mekânsal olduğu tespiti doğruydu ve duruyor.
Yanlış olan, tek yüzey (poster) varsayımı ve donmuş bir biçimi atom saymaktı.

**Sayım düzeltmesi:** İtirazda "12 SPK XMind" geçiyor; Claude Code'un doğrudan
listelemesinde `MAPSPK` altında **14** XMind var (12, kök `SPK HCC` klasöründeki
sayıdır). `FİNANSAL YÖNETİM/MAPS` altındaki 13 XMind iddiası **bağımsız
doğrulanmadı** — o klasör listelenmedi.

---

## K-004 · Köprü deposu public olacak
**Tarih:** 08.09.2026 · **Veren:** Cihan · **Öneren:** Claude Code

Claude.ai sohbeti ve ChatGPT private depoları okuyamaz. Bu deponun tek varlık sebebi
onların okuyabilmesi olduğundan public olmak zorunda. Karşılığında depo, mükellef ve
kişisel veriden tamamen arındırılmış tutulur ve `claude-practice` ağacının dışında,
ayrı bir dizinde yaşar.

---

## K-003 · Mevzuat doğrulaması MCP bağlantısı düzelene kadar ertelendi
**Tarih:** 08.09.2026 · **Veren:** Cihan

`Mevzuat MCP` ve `yargi-mcp` bağlantı hatası verdiği için mevzuat teyitleri bekliyor.
Web kazıma araçlarıyla teyit **reddedildi**: resmî mevzuat için ikinci sınıf kaynak.
Doğrulanmamış her parametre `[TEYİT: kaynak gerekli]` ile işaretlenir.

---

## K-002 · Yeni vault açılmayacak; bilgi ağacı `ymm-korpus` içine kuruldu
**Tarih:** 08.09.2026 · **Veren:** Cihan · **Öneren:** Claude Code, Astra

Sistemde zaten 8 kayıtlı Obsidian vault'u var ve asıl şikâyet dağınıklık. 9. vault
tanıya değil semptoma ekleme olurdu. `ymm-korpus` zaten hem kayıtlı bir vault hem de
kendi GitHub deposu — bilgi ağacı oraya `09_bilgi/` olarak kuruldu. `TEKNO AI HcC`
vault'u gerçek inceleme bulguları için temiz bırakıldı.

---

## K-001 · Bilgi atomu "kart" değil "poster"  ~~[REVİZE EDİLDİ → K-005]~~
**Tarih:** 08.09.2026 · **Veren:** Claude Code (Cihan onayladı)

Eski sistem bilgi birimi olarak SRS kartını seçti; kartlar kullanılabilir çıkmadı.
Drive arşivi 2022'den 2025'e dört farklı derste tek bir tutarlı format gösteriyor:
tek konu / tek sayfa / görsel tablo. Yeni sistemin birim kaydı budur. Her poster
makine-okunur künye taşır: `dayanak`, `gecerlilik_donemi`, `son_dogrulama`,
`dogrulama_durumu`.

**Sonucu:** "Kendi kendine öğrenen sistem" somut bir anlam kazanır — bayatlama,
`dayanak` alanının mevzuattan periyodik yeniden doğrulanmasıdır.
