---
created: 2026-03-02
tags:
  - 0🌲
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
include: 
exclude: 
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# Osnovne iformacije

- statika je del mehanike kejr telo mirujeali pa se giblje z konstantno hitrostjo zato je **rezultanta sil vedno enaka 0** 
- usa telesa so **deformabilna**- togo telo. da izračunamo sile in momente brez upostevanja mansih deformacij. 
## Postopek reševanja

- ali je točka ali pa togo telo (POJAVIJO SE SE POGOJI Z MOMENTI) 
![[Pasted image 20260302151025.png]]
če miruje pomeni da je rezultanta sil nič

# 2) Sila, moment, dvojica (Force, Moment, Couple)

- **Sila (Force)** je vektor: ima velikost, smer in prijemališče (kjer deluje). V ravnini jo običajno razstavimo na komponente Fx,FyFx,Fy in računamo z vsotami komponent.

- **Moment sile (Moment of a force)** pove, kako močno sila “vrti” telo okrog točke: v 2D je ideja M=F⋅dM=F⋅d (sila krat pravokotna ročica).

- **Dvojica sil (Couple moment)** je par enako velikih nasprotnih sil, ki povzroča čisto vrtenje (brez translacije) in je “svobodni vektor” — lahko jo narišeš kamorkoli na FBD.

## 3) Redukcija sistema sil (Reduction of a force system)

Cilj redukcije je: več sil na togem telesu zamenjamo z **ekvivalentnim** sistemom v izbrani točki OO:

- rezultanta R=∑FR=∑F (Resultant force)
    
- in glavni moment MO=∑(r×F)+∑MMO=∑(r×F)+∑M (Resultant couple moment at O).
    

To je osnova, da sploh znaš potem pravilno pisati ravnotežne enačbe za togo telo. V nalogah Jesenko imaš direkt tipične primere “Reduciraj sistem v točko O” (to je točno redukcija!).

Spodaj je moja skica (da si predstavljaš idejo): sile zamenjamo z RR v točki OO + momentom MOMO.

(Priložena slika kot artefakt)

- **reduction_force_couple.png** [code_file]
    

## 4) Enačbe statičnega ravnovesja (Equations of static equilibrium) + FBD

Najbolj pomembno pravilo: **naloge ne rešujemo brez diagrama prostega telesa** (Free-Body Diagram, FBD).​

## 4.1 Ravnovesje točke (Particle equilibrium)

Če je telo modelirano kot točka v 2D, sta pogoja:

- ∑Fx=0∑Fx=0
    
- ∑Fy=0∑Fy=0  
    To je v Hibbelerju v **Chapter 3 (Equilibrium of a Particle)**, kjer je tudi postopek risanja FBD.​
    

Realni primer (točka): obroček, na katerem visijo 2 vrvi in masa. Sestaviš FBD obročka in rešiš 2 enačbi za 2 neznanki (napetosti).​

## 4.2 Ravnovesje togega telesa (Rigid body equilibrium)

Four beam support types: fixed support with moment, pin support, roller support, and free end with reaction forces [](https://www.eigenplus.com/basic-terminologies-in-structure/)

Če ima telo “dimenzije” (nosilec, plošča, drog), potrebuješ še moment:

- ∑Fx=0∑Fx=0
    
- ∑Fy=0∑Fy=0
    
- ∑MO=0∑MO=0 (moment okrog poljubne točke OO)  
    To je v Hibbelerju v **Chapter 5 (Equilibrium of a Rigid Body)**, kjer so tudi reakcije podpor in pravila za FBD.​
    

Spodaj je moja skica tipičnega nosilca s **zglobom (pin)** in **valjem (roller)** ter reakcijami.

(Priložena slika kot artefakt)

- **fbd_beam_pin_roller.png** [code_file] 
    

## Reakcije podpor (Support reactions)

Ključna ideja: podpora prepreči določene pomike → zato nastanejo ustrezne reakcije.​

- Zglob/pin: običajno Ax,AyAx,Ay (2 neznanki).​
    
- Valj/roller: običajno samo ByBy (1 neznanka).​
    
- Vpetje/fixed: Ax,AyAx,Ay in še moment MAMA (3 neznanke).​