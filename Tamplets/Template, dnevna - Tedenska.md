---
type: daily
date: <% tp.file.title %>
---
# <% tp.file.title %>

> **Prev::** [[<% tp.date.now("YYYY-[W]ww", -1, tp.file.title, "YYYY-[W]ww") %>]]
> **Next::** [[<% tp.date.now("YYYY-[W]ww", 1, tp.file.title, "YYYY-[W]ww") %>]]
> **Parent::** [[<% tp.date.now("YYYY-MM", 0, tp.file.title, "YYYY-[W]ww") %>]], [[<% tp.date.now("YYYY", 0, tp.file.title, "YYYY-[W]ww") %>]]
>
> ---
> - [Google Calendar](https://calendar.google.com)  <!-- prilagodi link -->
> - Inbox: [[00 Inbox]]
>
> **Week range:** <%* tR += moment(tp.file.title, "YYYY-[W]ww").startOf('isoWeek').format("YYYY-MM-DD") + " — " + moment(tp.file.title, "YYYY-[W]ww").endOf('isoWeek').format("YYYY-MM-DD"); %>

---

## 🧭 Weekly Overview
**Tema / Fokus za ta teden:**  
**Ključni cilji (3 MITs)**  
- [x] MIT 1 — zaključi do (rok): ✅ 2025-10-14
- [x] MIT 2 — ✅ 2025-10-14
- [x] MIT 3 — ✅ 2025-10-14

**Prioritete:**  
1.  
2.  
3.

**Glavni projekti/fokus:**  
- [[20 Projekti/Projekt - ImeA]] — ključna naloga:  
- [[20 Projekti/Projekt - ImeB]] — ključna naloga:

---

## 📅 Pregled tedna — dnevne povezave
<!-- Automatsko generira povezave do posameznih dnevnih zapiskov v tem tednu (pon-ned) -->
<%*
const w = moment(tp.file.title, "YYYY-[W]ww");
const days = [];
for (let i = 1; i <= 7; i++) {
  const d = w.clone().isoWeekday(i).format("YYYY-MM-DD");
  days.push(`- [ ] [[${d}]] — ${w.clone().isoWeekday(i).format("dddd")}`);
}
tR += days.join("\n");
%>

---

## 📈 Habit / Routine tracker (pon→ned)
| Navada | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---:|---:|---:|---:|---:|---:|---:|
| Spanec 7+ h | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Učenje 30 min | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| Gibanje | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

---

## 🗂️ Week schedule (glavni dogodki)
- **Ponedeljek:**  
- **Torek:**  
- **Sreda:**  
- **Četrtek:**  
- **Petek:**  
- **Sobota:**  
- **Nedelja:**  

(Pripni pomembne linke/meeting notes: npr. `Meeting - 2025-10-15`)

---

## ✅ Naloge (Tasks) — teden (vse nedokončane naloge, schedulane v tem tednu)
```tasks
not done
scheduled after <%* tR += moment(tp.file.title, "YYYY-[W]ww").startOf('isoWeek').format("YYYY-MM-DD") %>
scheduled before <%* tR += moment(tp.file.title, "YYYY-[W]ww").endOf('isoWeek').format("YYYY-MM-DD") %>
sort by priority















