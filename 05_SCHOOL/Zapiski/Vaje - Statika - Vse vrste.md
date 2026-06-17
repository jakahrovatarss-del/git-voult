---
tags: [mehanika, statika, reakcije, škripec, paličje, 3D-statika, valji, steiner, uklon, ravnovesje, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# Vaje — Statika: Vse vrste nalog

## Namen

Celovite rešene naloge za **1. SKLOP: Statika** — pokriva vse tipe izpitnih vprašanj. Vsaka naloga z FBD, izpeljavo korak za korakom, pogosto napako in cross-linki. Združuje škripce, posebna telesa (valji), 3D statiko, Steiner in paličja.

---

## Kazalo nalog

| Naloga | Tip | Ključna tehnika |
|--------|-----|-----------------|
| [[#NALOGA 1 — Škripec, navpična vrv\|N1]] | Škripec, reakcije v vpetju | S = G, ΣM okrog B |
| [[#NALOGA 2 — Škripec, nagnjena vrv\|N2]] | Škripec + kot vrvi | Razstavi S na Sx, Sy |
| [[#NALOGA 3 — Prostoležeč nosilci z q in F\|N3]] | Klasičen nosilci A–B | ΣMA = 0 → By direktno |
| [[#NALOGA 4 — Nagnjena sila pod kotom\|N4]] | Sila pod kotom α od navpičnice | Fx = Fsinα, Fy = Fcosα |
| [[#NALOGA 5 — 3D statika: redukcija sistema sil\|N5]] | 3D vektorji R, M₀ | Vektorski produkt r × F |
| [[#NALOGA 6 — Valji v kupu (3+2+1)\|N6]] | Posebna telesa | Geometrija 60°, N1 iz cos30° |
| [[#NALOGA 7 — Steiner za T-prerez\|N7]] | Geometrija prereza | yT, I (Steiner), Wsp ≠ Wzg |
| [[#NALOGA 8 — Paličje: metoda vozlišč\|N8]] | Paličje, 5 palic | ΣF = 0 v vsakem vozlišču |
| [[#NALOGA 9 — Kombinirana: nosilci + NTM + Steiner\|N9]] | Veriga Blok 0→1→1.5→2 | Reakcije → Mmax → W → σ |
| [[#NALOGA 10 — Kombinirana: nagnjena sila + Steiner + uklon\|N10]] | BTF tip (konzola + Euler) | FN, F⊥, I_min, Fk, ν |

---

## NALOGA 1 — Škripec, navpična vrv

> **Besedilo naloge:** Kovinsko dvigalo (nosilci v obliki L) je togo vpeto v B. Na koncu konzolnega dela (točka A) je pritrjen škripec. Vodoravna ročica $a = 2\ \text{m}$, višina stebra $H = 4\ \text{m}$. Dvigamo tovor mase $m = 20\ \text{kg}$. Izračunajte reakcije v vpetju B. ($g = 10\ \text{m/s}^2$)

**Podatki:** $m = 20\ \text{kg}$, $G = 0{,}2\ \text{kN}$, $a = 2\ \text{m}$, $H = 4\ \text{m}$

---

### Korak 1 — Sila v vrvi

$$S = G = m \cdot g = 20 \cdot 10 = \boxed{200\ \text{N} = 0{,}2\ \text{kN}}$$

Na škripec delujeta **dve veji vrvi**, obe navpično navzdol:

$$F_A = 2 \cdot S = \boxed{0{,}4\ \text{kN}\ \downarrow}$$

> **Zakaj 2S?** Škripec drži dve veji. Vsaka nese $S = G$. Skupna sila na ležaje = $2S$.

> **Poenostavitev (BTF):** Ko naloga navede le tovor brez opisa poteka vrvi → privzamemo $F = G$ (ena veja).

> **glej:** [[Blok 0 - Statika#Intuicija]]

---

### Korak 2 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad \boxed{B_x = 0}$$

$$\sum F_y = 0 \quad \Rightarrow \quad \boxed{B_y = 0{,}4\ \text{kN}\ \uparrow}$$

$$\sum M_B = 0 \quad \Rightarrow \quad M_B = F_A \cdot a = 0{,}4 \cdot 2 = \boxed{0{,}8\ \text{kNm}}$$

> ⚠️ **Napaka:** Ročica momenta je $a$ (vodoravna razdalja), ne $H$!

---

## NALOGA 2 — Škripec, nagnjena vrv

> **Besedilo naloge:** Isti L-nosilci, a prosta veja vrvi teče pod kotom $\alpha = 30°$ od navpičnice. Tovor $m = 50\ \text{kg}$, $a = 1{,}5\ \text{m}$, $H = 4\ \text{m}$. Izračunajte $B_x$, $B_y$, $M_B$.

**Podatki:** $G = 0{,}5\ \text{kN}$, $\alpha = 30°$, $a = 1{,}5\ \text{m}$, $H = 4\ \text{m}$

---

### Korak 1 — Sili v škripcu

Sila v vrvi je povsod enaka $S = G = 0{,}5\ \text{kN}$.

| Veja vrvi | $S_x$ | $S_y$ |
|-----------|-------|-------|
| Navpična (tovor) | 0 | $-0{,}5\ \text{kN}$ |
| Pod $\alpha = 30°$ od navpičnice | $+S\sin30° = +0{,}25$ | $-S\cos30° = -0{,}433$ |
| **Skupaj** | **$+0{,}25$** | **$-0{,}933$** |

> **Pravilo:** Kot od **navpičnice** → sin = vodoravna, cos = navpična komponenta.

> **zobacz:** [[Blok 0 - Statika#Razstavljanje sil po komponentah]]

---

### Korak 2 — Enačbe ravnovesja

$$\sum F_x = 0 \quad \Rightarrow \quad \boxed{B_x = -0{,}25\ \text{kN}\ \leftarrow}$$

$$\sum F_y = 0 \quad \Rightarrow \quad \boxed{B_y = +0{,}933\ \text{kN}\ \uparrow}$$

$$\sum M_B = 0 \quad \Rightarrow \quad M_B = |F_{A,y}| \cdot a + |F_{A,x}| \cdot H = 0{,}933 \cdot 1{,}5 + 0{,}25 \cdot 4 = \boxed{2{,}4\ \text{kNm}}$$

> ⚠️ **Ključno:** $F_{A,y}$ (navpična) ima ročico $a$; $F_{A,x}$ (vodoravna) ima ročico $H$!

---

## NALOGA 3 — Prostoležeč nosilci z q in F

> **Besedilo naloge:** Vodoravni nosilci $L = 6\ \text{m}$, prostoležeč med A (nepomični tečaj) in B (pomični valj). Enakomerna porazdeljena obtežba $q = 2\ \text{kN/m}$ po celotni dolžini, točkovna sila $F = 12\ \text{kN}$ pri $x_C = 4\ \text{m}$ od A. Izračunajte $A_x$, $A_y$, $B_y$.

---

### Korak 1 — Rezultanta $q$

$$Q = q \cdot L = 2 \cdot 6 = 12\ \text{kN} \qquad x_Q = L/2 = 3\ \text{m od A}$$

---

### Korak 2 — ΣMA = 0 direktno da $B_y$

$$B_y \cdot 6 = Q \cdot 3 + F \cdot 4 = 36 + 48 = 84 \quad \Rightarrow \quad \boxed{B_y = 14\ \text{kN}\ \uparrow}$$

> **Taktika:** Momentna enačba okrog A izniči $A_x$ in $A_y$ → direktno $B_y$!

---

### Korak 3 — Preostali reakciji

$$A_y = Q + F - B_y = 24 - 14 = \boxed{10\ \text{kN}\ \uparrow}$$

$$\boxed{A_x = 0}$$

**Kontrola:** $A_y + B_y = 24 = Q + F = 24\ ✓$

---

## NALOGA 4 — Nagnjena sila pod kotom

> **Besedilo naloge:** Prostoležeč nosilci dolžine $L = 6\ \text{m}$ je podprt v A (nepomični tečaj) in B (pomični valj). Na točki C ($x_C = 4\ \text{m}$ od A) deluje sila $F = 15\ \text{kN}$ pod kotom $\alpha = 40°$ glede na navpičnico. Izračunajte $A_x$, $A_y$, $B_y$.

---

### Korak 1 — Razstavi F

$$F_x = F \sin\alpha = 15 \cdot \sin 40° = 15 \cdot 0{,}643 = \boxed{9{,}64\ \text{kN}}$$

$$F_y = F \cos\alpha = 15 \cdot \cos 40° = 15 \cdot 0{,}766 = \boxed{11{,}49\ \text{kN}}$$

---

### Korak 2 — ΣMA = 0

> $F_x$ je vodoravna sila na vodoravnem nosilcu → ročica = 0 okrog točke na osi!

$$B_y \cdot 6 = F_y \cdot x_C = 11{,}49 \cdot 4 = 45{,}96 \quad \Rightarrow \quad \boxed{B_y = 7{,}66\ \text{kN}\ \uparrow}$$

---

### Korak 3 — Preostali reakciji

$$A_y = F_y - B_y = 11{,}49 - 7{,}66 = \boxed{3{,}83\ \text{kN}\ \uparrow}$$

$$A_x = F_x = \boxed{9{,}64\ \text{kN}\ \rightarrow}$$

**Kontrola ΣMB = 0:** $-3{,}83 \cdot 6 + 11{,}49 \cdot 2 = -22{,}98 + 22{,}98 = 0\ ✓$

> ⚠️ **Napaka:** Pozabiti $A_x$ — nepomični tečaj ima **dve** reakciji. Pomični valj B ima samo $B_y$!

---

## NALOGA 5 — 3D statika: redukcija sistema sil

> **Besedilo naloge:** Na kvadrasto telo ($a = 3\ \text{m}$) delujeta sili $\vec{F}_1 = (-1,\ 5,\ -8)\ \text{kN}$ v točki $P_1 = (3,\ 0,\ 3)\ \text{m}$ in $\vec{F}_2 = (0,\ 0,\ -4)\ \text{kN}$ v točki $P_2 = (3,\ 3,\ 3)\ \text{m}$. Reducirajte sistem na izvorišče $O$.

---

### Korak 1 — Rezultanta $\vec{R}$

$$\vec{R} = \vec{F}_1 + \vec{F}_2 = (-1,\ 5,\ -12)\ \text{kN}, \quad |\vec{R}| = \sqrt{1+25+144} = \boxed{13{,}04\ \text{kN}}$$

---

### Korak 2 — Momenti okrog O

$$\vec{M}_i = \vec{r}_i \times \vec{F}_i = \begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\r_x&r_y&r_z\\F_x&F_y&F_z\end{vmatrix}$$

**$\vec{M}_1$** ($\vec{r}_1 = (3,0,3)$, $\vec{F}_1 = (-1,5,-8)$):

$$M_{1,x} = 0\cdot(-8)-3\cdot5=-15, \quad M_{1,y}=3\cdot(-1)-3\cdot(-8)=21, \quad M_{1,z}=3\cdot5-0\cdot(-1)=15$$

**$\vec{M}_2$** ($\vec{r}_2 = (3,3,3)$, $\vec{F}_2 = (0,0,-4)$):

$$M_{2,x}=3\cdot(-4)-3\cdot0=-12, \quad M_{2,y}=3\cdot0-3\cdot(-4)=12, \quad M_{2,z}=3\cdot0-3\cdot0=0$$

---

### Korak 3 — Skupni moment

$$\vec{M}_O = \vec{M}_1 + \vec{M}_2 = (-27,\ 33,\ 15)\ \text{kNm}, \quad |\vec{M}_O| = \sqrt{729+1089+225} \approx \boxed{45{,}2\ \text{kNm}}$$

> ⚠️ **Napaka:** Napačen predznak pri determinantnem razvoju — pazi na alternirajoče predznake pri vrsticah $i, j, k$!

---

## NALOGA 6 — Valji v kupu (3+2+1)

> **Besedilo naloge:** 6 enakih gladkih valjev teže $G = 800\ \text{N}$ v piramidi (3 spodaj, 2 v sredini, 1 zgoraj). Navpični gladki steni zadržujeta kup. Izračunajte: (a) kontaktno silo $N_1$ (zgornji–srednji), (b) silo stene $F$.

---

### Korak 1 — Geometrija

Središča treh valjev tvorijo enakostranični trikotnik → kontaktna sila pod **30° od navpičnice**.

```
       ( O )        ← zgornji
      /     \
  30°         30°   ← N1
  ( O )   ( O )     ← sredinska
```

---

### Korak 2 — FBD zgornjega valja

$$\sum F_y = 0 \quad \Rightarrow \quad 2 N_1 \cos 30° = G$$

$$N_1 = \frac{G}{2\cos 30°} = \frac{800}{2 \cdot 0{,}866} = \frac{800}{\sqrt{3}} = \boxed{462\ \text{N}}$$

---

### Korak 3 — FBD zunanjega sredinskega valja

$$\sum F_y = 0 \quad \Rightarrow \quad N_{tal} = G + N_1\cos 30° = 800 + 400 = \boxed{1200\ \text{N}}$$

$$\sum F_x = 0 \quad \Rightarrow \quad F = N_1 \sin 30° = 462 \cdot 0{,}5 = \boxed{231\ \text{N}}$$

> ⚠️ **Napaka:** Privzeti, da kontaktne sile kažejo navpično. **Ne!** Vedno kažejo skozi središči valjev.

---

## NALOGA 7 — Steiner za T-prerez

> **Besedilo naloge:** Jekleni T-prerez: pasnica $b_p = 12\ \text{cm}$, $h_p = 2\ \text{cm}$ (zgoraj), stojina $b_s = 2\ \text{cm}$, $h_s = 12\ \text{cm}$ (spodaj). Skupna višina $H = 14\ \text{cm}$. Izračunajte: $y_T$, $I$, $W_{sp}$, $W_{zg}$.

---

### Korak 1 — Razdelitev in težišče

| Del | $A_i$ [cm²] | $y_i$ od spodaj [cm] | $A_i y_i$ |
|-----|-------------|----------------------|-----------|
| Stojina | 24 | 6,0 | 144 |
| Pasnica | 24 | 13,0 | 312 |
| **Skupaj** | **48** | | **456** |

$$y_T = \frac{456}{48} = \boxed{9{,}5\ \text{cm}}, \quad e_{sp} = 9{,}5\ \text{cm}, \quad e_{zg} = 4{,}5\ \text{cm}$$

---

### Korak 2 — Relationship momentov inercije (Steiner)

**Stojina** ($d_1 = 6{,}0 - 9{,}5 = -3{,}5\ \text{cm}$):

$$I_{stoj} = \frac{2 \cdot 12^3}{12} + 24 \cdot 3{,}5^2 = 288 + 294 = 582\ \text{cm}^4$$

**Pasnica** ($d_2 = 13{,}0 - 9{,}5 = +3{,}5\ \text{cm}$):

$$I_{pas} = \frac{12 \cdot 2^3}{12} + 24 \cdot 3{,}5^2 = 8 + 294 = 302\ \text{cm}^4$$

$$\boxed{I = 582 + 302 = 884\ \text{cm}^4}$$

---

### Korak 3 — Odpornostna momenta

$$W_{sp} = \frac{884}{9{,}5} = \boxed{93{,}1\ \text{cm}^3} \quad \leftarrow \textbf{KRITIČEN! (manjši)}$$

$$W_{zg} = \frac{884}{4{,}5} = \boxed{196{,}4\ \text{cm}^3}$$

> ⚠️ **Ključno:** Kritičen rob = tisti z **večjim** $e$ = **manjšim** $W$. Ne nujno natezni!

> **sijaj:** [[Blok 1.5 - Geometrijske Karakteristike#Intuicija]]

---

## NALOGA 8 — Paličje: metoda vozlišč

> **Besedilo naloge:** Paličje 5 palic, 4 vozlišča. A(0,0) = nepomični tečaj, B(4,0) = pomični valj. Razpon $L = 4\ \text{m}$, višina $H = 3\ \text{m}$. Sila $F = 10\ \text{kN}\ \downarrow$ v D(0,3), sila $P = 6\ \text{kN}\ \rightarrow$ v C(4,3).

---

### Korak 1 — Globalno ravnovesje

$$\sum M_A = 0: \quad B_y \cdot 4 = P \cdot 3 = 18 \quad \Rightarrow \quad \boxed{B_y = 4{,}5\ \text{kN}}$$

$$A_y = F - B_y = 10 - 4{,}5 = \boxed{5{,}5\ \text{kN}}, \quad A_x = -P = \boxed{-6\ \text{kN}}$$

---

### Korak 2 — Kotni podatki diagonal

Diagonala AC (od A(0,0) do C(4,3)), dolžina = 5 m:

$$\sin\phi = 3/5 = 0{,}6, \quad \cos\phi = 4/5 = 0{,}8$$

---

### Korak 3 — Vozlišče A (2 neznani: $S_{AD}$, $S_{AC}$)

$$\sum F_x = 0: \quad -6 + S_{AC} \cdot 0{,}8 = 0 \quad \Rightarrow \quad \boxed{S_{AC} = +7{,}5\ \text{kN}\ \text{(N)}}$$

$$\sum F_y = 0: \quad 5{,}5 + 7{,}5 \cdot 0{,}6 + S_{AD} = 0 \quad \Rightarrow \quad \boxed{S_{AD} = -10\ \text{kN}\ \text{(T)}}$$

---

### Korak 4 — Vozlišče D

$$\sum F_y = 0: \quad -10 + 10 - S_{DB} \cdot 0{,}6 = 0 \quad \Rightarrow \quad \boxed{S_{DB} = -33{,}3\ \text{kN}\ \text{(T)}}$$

$$\sum F_x = 0: \quad S_{DC} = -S_{DB}\cos\phi = 33{,}3 \cdot 0{,}8 = \boxed{26{,}7\ \text{kN}\ \text{(N)}}$$

---

### Korak 5 — Tabela sil

| Palica | Sila [kN] | Tip |
|--------|-----------|-----|
| $S_{AC}$ | +7,5 | Nateg |
| $S_{AD}$ | −10,0 | **Tlak** |
| $S_{DB}$ | −33,3 | **Tlak** |
| $S_{DC}$ | +26,7 | Nateg |

> ⚠️ **Pravilo:** Začni z vozliščem z **≤ 2 neznanima** palicama. Nikoli 3!

> **glej:** [[Blok 0 - Statika#Paličje — metoda vozlišč]]

---

## NALOGA 9 — Kombinirana: nosilci + NTM + Steiner

> **Besedilo naloge:** Leseni T-nosilci ($L = 5\ \text{m}$, prostoležeč) z $F = 8\ \text{kN}$ na sredini. T-prerez: pasnica $10 \times 2\ \text{cm}$, stojina $2 \times 10\ \text{cm}$. $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$. Preverite trdnost.

---

### Korak 1 — Reakcije + Mmax

$$A_y = B_y = F/2 = 4\ \text{kN}, \quad M_{max} = \frac{F \cdot L}{4} = \frac{8 \cdot 5}{4} = \boxed{10\ \text{kNm} = 1000\ \text{kNcm}}$$

---

### Korak 2 — Steiner T-prereza ($H = 12\ \text{cm}$)

| Del | $A_i$ | $y_i$ | $A_i y_i$ |
|-----|--------|--------|-----------|
| Stojina $2\times10$ | 20 | 5,0 | 100 |
| Pasnica $10\times2$ | 20 | 11,0 | 220 |

$$y_T = 320/40 = 8\ \text{cm}, \quad e_{sp} = 8\ \text{cm}, \quad e_{zg} = 4\ \text{cm}$$

$$I_{stoj} = \frac{2\cdot10^3}{12}+20\cdot9 = 166{,}7+180 = 346{,}7\ \text{cm}^4$$

$$I_{pas} = \frac{10\cdot2^3}{12}+20\cdot9 = 6{,}7+180 = 186{,}7\ \text{cm}^4$$

$$I = 533{,}4\ \text{cm}^4$$

---

### Korak 3 — Kontrola trdnosti

$$W_{sp} = 533{,}4/8 = 66{,}7\ \text{cm}^3 \quad (\text{kritičen!})$$

$$\sigma_{max} = \frac{M_{max}}{W_{sp}} = \frac{1000}{66{,}7} = \boxed{15{,}0\ \text{kN/cm}^2} \gg \sigma_{dop} = 1{,}0 \quad \Rightarrow \quad \textbf{❌ PREKORAČENO}$$

> **Zaključek:** Prerez je 15× premajhen. Za $W_{potr} = 1000\ \text{cm}^3$ bi potrebovali bistveno večji T ali pravokotnik.

---

## NALOGA 10 — Kombinirana: nagnjena sila + Steiner + uklon

> **Besedilo naloge (BTF tip):** Leseni steber pravokotnega prereza $b = 6\ \text{cm}$, $h = 10\ \text{cm}$, $L = 3\ \text{m}$. Na vrhu deluje $F = 8\ \text{kN}$ pod kotom $\alpha = 25°$ od navpičnice. Vpetje spodaj (konzola). Preverite upogib, napetost in uklon. ($E = 1000\ \text{kN/cm}^2$, $\sigma_{dop} = 1{,}2\ \text{kN/cm}^2$, $\nu_{zaht} = 3$)

---

### Korak 1 — Razstavi F

$$F_N = F\cos\alpha = 8 \cdot 0{,}906 = \boxed{7{,}25\ \text{kN}} \quad \text{(osna, tlačna)}$$

$$F_\perp = F\sin\alpha = 8 \cdot 0{,}423 = \boxed{3{,}38\ \text{kN}} \quad \text{(prečna → upogib)}$$

---

### Korak 2 — Geometrija prereza

$$A = 6 \cdot 10 = 60\ \text{cm}^2, \quad W = \frac{6 \cdot 10^2}{6} = 100\ \text{cm}^3$$

$$I_{min} = \frac{10 \cdot 6^3}{12} = \boxed{180\ \text{cm}^4} \quad \leftarrow \text{šibka os → za uklon!}$$

---

### Korak 3 — Upogib

$$M_{max} = F_\perp \cdot L = 3{,}38 \cdot 300 = 1014\ \text{kNcm}$$

$$\sigma_M = 1014/100 = 10{,}14\ \text{kN/cm}^2$$

$$\sigma_N = F_N / A = 7{,}25/60 = 0{,}12\ \text{kN/cm}^2$$

$$\sigma_{max} = 10{,}14 + 0{,}12 = \boxed{10{,}26\ \text{kN/cm}^2} \gg 1{,}2 \quad \Rightarrow \quad \textbf{❌}$$

---

### Korak 4 — Euler uklon

Konzola: $\beta = 2$, $l_u = 2 \cdot 300 = 600\ \text{cm}$

$$F_k = \frac{\pi^2 \cdot 1000 \cdot 180}{600^2} = \frac{1{,}776 \cdot 10^6}{360\,000} = \boxed{4{,}93\ \text{kN}}$$

---

### Korak 5 — Vitkost + varnostni faktor

$$i_{min} = \sqrt{180/60} = 1{,}732\ \text{cm}, \quad \lambda = 600/1{,}732 = 346$$

$$\lambda_e(\text{les}) = \pi\sqrt{1000/1{,}2} = 90{,}7 \quad \Rightarrow \quad \lambda > \lambda_e \quad \text{Euler velja ✓}$$

$$\nu = F_k / F_N = 4{,}93/7{,}25 = \boxed{0{,}68} < 3 \quad \Rightarrow \quad \textbf{❌ UKLON GROZI}$$

---

### Korak 6 — Zaključna tabela

| Kontrola | Vrednost | Dopustno | Ocena |
|----------|----------|----------|-------|
| $\sigma_{max}$ | 10,26 kN/cm² | 1,2 kN/cm² | ❌ |
| $\nu_{uklon}$ | 0,68 | ≥ 3 | ❌ |

> **Zaključek:** Prerez $6 \times 10$ cm je premajhen. Potrebno dimenzioniranje iz $\sigma_{dop}$ ali skrajšanje stebra.

> **glej:** [[Blok 4 - Euler Uklon#Intuicija]] | [[Blok 2 - Upogib#Intuicija]]

---

## Povzetek formul — izpit na hitro

### Reakcije

$$\sum F_x=0,\quad \sum F_y=0,\quad \sum M_A=0$$

Momentna enačba okrog točke z največ neznankami → direktna rešitev!

### Škripec

| Situacija | Sila na škripec |
|-----------|-----------------|
| Navpična vrv (tovor + fiksna) | $F = 2S = 2G$ |
| Prosta vrv pod $\alpha$ od navpičnice | $F_x = S\sin\alpha$, $F_y = S\cos\alpha + G$ |

### Razstavljanje sile pod kotom

| Kot od... | Vodoravna | Navpična |
|-----------|-----------|----------|
| Navpičnice | $F\sin\alpha$ | $F\cos\alpha$ |
| Vodoravnice | $F\cos\alpha$ | $F\sin\alpha$ |

### 3D redukcija

$$\vec{R} = \sum\vec{F}_i, \qquad \vec{M}_O = \sum\vec{r}_i\times\vec{F}_i$$

### Valji v kupu

$$N_1 = \frac{G}{2\cos30°} = \frac{G}{\sqrt{3}} \approx 0{,}577G, \qquad F_{stene} = N_1\sin30° \approx 0{,}289G$$

### Steiner

$$y_T = \frac{\sum A_i y_i}{\sum A_i}, \quad I = \sum\left(\frac{bh^3}{12}+A_id_i^2\right), \quad W_{krit} = \frac{I}{e_{max}}$$

### Konzolni steber z nagnjeno silo

1. $F_N = F\cos\alpha$ (osna), $F_\perp = F\sin\alpha$ (prečna)
2. $\sigma = M/W + F_N/A$, $M = F_\perp \cdot L$
3. Uklon: $l_u = 2L$, $F_k = \pi^2 EI_{min}/l_u^2$, $\nu = F_k/F_N \geq \nu_{zaht}$

---

## Povezave

- [[Blok 0 - Statika]] ← ravnovesje, FBD, vrste podpor
- [[Blok 1 - NTM Diagrami]] ← reakcije → Mmax
- [[Blok 1.5 - Geometrijske Karakteristike]] ← Steiner, yT, I, W
- [[Blok 2 - Upogib]] ← σ = M/W
- [[Blok 4 - Euler Uklon]] ← Fk, λ, β
- [[Vaje - NTM diagrami - Vse vrste]] ← nadaljevanje
- [[Vaje - Trdnost in dimenzioniranje]] ← celotna trdnostna veriga
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
