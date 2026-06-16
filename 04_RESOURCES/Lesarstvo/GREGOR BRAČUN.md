---
name: <% tp.file.title %>
aliases: 
type:
  - Person
date-met: 01.09.2023
location: ŠOLA
fukcija: PROFESOR
---


# <% tp.file.title %>

> [! sun]- ## KTATEK OPIS
> ### 📋 
> log-spol:: M
> log-ZANIMIVOST:: 8
>log-stopnja prijateljstva 7
> 
> 
> :: 
> 
> ### ✅ pogostost videnja:
> - [x] vsak dan ✅ 2025-10-14
> - [x] tedn
> - [x] mesec ✅ 2025-10-14
> - [x] leto ✅ 2025-10-14
> :: 
> 
> ### prednosti
> - [x] vsak dan ✅ 2025-10-14
> - [x] tedn
>
> 
>
> 
>
> ### ☑ avtizem
> - [x] ja-ne
> :: 

## PREDNOSTI 

EDEN NAJBOLJŠIH PROFESROJEV KI SEM JIH SPOZNA. ZDI SE MI DA JE ZELO DOBER PRIDOBITEK MOJI ŠOLI IN MI JE ŽAL DA JE PRIŠEL TAKO POZNO DA ME NE MORE UČIT. Z NJIM SMO ŠLI V FRANCIJO NA IZMENJAVO [[FRANCIJA ERAZMUS]] TAKO DE JE SUPER

## SLABOSTI
[[2023-11-14]] 
TO POVZAME



```dataview
TABLE
rows.Details as "Details"
Where contains(log, this.file.name)
FLATTEN log as Details
WHERE contains(Details, this.file.name)
GROUP BY file.link as Source
SORT rows.file.day desc
```
