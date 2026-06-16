<%*
// Auto-ustvari dnevni dashboard IN supplement taske za danes
const today = tp.date.now("YYYY-MM-DD");
const todayHuman = tp.date.now("dddd, DD. MMMM YYYY");
const tasksFolder = "TaskNotes/Tasks";

// Preveri če supplement teski že obstajajo
const existing = app.vault.getAbstractFileByPath(`${tasksFolder}/${today} 03 Vyvanse 40mg.md`);

// Ime datoteke
const dashPath = `09_DASHBOARDS/Daily/${today}.md`;

// Ustvari Daily mapo če ne obstaja
try { await app.vault.createFolder("09_DASHBOARDS/Daily"); } catch(e) {}

// Nastavi naslov datoteke
await tp.file.rename(today);
_%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - daily
  - dashboard
---

# 📅 <% tp.date.now("dddd, DD. MMMM YYYY") %>

> [[2026-06-13|🏠 Glavni Dashboard]] | [[<% tp.date.now("YYYY-MM-DD", -1) %>|◀ Včeraj]] | [[<% tp.date.now("YYYY-MM-DD", 1) %>|Jutri ▶]]

---

## 💊 Supplement Tracker

<%*
const t = tp.date.now("YYYY-MM-DD");
const exists = app.vault.getAbstractFileByPath(`TaskNotes/Tasks/${t} 03 Vyvanse 40mg.md`);
if (!exists) {
    tR += `> ⚠️ **Supplement teski za danes še niso ustvarjeni!**\n> Pritisni \`Ctrl+Shift+S\` da jih ustvariš.\n`;
} else {
    tR += `> ✅ Supplement teski so pripravljeni.\n`;
}
_%>

```tasknotes
filter by tag: supplement
filter by scheduled date: <% tp.date.now("YYYY-MM-DD") %>
sort by scheduled
```

---

## ✅ Odprte Naloge

```tasknotes
filter by status: open
sort by priority
sort by scheduled
```

---

## 📝 Dnevi Zapiski & Opombe

*(Piši tukaj — misli, opažanja, ideje)*

---

## 🌅 Jutranja Refleksija

- [ ] Kako sem spal? (1-10): 
- [ ] Energija zjutraj (1-10): 
- [ ] Fokus danes:

---

## 🌙 Večerna Refleksija

- [ ] Kaj sem dosegel danes?
- [ ] Kaj je šlo dobro?
- [ ] Kaj bi spremenil?
- [ ] Energija zvečer (1-10):

---

## 💊 Supplement Opažanja

- Energija: ☐ Nizka ☐ Srednja ☐ Visoka
- Apetit: ☐ Zmanjšan ☐ Normalen ☐ Povečan
- Spanec prejšnjo noč: ☐ Slab ☐ Okej ☐ Odličen
- Vadba: ☐ Da ☐ Ne
- Stranski učinki: 

---

## 🔗 Povezave

- [[2026-06-13|2026-06-13]]
- [[02_AREAS/Peptidni Dnevnik/Dnevni Urnik - Peptide Protocol|💊 Peptide Urnik]]
