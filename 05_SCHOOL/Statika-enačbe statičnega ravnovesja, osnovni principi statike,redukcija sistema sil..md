---
created: 2026-03-01
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

# kaj je statika 

Statika je veja mehanike, ki obravnava telesa v stanju **mirovanja** ali gibanja s konstantno hitrostjo. Za lažje računanje uporabljamo dve ključni poenostavitvi:

##  **Togo telo (Rigid Body)**: 

- Predpostavljamo, da se telo pod obremenitvijo ne deformira. Razdalje med točkami v telesu ostajajo enake.

## **Masna točka (Particle):** 

- Telo obravnavamo, kot da ima maso, a so njegove dimenzije zanemarljive. To uporabimo, ko se vse sile sekajo v eni točki.

## Zakoni

### **Newtonov 1. zakon (Newton’s First Law): 

Telo ostane v stanju mirovanja ali enakomernega gibanja, če nanj ne deluje neuravnotežena sila.

![[Pasted image 20260301173150.png]]

### **Newtonov 3. zakon (Newton’s Third Law):** 

Sile med dvema telesoma so vedno enako velike, a nasprotno usmerjene (akcija in reakcija).

![[Pasted image 20260301173211.png]]

### **Koncentrirana sila (****Concentrated Force****)**:** 

Učinek obremenitve, za katero predpostavljamo, da deluje v eni sami točki

![[Pasted image 20260301174859.png]]


# Redukcija sistema sil (Reduction of a Force System)

Redukcija je postopek, s katerim ta zapleten sistem nadomestimo z enostavnejšim, **ekvivalentnim sistemom** (_equivalent system_) v izbrani točki OKer na konstrukcije pogosto deluje več sil hkrati, jih zaradi lažjega računanja poenostavimo:

- ## **Rezultanta sil (Resultant Force -** R![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.471em"%20height="0.714em"%20style="width:0.471em"%20viewBox="0%200%20471%20714"%20preserveAspectRatio="xMinYMin"><path%20d="M377%2020c0-5.333%201.833-10%205.5-14S391%200%20397%200c4.667%200%208.667%201.667%2012%205%0A3.333%202.667%206.667%209%2010%2019%206.667%2024.667%2020.333%2043.667%2041%2057%207.333%204.667%2011%0A10.667%2011%2018%200%206-1%2010-3%2012s-6.667%205-14%209c-28.667%2014.667-53.667%2035.667-75%2063%0A-1.333%201.333-3.167%203.5-5.5%206.5s-4%204.833-5%205.5c-1%20.667-2.5%201.333-4.5%202s-4.333%201%0A-7%201c-4.667%200-9.167-1.833-13.5-5.5S337%20184%20337%20178c0-12.667%2015.667-32.333%2047-59%0AH213l-171-1c-8.667-6-13-12.333-13-19%200-4.667%204.333-11.333%2013-20h359%0Ac-16-25.333-24-45-24-59z"></path></svg>)**):** 

- To je ena sama sila, ki je vektorska vsota vseh sil v sistemu.

![[Pasted image 20260301173728.png]]

- ## **Rezultantni navor ali moment (Resultant Moment -** M![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.471em"%20height="0.714em"%20style="width:0.471em"%20viewBox="0%200%20471%20714"%20preserveAspectRatio="xMinYMin"><path%20d="M377%2020c0-5.333%201.833-10%205.5-14S391%200%20397%200c4.667%200%208.667%201.667%2012%205%0A3.333%202.667%206.667%209%2010%2019%206.667%2024.667%2020.333%2043.667%2041%2057%207.333%204.667%2011%0A10.667%2011%2018%200%206-1%2010-3%2012s-6.667%205-14%209c-28.667%2014.667-53.667%2035.667-75%2063%0A-1.333%201.333-3.167%203.5-5.5%206.5s-4%204.833-5%205.5c-1%20.667-2.5%201.333-4.5%202s-4.333%201%0A-7%201c-4.667%200-9.167-1.833-13.5-5.5S337%20184%20337%20178c0-12.667%2015.667-32.333%2047-59%0AH213l-171-1c-8.667-6-13-12.333-13-19%200-4.667%204.333-11.333%2013-20h359%0Ac-16-25.333-24-45-24-59z"></path></svg>)O​**):** 

- Ker sile ne delujejo nujno v točki O, povzročajo težnjo po vrtenju okoli nje. Moment izračunamo kot produkt sile in pravokotne razdalje (ročice) do točke: M=F⋅d (_scalar formulation_) ali vektorsko kot M![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.471em"%20height="0.714em"%20style="width:0.471em"%20viewBox="0%200%20471%20714"%20preserveAspectRatio="xMinYMin"><path%20d="M377%2020c0-5.333%201.833-10%205.5-14S391%200%20397%200c4.667%200%208.667%201.667%2012%205%0A3.333%202.667%206.667%209%2010%2019%206.667%2024.667%2020.333%2043.667%2041%2057%207.333%204.667%2011%0A10.667%2011%2018%200%206-1%2010-3%2012s-6.667%205-14%209c-28.667%2014.667-53.667%2035.667-75%2063%0A-1.333%201.333-3.167%203.5-5.5%206.5s-4%204.833-5%205.5c-1%20.667-2.5%201.333-4.5%202s-4.333%201%0A-7%201c-4.667%200-9.167-1.833-13.5-5.5S337%20184%20337%20178c0-12.667%2015.667-32.333%2047-59%0AH213l-171-1c-8.667-6-13-12.333-13-19%200-4.667%204.333-11.333%2013-20h359%0Ac-16-25.333-24-45-24-59z"></path></svg>)=r![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.471em"%20height="0.714em"%20style="width:0.471em"%20viewBox="0%200%20471%20714"%20preserveAspectRatio="xMinYMin"><path%20d="M377%2020c0-5.333%201.833-10%205.5-14S391%200%20397%200c4.667%200%208.667%201.667%2012%205%0A3.333%202.667%206.667%209%2010%2019%206.667%2024.667%2020.333%2043.667%2041%2057%207.333%204.667%2011%0A10.667%2011%2018%200%206-1%2010-3%2012s-6.667%205-14%209c-28.667%2014.667-53.667%2035.667-75%2063%0A-1.333%201.333-3.167%203.5-5.5%206.5s-4%204.833-5%205.5c-1%20.667-2.5%201.333-4.5%202s-4.333%201%0A-7%201c-4.667%200-9.167-1.833-13.5-5.5S337%20184%20337%20178c0-12.667%2015.667-32.333%2047-59%0AH213l-171-1c-8.667-6-13-12.333-13-19%200-4.667%204.333-11.333%2013-20h359%0Ac-16-25.333-24-45-24-59z"></path></svg>)×F![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.471em"%20height="0.714em"%20style="width:0.471em"%20viewBox="0%200%20471%20714"%20preserveAspectRatio="xMinYMin"><path%20d="M377%2020c0-5.333%201.833-10%205.5-14S391%200%20397%200c4.667%200%208.667%201.667%2012%205%0A3.333%202.667%206.667%209%2010%2019%206.667%2024.667%2020.333%2043.667%2041%2057%207.333%204.667%2011%0A10.667%2011%2018%200%206-1%2010-3%2012s-6.667%205-14%209c-28.667%2014.667-53.667%2035.667-75%2063%0A-1.333%201.333-3.167%203.5-5.5%206.5s-4%204.833-5%205.5c-1%20.667-2.5%201.333-4.5%202s-4.333%201%0A-7%201c-4.667%200-9.167-1.833-13.5-5.5S337%20184%20337%20178c0-12.667%2015.667-32.333%2047-59%0AH213l-171-1c-8.667-6-13-12.333-13-19%200-4.667%204.333-11.333%2013-20h359%0Ac-16-25.333-24-45-24-59z"></path></svg>) (_vector formulation_)..

![[Pasted image 20260301173855.png]]

- ## **Ekvivalentni sistem (Equivalent System):** 

- Celoten sistem sil zamenjamo z eno rezultanto in enim glavnim navorom v izbrani točki, kar ima na telo enak zunanji učinek.


![[Pasted image 20260301174049.png]]

# . Enačbe statičnega ravnovesja (Equations of Static Equilibrium)

Da telo dejansko miruje, morata biti izpolnjena dva pogoja: vsota vseh sil in vsota vseh navorov morata biti enaki nič.



![[Pasted image 20260301174152.png]]

## **V ravnini (2D Equilibrium):** 

Uporabljamo tri enačbe, ki preprečujejo premikanje levo/desno, gor/dol in vrtenje:
    1. ∑Fx​=0 (vsota vodoravnih sil).
    2. ∑Fy​=0 (vsota navpičnih sil).
    3. ∑MO​=0 (vsota navorov okoli poljubne točke O).


![[Pasted image 20260301174233.png]]
## **V prostoru (3D Equilibrium):** 

- Tukaj potrebujemo šest enačb, saj se telo lahko premika ali vrti v treh različnih smereh (∑Fx,y,z​=0 in ∑Mx,y,z​=0).


![[Pasted image 20260301174335.png]]

# **Diagram prostega telesa (****Free-Body Diagram - FBD****):** 


Preden začnete pisati enačbe, morate vedno narisati FBD. To je skica telesa, kjer odstranite vse podpore in jih nadomestite z **reakcijami** (_reactions_)

![[Pasted image 20260301175521.png]]


## Primer diagram prostega telesa

![[Pasted image 20260301175643.png]]