# Setup Guide

Ta vault je narejen kot povezan sistem za osebno organizacijo, projekte, šolo in solo učenje. Vsak nov koncept naj bo linkan, da se znanje ne kopiči v izolirane zapiske.

## Struktura

- `00_INBOX` za hitre capture zapiske.
- `01_SYSTEM` za pravila, tokove dela in operativne vodiče.
- `02_AREAS` za stalna področja odgovornosti.
- `03_PROJECTS` za aktivne projekte z jasnim izidom.
- `04_RESOURCES` za reference, članke, ideje in podporno gradivo.
- `05_SCHOOL` za formalno šolo, predmete, naloge in izpite.
- `06_LEARNING` za samostojno učenje, skill trees in study plans.
- `07_AI` za AI workflowe, prompte in avtomatizacije.
- `08_TEMPLATES` za reusable predloge.
- `09_DASHBOARDS` za vstopne točke.

## Ključna pravila linkanja

1. Vsak nov koncept dobi svojo opombo ali pa se poveže na obstoječo opombo.
2. Prva omemba pomembnega pojma naj uporablja `[[wikilink]]`.
3. Če ustvariš novo temo, dodaj vsaj eno povezavo nazaj na širši kontekst.
4. Vsaka predmetna ali učna opomba mora imeti sekcijo `Povezave`.
5. Ne piši izoliranih seznamov brez konteksta; poveži jih z `[[Predmet]]`, `[[Projekt]]`, `[[Koncept]]`, `[[Vir]]`.

## Kako vgraditi šolo

Mapa `05_SCHOOL` naj pokriva formalne obveznosti.

Predlagana struktura:
- `05_SCHOOL/Predmeti/`
- `05_SCHOOL/Naloge/`
- `05_SCHOOL/Izpiti/`
- `05_SCHOOL/Zapiski/`
- `05_SCHOOL/Profesorji/`

Za vsak predmet naredi hub note, npr. `[[Matematika]]`, ki linka na:
- tedenske zapiske,
- domače naloge,
- izpitne priprave,
- ključne koncepte,
- uporabne vire.

Primer toka:
- Predavanje ustvari `[[Matematika - 2026-05-25]]`
- Koncept iz predavanja dobi svojo opombo, npr. `[[Linearna funkcija]]`
- Naloga se poveže na predmet in koncept: `[[Naloga - Matematika - Vaje 3]]`
- Priprava na test se poveže na vse relevantne koncepte: `[[Izpit - Matematika - Algebra 1]]`

## Kako vgraditi solo učenje

Mapa `06_LEARNING` je za samostojno učenje izven formalne šole. To je pomembno ločiti od `05_SCHOOL`, ker ima drugačen tempo, motive in metrike.

Predlagana struktura:
- `06_LEARNING/Teme/`
- `06_LEARNING/Skill Trees/`
- `06_LEARNING/Study Plans/`
- `06_LEARNING/Projects/`
- `06_LEARNING/Summaries/`

Model:
- Tema: široko področje, npr. `[[Programiranje]]`
- Koncept: ožja ideja, npr. `[[Python funkcije]]`
- Plan: pot učenja, npr. `[[Study Plan - Python Osnove]]`
- Projekt: praktična uporaba, npr. `[[Mini projekt - Python kalkulator]]`
- Refleksija: kaj znaš, kaj manjka, kaj je naslednje

Za vsako temo vodi:
- zakaj se učiš,
- katere podteme obstajajo,
- kateri viri so najboljši,
- kateri projekti dokazujejo razumevanje,
- kaj je naslednji korak.

## Povezovanje šole in solo učenja

Šola in solo učenje naj ne bosta ločena sveta. Poveži jih, kjer se prekrivata.

Primeri:
- `[[Fizika]]` poveži z `[[Matematika]]` in `[[Problem solving]]`
- `[[Angleščina]]` poveži z `[[Writing]]`, `[[Vocabulary building]]`, `[[Public speaking]]`
- `[[Programiranje]]` v šoli poveži z `[[Programiranje]]` v solo učenju, vendar imej ločene opombe za formalne naloge in samostojne projekte

## Dnevni workflow

1. Capture v `00_INBOX`.
2. Obdelaj zapisek in ga premakni v pravo mapo.
3. Dodaj povezave na obstoječe koncepte.
4. Če je koncept nov, ustvari concept note.
5. Na koncu tedna posodobi dashboarde in study plane.

## Tedenski review

Preveri:
- kateri predmeti potrebujejo več pozornosti,
- kateri learning tracks stagnirajo,
- kateri koncepti nimajo dovolj povezav,
- kateri projekti lahko služijo kot dokaz znanja,
- kateri viri so dejansko uporabni.
