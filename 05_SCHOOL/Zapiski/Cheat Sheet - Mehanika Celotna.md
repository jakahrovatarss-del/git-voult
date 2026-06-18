---
tags: [mehanika, cheat-sheet, statika, trdnost, kinematika, dinamika, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# CHEAT SHEET — Mehanika (vsi 4 sklopi)

> **Kako brati:** Vsak tip naloge: ZAKON → izpeljava → **FORMULA** → ⚠️ pasti → ✓ kontrola

---

## 📋 KAZALO

| Sklop              | TIP | Tema                                         | Rešen primer                                             |
| ------------------ | --- | -------------------------------------------- | -------------------------------------------------------- |
| **1 — STATIKA**    | A   | Reakcije 2D (prostoležeč nosilci)            | N3, N4 → [[Vaje - Statika - Vse vrste]]                  |
|                    | A2  | Stabilnost — kritični kot guganja            | [[Naloga - Mehanika - Statika Stol Valj Stabilnost]]     |
|                    | B   | Razstavljanje sil, koti                      | [[Vaje - Statika - Vse vrste]]                           |
|                    | C   | Škripci                                      | N1, N2 → [[Vaje - Statika - Vse vrste]]                  |
|                    | D   | 3D statika — redukcija sistema sil           | N5 → [[Vaje - Statika - Vse vrste]]                      |
|                    | E   | Valji v kupu (60°)                           | N6 → [[Vaje - Statika - Vse vrste]]                      |
|                    | F   | Paličje — metoda vozlišč                     | N8 → [[Vaje - Statika - Vse vrste]]                      |
|                    | F2  | Paličje — Ritter (metoda prereza)            | N13 → [[Poglavje - Statika]]                             |
|                    | G   | Gerber nosilci                               | N16 → [[Poglavje - Statika]]                             |
|                    | H   | Steiner (yT, I, W)                           | N7 Vaje, N15 → [[Poglavje - Statika]]                    |
|                    | I   | Trenje — Coulomb + **zagozda**               | N17 → [[Poglavje - Statika]]                             |
|                    | J   | Euler jermen + **kolut+trak**                | N18 → [[Poglavje - Statika]]                             |
|                    | K   | Vrvi — katenoida + **segmentna vrv**         | N10, N11 → [[Poglavje - Statika]]                        |
| **2 — TRDNOST**    | A   | NTM diagrami — 6 korakov                     | N1–N5 → [[Vaje - NTM diagrami - Vse vrste]]              |
|                    | A2  | Lomljeni nosilci / portalni okviri           | N3, N4; [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] |
|                    | A3  | 3D NTM — prostorska gred (jermenica, zobnik) | NotrSileVaje N2                                          |
|                    | B   | Upogib: σ = M/W, dimenzioniranje             | N1, N3, N9 → [[Vaje - Trdnost in dimenzioniranje]]       |
|                    | C   | Ekscentrični tlak N + M                      | N4 → [[Vaje - Trdnost in dimenzioniranje]]               |
|                    | D   | Napetostni tenzor + Mohrova krožnica         | N1–N5 → [[Vaje - Napetostni tenzor in Mohrova kroznica]] |
|                    | E   | Hipoteze porušitve: Tresca + Von Mises       | N5 Mohr, N16 → [[Poglavje - Trdnost]]                    |
|                    | F   | Uklon — Euler                                | N2, N6 Vaje; N19, N20 → [[Poglavje - Trdnost]]           |
|                    | G   | Uklon — Tetmajer                             | N21 → [[Poglavje - Trdnost]]                             |
|                    | H   | Torzija — polna gred                         | N5 Vaje, N17 → [[Poglavje - Trdnost]]                    |
|                    | I   | Torzija — Bredt (votli prerez)               | N18 → [[Poglavje - Trdnost]]                             |
|                    | J   | Sestavljene obremenitve N + M + Mt           | N22 → [[Poglavje - Trdnost]] ("Rezkar")                  |
| **3 — KINEMATIKA** | A   | Kinematika točke: at, an, a                  | N1 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | B   | Pol hitrosti — splošna metoda                | N2–N4 → [[Poglavje - Kinematika in Dinamika]]            |
|                    | B1  | Kolo na ravnini — kotaljenje                 | N2 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | B2  | Bat-klip drsnik                              | N3 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | B3  | Štiričlenski mehanizem (pogon + odvodna pal.)| [[Naloga - Mehanika - Kinematika Mehanizem ADAC]]        |
|                    | C   | Coriolisov pospešek                          | N5 → [[Poglavje - Kinematika in Dinamika]]               |
| **4 — DINAMIKA**   | D   | Newton II — dve kladi                        | N6 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | E   | Newton II — klanec s trenjem                 | N7 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | F   | Dinamika togega telesa — rotacija            | N9; [[Naloga - Mehanika - Dinamika Mesalo Steiner]]      |
|                    | G   | Energetski zakoni                            | N8 → [[Poglavje - Kinematika in Dinamika]]               |
|                    | H   | Nihanje — lastna frekvenca ω₀                | N10 → [[Poglavje - Kinematika in Dinamika]]              |
|                    | I   | Resonanca                                    | N11 → [[Poglavje - Kinematika in Dinamika]]              |

---

# ═══════════════════════════════════
# SKLOP 1 — STATIKA
# ═══════════════════════════════════

## OSNOVA: Newton I (ravnotežje = nič pospeška)

$$\sum \vec{F} = 0 \quad \text{in} \quad \sum \vec{M}_O = 0$$

**2D** → 3 enačbe:

$$\sum F_x = 0, \qquad \sum F_y = 0, \qquad \sum M_A = 0$$

**3D** → 6 enačb:

$$\sum F_x=\sum F_y=\sum F_z=0, \qquad \sum M_x=\sum M_y=\sum M_z=0$$

---

## PODPORE IN REAKCIJE

![[ntm_vrste_podpor.svg|697]]

| Podpora | Simbol | Reakcije | Neznanke |
|---------|--------|----------|----------|
| Nepomični členek (tečaj) | △ | $A_x, A_y$ | 2 |
| Pomični členek (valj) | ○— | $B_y$ | 1 |
| Togo vpetje (konzola) | ▬ | $A_x, A_y, M_A$ | 3 |
| Prost konec | — | nič | 0 → $T=M=0$! |
| Notranji členek (Gerber) | ○ na gredi | +pogoj $M_{čl}=0$ | −1 |

**Statično določena 2D:** $\sum\text{neznank} = 3$

---

## SPLOŠNI POSTOPEK ZA REAKCIJE

```
1. Nariši FBD — vse sile + reakcije
2. Razstavi vsako poševno silo: Fx = F·sinα ali F·cosα
3. ΣFx = 0  → Ax
4. ΣMA = 0  → By  (moment okrog točke z največ neznankami!)
5. ΣFy = 0  → Ay
6. Kontrola: ΣMB = 0 → mora biti 0
```

> **Trik:** Moment okrog točke, kjer se sekata 2 neznani → direktno 3. neznanko.

---

## TIP A: REAKCIJE — 2D (prostoležeč nosilci)

**Izhodišče:** Newton I + ΣMA = 0

**Primer N3 (Vaje):** $q = 2\ \text{kN/m}$, $L = 6\ \text{m}$, $F = 12\ \text{kN}$ pri $x=4\ \text{m}$:

$$\sum M_A = 0: \quad B_y \cdot 6 = q \cdot 6 \cdot 3 + F \cdot 4 = 36 + 48 \quad \Rightarrow \quad \boxed{B_y = 14\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y = 12+12-14 = \boxed{10\ \text{kN}}$$

![[statika_n1.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N3

---

**Primer N4 (Vaje):** $F=15\ \text{kN}$, kot $\alpha=40°$ od navpičnice, $L=6\ \text{m}$:

$$F_x = F\sin40° = 9{,}64\ \text{kN}, \qquad F_y = F\cos40° = 11{,}49\ \text{kN}$$

$$\sum M_A = 0: \quad B_y \cdot 6 = 45{,}96 \quad \Rightarrow \quad \boxed{B_y = 7{,}66\ \text{kN}}$$

$$\boxed{A_y = 3{,}83\ \text{kN}}, \qquad \boxed{A_x = 9{,}64\ \text{kN}}$$

![[statika_n2.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N4

---

**Primer N3 (Poglavje):** konzola s silami → $A_y = 20{,}2\ \text{kN}$, $M_A = 49{,}9\ \text{kNm}$

![[ravnotezje_T_rama.svg|697]]

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N3

---

## TIP A2: STABILNOST — kritični kot guganja

**Pogoj:** Ko se telo nagne za $\alpha$, se podpora dvigne ($B_y = 0$). Telo balansira na vrtišču A samo, kadar leži težišče T točno nad A.

$$\boxed{\tan\alpha = \frac{x_T}{y_T}}$$

$x_T$ = vodoravna razdalja težišča od vrtišča A, $y_T$ = navpična razdalja.

| # | Korak | Opis |
|---|-------|------|
| 1 | Določi koordinate | izhodišče = vrtišče A, poišči xT, yT glede na A |
| 2 | Mirovanje: By | $\sum M_A = 0 \to B_y = \frac{G/2 \cdot x_T}{d}$ |
| 3 | Mirovanje: Ay | $\sum F_y = 0 \to A_y = G/2 - B_y$ |
| 4 | Guganje (By=0) | $\tan\alpha = x_T / y_T$ |
| 5 | Kot | $\alpha = \arctan(x_T / y_T)$ |

⚠️ $y_T$ = višina sedala + polmer valja — ne samo polmer!
⚠️ Visoko težišče → majhen $\alpha$ → manjša stabilnost

**Primer — stol + valj** ($d$×$d$ sedalo, naslonjalo do $2d$, valj $R=d/2$):

$x_T = d/2$, $y_T = d + d/2 = 3d/2$ → $\tan\alpha = \frac{1}{3}$ → $\boxed{\alpha \approx 18{,}43°}$

$B_y = G/4$, $A_y = G/4$ (simetrično, ker $x_T = d/2$)

> 🔗 **Rešeno:** [[Naloga - Mehanika - Statika Stol Valj Stabilnost]] — BTF izpit 1. feb 2019

---

## TIP B: KOT SILE — razstavljanje

| Definicija kota | $F_x$ | $F_y$ |
|-----------------|-------|-------|
| Kot **od navpičnice** $\alpha$ | $F\sin\alpha$ | $F\cos\alpha$ |
| Kot **od vodoravnice** $\alpha$ | $F\cos\alpha$ | $F\sin\alpha$ |

⚠️ **PAST:** Mejni preizkus — $\alpha=0°$ od navpičnice → $F_x=0$, $F_y=F$ ✓

![[nagnjene_ravnine.svg|697]]

---

## TIP C: ŠKRIPCI (N1, N2 — Vaje)

**Izhodišče:** Vzporedni sistem vrvi, idealen škripec:

$$S = G \qquad \text{(sila v vsaki veji vrvi)}$$

$$\text{Fiksni škripec:} \quad F_A = 2G \qquad \text{Gibljivi:} \quad S = G/2$$

**Moment v vpetju B** (N1): $M_B = 2G \cdot a$

**Pod kotom $\theta$** (N2): $S_x = S\sin\theta$, $S_y = S\cos\theta$ → 3 enačbe ravnotežja

![[statika_n3.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N1, N2

---

## TIP D: 3D STATIKA — redukcija sistema sil (N5 — Vaje)

**Izhodišče:**

$$\vec{R} = \sum \vec{F}_i, \qquad \vec{M}_O = \sum (\vec{r}_i \times \vec{F}_i)$$

$$\vec{M} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ x & y & z \\ F_x & F_y & F_z \end{vmatrix} = (yF_z-zF_y)\vec{i} - (xF_z-zF_x)\vec{j} + (xF_y-yF_x)\vec{k}$$

**Primer N5 (Vaje):** $\vec{F}_1=(-1,5,-8)$, $\vec{F}_2=(0,0,-4)$ → $\vec{R} = (-1,5,-12)\ \text{kN}$

**Primer N5 (Poglavje):** kvader 3D → $\vec{R} = (0,\ 5{,}15,\ -13{,}58)\ \text{kN}$

![[statika_n4.svg|697]]

![[kvader_3d.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N5 · [[Poglavje - Statika]] — N5

---

## TIP E: VALJI V KUPU (N6 — Vaje)

**Izhodišče:** Valji enakih polmerov → kontaktne sile normalne na dotikalno točko → **koti 60°/30°**

Središča tvorijo **enakostranični trikotnik**, kontaktna sila med valji: naklon **30° od navpičnice**

**Postopek** ($G=800\ \text{N}$):
```
1. Zgornji valj (ΣF=0):
   2N1·cos30° = G  →  N1 = 800/1,732 = 462 N
2. Sila na steno: F_stena = N1·sin30° = 231 N
3. Spodnji valj: Ntal = G/2 + N1·cos30° = 800 N
```

![[statika_n5.svg|697]]

![[statika_n6.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N6

---

## TIP F: PALIČJE — metoda vozlišč (N8 — Vaje)

### Osnove paličja

**Paličje** je statična konstrukcija, sestavljena iz ravnih palic, ki so na obeh koncih artikilirano (členkovito) pritrjene v vozlišča. Ključna lastnost: **vsaka palica je dvoročica (dvosila)** — prenaša samo osno silo $S$ (nateg ali tlak), brez upogibnih momentov.

**Predpostavke:**
- Obtežbe delujejo **samo v vozliščih** (ne vzdolž palic)
- Palice so lahke (brez lastne teže)
- Vsaka palica = ena neznana ($S_i$)

**Predznaki:**
| Vrsta | Simbol | Pomen |
|-------|--------|-------|
| **Nateg** | $S > 0$ (+) | Palica se razteza — sila kaže **stran od vozlišča** |
| **Tlak** | $S < 0$ (−) | Palica se stiska — sila kaže **v vozlišče** |

> ⚠️ **Konvencija:** Vedno predpostavi nateg ($S > 0$). Če pride negativen rezultat → palica je v tlaku.

---

### Ničelne palice (Ničelne palice — pogoji)

Ničelne palice nosijo silo $S = 0$. Hitro jih prepoznaš:

**Pravilo 1 — Prazno vozlišče, 2 palici (niso kolinearne):**  
Če v vozlišče prita 2 palici, ki **nista v isti liniji**, in ni nobene zunanje sile → **obe palici ste ničelni**.

**Pravilo 2 — 3 palice, 2 kolinearni:**  
Če v vozlišče prihajajo 3 palice, od katerih sta 2 kolinearni (v isti liniji), in ni nobene zunanje sile → **tretja palica je ničelna**.

> 💡 Ničelne palice identificiraj **PRED začetkom računanja** — prihrani cel korak.

---

### Algoritem — metoda vozlišč

```
KORAK 1: Globalne reakcije
  ΣMA = 0  →  Dy (ali Ay)
  ΣFy = 0  →  Ay
  ΣFx = 0  →  Ax

KORAK 2: Poišči ničelne palice (pravili zgoraj)

KORAK 3: Začni pri vozlišču z ≤ 2 neznankama
  → Za vsako vozlišče: ΣFx = 0, ΣFy = 0 → reši 2 neznani
  → Smer sile: predpostavi nateg (stran od vozlišča)

KORAK 4: Napreduj na naslednje vozlišče
  → Rešene sile prenesi kot znane

KORAK 5: Kontrola — zadnje vozlišče
  → ΣFx = 0 in ΣFy = 0 morata biti izpolnjeni (0 = 0)
```

**Koristni kotni razmerji:**

| Geometrija            | sin                                  | cos                                  |
| --------------------- | ------------------------------------ | ------------------------------------ |
| 45°                   | $\frac{\sqrt{2}}{2} \approx 0{,}707$ | $\frac{\sqrt{2}}{2} \approx 0{,}707$ |
| 30° / 60°             | $0{,}5$ / $0{,}866$                  | $0{,}866$ / $0{,}5$                  |
| Splošno: h=140, l=150 | $\frac{h}{l}$                        | $\frac{\sqrt{l^2-h^2}}{l}$           |

![[palicje_diagram.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N8

---

## TIP F2: PALIČJE — metoda prereza (Ritter) (N13 — Poglavje Statika)

### Kdaj uporabiti Ritter?

Metoda vozlišč zahteva računanje vseh palic po vrsti — zamudno za velika paličja. **Ritterjeva metoda prereza** ti omogoča, da **direktno izračunaš silo v eni specifični palici** brez reševanja celega sistema.

### Algoritem — metoda prereza

```
KORAK 1: Globalne reakcije (kot pri metodi vozlišč)

KORAK 2: Nariši prerez
  → Prereži natanko 3 palice, katerih sile iščeš
  → Prerez narišeš kot namišljeno linijo skozi paličje
  ⚠️ MAX 3 neznane palice v prerezu!

KORAK 3: Izberi levo ALI desno stran prereza
  → Upoštevaj vse sile na izbrani strani (obtežbe + reakcije)

KORAK 4: Momentno ravnotežje
  → ΣM okrog točke, kjer se sekata 2 od 3 neznanih palic
  → Direktno dobiš 3. silo brez matrik!

KORAK 5: Ravnotežje sil
  → ΣFy = 0 → ena od preostalih dveh
  → ΣFx = 0 → zadnja sila

KORAK 6: Kontrola predznaka
  → Pozitivno = nateg (+), negativno = tlak (−)
```

### Ključna tehnika — izbira momentne točke

| Iščeš silo palice | Postavi ΣM okrog                       |
| ----------------- | -------------------------------------- |
| Zgornjega pasu    | Vozlišče spodnjega pasu pod njo        |
| Spodnjega pasu    | Vozlišče zgornjega pasu nad njo        |
| Diagonale         | Presečišče zgornjega in spodnjega pasu |
|                   |                                        |

> 💡 Vedno izberi točko, ki **eliminira 2 neznani naenkrat** → preostane 1 enačba, 1 neznanka.

**Primer N13:**

$$S_{GH} = +30\ \text{kN (nateg)}, \quad S_{EF} = -45\ \text{kN (tlak)}, \quad S_{EH} = +21{,}2\ \text{kN (nateg)}$$

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N13

---

## TIP G: GERBER NOSILCI (N16 — Poglavje Statika)

**Izhodišče:** Notranji členek → $M_{čl} = 0$ → dodaten pogoj.

```
1. RAZSTAVI v členku → dva ločena delčka
2. "Viseči" del → izračunaj silo v členku
3. Preneši silo (nasprotno!) na drugi del → preostale reakcije
4. NTM ločeno za vsak del
```

**Primer N16:** $A_y = 16\ \text{kN}$, $B_y = 10\ \text{kN}$

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N16

---

## TIP H: STEINER — GEOMETRIJSKE KARAKTERISTIKE (N7, N15 — Vaje/Poglavje)

| # | Korak | Formula |
|---|-------|---------|
| 1 | Razstavi na enostavne like | Pravokotnik, krog, odprtina (−A) |
| 2 | Težišče vsakega dela | $y_i$ meri od spodnjega roba |
| 3 | Skupno težišče | $y_T = \sum A_i y_i / \sum A_i$ |
| 4 | Lastni I vsakega dela | $I_{x,i} = b_i h_i^3 / 12$ |
| 5 | Steiner | $I = \sum(I_{x,i} + A_i \cdot d_i^2)$; $d_i = \|y_T - y_{T,i}\|$ |
| 6 | Odpornostni moment | $W_{sp} = I/e_{sp}$, $W_{zg} = I/e_{zg}$ |

$e_{sp} = y_T$ (spodnja vlakna), $e_{zg} = H - y_T$ (zgornja vlakna)

$$\boxed{y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}}, \qquad \boxed{I = \sum\left(\frac{b_i h_i^3}{12} + A_i \cdot d_i^2\right)}$$

⚠️ Za asimetrične prereze: kritičen je **manjši** $W$ (večji $e$) — tam je $\sigma$ največji!
⚠️ Steiner = $A_i \cdot d_i^2$, **ne** $I_i \cdot d_i^2$!

**Primer N15 (Poglavje):** U-prerez → $y_T = 4{,}077\ \text{cm}$, $I = 485\ \text{cm}^4$

> 🔗 **Rešeno:** [[Vaje - Statika - Vse vrste]] — N7 · [[Poglavje - Statika]] — N15

**Standardni prerezi:**

![[upogib_c_prerez.svg|697]]

![[upogib_krozni_prerez.svg|697]]

![[upogib_skatlaski_profil.svg|697]]

![[vztrajnostni_moment_prerezi.svg|697]]

| Prerez | $I$ | $W$ |
|--------|-----|-----|
| Pravokotnik $b \times h$ | $\frac{bh^3}{12}$ | $\frac{bh^2}{6}$ |
| Krog $d$ | $\frac{\pi d^4}{64}$ | $\frac{\pi d^3}{32}$ |
| Votel krog $D, d$ | $\frac{\pi(D^4-d^4)}{64}$ | $\frac{\pi(D^4-d^4)}{32D}$ |

---

## TIP I: TRENJE — COULOMB (N17 — Poglavje Statika)

$$\boxed{F_{tr} \leq \mu_s \cdot N}$$

**Klanec:** $mg\sin\alpha \leq \mu_s \cdot mg\cos\alpha \Rightarrow \boxed{\tan\alpha \leq \mu_s}$

| # | Korak | Opis |
|---|-------|------|
| 1 | N = mg·cosα | normalna sila na površino |
| 2 | F_tang = mg·sinα | gonilna sila |
| 3 | F_tr,max = μs·N | max trenjska sila |
| 4 | Pogoj | F_tang ≤ F_tr,max  (ali tan α ≤ μs) |

**Primer N17:** $F = 84\ \text{N}$

### Zagozda (wedge friction)

Na **vsaki** kontaktni površini ločeno: $F_{tr,i} = \mu_i \cdot N_i$

$$\text{FBD zagozde} \to \sum F_x = 0,\ \sum F_y = 0 \to F_{min}$$

| # | Korak | Opis |
|---|-------|------|
| 1 | FBD za vsako telo posebej | zaznamuj vse normale + trenjske sile |
| 2 | Smer trenja | nasprotna smeri premika zagozde |
| 3 | Za vsako površino | $N_i$ ⊥ površini, $F_{tr,i} = \mu_i \cdot N_i$ vzdolž površine |
| 4 | Ravnotežje zagozde | ΣFx=0, ΣFy=0 → $F_{min}$ |
| 5 | Ravnotežje bremena | ΣF=0 → preveritev |

⚠️ Tipično 2–3 trenjske sile hkrati — zapiši vsako ločeno!

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N17, zagozda

---

## TIP J: EULER JERMEN (N18 — Poglavje Statika)

$$\boxed{\frac{F_1}{F_2} = e^{\mu \theta}}$$

$F_1 > F_2$ (napeta stran), $\theta$ = kot ovoja v **radianih** (180° = π, 270° = 3π/2)

| # | Korak | Opis |
|---|-------|------|
| 1 | Določi θ [rad] | 180° = π, 270° = 3π/2 |
| 2 | F1/F2 = e^(μθ) | Euler razmerje |
| 3 | Dodatni pogoj | F1 + F2 = skupna sila ali M = (F1−F2)·R |
| 4 | Reši | F1, F2 iz razmerja + vsote |

### Kolut + trak (band brake)

$$\boxed{M_{zav} = (F_1 - F_2) \cdot R}, \qquad \frac{F_1}{F_2} = e^{\mu\theta}$$

| # | Korak | Opis |
|---|-------|------|
| 1 | θ [rad] | kot ovoja traku na kolutu |
| 2 | Euler → F1/F2 | $F_1 = F_2 \cdot e^{\mu\theta}$ |
| 3 | M_zav = M_mot | določi $F_1 - F_2$ |
| 4 | Reši F1, F2 | iz razmerja in razlike |
| 5 | Momentno ravnotežje diska | preveri prenos momenta |

⚠️ $F_1$ = napeta (vlečna) stran, $F_2$ = ohlapna stran — ne zamenjaj!

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N18, kolut+trak

---

## TIP K: VRVI (N10, N11 — Poglavje Statika)

### Katenoida (zvezna obtežba)

**Katenoida:** $y = a\cosh(x/a)$, $a = H_0/q_0$

$H_0$ = vodoravna komponenta (**konstanta vzdolž vrvi!**), $q_0$ = obtežba na m.

**Primer N10:** vrv → $H = 7{,}78\ \text{kN}$

**Primer N11:** katenoida → $H = 2{,}0\ \text{kN}$, $T_{max} = 2{,}04\ \text{kN}$

### Segmentna vrv (točkovne obtežbe)

$$H = \text{const}, \qquad T_i = \sqrt{H^2 + V_i^2}, \qquad \tan\theta_i = \frac{V_i}{H}$$

| # | Korak | Opis |
|---|-------|------|
| 1 | FBD celote | globalno ΣFx=0, ΣFy=0, ΣM=0 → Ax, Ay, Bx, By |
| 2 | $V_i$ po segmentih | seštevaj vertikalne sile od leve |
| 3 | H iz geometrije | kotota vozlišča ali dolžina segmenta |
| 4 | Ti = √(H²+Vi²) | natezna sila v i-tem segmentu |
| 5 | T_max | segment z max \|Vi\| |

⚠️ $H$ je ista v vseh segmentih — to je ključni pogoj!

> 🔗 **Rešeno:** [[Poglavje - Statika]] — N10, N11, segmentna vrv

---

# ═══════════════════════════════════
# SKLOP 2 — TRDNOST
# ═══════════════════════════════════

## OSNOVA: Notranje sile in napetosti

$$\text{Statika} \xrightarrow{\text{reakcije}} \text{NTM diagrami} \xrightarrow{\text{prerez}} \text{napetosti} \xrightarrow{} \text{kontrola}$$

---

## TIP A: NTM DIAGRAMI — splošni postopek

**Referenčni diagrami:**

![[ntm_diagrami.svg|697]]

![[m_diagram_tipi.svg|697]]

![[m_diagram_predznak.svg|697]]

**6 korakov:**

| # | Korak | Kaj naredis |
|---|-------|-------------|
| 0 | Tip konstrukcije | Prosta greda / konzola / L-oblika / Gerber? Je os zlomljena? → N≠0 |
| 1 | FBD + reakcije | Nariši vse sile, izračunaj Ay, By, Ax (ΣMA→By, ΣFy→Ay) |
| 2 | Območja | Razdeli pri vsaki točkovni sili, momentu, začetku/koncu q |
| 3 | T(x), M(x) | Za vsako območje: T = Ay − q·x; M = Ay·x − q·x²/2 − … |
| 4 | Mmax | Reši T(x)=0 → vstavi x₀ v M(x) |
| 5 | Diagrami | Nariši T in M; parabola kjer q≠0, ravna črta kjer q=0 |
| 6 | Kontrola | Prosti konec: T=M=0 ✓; Vpetje: preberi Mmax ✓ |

**Pravila za obliko diagrama:**

$$\boxed{\frac{dT}{dx} = -q}, \qquad \boxed{\frac{dM}{dx} = T}$$

| Obtežba | T | M |
|---------|---|---|
| Brez q | konstantna | linearna |
| Enakomerna q | linearna | parabola (2. red) |
| Točkovna F↓ | **skok −F** | kink (lom) |
| Moment M₀ | brez skoka | **skok +M₀** |

$$T(x) = A_y - q\cdot x = 0 \quad \Rightarrow \quad x_{T=0} \quad \Rightarrow \quad M_{max}$$

---

**Primer N1 (Vaje NTM):** prosta greda z $q$ in točkasto silo

![[ntm_naloga1.svg|697]]

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N1

---

**Primer N2 (Vaje NTM):** konzola ali greda s previsnim delom

![[ntm_naloga2.svg|697]]

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N2

---

**Primer N3 (Vaje NTM):** L-oblika — lomljeni nosilci

![[ntm_naloga3.svg|697]]

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N3

---

**Primer N4 (Vaje NTM / Trdnost):** $B_y = 19{,}25\ \text{kN}$, $M_{max} = 19{,}4\ \text{kNm}$

![[ntm_naloga4.svg|697]]

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N4 · [[Poglavje - Trdnost]] — N4

---

**Primer N5 (Vaje NTM):** portalni okvir ali Gerber

![[ntm_naloga5.svg|697]]

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N5

---

## TIP A2: LOMLJENI NOSILCI / PORTALNI OKVIRI (N3, N4 — Vaje NTM)

**Ključni zakon:** V vogalu L-oblike ali okvira se osna sila prelevi v prečno silo:

$$N_{navp} = T_{vodor}, \qquad T_{navp} = N_{vodor}$$

Portalni okvir: vodoravna sila → stebra nosita $N + T + M$; prečnik samo $M + T$.

**Gerber + L-oblika** (NotrSileVaje N1 — 5 polj): Razreži v Gerber členku → reši ločeno za vsak del → preneši reakcijo členka naprej → NTM za vsako polje posebej.

> 🔗 **Rešeno:** [[Vaje - NTM diagrami - Vse vrste]] — N3, N4
> 🔗 **Naloga:** [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] — 3 palice, 5 polj, $A_y=-1{,}25$ kN (nateg!), $M_{CD,max}=-6$ kNm

---

## TIP A3: 3D NTM — PROSTORSKA GRED (NotrSileVaje N2)

Gred prenaša **6 notranjih veličin:** $N$, $T_n$, $T_b$, $M_t$, $M_n$, $M_b$.

**Naravni koordinatni sistem:** $t$ = os gredi (tangenta), $n$ = navpično (normala), $b$ = vodoravno (binormala). Sistem je levoročni.

**Zunanje obremenitve gredi:**

| Vir | Sila/moment |
|-----|-------------|
| Jermenica (polmer $R$) | $M_t = (S_1-S_2)\cdot R$; prečni sili $S_1+S_2$ |
| Poševno ozobljenje ($\beta$) | $F_t = F\cos\beta$ (tang.), $F_a = F\sin\beta$ (aks.) |
| Radialni ležaj | prečni reakciji $A_y$, $A_z$ |
| Radialno-aksialni ležaj | $A_y$, $A_z$ + aksialno $A_x$ |

**Postopek — 3D gred:**

```
1. Shema gredi + razstavi vse obremenitve na komponente (Ft, Fa, Fn)
2. Poveži z naravnim koordinatnim sistemom gredi (t, n, b)
3. Zapiši 6 ravnotežnih enačb → reši 6 reakcij
4. Razdeli gred na polja (med ležaji, med obremenitvami)
5. Za vsako polje — prerez pri P (koordinata s):
   • Levi del (ali desni — izberi manj sil)
   • 6 enačb: t→N,Mt; n→Tn,Mn; b→Tb,Mb
   • Nekatere so konstantne, nekatere linearne v s
6. Nariši 4 diagrame: N, T (Tn↕ in Tb↔ skupaj), Mt, M (Mn↔ in Mb↕ skupaj)
```

**Skoki v diagramih:**
- $M_t$: skoči pri jermenici/zobniku za $M_t = (S_1-S_2)\cdot R$
- $M_n$ ali $M_b$: skoči pri aksialni sili $F_a$ na ročici $r$: $\Delta M = F_a \cdot r$

⚠️ Naravni koordinatni sistem je **levoročni** v standardni obliki (desnoročni le pri desni strani prereza).

**Primer N2 (NotrSileVaje):** Gred z jermenico ($S_1=2$, $S_2=5$, $R=0{,}2$ m) in poševnim zobnikom ($\beta=15°$):
$$F_t = 3{,}0\ \text{kN},\quad F_a = 0{,}803\ \text{kN},\quad M_t = -0{,}6\ \text{kNm}$$
$$A_x = 0{,}803\ \text{kN},\quad A_y = 2{,}307\ \text{kN},\quad A_z = 2{,}277\ \text{kN}$$

> 🔗 Vir: NotrSileVaje (1).pdf — N2

---

## TIP B: UPOGIB — NAPETOSTI IN DIMENZIONIRANJE (N1, N3, N9 — Vaje Trdnost)

**Bernoullijeva hipoteza:**

$$\boxed{\sigma_{max} = \frac{M}{W}}$$

**Dimenzioniranje:** $W_{min} = M_{max}/\sigma_{dop}$

**Za $h = 2b$** (leseni nosilci, N1 Vaje):

$$W = \frac{2b^3}{3} \quad \Rightarrow \quad \boxed{b = \sqrt[3]{\frac{3W_{min}}{2}}}$$

![[trdnost_n1.svg|697]]

![[upogib_lesen_nosilec.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Trdnost in dimenzioniranje]] — N1

---

**Za $h = 1{,}5b$** (N9 Poglavje):

$$W = 0{,}375b^3 \quad \Rightarrow \quad \boxed{b = \sqrt[3]{W_{min}/0{,}375}}$$

**Strižna napetost** (pravokotni prerez):

$$\tau_{max} = \frac{3}{2}\cdot\frac{T}{A}$$

![[trdnost_n2.svg|697]]

![[trdnost_n3.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Trdnost in dimenzioniranje]] — N3, N9

---

**U-prerez — napetosti pri asimetričnem prerezu (N15 Poglavje):**

![[upogib_U_prerez_napetosti.svg|697]]

![[reakcije_U_prerez_razlaga.svg|697]]

> 🔗 **Rešeno:** [[Poglavje - Trdnost]] — N15

---

## TIP C: EKSCENTRIČNI TLAK N + M (N4 — Vaje Trdnost)

**Superpozicija:**

$$\boxed{\sigma = \frac{N}{A} \pm \frac{M}{W}}$$

$$\sigma_{sp} = \frac{N}{A} + \frac{M}{W_{sp}}, \qquad \sigma_{zg} = \frac{N}{A} - \frac{M}{W_{zg}}$$

Kritično vlakno = kjer je $|\sigma|$ največja.

> **Intuicija:** Tlačna palica z ekscentrično silo ima na eni strani večji tlak, na drugi morda celo nateg!

![[trdnost_n4.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Trdnost in dimenzioniranje]] — N4

---

## TIP D: NAPETOSTNI TENZOR + MOHROVA KROŽNICA (N1–N5 — Vaje Mohr)

$$[\sigma] = \begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{xy} & \sigma_y \end{pmatrix}$$

![[napetostni_element_3d.svg|697]]

**6-koračni postopek:**

| # | Korak | Formula |
|---|-------|---------|
| 1 | Preberi napetosti | $\sigma_x$, $\sigma_y$, $\tau_{xy}$ |
| 2 | Središče krožnice | $S = (\sigma_x+\sigma_y)/2$ |
| 3 | Polmer | $R = \sqrt{((\sigma_x-\sigma_y)/2)^2+\tau_{xy}^2}$ |
| 4 | Glavne napetosti | $\sigma_{1,2} = S \pm R$ |
| 5 | Kot ravnine | $\tan(2\varphi_0) = 2\tau_{xy}/(\sigma_x-\sigma_y)$ |
| 6 | Max strižna | $\tau_{max} = R$ |

$$\boxed{S = \frac{\sigma_x+\sigma_y}{2}}, \quad \boxed{R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}}, \quad \boxed{\sigma_{1,2} = S \pm R}$$

![[mohrova_kroznica.svg|697]]

⚠️ Kot na krožnici je $2\varphi_0$ — v fizičnem prostoru je $\varphi_0$!
⚠️ Kontrola: $\sigma_1 + \sigma_2 = \sigma_x + \sigma_y$ (invarianta — mora se ujemati!)

---

**Primer N1 (Vaje Mohr):** 2D napetostno stanje → $\sigma_{1,2}$, $\tau_{max}$

![[mohr_naloga1.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N1

---

**Primer N2 (Vaje Mohr):** 3D tenzor → $\det([\sigma]-\sigma I)=0$ → $\sigma_1 \geq \sigma_2 \geq \sigma_3$

![[mohr_naloga2.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N2

---

**Primer N3 (Vaje Mohr):** risanje in odčitavanje Mohrove krožnice

![[mohr_naloga3.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N3

---

**Primer N4 (Vaje Mohr):** napetosti iz deformacij — Lamé-jev zakon

$$\sigma_x = \frac{E}{(1+\nu)(1-2\nu)}\left[(1-\nu)\varepsilon_x+\nu(\varepsilon_y+\varepsilon_z)\right], \qquad \tau_{xy} = G\cdot\gamma_{xy}$$

![[mohr_naloga4.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N4

---

**Primer N5 (Vaje Mohr):** kontrola s Tresca / Von Mises

![[mohr_naloga5.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N5

---

## TIP E: HIPOTEZE PORUŠITVE — Tresca + Von Mises

**Von Mises** (distorzijska energija):

$$\boxed{\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop}}$$

$$\sigma_{ekv,VM} = \frac{1}{\sqrt{2}}\sqrt{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}$$

**Tresca** (maksimalna strižna napetost — konzervativnejša):

$$\boxed{\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} \leq \sigma_{dop}}$$

⚠️ **Tresca ≥ Von Mises** → varnostni: Tresca; ekonomičen: VM.

**Za 2D** ($\sigma_3 = 0$):

$$\sigma_{ekv,VM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}$$

![[hipoteze_porusitve.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Napetostni tenzor in Mohrova kroznica]] — N5 · [[Poglavje - Trdnost]] — N16

---

## TIP F: UKLON — EULER (N2, N6 — Vaje; N19, N20 — Poglavje Trdnost)

$$\boxed{F_k = \frac{\pi^2 E I_{min}}{l_u^2}}, \qquad l_u = \beta \cdot L$$

| Tip stebra | $\beta$ | $l_u$ |
|-----------|---------|--------|
| Prosto-prosto | 1 | $L$ |
| Konzola (vpeto-prosto) | 2 | $2L$ |
| Vpeto-vpeto | 0,5 | $L/2$ |
| Vpeto-pomično | 0,7 | $0{,}7L$ |

$$\boxed{\lambda = \frac{l_u}{i_{min}}}, \qquad i_{min} = \sqrt{\frac{I_{min}}{A}}, \qquad \lambda_E = \pi\sqrt{\frac{E}{\sigma_{dop}}}$$

$$\boxed{\nu = \frac{F_k}{F} \geq \nu_{zaht}} \quad (\nu_{zaht} = 3\text{–}5 \text{ za les})$$

**Šibka os:** uklon vedno po $I_{min}$! Za $b \times h$ kjer $b < h$: $I_{min} = \frac{h b^3}{12}$ — **manjša dimenzija $b$ se kubira!**

| Postopek dimenzioniranja | |
|---|---|
| 1. Določi β (vpetje) | 2. $l_u = \beta \cdot L$ |
| 3. $i = \sqrt{I_{min}/A}$ | 4. $\lambda = l_u/i$ |
| 5. Primerjaj z $\lambda_E$ | 6. Euler ($\lambda>\lambda_E$) ali Tetmajer |
| 7. $F_k = \pi^2 E I_{min}/l_u^2$ | 8. $\nu = F_k/F \geq \nu_{zaht}$ |

![[uklon_palica_Sdop.svg|697]]

![[uklon_lesena_deska.svg|697]]

![[trdnost_n6.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Trdnost in dimenzioniranje]] — N2, N6 · [[Poglavje - Trdnost]] — N19, N20

---

## TIP G: UKLON — TETMAJER (N21 — Poglavje Trdnost)

$$\boxed{\sigma_k = a_T - b_T \cdot \lambda}$$

Les (iglavci): $a_T = 2{,}93\ \text{kN/cm}^2$, $b_T = 0{,}0194\ \text{kN/cm}^2$

```
λ < 60 (les):      zdrs → σ_dop direktno
60 < λ < 90 (les): TETMAJER
λ > 90 (les):      EULER
```

**Postopek:**
```
1. i = √(I/A)       2. λ = lu/i
3. λE = π·√(E/σdop) 4. Tetmajer ali Euler?
5. σk = aT - bT·λ   6. Fk = σk·A   7. ν = Fk/F
```

**Primer N21:** $\lambda = 86{,}6$ → Tetmajer → $F_k = 125\ \text{kN}$, $\nu = 5{,}0\ ✓$

> 🔗 **Rešeno:** [[Poglavje - Trdnost]] — N21

---

## TIP H: TORZIJA — POLNA GRED (N5 — Vaje; N17 — Poglavje Trdnost)

$$\tau = \frac{M_t \cdot \rho}{I_p}, \qquad \boxed{\tau_{max} = \frac{M_t}{W_t}}$$

| Prerez | $W_t$ | Zveza |
|--------|-------|-------|
| Polni krog $d$ | $\frac{\pi d^3}{16}$ | $W_t = 2W$ |
| Votel krog $D, d$ | $\frac{\pi(D^4-d^4)}{16D}$ | — |
| Kvadrat $a$ | $\approx 0{,}208\,a^3$ | — |

⚠️ Za krog: $W_t = 2W$ (ker $I_p = 2I$)!

![[torzija_palica.svg|697]]

![[trdnost_n5.svg|697]]

> 🔗 **Rešeno:** [[Vaje - Trdnost in dimenzioniranje]] — N5 · [[Poglavje - Trdnost]] — N17

---

## TIP I: TORZIJA — BREDT votli tankostenski prerez (N18 — Poglavje Trdnost)

$$\boxed{\tau = \frac{M_t}{2 \cdot A_m \cdot t}}$$

$A_m$ = ploščina, ki jo **oklepa srednja linija** stene (ne zunanja, ne luknja!)

Za pravokotni votli profil $B \times H$, stena $t$: $A_m = (B-t)(H-t)$

⚠️ **BREDTOVA PAST:** $A_m \neq B \cdot H$ in $\neq (B-2t)(H-2t)$ — srednja linija po SREDINI stene!

Bredt velja samo za zaprte profile, tankostenski ($t \ll B, H$).

**Primer N18:** $A_m = 123{,}25\ \text{cm}^2$, $\tau = 0{,}974 > 0{,}9\ \text{kN/cm}^2$ ❌

![[torzija_skatlast_prerez.svg|697]]

> 🔗 **Rešeno:** [[Poglavje - Trdnost]] — N18

---

## TIP J: SESTAVLJENE OBREMENITVE N + M + $M_t$ (N22 "Rezkar" — Poglavje Trdnost)

**2D verzija (N22):**

```
1. Mmax = F⊥·L           (upogib)
2. σM = Mmax/W           (upogibna napetost)
3. σN = FN/A             (osna napetost, ±!)
4. σ = σM ± σN           (kritično vlakno = aditivno!)
5. τ = Mt/Wt             (torzija)
6. σekv = √(σ²+3τ²) ≤ σdop   (Von Mises)
   σekv = √(σ²+4τ²) ≤ σdop   (Tresca)
```

**3D verzija (DN1 — Rezkar, NotrSileVaje):** konzola z $F_a$ (aksialno), $F_r$ (radialno), $F_c$ (obodno/cirkularno):

```
Reduciraj sile v vrh konzole:
  Fa → osna sila N v konzoli (brez momenta vzdolž osi)
  Fr → radialna sila → upogib v eni ravnini: Mb = Fr·s
  Fc → obodna sila → upogib v drugi ravnini: Mn = Fc·s
             PLUS torzija: Mt = Fc·r (r = polmer rezkarja)

6 notranjih veličin: N, Tn, Tb, Mt, Mn, Mb (gl. TIP A3)
Kritično mesto: vpetje (s = L), kjer so vsi momenti max.
```

**Primer N22 Rezkar (2D):** $\sigma_{ekv,VM} = 42{,}2 \gg \sigma_{dop} = 15\ \text{kN/cm}^2$ ❌

> 🔗 **Rešeno:** [[Poglavje - Trdnost]] — N22 · NotrSileVaje DN1

---

# ═══════════════════════════════════
# SKLOP 3 — KINEMATIKA
# ═══════════════════════════════════

## OSNOVA: Kinematika = geometrija gibanja (brez sil)

$$v = \dot{s}, \quad a = \ddot{s}, \quad \omega = \dot{\varphi}, \quad \alpha = \dot{\omega}$$

$$\boxed{v = \omega \cdot R}, \qquad \boxed{a_t = \alpha \cdot R}, \qquad \boxed{a_n = \omega^2 \cdot R = \frac{v^2}{\rho}}$$

**Pretvorba:** $\omega = \frac{2\pi n}{60}$ [rad/s]

---

## GIBALNA STANJA

| Stanje | $v(t)$ | $a_t$ | $a_n$ |
|--------|--------|-------|-------|
| Enakomerno premočrtno | $v_0$ | 0 | 0 |
| Enakopospešeno | $v_0+at$ | $a$ | 0 |
| Enakomerno krožno | $\omega R$ | 0 | $\omega^2 R$ |
| Neenakomerno krožno | $\omega R$ | $\alpha R$ | $\omega^2 R$ |
| Harmonično | $-A\omega_0\sin(\omega_0 t+\phi)$ | $-\omega_0^2 x$ | — |

---

## TIP A: KINEMATIKA TOČKE — $a_t$, $a_n$, $a$ (N1 — Poglavje)

```
1. ω(t) = ω₀ + α·t
2. at = α·R      (vzdolž tangente — menja velikost v)
3. an = ω²·R     (kaže PROTI središču — menja smer v)
4. a = √(at² + an²)
5. φ = arctan(an/at) od tangente
```

⚠️ $a_n$ je **vedno** prisoten pri krožnem gibanju (razen $\omega=0$). Naraste s $\omega^2$!

**Primer N1:** $a_t = 1{,}0$, $a_n = 32{,}0$, $a = 32{,}02\ \text{m/s}^2$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N1

---

## TIP B: POL HITROSTI — splošna metoda (N2–N4 — Poglavje)

**Vsako ravninsko gibanje = vrtenje okrog trenutnega pola P ($v_P = 0$):**

$$\boxed{v_A = \omega \cdot \overline{PA}} \qquad \text{smer: ⊥ na } \overrightarrow{PA}$$

```
1. Nariši mehanizem v danem položaju
2. Za vsako točko z znano smerjo v: nariši pravokotnico na v
3. P = presečišče pravokotnic
4. ω = v_znana / r_P,znana
5. v_iskana = ω · r_P,iskana  (smer: ⊥ na r_P,iskana)
```

⚠️ Pravokotnica NA HITROST, ne na telo!

| Gibanje | Pol P |
|---------|-------|
| Kolo se kotali | stična točka s podlago |
| Translacija | P v neskončnosti |
| Čisto vrtenje okrog O | P = O |

![[pol_hitrosti.svg|697]]

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N2, N3, N4

---

## TIP B3: ŠTIRIČLENSKI MEHANIZEM — pogon + odvodna palica

**Vzorec:** gred AD (vhod, NI = D) + palica AC (coupler) + odvodna palica EB (NI = E, pod kotom β)

| # | Korak | Formula |
|---|-------|---------|
| 1 | vA = vhod | $v_A = \omega_{vhod} \cdot r_{DA}$, smer ⊥ na DA |
| 2 | Pogoj EB | $v_B \perp \text{EB}$ → razmerje $v_{Bx}/v_{By} = -\cot\beta$ ali $-\tan\beta$ (glede na orientacijo) |
| 3 | vB iz palice AC | $\vec{v}_B = \vec{v}_A + \omega_{AC}\hat{k}\times\vec{r}_{AB}$, dve enačbi |
| 4 | Reši ωAC | iz razmerja vBx/vBy |
| 5 | vC | $\vec{v}_C = \vec{v}_A + \omega_{AC}\hat{k}\times\vec{r}_{AC}$ |
| 6 | Pol P (kontrola) | P = presečišče ⊥ na vA in ⊥ na vB; $v_C = \omega_{AC} \cdot PC$ |

⚠️ Smer $v_B$: določi pravo perpendikularno orientacijo (iz znaka vBx)!
⚠️ $\omega_{AC}$ negativen → urna smer (CW)

**Primer — Izpit 17. 4. 2015** (AD=2m navp., AC=4m vorav., EB=60°, ω=2π):

$$v_A = 4\pi\ \text{m/s},\quad \omega_{AC} = \frac{4\pi\sqrt{3}}{9} \approx 2{,}42\ \text{rad/s\ (↻)},\quad v_C = \frac{4\pi\sqrt{129}}{9} \approx 15{,}86\ \text{m/s}$$

> 🔗 **Rešeno:** [[Naloga - Mehanika - Kinematika Mehanizem ADAC]] — Izpit 17. 4. 2015

---

## TIP B1: KOLO NA RAVNINI — kotaljenje (N2 — Poglavje)

```
P = stična točka (spodaj)
ω = vC/R
v_vrh = 2vC
v_točke A (90° od vrha): rPA = R√2 → vA = ω·R√2
Smer: ⊥ na PX
```

**Primer N2:** $\omega = 5\ \text{rad/s}$, $v_D = 3{,}0\ \text{m/s}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N2

---

## TIP B2: BAT-KLIP DRSNIK (N3 — Poglavje)

Ročica AB (A vodoravno, B navpično), naklon $\theta$:

```
P = (L·cosθ, L·sinθ)
ω = vA / (L·sinθ)
vB = ω · L·cosθ = vA/tanθ
```

**Primer N3:** $\omega = 6\ \text{rad/s}$, $v_B = 2{,}6\ \text{m/s}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N3

---

## TIP C: CORIOLISOV POSPEŠEK (N5 — Poglavje)

$$\vec{a}_{abs} = \vec{a}_{rel} + \vec{a}_{trans} + \vec{a}_{Cor}$$

$$\boxed{a_{Cor} = 2\omega \cdot v_{rel}} \qquad \text{smer: ⊥ na } v_{rel} \text{ v smeri vrtenja}$$

Pojavi se SAMO ko **$\omega \neq 0$** IN **$v_{rel} \neq 0$** hkrati!

```
1. a_trans,n = ω²·r  (centripetalni)
2. a_trans,t = α·r   (samo če α≠0)
3. a_Cor = 2ω·v_rel  (⊥ na v_rel)
4. a_abs = vektorska vsota
```

**Primer N5:** $a_{Cor} = 3{,}0\ \text{m/s}^2$, $a_{abs} = 4{,}69\ \text{m/s}^2$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N5

---

# ═══════════════════════════════════
# SKLOP 4 — DINAMIKA
# ═══════════════════════════════════

## OSNOVA: Newton II — vzrok gibanja

$$\boxed{\sum \vec{F} = m\vec{a}} \qquad \boxed{\sum M_O = I_O \cdot \alpha}$$

**D'Alembert:** $\sum \vec{F} + (-m\vec{a}) = 0$ → reši kot statiko

---

## TIP D: NEWTON II — DVE KLADI (N6 — Poglavje)

```
1. FBD za vsako telo LOČENO
2. m₁ (↓+): m₁g - S = m₁a                    (1)
3. m₂ (→+): S - μm₂g = m₂a                   (2)
4. (1)+(2): a = (m₁g - μm₂g)/(m₁+m₂)
5. S = m₁g - m₁a
```

**Primer N6:** $a = 2{,}62\ \text{m/s}^2$, $S = 36{,}9\ \text{N}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N6

---

## TIP E: NEWTON II — KLANEC S TRENJEM (N7 — Poglavje)

```
N = mg·cosα
F_tr = μk·mg·cosα
a = g(sinα - μk·cosα)
v(t) = a·t,   s(t) = ½·a·t²
```

**Primer N7:** $a = 2{,}87\ \text{m/s}^2$, $v(3) = 8{,}6\ \text{m/s}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N7

---

## MOMENTI INERCIJE TOGIH TELES

| Telo | Os | $I$ |
|------|----|-----|
| Točkasta masa $m$ na $r$ | vrtenja | $mr^2$ |
| Palica $L$ | Skozi konec | $\frac{mL^2}{3}$ |
| Palica $L$ | Skozi sredino | $\frac{mL^2}{12}$ |
| Disk/valj $R$ | Os vrtenja | $\frac{mR^2}{2}$ |
| Obroč $R$ | Os vrtenja | $mR^2$ |
| Sfera $R$ | Premer | $\frac{2mR^2}{5}$ |

$$\boxed{I_O = I_T + m \cdot d^2} \qquad \text{(Steinerjev stavek)}$$

---

## TIP F: DINAMIKA TOGEGA TELESA — ROTACIJA (N9 — Poglavje)

| # | Korak | Formula |
|---|-------|---------|
| 1 | Vztrajnostni moment | $I_O = I_T + m\cdot d^2$ (Steiner za vsak del) |
| 2 | Newton II rotacija | $\sum M_O = I_O \cdot \alpha$ |
| 3 | Kotni pospešek | $\alpha = \Delta\omega / \Delta t$ |
| 4 | Kotna hitrost | $\omega = 2\pi n / 60$ [rad/s] |
| 5 | Navor | $M = I \cdot \alpha$ [Nm] |

**Momenti inercije:**

| Telo | Formula |
|------|---------|
| Palica skozi konec | $mL^2/3$ |
| Palica skozi sredino | $mL^2/12$ |
| Disk/valj $R$ | $mR^2/2$ |
| Pravokotna plošča $a\times b$ (os ⊥ skozi težišče) | $m(a^2+b^2)/12$ |

⚠️ Masa v **kg** (ne kN!), razdalje v **m** (ne mm!) za $I$ v kg·m²

**Primer N9:** $\alpha = 5\ \text{rad/s}^2$, $\omega(3) = 15\ \text{rad/s}$, $n = 143\ \text{obr/min}$

**Primer — Mešalo** (Steiner za odmaknjeno rezilo):
$$e = r_{gred} + L/2, \quad I_{rezilo} = \frac{m(L^2+w^2)}{12} + m\cdot e^2$$
$$M_z = I_{tot}\cdot\alpha \quad [\text{Nm}] \qquad \text{(min. navor brez upora tekočine)}$$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N9 · [[Naloga - Mehanika - Dinamika Mesalo Steiner]]

---

## TIP G: ENERGETSKI ZAKONI (N8 — Poglavje)

$$\boxed{A_{net} = \Delta E_k}, \qquad \boxed{E_{k1} + E_{p1} = E_{k2} + E_{p2}}$$

$$E_k = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2, \quad E_{p,grav} = mgh, \quad E_{p,vzmet} = \tfrac{1}{2}kx^2$$

**Vzmet iz stisnjenja $x_0$** (N8):

$$\tfrac{1}{2}kx_0^2 = \tfrac{1}{2}mv^2 \quad \Rightarrow \quad \boxed{v_{max} = x_0\cdot\omega_0}$$

**Primer N8:** $v_{max} = 2{,}0\ \text{m/s}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N8

---

## TIP H: NIHANJE — LASTNA FREKVENCA (N10 — Poglavje)

$$m\ddot{x} + kx = 0$$

$$\boxed{\omega_0 = \sqrt{\frac{k}{m}}}\ [\text{rad/s}], \qquad \boxed{f_0 = \frac{\omega_0}{2\pi}}\ [\text{Hz}], \qquad \boxed{T_0 = \frac{2\pi}{\omega_0}}\ [\text{s}]$$

**Vzporedne vzmeti:** $k_{eq} = k_1 + k_2$

**Zaporedne vzmeti:** $\frac{1}{k_{eq}} = \frac{1}{k_1} + \frac{1}{k_2}$

**Z dušenjem:** $\xi = \frac{c}{2\sqrt{km}}$, $\omega_d = \omega_0\sqrt{1-\xi^2}$

**Primer N10:** $\omega_0 = 15{,}81\ \text{rad/s}$, $T_0 = 0{,}397\ \text{s}$

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N10

---

## TIP I: RESONANCA (N11 — Poglavje)

$$m\ddot{x}+kx = F_0\sin(\Omega t) \quad \Rightarrow \quad \text{Resonanca pri } \Omega = \omega_0$$

Priporoča se $|\Omega/\omega_0 - 1| > 20\%$

**Ukrepi:** sprememba $n$, dodaj maso ($\omega_0\downarrow$), ojači vzmet ($\omega_0\uparrow$), dušilnik.

**Primer N11:** $\omega_{vzb} = 15{,}71 \approx \omega_0 = 15{,}81$ → resonanca!

> 🔗 **Rešeno:** [[Poglavje - Kinematika in Dinamika]] — N11

---

# ═══════════════════════════════════
# ⚡ HITRE FORMULE — IZPITNI LIST
# ═══════════════════════════════════

## STATIKA

$$\sum F_x=0,\ \sum F_y=0,\ \sum M_A=0 \quad \text{(2D)}$$

$$y_T = \frac{\sum A_iy_i}{\sum A_i}, \quad I = \sum\left(\frac{bh^3}{12}+A_id_i^2\right), \quad W = I/e$$

$$F_{tr} \leq \mu N, \quad \tan\alpha\leq\mu_s, \quad \frac{F_1}{F_2}=e^{\mu\theta}$$

## TRDNOST

$$\sigma=M/W, \quad W_{min}=M/\sigma_{dop}$$

$$S=\frac{\sigma_x+\sigma_y}{2},\ R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau^2},\ \sigma_{1,2}=S\pm R$$

$$\sigma_{ekv,VM}=\sqrt{\sigma^2+3\tau^2},\quad \sigma_{ekv,T}=\sqrt{\sigma^2+4\tau^2}$$

$$F_k=\frac{\pi^2EI_{min}}{l_u^2},\quad \lambda=\frac{l_u}{i},\quad \sigma_k=a_T-b_T\lambda$$

$$\tau=\frac{M_t}{W_t}\ \text{(polna)},\quad \tau=\frac{M_t}{2A_m t}\ \text{(Bredt)}$$

## KINEMATIKA + DINAMIKA

$$v=\omega R,\quad a_t=\alpha R,\quad a_n=\omega^2R,\quad a_{Cor}=2\omega v_{rel}$$

$$v_A=\omega\cdot r_{PA},\quad \text{Pol P: presečišče ⊥ na }v$$

$$\sum F=ma,\quad \sum M_O=I_O\alpha,\quad I_O=I_T+md^2$$

$$A_{net}=\Delta E_k,\quad E_k+E_p=\text{const},\quad \omega_0=\sqrt{k/m}$$

---

## Povezave

- [[Poglavje - Statika]] ← vse naloge 1. sklopa
- [[Poglavje - Trdnost]] ← vse naloge 2. sklopa
- [[Poglavje - Kinematika in Dinamika]] ← vse naloge 3.+4. sklopa
- [[Naloga - Mehanika - Statika Stol Valj Stabilnost]] ← TIP A2 Statika: guganje, tan α = xT/yT, BTF 2019
- [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] ← TIP A2 Trdnost: Gerber + L-oblika, 5 polj
- [[Naloga - Mehanika - Dinamika Mesalo Steiner]] ← TIP F: Steiner za odmaknjeno telo, navor
- [[Naloga - Mehanika - Kinematika Mehanizem ADAC]] ← TIP B3: štiričlenski mehanizem, izpit 2015
- [[Vaje - Statika - Vse vrste]] · [[Vaje - NTM diagrami - Vse vrste]]
- [[Vaje - Trdnost in dimenzioniranje]] · [[Vaje - Napetostni tenzor in Mohrova kroznica]]
- [[Blok 0 - Statika]] | [[Blok 1 - NTM Diagrami]] | [[Blok 2 - Upogib]]
- [[Blok 3 - Napetostno Stanje]] | [[Blok 3.5 - Hipoteze Porusitve]]
- [[Blok 4 - Euler Uklon]] | [[Blok 5 - Torzija]]
- [[Blok 6 - Kinematika]] | [[Blok 7 - Dinamika Nihanje]]
- [[Izpit - Mehanika - Celoletni 2026]] · [[Mehanika Hub]]
