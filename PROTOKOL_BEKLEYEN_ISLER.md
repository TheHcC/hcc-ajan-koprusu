---
name: PROTOKOL_BEKLEYEN_ISLER
surum: v1
tarih: 2026-10-29
karar: K-012
gecerli: Claude (sohbet + Claude Code), ChatGPT, Codex, Hermes — hepsi
---

# Devir ve Hatırlatıcı Protokolü (K-012)

**Sorun:** Bir ajan "bunu Codex'e ver / Claude Code'a şunu yaz" diyor, o ajan o an kapalı, hatırlatıcı kurulmuyor, iş yarım kalıp unutuluyor.

**Çözüm:** Her devir **aynı yanıtta** iki iz bırakır: listeye bir satır + takvime bir hatırlatıcı. Liste tek yerde durur.

## Tek liste
`HcC Kasa Obsidian/00-Ajan-Tahtasi/BEKLEYEN_ISLER.md` (Google Drive). Obsidian açılış sayfası budur.
Depo tarafındaki görev kayıtları (`ymm-korpus/direktifler/ATAMA_TAHTASI.md`) ayrıca sürer; BEKLEYEN_ISLER insanın baktığı özet listedir.

Satır biçimi:
`| # | Ajan | İş | Komut / ne yapılacak (kopyala-yapıştır) | Nerede | Hatırlatıcı | Durum |`
Durum: `⏳ BEKLİYOR` · `🟡 ONAYINI BEKLİYOR` · `⏸ BEKLEMEDE` · `✅ <tarih>`

---

## Instructions for every agent (English; output in Turkish)

**Trigger:** any time you (a) hand work to another agent (Codex, Claude Code, Claude chat, ChatGPT, Hermes, Gemini), or (b) tell Cihan to do something later in another tool.

**In the same reply, before you finish:**
1. **List row.** If you can write to Google Drive, add the row to `BEKLEYEN_ISLER.md` yourself (Drive cannot edit in place: read → recreate the file with the row added → trash the old one). If you cannot write to Drive, end your reply with a block titled `📌 BEKLEYEN_ISLER satırı` containing the exact Markdown row, ready to paste.
2. **Reminder.** If you have a calendar tool, create a Google Calendar event (default: next day 10:00 Europe/Istanbul, popup at −60 and 0 min). The description must contain: the exact copy-paste command for the target agent, the file/directive path or link, and the link to the current conversation. If you have no calendar tool, end your reply with a block titled `⏰ Hatırlatıcı` containing date, time, title and description, ready to paste into Google Calendar or to send to Hermes.
3. **Command first.** The command in the row must work on its own when pasted into the target agent — no "see above", no references to this chat's context.
4. **Close.** When a delivery for a row arrives and is checked, change the row to `✅ <GG.AA>`. Rows that are ✅ for 14+ days move to the ARŞİV section.
5. **No sensitive data.** No taxpayer names, VKN/TCKN, amounts from inspections or file contents in the row, the reminder or the Telegram digest. Use the task ID only.

**Language:** All rows, reminders and messages to Cihan are in Turkish.

## Hermes (daily digest)
Task file `HERMES_GOREV_BEKLEYEN-OZET_2026-10-29_v1.md`: reads the list read-only every day at 08:30 TSİ and sends a ≤15-line Telegram summary; `komut <n>` returns that row's command. Starts only when Cihan places it in `VPS-KUTUSU/GIRIS/`.

## Repo side (HCC Graph A2)
Once A2 is merged, the Graph workflow lists open board rows with their age (❗ ≥3 days) every morning in the GitHub Actions summary. This is the repo mirror of the same idea; it does not read or write Drive.
