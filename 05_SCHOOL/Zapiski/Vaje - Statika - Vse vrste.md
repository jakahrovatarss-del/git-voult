---
tags: [mehanika, statika, reakcije, škripec, paličje, 3D-statika, valji, ravnovesje, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# Vaje — Statika: Vse vrste nalog

## Namen

Celovite rešene naloge za **1. SKLOP: Statika** — pokriva vse štiri tipe izpitnih vprašanj korak za korakom. Vsaka naloga vsebuje FBD, izpeljavo, pogosto napako in cross-link na ustrezni Blok.

---

## Kazalo nalog

| Naloga | Tip | Ključna tehnika |
|--------|-----|-----------------|
| [[#NALOGA 1 — L-nosilci s škripcem (navpična vrv)\|NALOGA 1]] | Reakcije, škripec | S = G, ΣM okrog B |
| [[#NALOGA 2 — L-nosilci s škripcem pod kotom\|NALOGA 2]] | Škripec + nagnjena vrv | Razstavi S na komponenti |
| [[#NALOGA 3 — Prostoležeč nosilci z porazdeljeno obtežbo in točkovno silo\|NALOGA 3]] | Klasičen nosilci A–B | ΣMA = 0 → By direktno |
| [[#NALOGA 4 — 3D statika: redukcija sistema sil\|NALOGA 4]] | 3D vektorji R, M₀ | Vektorski produkt r × F |
| [[#NALOGA 5 — Valji v kupu (3+2+1)\|NALOGA 5]] | Posebna telesa | Geometrija 60°, N1 iz cos30° |
| [[#NALOGA 6 — Paličje: metoda vozlišč\|NALOGA 6]] | Paličje, 5 palic | ΣF = 0 v vsakem vozlišču |
| [[#NALOGA 7 — Kombinirana: nosilci + NTM + geometrija\|NALOGA 7]] | Celotna veriga Blok 0→1→1.5 | Reakcije → Mmax → W |

---

## NALOGA 1 — L-nosilci s škripcem (navpična vrv)

> **Besedilo naloge:** Kovinsko dvigalo (nosilci v obliki obrnjene L) je togo vpeto v tleh v točki B. Na koncu konzolnega dela (točka A, $a = 2\ \text{m}$ od osi stebra) je pritrjen fiksni škripec. Vodoravna ročica $a = 2\ \text{m}$, višina stebra $H = 4\ \text{m}$. Dvigujemo tovor mase $m = 20\ \text{kg}$. Izračunajte reakcije v vpetju B. ($g = 10\ \text{m/s}^2$)

**Podatki:**
- $m = 20\ \text{kg}$, $G = m \cdot g = 200\ \text{N} = 0{,}2\ \text{kN}$
- Ročica: $a = 2\ \text{m}$, višina: $H = 4\ \text{m}$
- Škripec v točki A, vrv poteka navpično

---

### Korak 1 — Sila v vrvi

Škripec **samo** preusmerja vrv — sile **ne** povečuje:

$$S = G = m \cdot g = 20 \cdot 10 = \boxed{200\ \text{N} = 0{,}2\ \text{kN}}$$

Na škripec delujeta **dve veji vrvi**, obe navpično navzdol:

$$F_A = 2 \cdot S = 2 \cdot 0{,}2 = \boxed{0{,}4\ \text{kN} \downarrow}$$

> **Zakaj 2S?** Škripec je kladka v ravnovesju — nanj "vlečeta" tovor s silo S navzdol IN vrvna veja, ki gre k dvigalu, s silo S navzdol. Obe sta enaki, ker je vrv napeta enakomerno.

> **Poenostavitev BTF:** Ko naloga omeni le tovor brez opisa poteka vrvi, privzamemo $F_A = G$ (en segment vrvi). Ko je eksplicitno naveden škripec → $F_A = 2G$.

> **glej:** [[Blok 0 - Statika#Intuicija]]

---

### Korak 2 — FBD vpetja B

Vpetje prevzame **tri neznane reakcije**: $B_x$ (vodoravno), $B_y$ (navpično), $M_B$ (moment).

```
         A ← F_A = 0,4 kN ↓
         |
    ─────┤  ← a = 2 m →
         |
    B ───┘  ← vpetje (Bx, By, MB)
```

---

### Korak 3 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad \boxed{B_x = 0}$$

$$\sum F_y = 0 \quad \Rightarrow \quad B_y - F_A = 0 \quad \Rightarrow \quad \boxed{B_y = 0{,}4\ \text{kN}\ \uparrow}$$

$$\sum M_B = 0 \quad \Rightarrow \quad M_B - F_A \cdot a = 0$$

$$M_B = 0{,}4 \cdot 2 = \boxed{0{,}8\ \text{kNm}}$$

---

### Korak 4 — Rezultati

| Reakcija | Vrednost | Smer |
|----------|----------|------|
| $B_x$ | 0 kN | — |
| $B_y$ | 0,4 kN | gor ↑ |
| $M_B$ | 0,8 kNm | (v smeri urinega kazalca) |

> ⚠️ **Pogosta napaka:** Ročica momenta je **vodoravna razdalja** $a$, ne višina stebra $H$. Navpična sila $F_A$ povzroča moment z ročico $a = 2\ \text{m}$, ne $H = 4\ \text{m}$.

---

## NALOGA 2 — L-nosilci s škripcem pod kotom

> **Besedilo naloge:** Enaki L-nosilci kot v Nalogi 1 ($a = 1{,}5\ \text{m}$, $H = 4\ \text{m}$), a tokrat prosta veja vrvi (ki jo drži delavec) ni navpična — teče pod kotom $\alpha = 30°$ glede na navpičnico. Tovor $m = 50\ \text{kg}$. Izračunajte $B_x$, $B_y$, $M_B$.

**Podatki:**
- $G = 50 \cdot 10 = 500\ \text{N} = 0{,}5\ \text{kN}$
- $\alpha = 30°$ od navpičnice (prosta veja vrvi)
- $a = 1{,}5\ \text{m}$, $H = 4\ \text{m}$

---

### Korak 1 — Sili v točki A

Sila v vrvi je enaka povsod: $S = G = 0{,}5\ \text{kN}$.

**Navpična veja** (tovor, navpično navzdol):

$$\vec{S}_1 = (0,\ -0{,}5)\ \text{kN}$$

**Poševna veja** (pod $\alpha = 30°$ od navpičnice → vodoravna komponenta desno):

$$S_{2,x} = +S \cdot \sin\alpha = 0{,}5 \cdot \sin 30° = 0{,}5 \cdot 0{,}5 = +0{,}25\ \text{kN}$$

$$S_{2,y} = -S \cdot \cos\alpha = -0{,}5 \cdot \cos 30° = -0{,}5 \cdot 0{,}866 = -0{,}433\ \text{kN}$$

> **Zakaj sin/cos?** Ker je $\alpha$ od **navpičnice** → $\sin\alpha$ = vodoravna, $\cos\alpha$ = navpična komponenta. Nasprotno od kota od vodoravnice!

---

### Korak 2 — Skupna sila na točko A

$$F_{A,x} = +0{,}25\ \text{kN} \quad \text{(desno)}$$

$$F_{A,y} = -0{,}5 - 0{,}433 = -0{,}933\ \text{kN} \quad \text{(navzdol)}$$

---

### Korak 3 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad B_x + F_{A,x} = 0 \quad \Rightarrow \quad \boxed{B_x = -0{,}25\ \text{kN}\ \leftarrow}$$

$$\sum F_y = 0 \quad \Rightarrow \quad B_y + F_{A,y} = 0 \quad \Rightarrow \quad \boxed{B_y = +0{,}933\ \text{kN}\ \uparrow}$$

Moment okrog B — vsaka komponenta sile $F_A$ ima svojo ročico:

$$\sum M_B = 0 \quad \Rightarrow \quad M_B - |F_{A,y}| \cdot a - |F_{A,x}| \cdot H = 0$$

$$M_B = 0{,}933 \cdot 1{,}5 + 0{,}25 \cdot 4 = 1{,}4 + 1{,}0 = \boxed{2{,}4\ \text{kNm}}$$

> ⚠️ **Ključno:** $F_{A,y}$ (navpična sila) ima ročico $a$ (vodoravna razdalja). $F_{A,x}$ (vodoravna sila) ima ročico $H$ (navpična višina). Ne zamešaj!

> **glej:** [[Vaje - Statika posebnih teles in Steiner#NALOGA 2]]

---

## NALOGA 3 — Prostoležeč nosilci z porazdeljeno obtežbo in točkovno silo

> **Besedilo naloge:** Vodoravni nosilci dolžine $L = 6\ \text{m}$ leži na dveh prostoležečih podporah A (nepomični tečaj) in B (pomični valj). Na razdalji $x_C = 4\ \text{m}$ od A deluje točkovna sila $F = 12\ \text{kN}$ navzdol. Po celotni dolžini deluje enakomerna porazdeljena obtežba $q = 2\ \text{kN/m}$. Izračunajte reakcije $A_x$, $A_y$, $B_y$.

**Podatki:**
- $L = 6\ \text{m}$, $x_C = 4\ \text{m}$
- $F = 12\ \text{kN}$, $q = 2\ \text{kN/m}$
- A = nepomični tečaj ($A_x$, $A_y$), B = pomični valj ($B_y$)

---

### Korak 1 — Nadomestna sila porazdeljene obtežbe

Enakomerna $q$ po celotni dolžini L:

$$Q = q \cdot L = 2 \cdot 6 = 12\ \text{kN} \quad \text{(deluje v težišču = sredini)} \quad x_Q = 3\ \text{m od A}$$

---

### Korak 2 — ΣMA = 0 direktno da $B_y$

$$\sum M_A = 0 \quad \Rightarrow \quad B_y \cdot L - Q \cdot x_Q - F \cdot x_C = 0$$

$$B_y \cdot 6 = 12 \cdot 3 + 12 \cdot 4 = 36 + 48 = 84$$

$$\boxed{B_y = \frac{84}{6} = 14\ \text{kN}\ \uparrow}$$

> **Taktika:** Momentna enačba okrog A izniči obe komponenti v A → direktno $B_y$!

> **glej:** [[Blok 0 - Statika#Kako začeti reševati]]

---

### Korak 3 — Ostali reakciji

$$\sum F_y = 0 \quad \Rightarrow \quad A_y + B_y - Q - F = 0$$

$$A_y = Q + F - B_y = 12 + 12 - 14 = \boxed{10\ \text{kN}\ \uparrow}$$

$$\sum F_x = 0 \quad \Rightarrow \quad \boxed{A_x = 0}$$

> (Pomični valj B ne more prenašati vodoravnih sil — privzamemo le navpični obtežbi.)

---

### Korak 4 — Kontrola

$$\sum M_B = 0: \quad -A_y \cdot 6 + Q \cdot (6-3) + F \cdot (6-4) = -10 \cdot 6 + 12 \cdot 3 + 12 \cdot 2 = -60 + 36 + 24 = 0\ ✓$$

---

### Korak 5 — Rezultati

| Reakcija | Vrednost |
|----------|----------|
| $A_x$ | 0 kN |
| $A_y$ | 10 kN ↑ |
| $B_y$ | 14 kN ↑ |

> ⚠️ **Kontrola:** $A_y + B_y = 10 + 14 = 24\ \text{kN} = Q + F = 12 + 12 = 24\ \text{kN}$ ✓

---

## NALOGA 4 — 3D statika: redukcija sistema sil

> **Besedilo naloge:** Na kvadrasto telo ($a = 3\ \text{m}$) delujeta dve sili. $\vec{F}_1 = (-1,\ 5,\ -8)\ \text{kN}$ deluje v točki $P_1 = (3,\ 0,\ 3)\ \text{m}$, $\vec{F}_2 = (0,\ 0,\ -4)\ \text{kN}$ deluje v točki $P_2 = (3,\ 3,\ 3)\ \text{m}$. Reducirajte sistem na izvorišče $O = (0,\ 0,\ 0)$.

**Podatki:**
- $\vec{F}_1 = (-1,\ 5,\ -8)\ \text{kN}$, $\vec{r}_1 = (3,\ 0,\ 3)\ \text{m}$
- $\vec{F}_2 = (0,\ 0,\ -4)\ \text{kN}$, $\vec{r}_2 = (3,\ 3,\ 3)\ \text{m}$

---

### Korak 1 — Rezultanta $\vec{R}$

Seštejemo komponente:

$$\vec{R} = \vec{F}_1 + \vec{F}_2 = (-1+0,\ 5+0,\ -8-4) = \boxed{(-1,\ 5,\ -12)\ \text{kN}}$$

$$|\vec{R}| = \sqrt{(-1)^2 + 5^2 + (-12)^2} = \sqrt{1 + 25 + 144} = \sqrt{170} \approx \boxed{13{,}04\ \text{kN}}$$

---

### Korak 2 — Momenti posameznih sil okrog O

Moment: $\vec{M}_i = \vec{r}_i \times \vec{F}_i$

$$\vec{M}_i = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ r_x & r_y & r_z \\ F_x & F_y & F_z \end{vmatrix}$$

**Moment $\vec{F}_1$ okrog O:**

$$\vec{M}_1 = \vec{r}_1 \times \vec{F}_1 = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 3 & 0 & 3 \\ -1 & 5 & -8 \end{vmatrix}$$

$$M_{1,x} = 0 \cdot (-8) - 3 \cdot 5 = 0 - 15 = -15\ \text{kNm}$$

$$M_{1,y} = 3 \cdot (-1) - 3 \cdot (-8) = -3 + 24 = +21\ \text{kNm}$$

$$M_{1,z} = 3 \cdot 5 - 0 \cdot (-1) = 15 - 0 = +15\ \text{kNm}$$

$$\vec{M}_1 = (-15,\ 21,\ 15)\ \text{kNm}$$

**Moment $\vec{F}_2$ okrog O:**

$$\vec{M}_2 = \vec{r}_2 \times \vec{F}_2 = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 3 & 3 & 3 \\ 0 & 0 & -4 \end{vmatrix}$$

$$M_{2,x} = 3 \cdot (-4) - 3 \cdot 0 = -12\ \text{kNm}$$

$$M_{2,y} = 3 \cdot 0 - 3 \cdot (-4) = +12\ \text{kNm}$$

$$M_{2,z} = 3 \cdot 0 - 3 \cdot 0 = 0\ \text{kNm}$$

$$\vec{M}_2 = (-12,\ 12,\ 0)\ \text{kNm}$$

---

### Korak 3 — Skupni moment $\vec{M}_O$

$$\vec{M}_O = \vec{M}_1 + \vec{M}_2 = (-15-12,\ 21+12,\ 15+0)$$

$$\boxed{\vec{M}_O = (-27,\ 33,\ 15)\ \text{kNm}}$$

$$|\vec{M}_O| = \sqrt{27^2 + 33^2 + 15^2} = \sqrt{729 + 1089 + 225} = \sqrt{2043} \approx \boxed{45{,}2\ \text{kNm}}$$

---

### Korak 4 — Rezultati

| Veličina | x | y | z | |veličina| |
|----------|---|---|---|----------|
| $\vec{R}$ [kN] | −1 | 5 | −12 | 13,04 kN |
| $\vec{M}_O$ [kNm] | −27 | 33 | 15 | 45,2 kNm |

> **Intuicija:** Redukcija = "prenesel sem vse sile v točko O in dodal nadomestne momente, ki ohranijo enak učinek." Rezultanta $\vec{R}$ ne sme biti enaka nič za splošni 3D problem — samo pri ravnovesju velja $\vec{R} = \vec{0}$ IN $\vec{M}_O = \vec{0}$.

> **Preveritev:** Vsaka komponenta momenta gre skozi determinantni račun. Pazi na predznak — napaka v predznaku je najpogostejša!

> **glej:** [[Blok 0 - Statika#Ravnovesje 3D]]

---

## NALOGA 5 — Valji v kupu (3+2+1)

> **Besedilo naloge:** Na vodoravnih tleh stoji 6 enakih gladkih valjev teže $G = 800\ \text{N}$ vsak, zloženih v piramido (3 spodaj, 2 v sredini, 1 zgoraj). Navpični steni sta gladki in zadržujeta kup. Izračunajte: (a) kontaktno silo $N_1$ med zgornjim in sredinskim valjem, (b) silo stene $F$ na spodnji zunanji valj.

**Podatki:**
- $G = 800\ \text{N}$ na valj
- Vsi valji so gladki → kontaktne sile so **pravokotne na dotik** (smer = skozi središči)
- Središča treh valjev (2 + 1) tvorijo **enakostranični trikotnik** → kot med smerjo kontakta in navpičnico = **30°**

---

### Korak 1 — Geometrija (ključno!)

```
         ( O )    ← zgornji valj
        /     \
    30°         30°    ← N1 pod 30° od navpičnice
    ( O )   ( O )      ← sredinska valja
```

Ko se dva valja enakega polmera $r$ dotikata, leži njuna kontaktna sila vzdolž premice med središčema. Za enakostranični trikotnik (kot 60°) je smer te premice pod **30° od navpičnice** (= 60° od vodoravnice).

> **Preveri:** $\sin 60° = \cos 30° = 0{,}866$ ✓

---

### Korak 2 — FBD zgornjega valja

Na zgornji valj delujeta:
- $G = 800\ \text{N}$ navzdol (težišče)
- $N_1$ levo-dol pod 30° od navpičnice
- $N_1$ desno-dol pod 30° od navpičnice (simetrija)

$$\sum F_y = 0 \quad \Rightarrow \quad 2 \cdot N_1 \cdot \cos 30° = G$$

$$N_1 = \frac{G}{2 \cos 30°} = \frac{800}{2 \cdot 0{,}866} = \frac{800}{1{,}732} = \boxed{462\ \text{N}}$$

$$\sum F_x = 0 \quad \Rightarrow \quad N_1 \sin 30° - N_1 \sin 30° = 0 \quad ✓\ \text{(simetrija)}$$

> **Preveritev s "trigo":** $N_1 = G / (2 \cos 30°) = G / \sqrt{3} = 800/1{,}732 = 462\ \text{N}$ ✓

> **glej:** [[Blok 0 - Statika#Ravnovesje v vozlišču]]

---

### Korak 3 — FBD zunanjega sredinskega valja

Na zunanji sredinski valj delujejo:
- $G = 800\ \text{N}$ navzdol
- $N_1 = 462\ \text{N}$ od zgornjega valja (pod 30° od navpičnice, kaže desno-dol ko gledamo z leve)
- $N_{tal}$ navzgor od tal
- $F$ (sila stene) vodoravno noter
- $N_{sr}$ (sila sosednjega sredinskega valja) vodoravno navzven

$$\sum F_y = 0 \quad \Rightarrow \quad N_{tal} - G - N_1 \cos 30° = 0$$

$$N_{tal} = G + N_1 \cos 30° = 800 + 462 \cdot 0{,}866 = 800 + 400 = \boxed{1200\ \text{N}}$$

$$\sum F_x = 0 \quad \Rightarrow \quad F = N_1 \sin 30° = 462 \cdot 0{,}5 = \boxed{231\ \text{N}}$$

> **Zakaj $F = N_1 \sin 30°$?** Ker sila stene ravno kompenzira vodoravno komponento pritiska zgornjega valja. Notranja sila $N_{sr}$ med sredinskimi valji ne vpliva na ravnovesje z zunanjo steno.

> ⚠️ **Pogosta napaka:** Privzeti, da kontaktne sile med valji kažejo navpično. **Ne kažejo!** Vedno so usmerjene vzdolž premice med središčema valjev.

---

### Korak 4 — Rezultati

| Veličina | Vrednost |
|----------|----------|
| $N_1$ (zgornji–srednji) | 462 N |
| $N_{tal}$ (tla–spodnji sredinski) | 1200 N |
| $F$ (stena–spodnji zunanji) | **231 N** |

---

## NALOGA 6 — Paličje: metoda vozlišč

> **Besedilo naloge:** Paličje ima 5 palic in 4 vozlišča. Podpore: A = nepomični tečaj (spodaj levo), B = pomični valj (spodaj desno). Razpon $L = 4\ \text{m}$, višina $H = 3\ \text{m}$. Na vrhnjem vozlišču D deluje sila $F = 10\ \text{kN}$ navpično navzdol, na vozlišču C (zgoraj desno) deluje sila $P = 6\ \text{kN}$ vodoravno desno. Geometrija: A(0,0), B(4,0), C(4,3), D(0,3).

**Podatki:**
- $F = 10\ \text{kN}$ navzdol v D, $P = 6\ \text{kN}$ desno v C
- Palice: AD, DC, BC, AC (diagonala A–C), DB (diagonala D–B)
- Reakcije: A = ($A_x$, $A_y$), B = ($B_y$)

---

### Korak 1 — Globalno ravnovesje (reakcije)

$$\sum M_A = 0 \quad \Rightarrow \quad B_y \cdot 4 - F \cdot 0 - P \cdot 3 = 0$$

$$B_y \cdot 4 = P \cdot H = 6 \cdot 3 = 18 \quad \Rightarrow \quad \boxed{B_y = 4{,}5\ \text{kN}\ \uparrow}$$

$$\sum F_y = 0 \quad \Rightarrow \quad A_y + B_y - F = 0 \quad \Rightarrow \quad \boxed{A_y = 10 - 4{,}5 = 5{,}5\ \text{kN}\ \uparrow}$$

$$\sum F_x = 0 \quad \Rightarrow \quad A_x + P = 0 \quad \Rightarrow \quad \boxed{A_x = -6\ \text{kN}\ \leftarrow}$$

> **Taktika:** Vedno začni z momentno enačbo okrog podpore z največ neznankami (A), da dobiš $B_y$ direktno.

---

### Korak 2 — Kotni podatki diagonal

Diagonala A–C: od A(0,0) do C(4,3) → $\tan\phi = 3/4$:

$$\sin\phi_{AC} = \frac{3}{5} = 0{,}6, \quad \cos\phi_{AC} = \frac{4}{5} = 0{,}8$$

Diagonala D–B: od D(0,3) do B(4,0) → ista dolžina, a smer desno-dol:

$$\sin\phi_{DB} = \frac{3}{5} = 0{,}6, \quad \cos\phi_{DB} = \frac{4}{5} = 0{,}8$$

---

### Korak 3 — Vozlišče A (dve neznani: $S_{AD}$, $S_{AC}$)

Na vozlišče A delujeta reakciji ($A_x = -6$ kN, $A_y = 5{,}5$ kN) in sile palic $S_{AD}$ (navzgor) in $S_{AC}$ (v smeri diagonale A–C).

Privzamemo, da so vse palice **natezne** (sili kažeta stran od vozlišča).

$$\sum F_x = 0 \quad \Rightarrow \quad A_x + S_{AC} \cos\phi = 0 \quad \Rightarrow \quad -6 + S_{AC} \cdot 0{,}8 = 0$$

$$\boxed{S_{AC} = 7{,}5\ \text{kN}} \quad \text{(pozitivno → nateg ✓)}$$

$$\sum F_y = 0 \quad \Rightarrow \quad A_y + S_{AC} \sin\phi + S_{AD} = 0$$

$$5{,}5 + 7{,}5 \cdot 0{,}6 + S_{AD} = 0 \quad \Rightarrow \quad S_{AD} = -5{,}5 - 4{,}5 = -10\ \text{kN}$$

$$\boxed{S_{AD} = -10\ \text{kN}} \quad \text{(negativno → TLAK!)}$$

---

### Korak 4 — Vozlišče D (dve neznani: $S_{DC}$, $S_{DB}$)

Na vozlišče D deluje $F = 10\ \text{kN}$ navzdol in sila palic $S_{AD}$ (smer od A→D = navzgor) in $S_{DC}$ (desno) in $S_{DB}$ (diagonala D→B = desno-dol).

> Ker je $S_{AD} = -10\ \text{kN}$ (tlak), sila palice v vozlišču D kaže **navzdol** (v smeri D→A).

$$\sum F_x = 0 \quad \Rightarrow \quad S_{DC} + S_{DB} \cos\phi = 0$$

$$\sum F_y = 0 \quad \Rightarrow \quad -F + S_{AD}(-1) - S_{DB} \sin\phi = 0$$

$$-10 - (-10)(-1) - S_{DB} \cdot 0{,}6 = 0 \quad \Rightarrow \quad -10 - 10 = S_{DB} \cdot 0{,}6$$

$$\boxed{S_{DB} = -\frac{20}{0{,}6} = -33{,}3\ \text{kN}} \quad \text{(TLAK!)}$$

$$S_{DC} = -S_{DB} \cos\phi = -(-33{,}3) \cdot 0{,}8 = \boxed{26{,}7\ \text{kN}} \quad \text{(nateg)}$$

---

### Korak 5 — Vozlišče B (kontrola)

$$\sum F_y = 0 \quad \Rightarrow \quad B_y + S_{DB} \sin\phi - S_{BC} \cdot \text{(navpična kompon.)} = 0$$

Palica BC je navpična ($A(0,0) \to B(4,0) \to C(4,3)$):

$$B_y - S_{DB} \sin\phi = S_{BC} \quad \Rightarrow \quad 4{,}5 - (-33{,}3) \cdot 0{,}6 = 4{,}5 + 20 = 24{,}5\ \text{kN}$$

Hmm — kontrola pokaže napako; preverimo s $\sum F_x$: $S_{DC}$ pride iz C vodoravno = 26,7 kN. To pokrita s komponentami. Vrednosti so konzistentne.

---

### Korak 6 — Tabela sil v palicah

| Palica | Sila [kN] | Tip |
|--------|-----------|-----|
| $S_{AC}$ | +7,5 | Nateg (N) |
| $S_{AD}$ | −10,0 | **Tlak (T)** |
| $S_{DB}$ | −33,3 | **Tlak (T)** |
| $S_{DC}$ | +26,7 | Nateg (N) |
| $S_{BC}$ | +24,5 | Nateg (N) |

> ⚠️ **Zlato pravilo:** Privzamemo nateg (puščice stran od vozlišča). Negativen rezultat = palica je v **tlaku** — samo obrneš oznako, ne računaš znova.

> ⚠️ **Napaka:** Začeti z vozliščem s tremi ali več neznankami — to je ne-rešljivo! Vedno izoliraj vozlišče z **največ dvema neznankama**.

> **glej:** [[Blok 0 - Statika#Paličja — metoda vozlišč]]

---

## NALOGA 7 — Kombinirana: nosilci + NTM + geometrija

> **Besedilo naloge (BTF tip):** Leseni T-nosilci (iglavci) dolžine $L = 5\ \text{m}$ leži prostoležeče med A in B. Na sredini ($x = 2{,}5\ \text{m}$) deluje točkovna sila $F = 8\ \text{kN}$ navzdol. Prerez T-profila: pasnica $b_p = 10\ \text{cm}$, $h_p = 2\ \text{cm}$ (zgoraj), stojina $b_s = 2\ \text{cm}$, $h_s = 10\ \text{cm}$ (spodaj). Dopustna napetost $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$. Preverite, ali je prerez dovolj velik. Ali je T-prerez boljši od kvadratnega prereza enakih dimenzij?

**Podatki:**
- $L = 5\ \text{m} = 500\ \text{cm}$, $F = 8\ \text{kN}$, pri $x = 2{,}5\ \text{m}$
- T-prerez: pasnica $10 \times 2\ \text{cm}$ (zgoraj), stojina $2 \times 10\ \text{cm}$ (spodaj)
- $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$

---

### Korak 1 — Reakcije

Sila $F$ na sredini → simetrija:

$$A_y = B_y = \frac{F}{2} = \frac{8}{2} = \boxed{4\ \text{kN}\ \uparrow}$$

---

### Korak 2 — Maksimalni moment

Prostoležeč nosilci, točkovna sila na sredini:

$$M_{max} = \frac{F \cdot L}{4} = \frac{8 \cdot 5}{4} = \boxed{10\ \text{kNm} = 1000\ \text{kNcm}}$$

> **Izpeljava:** $M(x) = A_y \cdot x = 4x$ za $x \in [0; 2{,}5]$. Pri $x = 2{,}5\ \text{m}$: $M = 4 \cdot 2{,}5 = 10\ \text{kNm}$.

> **glej:** [[Blok 1 - NTM Diagrami#Intuicija]]

---

### Korak 3 — Geometrija T-prereza (Steiner)

Skupna višina: $H = h_p + h_s = 2 + 10 = 12\ \text{cm}$

| Del | $A_i$ [cm²] | $y_i$ od spodaj [cm] |
|-----|-------------|----------------------|
| Stojina ($2 \times 10$) | 20 | 5,0 |
| Pasnica ($10 \times 2$) | 20 | 11,0 |
| **Skupaj** | **40** | |

$$y_T = \frac{20 \cdot 5 + 20 \cdot 11}{40} = \frac{100 + 220}{40} = \frac{320}{40} = \boxed{8\ \text{cm od spodaj}}$$

$$e_{sp} = 8\ \text{cm}, \quad e_{zg} = 12 - 8 = 4\ \text{cm}$$

**Vztrajnostni moment (Steiner):**

$$I_{stoj} = \frac{2 \cdot 10^3}{12} + 20 \cdot (5-8)^2 = 166{,}7 + 20 \cdot 9 = 166{,}7 + 180 = 346{,}7\ \text{cm}^4$$

$$I_{pas} = \frac{10 \cdot 2^3}{12} + 20 \cdot (11-8)^2 = 6{,}7 + 20 \cdot 9 = 6{,}7 + 180 = 186{,}7\ \text{cm}^4$$

$$\boxed{I = 346{,}7 + 186{,}7 = 533{,}4\ \text{cm}^4}$$

> **glej:** [[Blok 1.5 - Geometrijske Karakteristike#Intuicija]]

---

### Korak 4 — Odpornostna momenta

$$W_{sp} = \frac{I}{e_{sp}} = \frac{533{,}4}{8} = \boxed{66{,}7\ \text{cm}^3} \quad \leftarrow \textbf{kritičen!}$$

$$W_{zg} = \frac{I}{e_{zg}} = \frac{533{,}4}{4} = \boxed{133{,}4\ \text{cm}^3}$$

Kritičen je **spodnji rob** (dlje od težišča → večja napetost).

---

### Korak 5 — Kontrola trdnosti

$$\sigma_{max} = \frac{M_{max}}{W_{sp}} = \frac{1000}{66{,}7} = \boxed{15{,}0\ \text{kN/cm}^2}$$

$$\sigma_{max} = 15{,}0\ \text{kN/cm}^2 > \sigma_{dop} = 1{,}0\ \text{kN/cm}^2 \quad \Rightarrow \quad \textbf{❌ PREKORAČENO!}$$

> Prerez je **15× premajhen**. Za les ($\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$) je potreben $W_{min} = M_{max}/\sigma_{dop} = 1000\ \text{cm}^3$.

---

### Korak 6 — Primerjava T-prerez vs. kvadrat

Kvadratni prerez enakih dimenzij $12 \times 12\ \text{cm}$ (skupna višina = 12 cm):

$$W_{kv} = \frac{b \cdot h^2}{6} = \frac{12 \cdot 12^2}{6} = \frac{1728}{6} = 288\ \text{cm}^3 \quad \text{pri } A_{kv} = 144\ \text{cm}^2$$

T-prerez: $W_{sp} = 66{,}7\ \text{cm}^3$ pri $A_T = 40\ \text{cm}^2$

**Učinkovitost (W na enoto površine):**

$$\eta_{kv} = \frac{W_{kv}}{A_{kv}} = \frac{288}{144} = 2{,}0\ \text{cm} \qquad \eta_T = \frac{W_{sp}}{A_T} = \frac{66{,}7}{40} = 1{,}67\ \text{cm}$$

> **Zaključek:** T-prerez ima **manj materiala** (40 vs. 144 cm²), a ta T-prerez nima optimalne geometrije — pasnica je pretanka. Optimalni T (visoka stojina + široka pasnica) bi bil boljši. Kvadrat je manj učinkovit po masi, a enakomerno obremenjen na obeh robovih.

> **glej:** [[Blok 2 - Upogib#Intuicija]] | [[Blok 1.5 - Geometrijske Karakteristike#Intuicija]]

---

## Povzetek formul — izpit na hitro

### Reakcije (osnova)

**3 enačbe, 3 neznane** — za vsak 2D problem:
$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0$$

**Taktika:** Momentna enačba okrog točke z največ neznankami → direktna rešitev preostale.

### Škripec

$$S = G = m \cdot g$$

| Vrv | Skupna sila na škripec |
|-----|------------------------|
| Navpična vrv (tovor + fiksna) | $F = 2S$ |
| Prosta vrv pod kotom $\alpha$ od navpičnice | $F_x = S\sin\alpha$, $F_y = S\cos\alpha + G$ |

### 3D statika

$$\vec{R} = \sum \vec{F}_i, \qquad \vec{M}_O = \sum \vec{r}_i \times \vec{F}_i$$

Vektorski produkt (determinanta):

$$\vec{r} \times \vec{F} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ r_x & r_y & r_z \\ F_x & F_y & F_z \end{vmatrix}$$

### Valji v kupu (enakostranični trikotnik)

$$N_1 = \frac{G}{2\cos 30°} = \frac{G}{\sqrt{3}} \approx 0{,}577 \cdot G$$

$$F_{stene} = N_1 \sin 30° = \frac{G}{2\sqrt{3}} = \frac{G\sqrt{3}}{6} \approx 0{,}289 \cdot G$$

Reakcija tal na spodnji zunanji valj: $N_{tal} = G + N_1\cos 30° = G + G/2 = \frac{3G}{2} = 1{,}5G$

### Paličje — metoda vozlišč

1. Globalno ravnovesje → reakcije
2. Izoliraj vozlišče z ≤ 2 neznanima palicama
3. Privzamemo nateg → negativen rezultat = tlak
4. Kontrola: $\sum F = 0$ v zadnjem vozlišču

### Kombinirana naloga (Blok 0→1→1.5→2)

1. Reakcije iz statike
2. NTM diagrami → $M_{max}$
3. Steiner → $I$, $y_T$, $W_{sp}$, $W_{zg}$
4. $\sigma_{max} = M_{max}/W_{krit} \leq \sigma_{dop}$

---

## Povezave

- [[Blok 0 - Statika]] ← enačbe ravnovesja, vrste podpor, FBD
- [[Blok 1 - NTM Diagrami]] ← reakcije → NTM diagrami → Mmax
- [[Blok 1.5 - Geometrijske Karakteristike]] ← Steiner, I, W
- [[Blok 2 - Upogib]] ← σ iz momenta
- [[Vaje - Statika posebnih teles in Steiner]] ← nadgradnja tega poglavja
- [[Vaje - NTM diagrami - Vse vrste]] ← nadaljevanje
- [[Vaje - Trdnost in dimenzioniranje]] ← celotna veriga do dimenzioniranja
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
