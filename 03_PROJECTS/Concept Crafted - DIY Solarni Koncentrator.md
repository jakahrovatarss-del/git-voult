---
created: 2026-06-10
tags:
  - note
  - journal
source: https://www.youtube.com/watch?v=Alx_vwyksTw
---

# Uvod

![James Webb vesoljski teleskop — mozaik šesterokotnih ogledal (NASA)](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/James_Webb_Space_Telescope.jpg/500px-James_Webb_Space_Telescope.jpg)
*James Webb Space Telescope — 18 šesterokotnih zrcal iz katerih je bil povzet dizajn DIY solarnega koncentratorja*

Video prikazuje testiranje DIY solarnega generatorja ki je zasnovan po principu Jamesovega Webba — 18 ogledal razporejenih v mozaik, usmerja sončno svetlobo na zbiralnik vode. Rezultat: **~924 W** iz 1,31 m² odsevne površine.

# Struktura

- Princip: [[Solarni Koncentrator]] — 18 paraboličnih ogledal usmerja svetlobo na eno točko
- Sledenje: [[Sledenje Soncu - LDR]] — 4 LDR senzorji sledijo soncu
- Fizika: [[Specifična Toplota]] — izračun moči iz segrevanja vode

# Tehnična izvedba

**Ogledala:** 18 kosov, skupna odsevna površina 1,31 m². Vsako ogledalo je posamezno nastavljivo. Problem: 3D tiskane vzmeti za nastavljanje — ali zdržijo toploto?

**Zbiralnik:** bakrena plošča (kolektor) pobarvana črno da absorbira max toploto. Prvotni načrt (sekundarno ogledalo v centru) opuščen ker bi moralo sekundarno ogledalo zdržati enako temperaturo kot kolektor (do 200°+).

**Poravnava ogledal:** laserski sistem z LED + lupa → en velik rdeč pik ki pokrije celo ogledalo, namesto premikanja majhne laserske pike 18×.

# Rezultati testiranja

| Parameter | Vrednost |
|---|---|
| Začetna temperatura vode | 22,6 °C |
| Končna temperatura vode | 44,2 °C |
| Čas testa | 32 min (1.952 s) |
| Volumen vode | 20 L = 20.000 g |
| Energija Q | 183.840 J |
| Moč | **~924 W** |
| Moč na m² | **~705 W/m²** |
| Moč na ogledalo | **~51 W/ogledalo** |

Izračun: [[Specifična Toplota]] → Q = m · c · ΔT = 20.000 × 4,18 × 21,6 = 183.840 J → P = Q/t = 183.840/1952 ≈ **924 W**

# Problemi in rešitve

| Problem | Rešitev |
|---|---|
| Oblačno nebo → LDR ne ve kam | GPS/koordinatno sledenje (kompromis: drago) |
| LDR premalo natančno | Rokav ki blokira svetlobo iz stranskih smeri |
| Ogledalo se je prevrnilo v vetru | Premik kolektorja pred pivotno točko (napačna teža) |
| Sekundarno ogledalo bi se stopilo | Direktna montaža kolektorja |

# Naslednji korak

Avtor sprašuje: rebuild + popravki OR nova, vremensko zaščitena verzija z boljšimi ogledali?

# Viri

- Video: [My DIY Solar Generator Is WAY More Powerful Than I Thought](https://www.youtube.com/watch?v=Alx_vwyksTw) — Concept Crafted Creations
- Koncepti: [[Solarni Koncentrator]], [[Sledenje Soncu - LDR]], [[Specifična Toplota]]
- Sorodna tehnika: [[SpaceX]] (NASA inženiring), [[mehanika]]
