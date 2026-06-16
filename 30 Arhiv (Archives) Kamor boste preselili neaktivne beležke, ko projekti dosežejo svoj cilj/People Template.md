---
name: <% tp.file.title %>
aliases: 
type:
  - Person
  - Family
  - sister
date-met: 
location: 
fukcija:
---


# <% tp.file.title %>

> [! sun]- ## KTATEK OPIS
> ### 📋 
> log-spol:: 
> log-ZANIMIVOST:: 
>log-stopnja prijateljstva
> 
> 
> :: 
> 
> ### ✅ pogostost videnja:
> - [x] vsak dan ✅ 2025-10-14
> - [x] tedn ✅ 2025-10-14
> - [x] mesec ✅ 2025-10-14
> - [x] leto ✅ 2025-10-14
> :: 
> 
> ### prednosti
> - [x] vsak dan ✅ 2025-10-14
> - [x] tedn ✅ 2025-10-14
>
> 
>
> 
>
> ### ☑ avtizem
> - [x] ja-ne ✅ 2025-10-14
> :: 

## PREDNOSTI 

## SLABOSTI




```dataview
TABLE
rows.Details as "Details"
Where contains(log, this.file.name)
FLATTEN log as Details
WHERE contains(Details, this.file.name)
GROUP BY file.link as Source
SORT rows.file.day desc
```
