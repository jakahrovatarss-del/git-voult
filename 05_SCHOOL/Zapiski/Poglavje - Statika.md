---
tags: [mehanika, statika, poglavje, reakcije, paličje, trenje, vrvi, škripec, valji, steiner, 3D, izpit]
predmet: Mehanika
datum: 2026-06-17
---
```table-of-contents
```

# Poglavje — 1. SKLOP: Statika

## Namen

Celovit zapisek za **1. SKLOP: Statika** — vse tipe nalog z rešitvami, razdeljenimi po kategorijah. Že rešene naloge so zlinkane, nove so rešene inline.

> **Teorija:** [[Blok 0 - Statika]] | **Geometrija:** [[Blok 1.5 - Geometrijske Karakteristike]]

---

## Pregled tipov nalog

| # | Tip naloge | Ključna metoda | Naloge |
|---|-----------|----------------|--------|
| 1 | Redukcija sil 2D | ΣMA=0 direktno | N1–N4, N6 |
| 2 | Redukcija sil 3D | $\vec{r} \times \vec{F}$ | N5, N7 |
| 3 | Škripci in L-nosilci | S = G, ročice | N8, N9 |
| 4 | Valji v kupu | geometrija 60° | N10 |
| 5 | Vrvi z obtežbo | horizontalna komp. | N11 |
| 6 | Paličja | vozlišča/prerez | N12 |
| 7 | Geometrija prerezov | Steiner | N13 |
| 8 | Gerberjevi nosilci | členek → razstavi | N14 |
| 9 | Trenje | Coulomb | N15 |
| 10 | Kombinirane | veriga blokov | N16, N17 |

---

## 1. REDUKCIJA SIL 2D — Reakcije na nosilci

### N1 — Prostoležeč nosilci z q in F
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 3 — Prostoležeč nosilci z q in F]]

$$L=6\ \text{m},\ q=2\ \text{kN/m},\ F=12\ \text{kN pri }x_C=4\ \text{m} \quad \Rightarrow \quad A_y=10\ \text{kN},\ B_y=14\ \text{kN}$$

---

### N2 — Nagnjena sila pod kotom
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 4 — Nagnjena sila pod kotom]]

$$L=6\ \text{m},\ F=15\ \text{kN},\ \alpha=40°\text{ od nav.},\ x_C=4\ \text{m} \quad \Rightarrow \quad B_y=7{,}66\ \text{kN},\ A_y=3{,}83\ \text{kN},\ A_x=9{,}64\ \text{kN}$$

---

### N3 — Nosilci z momentno obremenitvijo (dvojica sil)

> **Besedilo (Jesenko, Nosilci):** Konzolno vpet nosilci dolžine $L = 4\ \text{m}$ je obremenjen z enakomerno obtežbo $q = 2{,}8\ \text{kN/m}$ in točkovno silo $F = 9\ \text{kN}$ pri $x_F = 2{,}5\ \text{m}$ od vpetja. Na koncu deluje par sil z momentom $M_0 = 5\ \text{kNm}$ (v smeri urinega kazalca). Izračunajte reakcije v vpetju A.

**Podatki:** $q=2{,}8\ \text{kN/m}$, $F=9\ \text{kN}$, $x_F=2{,}5\ \text{m}$, $M_0=5\ \text{kNm}$, $L=4\ \text{m}$

#### Korak 1 — Rezultanta q

$$Q = q \cdot L = 2{,}8 \cdot 4 = 11{,}2\ \text{kN} \qquad x_Q = L/2 = 2\ \text{m od vpetja}$$

#### Korak 2 — ΣFx = 0

Nobenih vodoravnih sil → $\boxed{A_x = 0}$

#### Korak 3 — ΣFy = 0

$$A_y = Q + F = 11{,}2 + 9 = \boxed{20{,}2\ \text{kN}\ \uparrow}$$

#### Korak 4 — ΣMA = 0

$$M_A = Q \cdot x_Q + F \cdot x_F + M_0 = 11{,}2 \cdot 2 + 9 \cdot 2{,}5 + 5 = 22{,}4 + 22{,}5 + 5 = \boxed{49{,}9\ \text{kNm}}$$

> ⚠️ **Moment pare sil (dvojica):** $M_0$ prispeva direktno k momentu vpetja, neodvisno od mesta prijema — par sil nima rezultante, le moment!

> **gl.:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

## 2. REDUKCIJA SISTEMA SIL 3D

### N4 — 3D statika (a = 3 m, dve sili)
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 5 — 3D statika redukcija sistema sil]]

$$\vec{R}=(-1,5,-12)\ \text{kN}, \qquad \vec{M}_O=(-27,33,15)\ \text{kNm}$$

---

### N5 — Prostorski sistem sil — Jesenko kvader (a = 2, b = 1,5, c = 2,5 m)

> **Besedilo (Jesenko, Ravnovesje 4):** Na kvader $a=2\ \text{m}$, $b=1{,}5\ \text{m}$, $c=2{,}5\ \text{m}$ delujeta sili: $\vec{F}_1=10\ \text{kN}$ v točki $F(a,0,c)$, kaže proti $B(a,b,0)$; $\vec{F}_2=5\ \text{kN}$ v točki $B(a,b,0)$, navpično navzdol. Reducirajte sistem v izvorišče $O(0,0,0)$.

**Koordinate:**

| Točka | x | y | z |
|-------|---|---|---|
| O | 0 | 0 | 0 |
| B | 2 | 1,5 | 0 |
| F | 2 | 0 | 2,5 |

#### Korak 1 — Enotski vektor $\vec{F}_1$ (od F proti B)

$$\vec{FB} = B - F = (2-2,\ 1{,}5-0,\ 0-2{,}5) = (0,\ 1{,}5,\ -2{,}5)$$

$$|\vec{FB}| = \sqrt{0 + 2{,}25 + 6{,}25} = \sqrt{8{,}5} \approx 2{,}915\ \text{m}$$

$$\hat{u}_1 = (0,\ 0{,}515,\ -0{,}858)$$

$$\vec{F}_1 = 10 \cdot (0,\ 0{,}515,\ -0{,}858) = (0,\ 5{,}15,\ -8{,}58)\ \text{kN}$$

#### Korak 2 — $\vec{F}_2$ (navpično navzdol v B)

$$\vec{F}_2 = (0,\ 0,\ -5)\ \text{kN}$$

#### Korak 3 — Rezultanta

$$\vec{R} = \vec{F}_1 + \vec{F}_2 = (0,\ 5{,}15,\ -13{,}58)\ \text{kN}, \quad |\vec{R}| = \sqrt{0 + 26{,}5 + 184{,}4} \approx \boxed{14{,}5\ \text{kN}}$$

#### Korak 4 — Momenti v O

**$\vec{M}_1$** ($\vec{r}_F = (2, 0, 2{,}5)$, $\vec{F}_1 = (0, 5{,}15, -8{,}58)$):

$$\vec{M}_1 = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&0&2{,}5\\0&5{,}15&-8{,}58\end{vmatrix} = \vec{i}(0\cdot(-8{,}58)-2{,}5\cdot5{,}15)-\vec{j}(2\cdot(-8{,}58)-2{,}5\cdot0)+\vec{k}(2\cdot5{,}15-0)$$

$$= (-12{,}875,\ +17{,}16,\ +10{,}3)\ \text{kNm}$$

**$\vec{M}_2$** ($\vec{r}_B = (2, 1{,}5, 0)$, $\vec{F}_2 = (0, 0, -5)$):

$$\vec{M}_2 = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&1{,}5&0\\0&0&-5\end{vmatrix} = (-7{,}5,\ +10,\ 0)\ \text{kNm}$$

#### Korak 5 — Skupni moment

$$\vec{M}_O = \vec{M}_1 + \vec{M}_2 = \boxed{(-20{,}4,\ 27{,}2,\ 10{,}3)\ \text{kNm}}$$

> ⚠️ **Napaka:** Ko pišeš $\vec{r} \times \vec{F}$, je $\vec{r}$ vektor od točke **redukcije** (O) do točke **prijema sile** (ne obratno)!

---

### N6 — Prostorski sistem — Drog z znakom

> **Besedilo (Jesenko, Ravnovesje 2):** Drog zanemarljive teže je navpično vpet v podlago (vpetje v O). Nanj je togo pritrjen pravokoten znak z maso $m = 20\ \text{kg}$. Veter povzroča silo $F_{veter} = 100\ \text{N}$ pravokotno na znak. Konzolna dolžina drog $h = 3\ \text{m}$, središče znaka na višini $h_s = 2\ \text{m}$, znak dimenzij $1{,}2 \times 0{,}8\ \text{m}$.

#### Korak 1 — Teža znaka

$$G = 20 \cdot 9{,}81 = 196{,}2\ \text{N} \downarrow \qquad \text{(deluje v težišču znaka)}$$

#### Korak 2 — Sile in momenti v vpetju O (3D)

$$\sum F_x = 0 \Rightarrow O_x = -100\ \text{N}$$

$$\sum F_y = 0 \Rightarrow O_y = 0$$

$$\sum F_z = 0 \Rightarrow O_z = 196{,}2\ \text{N}\ \uparrow$$

Momenti okrog O (veter v x-smeri, deluje na višini $h_s = 2\ \text{m}$):

$$M_{Oy} = F_{veter} \cdot h_s = 100 \cdot 2 = \boxed{200\ \text{Nm}} \quad \text{(upogibni)}$$

$$M_{Oz} = G \cdot \text{odmik} \approx 0 \quad \text{(znak simetričen na drog)}$$

> **Pouk:** Pri drogu v prostoru vedno preverite vse 3 momentne enačbe — pogosto ena od njih da torzijski moment!

---

## 3. ŠKRIPCI IN L-NOSILCI

### N7 — Škripec, navpična vrv
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 1 — Škripec navpična vrv]]

$$m=20\ \text{kg},\ a=2\ \text{m},\ H=4\ \text{m} \quad \Rightarrow \quad B_x=0,\ B_y=0{,}4\ \text{kN},\ M_B=0{,}8\ \text{kNm}$$

---

### N8 — Škripec, nagnjena vrv
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 2 — Škripec nagnjena vrv]]

$$m=50\ \text{kg},\ \alpha=30°,\ a=1{,}5\ \text{m} \quad \Rightarrow \quad B_x=-0{,}25\ \text{kN},\ B_y=0{,}933\ \text{kN},\ M_B=2{,}4\ \text{kNm}$$

---

## 4. VALJI V KUPU

### N9 — Valji v kupu (6 kosov, piramida 3-2-1)
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 6 — Valji v kupu (3+2+1)]]

$$G=800\ \text{N} \quad \Rightarrow \quad N_1=462\ \text{N},\ N_{tal}=1200\ \text{N},\ F_{stene}=231\ \text{N}$$

---

## 5. VRVI Z OBTEŽBO

### N10 — Vrv z dvema točkovnima bremenitnama

> **Besedilo:** Vodoravna vrv je vpeta v točkah $A$ in $B$ na isti višini, razdalja $L_{AB} = 6\ \text{m}$. V točki $C$ ($x_C = 2\ \text{m}$ od A) visi breme $F_C = 4\ \text{kN}$, v točki $D$ ($x_D = 4\ \text{m}$ od A) pa $F_D = 6\ \text{kN}$. Vrv se v $C$ odkloni za $h_C = 1{,}2\ \text{m}$ navzdol. Poiščite horizontalno komponento natega in reakcije v $A$ in $B$.

#### Korak 1 — Horizontalna komponenta $H$ (iz ravnovesja v C)

V točki C velja ravnovesje momentov za levi del (A do C):

$$H \cdot h_C = A_y \cdot x_C$$

Najprej $A_y$ iz globalnega ravnovesja:

$$\sum M_B = 0: \quad A_y \cdot 6 = F_C \cdot (6-2) + F_D \cdot (6-4) = 16 + 12 = 28$$

$$\boxed{A_y = 4{,}667\ \text{kN}}$$

$$B_y = F_C + F_D - A_y = 10 - 4{,}667 = \boxed{5{,}333\ \text{kN}}$$

#### Korak 2 — H iz ravnovesja levega dela A-C

$$H \cdot h_C = A_y \cdot x_C \quad \Rightarrow \quad H = \frac{4{,}667 \cdot 2}{1{,}2} = \boxed{7{,}78\ \text{kN}}$$

#### Korak 3 — Koti in nategi

Kot odseka AC od vodoravnice:

$$\tan\alpha_{AC} = h_C / x_C = 1{,}2/2 = 0{,}6 \quad \Rightarrow \quad \alpha_{AC} = 30{,}96°$$

Nateg v odseku AC:

$$T_{AC} = \frac{H}{\cos\alpha_{AC}} = \frac{7{,}78}{\cos 30{,}96°} = \boxed{9{,}08\ \text{kN}}$$

Višina v D: iz ravnovesja C-D dela → $h_D = h_C + \tan(\alpha_{CD}) \cdot (x_D - x_C)$

Ravnovesje v C (smer y):

$$T_{AC}\sin\alpha_{AC} + T_{CD}\sin\alpha_{CD} = F_C$$

$$7{,}78 \cdot \tan\alpha_{AC} = 4{,}667 \Rightarrow \tan\alpha_{AC}=0{,}6\ ✓$$

Kot odseka CD:

$$\tan\alpha_{CD} = (B_y - F_D)/H \text{ (od B) ... alternativno:}$$

$$\tan\alpha_{CD} = (B_y)/H\text{(od B)} = 5{,}333/7{,}78 \Rightarrow \alpha_{CD}\ \text{se izračuna geometrično}$$

Višina $h_D$ (odmik od AB linije):

$$h_D = h_C + (x_D - x_C) \cdot \tan\alpha_{CD,\downarrow}$$

Iz ravnovesja med C in D (prečna sila pod C = $A_y - F_C = 0{,}667\ \text{kN}\ \downarrow$):

$$\tan\alpha_{CD} = 0{,}667/7{,}78 = 0{,}0857 \quad \Rightarrow \quad h_D = 1{,}2 + 2 \cdot 0{,}0857 = \boxed{1{,}371\ \text{m}}$$

#### Korak 4 — Reakcije

$$\vec{R}_A = (-H, A_y) = (-7{,}78,\ +4{,}667)\ \text{kN}, \quad |\vec{R}_A| = \sqrt{60{,}5+21{,}8} = \boxed{9{,}07\ \text{kN}}$$

$$\vec{R}_B = (+H, B_y) = (+7{,}78,\ +5{,}333)\ \text{kN}, \quad |\vec{R}_B| = \boxed{9{,}37\ \text{kN}}$$

> ⚠️ **Ključ:** $H$ je **povsod enaka** v horizontalni vrvi brez trenja — ne glede na odsek! Vsaka točka obtežbe razbije vrv na odseke z različnim kotom, a enako $H$.

> **gl.:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

### N11 — Vrv pod lastno težo (viseča vrv / katenoida)

> **Besedilo:** Jeklena vrv linearne gostote $q = 0{,}08\ \text{kN/m}$ je obešena med točkama $A$ in $B$ na isti višini, horizontalna razdalja $a = 10\ \text{m}$. Najnižja točka vrvi je $f = 0{,}5\ \text{m}$ pod $A$ (ugrez). Izračunajte horizontalno komponento natega $H$ in maksimalni nateg $T_{max}$ (v podporah).

#### Korak 1 — Horizontalna komponenta

Za katenoido pri majhnem ugrezu ($f \ll a$) velja parabolična aproksimacija:

$$H \approx \frac{q \cdot a^2}{8 \cdot f} = \frac{0{,}08 \cdot 100}{8 \cdot 0{,}5} = \frac{8}{4} = \boxed{2{,}0\ \text{kN}}$$

#### Korak 2 — Navpična reakcija (simetrija → $V_A = V_B$)

$$V = q \cdot \frac{a}{2} = 0{,}08 \cdot 5 = \boxed{0{,}4\ \text{kN}}$$

#### Korak 3 — Maksimalni nateg (v podporah)

$$T_{max} = \sqrt{H^2 + V^2} = \sqrt{4 + 0{,}16} = \sqrt{4{,}16} = \boxed{2{,}04\ \text{kN}}$$

> **Ugrez formule:** $f = qL^2/(8H)$ ↔ $H = qL^2/(8f)$. Velja za $f/L < 0{,}1$ (parabolična aproks. OK).

---

## 6. PALIČJA

### N12 — Paličje metoda vozlišč (5 palic)
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 8 — Paličje metoda vozlišč]]

$$F=10\ \text{kN}\downarrow\ \text{v D},\ P=6\ \text{kN}\rightarrow\ \text{v C} \quad \Rightarrow \quad S_{AC}=+7{,}5,\ S_{AD}=-10,\ S_{DB}=-33{,}3,\ S_{DC}=+26{,}7\ \text{kN}$$

---

### N13 — Paličje metoda prereza (Ritterjeva)

> **Besedilo:** Simetrično ravninsko paličje: razpon $L=8\ \text{m}$, višina $H=2\ \text{m}$, 4 polja (vozlišča: $A(0,0),C(2,0),E(4,0),G(6,0),B(8,0)$ na pasnici; $D(2,2),F(4,2),H(6,2)$ na zgornjem pasu). Podpora: $A$ = tečaj, $B$ = valj. Bremeni: $F=15\ \text{kN}\downarrow$ v $F$ in $F=15\ \text{kN}\downarrow$ v $H$ (simetrijsko). Izračunajte sile v palicah $EF$, $EH$ in $GH$ z metodo prereza.

#### Korak 1 — Globalno ravnovesje (simetrija)

$$A_y = B_y = \frac{2 \cdot 15}{2} = \boxed{15\ \text{kN}}, \quad A_x = 0$$

#### Korak 2 — Metoda prereza: prereži EF, EH, GH

Obravnavamo **levi del** (od A do prereza med E in F/H).

$$\sum M_F = 0 \quad \text{(izniči } S_{EH} \text{ in } S_{EF}\text{)}$$

Sile na levem delu: $A_y=15\ \uparrow$ v A, breme 0 levo od F (breme $F$ je točno v F = na prerezu).

$$S_{GH} \cdot H = A_y \cdot 4 = 60 \quad \Rightarrow \quad \boxed{S_{GH} = +30\ \text{kN}\ \text{(N)}}$$

$$\sum M_H = 0: \quad S_{EF} \cdot H = -A_y \cdot 6 = -90 \quad \Rightarrow \quad \boxed{S_{EF} = -45\ \text{kN}\ \text{(T)}}$$

$$\sum F_y = 0: \quad A_y - S_{EH}\sin\theta = 0, \quad \tan\theta = H/2 = 1 \Rightarrow \theta=45°$$

$$S_{EH} = \frac{15}{\sin 45°} = \boxed{+21{,}2\ \text{kN}\ \text{(N)}}$$

> ⚠️ **Trik metode prereza:** Vedno reži točno 3 palice. Momentna enačba okrog presečišča 2 neznanih direktno da 3. palico.

> **gl.:** [[Blok 0 - Statika#Paličje — metoda prereza]]

---

## 7. GEOMETRIJA PREREZOV — STEINER

### N14 — Steiner za T-prerez
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 7 — Steiner za T-prerez]]

$$H=14\ \text{cm},\ \text{pasnica}\ 12\times2,\ \text{stojina}\ 2\times12 \quad \Rightarrow \quad y_T=9{,}5\ \text{cm},\ I=884\ \text{cm}^4,\ W_{sp}=93{,}1\ \text{cm}^3$$

---

### N15 — Steiner za U-prerez (odprt profil)

> **Besedilo:** U-prerez (korito): pasnica spodaj $b=10\ \text{cm}$, $h_p=2\ \text{cm}$; dve stojini $b_s=2\ \text{cm}$, $h_s=8\ \text{cm}$ (vsaka). Skupna višina $H=10\ \text{cm}$. Izračunajte $y_T$, $I$, $W_{sp}$, $W_{zg}$.

#### Korak 1 — Tabela delov

| Del | $b$ [cm] | $h$ [cm] | $A_i$ [cm²] | $y_i$ od spodaj [cm] | $A_i y_i$ |
|-----|----------|----------|-------------|----------------------|-----------|
| Spodnja pasnica | 10 | 2 | 20 | 1,0 | 20 |
| Leva stojina | 2 | 8 | 16 | 6,0 | 96 |
| Desna stojina | 2 | 8 | 16 | 6,0 | 96 |
| **Skupaj** | | | **52** | | **212** |

$$y_T = 212/52 = \boxed{4{,}077\ \text{cm}}, \quad e_{sp}=4{,}077\ \text{cm},\quad e_{zg}=5{,}923\ \text{cm}$$

#### Korak 2 — Steiner za vsak del

**Spodnja pasnica** ($d_1 = 1{,}0 - 4{,}077 = -3{,}077$):

$$I_1 = \frac{10\cdot2^3}{12}+20\cdot3{,}077^2 = 6{,}67+189{,}4 = 196{,}0\ \text{cm}^4$$

**Stojini (2×)** ($d_2 = 6{,}0 - 4{,}077 = 1{,}923$):

$$I_{stoj} = 2\left(\frac{2\cdot8^3}{12}+16\cdot1{,}923^2\right) = 2(85{,}3+59{,}2) = 289{,}0\ \text{cm}^4$$

$$\boxed{I = 196{,}0+289{,}0 = 485\ \text{cm}^4}$$

#### Korak 3 — Odpornostna momenta

$$W_{sp} = 485/4{,}077 = \boxed{119{,}0\ \text{cm}^3}$$

$$W_{zg} = 485/5{,}923 = \boxed{81{,}9\ \text{cm}^3} \quad \leftarrow \textbf{KRITIČEN! (manjši)}$$

> ⚠️ **Za U-prerez:** Kritičen je **zgornji** rob (farther from centroid) — prerez ni simetričen!

---

## 8. GERBERJEVI NOSILCI (sestavljena konstrukcija)

### N16 — Gerber z notranjim členkom

> **Besedilo:** Prostoležeč nosilci $A$–$B$ dolžine $L=10\ \text{m}$. Znotraj je notranji členek v točki $C$ pri $x_C=4\ \text{m}$ od $A$. Podpora: $A$ = tečaj, $B$ = valj. Enakomerna obtežba $q=3\ \text{kN/m}$ na delu $A$–$C$ ($0$ do $4\ \text{m}$), točkovna sila $F=20\ \text{kN}\downarrow$ v točki $D$ pri $x_D=7\ \text{m}$ od $A$.

**Shema:**
```
A────────C────────D────B
0   4   4   7   7  10
tečaj     členek      valj
```

#### Korak 1 — Razstavi v členku C

Notranji členek C prenaša le prečno in osno silo — **ne prenese momenta**. Razstavimo na:
- **Levi del** A–C: ima $A_y$ in $C_y$ (reakcija memberka)
- **Desni del** C–B: ima $C_y$, $B_y$ in $F$

#### Korak 2 — Desni del C–B (lažji!)

Na desnem delu delujeta: $C_y\downarrow$ v C, $F=20\ \text{kN}\downarrow$ v D, $B_y\uparrow$ v B.

$$\sum M_C = 0 \text{ (za desni del)}: \quad B_y \cdot (10-4) = F \cdot (7-4) = 20 \cdot 3 = 60$$

$$\boxed{B_y = 10\ \text{kN}\ \uparrow}$$

$$C_y = F - B_y = 20 - 10 = \boxed{10\ \text{kN}\ \downarrow} \quad \text{(sila na desni del)}$$

#### Korak 3 — Levi del A–C

Na levem delu: $A_y\uparrow$, $q=3\ \text{kN/m}$ na $x\in[0,4]$ → $Q=12\ \text{kN}$ v $x=2\ \text{m}$, $C_y=10\ \text{kN}\downarrow$ v $x=4\ \text{m}$.

$$\sum M_A = 0: \quad Q \cdot 2 + C_y \cdot 4 = A_y \cdot 0 + 0$$

$$A_y = \frac{Q \cdot 2 + C_y \cdot 4}{4} = \frac{12\cdot2+10\cdot4}{4} = \frac{24+40}{4} = \boxed{16\ \text{kN}\ \uparrow}$$

#### Korak 4 — Kontrola (ΣFy = 0 za celoten sistem)

$$A_y + B_y = Q + F \quad \Rightarrow \quad 16+10 = 12+20 = 26\ ✓$$

#### Korak 5 — Reakciji A

$$\boxed{A_x = 0,\quad A_y = 16\ \text{kN},\quad B_y = 10\ \text{kN}}$$

> ⚠️ **Metoda:** Vedno začni pri **konzolnem delu** (del z manj neznankami — tipično desni, "visečič" del). Iz njega dobiš $C_y$, ki ga prenesete kot znano silo na levi del.

> **gl.:** [[Blok 0 - Statika#Vrste podpor in reakcije]]

---

## 9. STATIKA S TRENJEM

### N17 — Klanec s trenjem (klanec pod kotom)

> **Besedilo:** Kla z maso $m=80\ \text{kg}$ leži na klancu pod kotom $\alpha=25°$. Koeficient statičnega trenja med klado in klancem je $\mu_s=0{,}35$. (a) Ali kla zdrsne sama od sebe? (b) Kolikšna sila $F$ (vzporedno s klancem, navzgor) je potrebna, da kla ravno ne zdrsne navzdol?

#### Korak 1 — FBD klada na klancu

Sila teže: $G = 80\cdot10 = 800\ \text{N}$

Komponenti vzdolž osi klanca:
- Normalna: $N = G\cos\alpha = 800\cdot\cos25° = 800\cdot0{,}906 = \boxed{725\ \text{N}}$
- Tangencialna (zdrs navzdol): $F_t = G\sin\alpha = 800\cdot\sin25° = 800\cdot0{,}423 = \boxed{338\ \text{N}}$

#### Korak 2 — Kontrola zdrsavanja

$$F_{tr,max} = \mu_s \cdot N = 0{,}35 \cdot 725 = \boxed{254\ \text{N}}$$

$$F_t = 338\ \text{N} > F_{tr,max} = 254\ \text{N} \quad \Rightarrow \quad \textbf{❌ KLANEC ZDRSNE!}$$

> Kla ne more mirovati sama — kotni pogoj: $\tan\alpha = \tan25° = 0{,}466 > \mu_s = 0{,}35$ ✓

#### Korak 3 — Potrebna sila F (da prepreči zdrs)

$$\sum F_{vzdolž} = 0: \quad F + F_{tr} - G\sin\alpha = 0$$

Ko kla ravno miruje → trenje je na maksimumu in kaže **navzgor** (upira se zdrsu):

$$F = G\sin\alpha - \mu_s \cdot N = 338 - 254 = \boxed{84\ \text{N}}$$

> Torej vsaj $F = 84\ \text{N}$ navzgor po klancu prepreči zdrs.

> **gl.:** [[Blok 0 - Statika#Trenje — Coulombov zakon]]

---

### N18 — Trenje na valju (jermenski prenos)

> **Besedilo:** Kolut polmera $R=0{,}5\ \text{m}$ je vpet v tečaj v središču. Nanj je ovit trak (jermen). Na eni strani traku visi breme $F_1=200\ \text{N}$, na drugi strani sila $F_2$. Koeficient trenja med trakom in kolutom $\mu=0{,}25$, kot ovoja $\theta=180°=\pi\ \text{rad}$. Kolikšna mora biti $F_2$, da kolut ostane v mirovanju?

#### Korak 1 — Eulerjev zakon traku

$$\frac{F_{napeta}}{F_{mlahava}} = e^{\mu\theta} = e^{0{,}25\cdot\pi} = e^{0{,}785} = \boxed{2{,}19}$$

#### Korak 2 — Pogoj ravnovesja

Da kolut miruje, je dovolj, da $F_2$ leži v mejah:

$$\frac{F_1}{e^{\mu\theta}} \leq F_2 \leq F_1 \cdot e^{\mu\theta}$$

$$\frac{200}{2{,}19} \leq F_2 \leq 200 \cdot 2{,}19 \quad \Rightarrow \quad \boxed{91{,}3\ \text{N} \leq F_2 \leq 438\ \text{N}}$$

> **Fizika:** Trenje med jermenom in kolutom je eksponentno odvisno od kota ovoja $\theta$ — zato debeli trakovi za male $\mu$ zavijajo v polkrog ali celo večkrat!

---

## 10. KOMBINIRANE NALOGE

### N19 — Nosilci + NTM + Steiner (T-prerez les)
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 9 — Kombinirana nosilci + NTM + Steiner]]

$$L=5\ \text{m},\ F=8\ \text{kN} \quad \Rightarrow \quad M_{max}=10\ \text{kNm},\ W_{sp}=66{,}7\ \text{cm}^3,\ \sigma_{max}=15{,}0\ \text{kN/cm}^2 \gg \sigma_{dop}\ ❌$$

---

### N20 — Nagnjena sila + Steiner + Uklon (konzola)
> Rešena naloga: [[Vaje - Statika - Vse vrste#NALOGA 10 — Kombinirana nagnjena sila + Steiner + uklon]]

$$b=6,\ h=10\ \text{cm},\ L=3\ \text{m},\ \alpha=25°,\ F=8\ \text{kN} \quad \Rightarrow \quad \sigma_{max}=10{,}26\ \text{kN/cm}^2\ ❌,\ \nu=0{,}68\ ❌$$

---

## Povzetek izpitnih formul

### Reakcije (vedno najprej)

$$\sum F_x=0,\quad \sum F_y=0,\quad \sum M_A=0$$

> Momentna enačba okrog točke z največ neznankami = direktna rešitev!

### 3D redukcija

$$\vec{R}=\sum\vec{F}_i, \qquad \vec{M}_O=\sum\vec{r}_i\times\vec{F}_i=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\end{vmatrix}$$

### Vrvi

$$H = \frac{qL^2}{8f}\ \text{(viseča)}, \qquad T_{max}=\sqrt{H^2+V^2}$$

### Trenje

$$F_{tr} \leq \mu_s N, \qquad \tan\alpha \leq \mu_s\ \text{(klanec)}, \qquad \frac{F_1}{F_2}=e^{\mu\theta}\ \text{(jermen)}$$

### Gerber nosilci

1. Razstavi v členku
2. Začni z "visi" delom (manj neznank) → $C_y$
3. Prenesi na levi del

### Steiner

$$y_T=\frac{\sum A_i y_i}{\sum A_i}, \quad I=\sum\left(\frac{bh^3}{12}+A_i d_i^2\right), \quad W_{krit}=\frac{I}{e_{max}}$$

---

## Hierarhija tipov po zahtevnosti

```
OSNOVNE:
  ├── 2D reakcije (prostoležeč, konzola)
  ├── Škripec (S = G)
  └── Valji v kupu (geometrija 60°)

SREDNJE:
  ├── 3D redukcija (vektorski produkt)
  ├── Vrv z obtežbo (H = const)
  ├── Paličje (vozlišča → prerez)
  └── Steiner (tabela + odmiki)

NAPREDNE:
  ├── Gerber nosilci (razstavi v členku)
  ├── Trenje na jermenu (Euler eksponent)
  └── Kombinirane (reakcije → NTM → σ → uklon)
```

---

## Povezave

- [[Blok 0 - Statika]] ← teorija, FBD, vrste podpor
- [[Blok 1.5 - Geometrijske Karakteristike]] ← Steiner, I, W
- [[Vaje - Statika - Vse vrste]] ← vse rešene naloge
- [[Blok 1 - NTM Diagrami]] ← naslednji korak po reakcijah
- [[Poglavje - NTM Diagrami]] ← naslednje poglavje
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
