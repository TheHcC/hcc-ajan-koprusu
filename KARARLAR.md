# KARARLAR — gerekçeleriyle

En yeni en üstte. Karar silinmez; değişirse yeni satır eklenir ve eskisi
"revize edildi" olarak işaretlenir.

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

## K-001 · Bilgi atomu "kart" değil "poster"
**Tarih:** 08.09.2026 · **Veren:** Claude Code (Cihan onayladı)

Eski sistem bilgi birimi olarak SRS kartını seçti; kartlar kullanılabilir çıkmadı.
Drive arşivi 2022'den 2025'e dört farklı derste tek bir tutarlı format gösteriyor:
tek konu / tek sayfa / görsel tablo. Yeni sistemin birim kaydı budur. Her poster
makine-okunur künye taşır: `dayanak`, `gecerlilik_donemi`, `son_dogrulama`,
`dogrulama_durumu`.

**Sonucu:** "Kendi kendine öğrenen sistem" somut bir anlam kazanır — bayatlama,
`dayanak` alanının mevzuattan periyodik yeniden doğrulanmasıdır.
