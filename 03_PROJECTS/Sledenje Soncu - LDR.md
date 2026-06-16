---
categories:
  - "[[Koncepti]]"
created: 2026-06-10
---

# Kaj je

![LDR (fotoupor) — svetlobno odvisen upor](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/LDR_1480405_6_7_HDR_Enhancer_1.jpg/250px-LDR_1480405_6_7_HDR_Enhancer_1.jpg)
*LDR (Light Dependent Resistor) — fotoupor čigar upornost pada z jakostjo svetlobe*

Sledenje soncu je ključen problem pri [[Solarni Koncentrator|solarnih koncentratorjih]] in solarnih panelih. Sonce se premika ~15°/h, kar pomeni da nepremični sistem hitro izgubi fokus.

# LDR metoda (preprosta, poceni)

4 LDR senzorji razporejeni v kvadrat z pregraditvami vmes. Logika: primerjaj napetost med levim/desnim in zgornjim/spodnjim LDR parom → motor premakne ogledalo v smer večje svetlobe.

**Prednosti:**
- Poceni (~1€ za 4 LDR)
- Enostavna implementacija
- Deluje brez GPS ali interneta

**Slabosti:**
- **Ne deluje v oblačnem vremenu** — razpršena svetloba, LDR ne ve kam
- Sence iz konstrukcije zmotijo senzorje → rešitev: rokav ki blokira stransko svetlobo
- Manjša natančnost kot koordinatni sistemi

**Izboljšava natančnosti:** 3D tiskani rokav (sleeve) ki omeji vidni kot vsakega LDR → senzor zazna samo neposredno sončno svetlobo, ne pa razpršene. [[Concept Crafted - DIY Solarni Koncentrator]]

# GPS/koordinatna metoda (natančna, draga)

Alternativa: izračunaj položaj sonca na podlagi GPS koordinat, datuma in časa. Astronomski algoritmi (npr. SPA — Solar Position Algorithm, NREL).

**Prednosti:**
- Deluje v oblačnem vremenu
- Visoka natančnost

**Slabosti:**
- Zahteva GPS modul ali internet
- Kompleksnejša programska oprema
- Ni samopopravljajoča (napaka mehanike se ne popravlja)

# Hibridna rešitev

Kombinacija: koordinatni algoritem za grobo pozicioniranje + LDR za fino korekcijo. Najboljši izkoristek, robustno.

# Povezano

[[Solarni Koncentrator]]
[[Specifična Toplota]]
[[Concept Crafted - DIY Solarni Koncentrator]]
[[mehanika]]
