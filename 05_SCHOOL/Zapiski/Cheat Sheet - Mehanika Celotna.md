---
tags: [mehanika, cheat-sheet, statika, trdnost, kinematika, dinamika, izpit]
predmet: Mehanika
datum: 2026-06-17
---

# CHEAT SHEET — Mehanika (vsi 4 sklopi)

> **Kako brati:** Vsak tip naloge: ZAKON → izpeljava → **FORMULA** → ⚠️ pasti → ✓ kontrola

---

# ═══════════════════════════════════
# SKLOP 1 — STATIKA
# ═══════════════════════════════════

## OSNOVA: Newton I (ravnotežje = nič pospeška)

$$\sum \vec{F} = 0 \quad \text{in} \quad \sum \vec{M}_O = 0$$

**2D** → 3 enačbe (3 prostostne stopnje: x, y, φ):

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

## SPLOŠNI POSTOPEK ZA REAKCIJE (vsi tipi)

```
1. Nariši FBD — vse sile + reakcije
2. Takoj razstavi vsako poševno silo: Fx = F·sinα ali F·cosα (pazi na definicijo kota!)
3. ΣFx = 0  → Ax
4. ΣMA = 0  → By  (moment okrog točke ki ima največ neznank!)
5. ΣFy = 0  → Ay
6. Kontrola: ΣMB = 0 → mora dati 0
```

> **Trik:** Moment piši okrog točke, kjer se sekata 2 neznani — dobiš direktno 3. neznanko.

---

![[statika_n1.svg|697]]

![[statika_n2.svg|697]]

## TIP A: REAKCIJE — 2D (prostoležeč nosilci)

**Izhodišče:** Newton I + ΣMA = 0

**Primer N3 (Vaje):** $q = 2\ \text{kN/m}$, $L = 6\ \text{m}$, $F = 12\ \text{kN}$ pri $x=4\ \text{m}$:

$$\sum M_A = 0: \quad B_y \cdot 6 = q \cdot 6 \cdot 3 + F \cdot 4 = 36 + 48 = 84 \quad \Rightarrow \quad \boxed{B_y = 14\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y = qL + F - B_y = 12+12-14 = \boxed{10\ \text{kN}}$$

**Primer N4 (Vaje):** Sila $F=15\ \text{kN}$ pod kotom $\alpha=40°$ od navpičnice, $L=6\ \text{m}$, $x_C=4\ \text{m}$:

$$F_x = F\sin40° = 9{,}64\ \text{kN}, \qquad F_y = F\cos40° = 11{,}49\ \text{kN}$$

$$\sum M_A = 0: \quad B_y \cdot 6 = F_y \cdot 4 = 45{,}96 \quad \Rightarrow \quad \boxed{B_y = 7{,}66\ \text{kN}}$$

$$\sum F_y = 0: \quad \boxed{A_y = 3{,}83\ \text{kN}}, \qquad \sum F_x=0: \quad \boxed{A_x = 9{,}64\ \text{kN}}$$

**Porazdeljena obtežba:** $q \cdot L$ deluje v težišču $= L/2$ od roba.

---

![[nagnjene_ravnine.svg|697]]

## TIP B: KOT SILE — razstavljanje

| Definicija kota | $F_x$ | $F_y$ |
|-----------------|-------|-------|
| Kot **od navpičnice** $\alpha$ | $F\sin\alpha$ | $F\cos\alpha$ |
| Kot **od vodoravnice** $\alpha$ | $F\cos\alpha$ | $F\sin\alpha$ |

⚠️ **PAST:** Sin je vedno pri manjši komponenti (od večje osi) — preveri z mejnim primerom: $\alpha=0°$ od navpičnice → $F_x=0$, $F_y=F$ ✓

---

![[statika_n3.svg|697]]

## TIP C: ŠKRIPCI (N1, N2 — Vaje)

**Izhodišče:** Vzporedni sistem vrvi, idealen škripec (brez trenja):

$$S = G = mg \qquad \text{(sila v vsaki veji vrvi)}$$

**Fiksni škripec** (ena vrv, dve veji na konzolo):

$$F_A = 2S = 2G \qquad \text{(na pritrdišče delujeta obe veji!)}$$

**Gibljivi škripec** (dviganje):

$$S = G/2 \qquad \text{(dvakratna mehanska prednost)}$$

**Moment v vpetju B** (N1): $M_B = F_A \cdot a = 2G \cdot a$

**Škripec pod kotom $\theta$** (N2): Vrv nagnjena → razstavi:
$$S_x = S\sin\theta, \quad S_y = S\cos\theta \quad \Rightarrow \quad B_x, B_y, M_B \text{ iz 3 enačb}$$

---

![[statika_n4.svg|697]]

## TIP D: 3D STATIKA — redukcija sistema sil (N5 — Vaje)

![[kvader_3d.svg|697]]

**Izhodišče:** Vsako silo prenesel v točko O + moment para:

$$\vec{R} = \sum \vec{F}_i, \qquad \vec{M}_O = \sum (\vec{r}_i \times \vec{F}_i)$$

**Vektorski produkt** $\vec{r} \times \vec{F}$ v 3D:

$$\vec{M} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ x & y & z \\ F_x & F_y & F_z \end{vmatrix} = (yF_z-zF_y)\vec{i} - (xF_z-zF_x)\vec{j} + (xF_y-yF_x)\vec{k}$$

**Primer N5 (Vaje):** $\vec{F}_1=(-1,5,-8)$, $\vec{F}_2=(0,0,-4)$:
$$\vec{R} = (-1,5,-12)\ \text{kN}, \quad \vec{M}_O = \vec{r}_1\times\vec{F}_1 + \vec{r}_2\times\vec{F}_2$$

---

![[statika_n5.svg|697]]

## TIP E: VALJI V KUPU (N6 — Vaje)

![[statika_n6.svg|697]]

**Izhodišče:** Valji enakih polmerov → kontaktne sile so normalne na dotikalni točki → **koti 60° / 30°**

**Geometrija** (3 valji polmera $r$):
- Središča tvorijo **enakostranični trikotnik**, stranica = $2r$
- Kontaktna sila med zgornjim in spodnjim valjem: naklon **30° od navpičnice**

**Postopek** (N6, $G=800\ \text{N}$):
```
1. Zgornji valj (velja ΣF=0): N1 je kontaktna sila na nagnjeni ploskvi
   2N1·cos30° = G  →  N1 = G/(2cos30°) = 800/1,732 = 462 N
2. Spodnji valj (ΣFy=0): Ntal = G/2 + N1·cos30° = 400+400 = 800 N
   (ali: Ntal = G za vsak spodnji valj ker simetrija)
3. Sila na steno: F_stena = N1·sin30° = 462·0,5 = 231 N
```

---

## TIP F: PALIČJE — metoda vozlišč (N8 — Vaje)

**Izhodišče:** Paličje = sistem dvosil. Vsaka palica: samo $N$ (nateg + ali tlak −).

**Predpostavka:** Nateg pozitiven (+). Negativen rezultat = tlak.

**Postopek:**
```
1. Globalne reakcije (ΣMA=0, ΣFy=0, ΣFx=0)
2. Začni pri vozlišču z ≤ 2 neznanima palicama
3. Za vsako vozlišče: ΣFx=0, ΣFy=0 → 2 neznani palici
4. Napreduj do naslednjega vozlišča
5. Kontrola: zadnje vozlišče mora dati 0=0
```

⚠️ **PAST:** Sile palic kažejo OD vozlišča (nateg) ali V vozlišče (tlak) — vedno predpostavi nateg!

---

## TIP F2: PALIČJE — metoda prereza (Ritter) (N13 — Poglavje Statika)

```
1. Prereži 3 palice katerih sile iščemo
2. Nariši FBD leve ali desne strani
3. ΣM okrog presečišča dveh neznanih palic → direktno 3. sila
4. ΣFy = 0 ali ΣFx = 0 → ostali dve
```

⚠️ Max **3 neznane** palice v prerezu!

---

## TIP G: GERBER NOSILCI (N16 — Poglavje Statika)

**Izhodišče:** Gerber = notranji členek → $M_{čl} = 0$ → dodaten pogoj.

**Postopek:**
```
1. RAZSTAVI v členku → dva ločena delčka
2. Začni z "visečim" (konzolnim) delom → izračunaj silo v členku
3. To silo prenesi (nasprotno!) na drugi del → izračunaj preostale reakcije
4. Nariši NTM ločeno za vsak del
```

---

## TIP H: STEINER — GEOMETRIJSKE KARAKTERISTIKE (N7, N15 — Vaje/Poglavje)

**Izhodišče:** Težišče prereza in upogibna togost.

**Korak 1 — Težiščna os:**

$$\boxed{y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}}$$

kjer je $y_i$ = razdalja težišča $i$-tega dela od referenčne osi (tipično spodnji rob).

**Korak 2 — Steinerjev stavek:**

$$\boxed{I = \sum\left(\frac{b_i h_i^3}{12} + A_i \cdot d_i^2\right)}$$

kjer je $d_i = |y_T - y_{T,i}|$ = razdalja od skupnega težišča do lastnega težišča dela $i$.

**Korak 3 — Odpornostni moment** (za upogib):

$$\boxed{W_{sp} = \frac{I}{e_{sp}}}, \qquad \boxed{W_{zg} = \frac{I}{e_{zg}}}$$

kjer je $e_{sp} = y_T$ (od sp. roba do težišča), $e_{zg} = H - y_T$ (od zg. roba).

⚠️ **PAST:** $W_{sp} \neq W_{zg}$ za asimetrične prereze → kritičen je **manjši** $W$ (večji $e$)!

**Standardni prerezi:**

![[upogib_c_prerez.svg]]

![[upogib_krozni_prerez.svg]]

![[upogib_skatlaski_profil.svg]]

![[vztrajnostni_moment_prerezi.svg]]

| Prerez | $I$ | $W$ |
|--------|-----|-----|
| Pravokotnik $b \times h$ | $\dfrac{bh^3}{12}$ | $\dfrac{bh^2}{6}$ |
| Krog $d$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^3}{32}$ |
| Votel krog | $\dfrac{\pi(D^4-d^4)}{64}$ | $\dfrac{\pi(D^4-d^4)}{32D}$ |

---

## TIP I: TRENJE — COULOMB (N17 — Poglavje Statika)

**Izhodišče:** Coulombov zakon mejnega trenja:

$$\boxed{F_{tr} \leq \mu_s \cdot N}$$

**Klanec — pogoj ravnovesja:**

$$mg\sin\alpha \leq \mu_s \cdot mg\cos\alpha \quad \Rightarrow \quad \boxed{\tan\alpha \leq \mu_s}$$

**Postopek (klanec):**
```
1. N = mg·cosα  (normalna sila)
2. F_tang = mg·sinα  (tangencialna komponenta teže)
3. Mejno trenje: F_tr,max = μs·N
4. Pogoj: F_tang ≤ F_tr,max → ne zdrsne
   Alternativno: tan(α) ≤ μs
```

---

## TIP J: EULER JERMEN — trenje na jermenskem gonilu (N18 — Poglavje Statika)

**Izhodišče:** Euler-Eytelweinova formula za jermen ali vrv na bobnu:

$$\boxed{\frac{F_1}{F_2} = e^{\mu \theta}}$$

kjer je $F_1 > F_2$ (napeta stran), $\mu$ = koeficient trenja, $\theta$ = kot ovoja v **radianih**.

**Postopek:**
```
1. Določi kot ovoja θ [rad] (npr. 180° = π, 270° = 3π/2)
2. F1/F2 = e^(μθ)
3. Iz F1+F2 = skupna sila (če je dano) → reši za F1, F2
4. Prenos sile: F_neto = F1 - F2
```

---

## TIP K: VRVI — Katenoida in vrv z 2 bremeni (N10, N11 — Poglavje Statika)

**Vrv z 2 koncentriciranima bremeni:** razstavi v vsakem vozlišču.

**Katenoida** (enakomerno porazdeljena vrv, obtežba na dolžino):

$$y = a\cosh\left(\frac{x}{a}\right), \qquad a = \frac{H_0}{q_0}$$

kjer je $H_0$ = vodoravna komponenta sile v vrvi (konstanta!), $q_0$ = obtežba na m.

⚠️ Na izpitu BTF: katenoida se pojavi redko — dovolj poznati da $H_0 = \text{const}$ vzdolž vrvi.

---

# ═══════════════════════════════════
# SKLOP 2 — TRDNOST
# ═══════════════════════════════════

## OSNOVA: Notranje sile in napetosti

Notranje sile (NTM) → napetosti → kontrola / dimenzioniranje.

$$\text{Statika} \xrightarrow{\text{reakcije}} \text{NTM diagrami} \xrightarrow{\text{prerez}} \text{napetosti} \xrightarrow{} \text{kontrola}$$

---

![[ntm_diagrami.svg|697]]

![[m_diagram_tipi.svg|697]]

![[m_diagram_predznak.svg|697]]

## TIP A: NTM DIAGRAMI — splošni postopek (N1–N5 Vaje NTM)

**6 korakov (za vse vrste nosilci):**

```
KORAK 0: Prepoznaj tip (prosta greda, konzola, L-oblika, okvir, Gerber)
KORAK 1: FBD + reakcije (glej STATIKA postopek)
KORAK 2: Določi območja med točkami spremembe obtežbe
KORAK 3: Za vsako območje zapiši T(x) in M(x)
KORAK 4: Poišči T=0 → tam je Mmax (ekstremu!)
KORAK 5: Nariši T in M diagram (znaki, skoki, parabole)
KORAK 6: Kontrola: na prostem koncu T=M=0, v vpetju preberi vrednosti
```

**Diferencialne zveze:**

$$\boxed{\frac{dT}{dx} = -q(x)}, \qquad \boxed{\frac{dM}{dx} = T(x)}$$

→ Kjer je $q$ → T je poševna črta → M je parabola.  
→ Kjer ni $q$ → T je konstanta → M je poševna črta.

**Skoki:**
- Točkovna sila $F$ ↓ pri $x=a$ → T skoči za $-F$ (navzdol)
- Točkasti moment $M_0$ pri $x=a$ → M skoči za $+M_0$ (brez skoka v T!)

**Poiščemo $T=0$** (kjer je $M = M_{max}$):

$$T(x) = A_y - q\cdot x - \sum F_i = 0 \quad \Rightarrow \quad x_{T=0}$$

$$M_{max} = A_y \cdot x_{T=0} - \frac{q\cdot x_{T=0}^2}{2} - \sum F_i \cdot (x_{T=0}-x_i)$$

---

## TIP A2: LOMLJENI NOSILCI / PORTALNI OKVIRI (N3, N4 — Vaje NTM)

**Ključni zakon:** V vogalu L-oblike ali okvira se osna sila enega elementa **prelevi** v prečno silo drugega:

$$N_{navp} = T_{vodor}, \qquad T_{navp} = N_{vodor}$$

**Portalni okvir:**
- Vodoravna zunanja sila → stebra nosita $N$ + $T$ + $M$
- Prečnik nosi samo $M$ + $T$ (brez $N$, razen poševne obtežbe)

---

## TIP B: UPOGIB — NAPETOSTI IN DIMENZIONIRANJE (N1, N3, N9 — Vaje Trdnost)

**Izhodišče:** Bernoullijeva hipoteza (ravni prerezi ostanejo ravni):

$$\varepsilon_x = \frac{y - y_T}{\rho} \xrightarrow{Hooke} \sigma_x = E\varepsilon_x = \frac{M}{I}(y-y_T)$$

**Maksimalna upogibna napetost** (na skrajnem vlaknu):

$$\boxed{\sigma_{max} = \frac{M}{W}}$$

**Dimenzioniranje** (dano $M_{max}$, $\sigma_{dop}$):

$$W_{min} = \frac{M_{max}}{\sigma_{dop}}$$

**Za $h = 2b$** (leseni nosilci, N1 Vaje):

$$W = \frac{b\cdot(2b)^2}{6} = \frac{4b^3}{6} = \frac{2b^3}{3} \quad \Rightarrow \quad b = \sqrt[3]{\frac{3W_{min}}{2}}$$

**Za $h = 1{,}5b$** (N9 Poglavje Trdnost):

$$W = \frac{b\cdot(1{,}5b)^2}{6} = \frac{2{,}25b^3}{6} = 0{,}375b^3 \quad \Rightarrow \quad b = \sqrt[3]{\frac{W_{min}}{0{,}375}}$$

**Strižna napetost** (N9):

$$\tau_{max} = \frac{3}{2}\cdot\frac{T}{A} \quad \text{(pravokotni prerez, v nevtralnem vlaknu)}$$

⚠️ Za T-prerez: $\tau$ v stojini je kritična, ne v pasnici!

---

## TIP C: EKSCENTRIČNI TLAK N + M (N4 — Vaje Trdnost)

**Izhodišče:** Superpozicija — osna in upogibna napetost se seštevata:

$$\boxed{\sigma = \frac{N}{A} \pm \frac{M}{W}}$$

**Predznak:** Nateg = +, Tlak = −. Določi za oba roba:

$$\sigma_{sp} = \frac{N}{A} + \frac{M}{W_{sp}}, \qquad \sigma_{zg} = \frac{N}{A} - \frac{M}{W_{zg}}$$

**Kritično vlakno** = tisto, kjer je $|\sigma|$ večja.

> **Intuicija:** Tlačna palica z ekscentrično silo ima na eni strani večji tlak, na drugi strani morda celo nateg — kljub temu da je splošna obtežba tlačna!

---

## TIP D: NAPETOSTNI TENZOR + MOHROVA KROŽNICA (N1–N5 — Vaje Mohr)

**Izhodišče:** Napetostno stanje v točki = tenzor:

$$[\sigma] = \begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{xy} & \sigma_y \end{pmatrix}$$

![[napetostni_element_3d.svg|697]]

**6-koračni postopek:**

```
1. Preberi σx, σy, τxy iz fizikalne slike (upogib → σ, torzija → τ)
2. Središče: S = (σx + σy)/2
3. Polmer:  R = √((σx-σy)²/4 + τxy²)
4. Glavne napetosti: σ1,2 = S ± R
5. Kot: tan(2φ0) = 2τxy/(σx-σy)  →  φ0 = (1/2)·arctan(...)
6. τmax = R  (na Mohrovi krožnici!)
```

**Formule:**

$$\boxed{S = \frac{\sigma_x+\sigma_y}{2}}, \qquad \boxed{R = \sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}}$$

$$\boxed{\sigma_{1,2} = S \pm R}, \qquad \boxed{\tau_{max} = R}$$

![[mohrova_kroznica.svg|697]]

![[mohr_naloga1.svg|697]]

![[mohr_naloga2.svg|697]]

![[mohr_naloga3.svg|697]]

![[mohr_naloga4.svg|697]]

![[mohr_naloga5.svg|697]]

⚠️ **PAST:** Kot na Mohrovi krožnici je $2\varphi_0$ — v fizičnem prostoru je $\varphi_0$!

**3D tenzor** (N2 Vaje Mohr): Karakteristična enačba $\det([\sigma]-\sigma I)=0$ → kubična enačba → $\sigma_1 \geq \sigma_2 \geq \sigma_3$.

**Iz deformacij** (N4 Vaje Mohr): Lame-jev zakon:

$$\sigma_x = \frac{E}{(1+\nu)(1-2\nu)}\left[(1-\nu)\varepsilon_x+\nu(\varepsilon_y+\varepsilon_z)\right]$$

$$\tau_{xy} = G\cdot\gamma_{xy}, \qquad G = \frac{E}{2(1+\nu)}$$

---

## TIP E: HIPOTEZE PORUŠITVE — Tresca + Von Mises (N5 Vaje Mohr, N16 Poglavje Trdnost)

**Izhodišče:** Kdaj material poruši? → primerjaj $\sigma_{ekv}$ s $\sigma_{dop}$.

**Von Mises** (distorzijska energija — bolj natančna):

$$\boxed{\sigma_{ekv,VM} = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop}}$$

Za splošno 3D stanje:

$$\sigma_{ekv,VM} = \frac{1}{\sqrt{2}}\sqrt{(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2}$$

**Tresca** (maksimalna strižna napetost — konzervativnejša):

$$\boxed{\sigma_{ekv,T} = \sqrt{\sigma^2 + 4\tau^2} = \max(|\sigma_1-\sigma_2|,|\sigma_2-\sigma_3|,|\sigma_3-\sigma_1|) \leq \sigma_{dop}}$$

⚠️ **Tresca je vedno ≥ Von Mises** → varnostni inženir: Tresca; ekonomičen: VM.

![[hipoteze_porusitve.svg|674]]

**Za 2D** ($\sigma_3 = 0$, ravninsko napetostno stanje):

$$\sigma_{ekv,VM} = \sqrt{\sigma_1^2 - \sigma_1\sigma_2 + \sigma_2^2}, \qquad \sigma_{ekv,T} = |\sigma_1 - \sigma_2| \quad \text{(če sta istega predznaka: }|\sigma_1|\text{ ali }|\sigma_2|\text{)}$$

---

![[trdnost_n1.svg|697]]

![[trdnost_n2.svg]]

![[trdnost_n3.svg]]

![[trdnost_n4.svg]]

![[trdnost_n5.svg]]

![[trdnost_n6.svg]]

![[upogib_lesen_nosilec.svg]]

![[upogib_U_prerez_napetosti.svg]]

![[reakcije_U_prerez_razlaga.svg]]

## TIP F: UKLON — EULER (N2, N6 — Vaje Trdnost; N19, N20 — Poglavje Trdnost)

**Izhodišče:** Tanka palica pod tlačno silo → nenadna bočna deformacija.

**Euler kritična sila:**

$$\boxed{F_k = \frac{\pi^2 E I_{min}}{l_u^2}}$$

kjer je $l_u = \beta \cdot L$ = uklonska dolžina.

**Robni pogoji → $\beta$:**

| Tip stebra | $\beta$ | $l_u$ |
|-----------|---------|--------|
| Prosto-prosto (prostoležeč) | 1 | $L$ |
| Konzola (vpeto-prosto) | 2 | $2L$ |
| Vpeto-vpeto (obe konci fiksni) | 0,5 | $L/2$ |
| Vpeto-pomično | 0,7 | $0{,}7L$ |

**Vitkost:**

$$\boxed{\lambda = \frac{l_u}{i_{min}}}, \qquad i_{min} = \sqrt{\frac{I_{min}}{A}}$$

**Euler velja za** $\lambda > \lambda_E$:

$$\lambda_E = \pi\sqrt{\frac{E}{\sigma_{dop}}}$$

**Varnostni faktor:**

$$\boxed{\nu = \frac{F_k}{F} \geq \nu_{zaht}} \quad (\nu_{zaht} = 3\text{–}5 \text{ za les})$$

**Šibka os** (N6 Vaje): Uklon vedno po osi z $I_{min}$! Za pravokotnik $b \times h$ ($b < h$):

$$I_{min} = \frac{h \cdot b^3}{12}$$

---

## TIP G: UKLON — TETMAJER (N21 — Poglavje Trdnost)

**Izhodišče:** Za $\lambda_P < \lambda < \lambda_E$ (srednje vitke palice) Euler ni veljaven → Tetmajer:

$$\boxed{\sigma_k = a_T - b_T \cdot \lambda}$$

**Koeficienti za les (iglavci/smreka):**
$a_T = 2{,}93\ \text{kN/cm}^2$, $b_T = 0{,}0194\ \text{kN/cm}^2$

**Meja območij:**

```
λ < λP (~60 za les):    zdrs materiala → σ_dop direktno (ni uklona)
λP < λ < λE (~90 za les): TETMAJER — linearna σk-λ
λ > λE:                  EULER — parabolična (Fk = π²EI/lu²)
```

**Postopek Tetmajer:**
```
1. i = √(I/A)
2. λ = lu/i
3. λE = π·√(E/σdop)
4. Je λ < λE? → Tetmajer; λ > λE? → Euler
5. σk = aT - bT·λ
6. Fk = σk·A
7. ν = Fk/F ≥ ν_zaht
```

---

## TIP H: TORZIJA — POLNA GRED (N17 — Poglavje Trdnost; N5 — Vaje Trdnost)

**Izhodišče:** Torzijsko napetostno stanje — strižna napetost po obodu:

$$\tau = \frac{M_t \cdot \rho}{I_p}$$

Na zunanjem robu ($\rho = R$):

$$\boxed{\tau_{max} = \frac{M_t}{W_t}}$$

**Torzijski odpornostni momenti:**

| Prerez | $W_t$ | Zveza z $W$ |
|--------|-------|------------|
| Polni krog $d$ | $\dfrac{\pi d^3}{16}$ | $W_t = 2W$ |
| Votel krog $D, d$ | $\dfrac{\pi(D^4-d^4)}{16D}$ | — |
| Kvadrat $a$ | $\approx 0{,}208\,a^3$ | — |

⚠️ Za krog: $W_t = 2W$ (ker $I_p = 2I$)!

---

## TIP I: TORZIJA — BREDT za votli tankostenski prerez (N18 — Poglavje Trdnost)

**Izhodišče:** Bredtova formula za zaprt tankostenski profil:

$$\boxed{\tau = \frac{M_t}{2 \cdot A_m \cdot t}}$$

kjer je $A_m$ = ploščina, ki jo **oklepa** srednja linija stene (ne zunanja, ne luknja!).

**Za pravokotni votli profil** $B \times H$, stena $t$:

$$A_m = (B-t)(H-t)$$

⚠️ **BREDTOVA PAST:** $A_m \neq B \cdot H$ (zunanja) in $\neq (B-2t)(H-2t)$ (notranja luknja)!  
→ Srednja linija teče po SREDINI stene.

**Bredt velja samo za:**
- Zaprte profile (brez razrezov!)
- Tankostenski ($t \ll B, H$)
- Enakomerna ali znana $t$

---

## TIP J: SESTAVLJENE OBREMENITVE — N + M + $M_t$ (N22 "Rezkar" — Poglavje Trdnost)

**Izhodišče:** Superpozicija + Von Mises/Tresca.

**Korak za korakom:**

```
1. Izračunaj Mmax = F⊥·L  (upogib od prečne sile)
2. σM = Mmax/W            (upogibna napetost)
3. σN = FN/A              (osna napetost, pazi na predznak!)
4. σ = σM ± σN            (superpozicija — kritično vlakno!)
5. τ = Mt/Wt              (torzijska napetost)
6. σekv = √(σ²+3τ²) ≤ σdop  (Von Mises)
   ALI
   σekv = √(σ²+4τ²) ≤ σdop  (Tresca)
```

**Kritično vlakno** = tisto, kjer sta $\sigma_M$ in $\sigma_N$ istega predznaka (aditivna)!

> **Pouk rezkar:** Torzija dominira pri majhnih prerezih ($\tau \propto 1/d^3$, $\sigma \propto 1/d^3$ → oba naraščata enako, a $3\tau^2$ je hujši).

---

# ═══════════════════════════════════
# SKLOP 3 — KINEMATIKA
# ═══════════════════════════════════

## OSNOVA: Kinematika = geometrija gibanja (brez sil)

$$v = \frac{ds}{dt} = \dot{s}, \qquad a = \frac{dv}{dt} = \ddot{s}, \qquad \omega = \dot{\varphi}, \qquad \alpha = \dot{\omega}$$

**Zveze za kotno in obodno gibanje:**

$$\boxed{v = \omega \cdot R}, \qquad \boxed{a_t = \alpha \cdot R}, \qquad \boxed{a_n = \omega^2 \cdot R = \frac{v^2}{\rho}}$$

---

## GIBALNA STANJA — primerjalna tabela

| Stanje | Pogoj | $s(t)$ / $\varphi(t)$ | $v(t)$ / $\omega(t)$ | $a_t$ | $a_n$ |
|--------|-------|----------------------|----------------------|-------|-------|
| Premočrtno enakomerno | $a=0$ | $s = v_0 t$ | $v = v_0$ | 0 | 0 |
| Premočrtno enakopospešeno | $a=\text{const}$ | $s = v_0t + \tfrac{1}{2}at^2$ | $v = v_0+at$ | $a\neq0$ | 0 |
| Enakomerno krožno | $\omega=\text{const}$ | $\varphi = \omega t$ | $\omega = \text{const}$ | 0 | $\omega^2 R$ |
| Neenakomerno krožno | $\alpha\neq0$ | $\varphi = \varphi_0+\omega_0 t+\tfrac{1}{2}\alpha t^2$ | $\omega = \omega_0+\alpha t$ | $\alpha R$ | $\omega^2 R$ |
| Harmonično | $\ddot{x}+\omega_0^2 x=0$ | $x=A\cos(\omega_0 t+\phi)$ | $v=-A\omega_0\sin(...)$ | $-\omega_0^2 x$ | — |

**Pretvorba:** $\omega = \dfrac{2\pi n}{60}$ [rad/s], kjer je $n$ v obr/min.

---

## TIP A: KINEMATIKA TOČKE — $a_t$, $a_n$, $a$ (N1 — Poglavje Kin+Din)

```
1. ω(t) = ω₀ + α·t
2. at = α·R      ← menja velikost v (vzdolž tangente)
3. an = ω²·R     ← menja smer v (kaže PROTI središču!)
4. a = √(at² + an²)
5. Smer a: φ = arctan(an/at) od tangente
```

⚠️ $a_n$ je **vedno** prisoten pri krogilnem gibanju (razen $\omega=0$). Naraste s $\omega^2$!

---

## TIP B: POL HITROSTI — splošna metoda (N2–N4 — Poglavje Kin+Din)

**Izhodišče:** Vsako ravninsko gibanje togega telesa = vrtenje okrog trenutnega pola P (kjer $v_P = 0$).

$$\boxed{v_A = \omega \cdot \overline{PA}} \qquad \text{(smer: ⊥ na } \overrightarrow{PA}\text{)}$$

**Iskanje pola P:**
```
1. Nariši mehanizem v danem položaju
2. Za vsako točko z znano smerjo v: nariši pravokotnico na v
3. P = presečišče pravokotnic
4. ω = v_znana / r_P,znana
5. v_iskana = ω · r_P,iskana  (smer: ⊥ na r_P,iskana)
```

⚠️ **PAST:** Pravokotnica NA HITROST, ne na telo!

**Posebni primeri:**

| Gibanje | Pol P |
|---------|-------|
| Kolo se kotali | P = stična točka s podlago |
| Translacija | P v neskončnosti (vse točke enaka v) |
| Čisto vrtenje okrog O | P = O |
| Obe ročici vzporedni | Translacijski položaj → pol v ∞ → $v_C = v_D$ |

---

## TIP B1: KOLO NA RAVNINI — kotaljenje (N2 — Poglavje Kin+Din)

```
P = stična točka (spodaj), r_PC = R
ω = vC/R
v_vrh = ω·2R = 2vC
v_točke A (na robu, 90° od vrha): rPA = R√2  →  vA = ω·R√2
Smer vsake hitrosti: ⊥ na PX (kjer je X točka)
```

---

## TIP B2: BAT-KLIP DRSNIK (N3 — Poglavje Kin+Din)

**Ročica AB** ($A$ drsi vodoravno, $B$ navpično), naklon $\theta$ od vodoravnice:

```
Koordinate: A = (L·cosθ, 0),  B = (0, L·sinθ)
P = (L·cosθ, L·sinθ)
rPA = L·sinθ,  rPB = L·cosθ
ω = vA / rPA = vA / (L·sinθ)
vB = ω · rPB = vA · cosθ/sinθ = vA/tanθ
```

---

## TIP C: CORIOLISOV POSPEŠEK (N5 — Poglavje Kin+Din)

**Izhodišče:** Sestavljeno gibanje = transportno + relativno:

$$\vec{a}_{abs} = \vec{a}_{rel} + \vec{a}_{trans} + \vec{a}_{Cor}$$

$$\boxed{a_{Cor} = 2\omega \cdot v_{rel}}$$

Smer: ⊥ na $v_{rel}$ v smeri vrtenja.

**Pogoji:** Pojavi se SAMO ko **$\omega \neq 0$** IN **$v_{rel} \neq 0$** hkrati!

```
1. a_trans,n = ω²·r  (centripetalni — kaže proti osi)
2. a_trans,t = α·r   (samo če α≠0)
3. a_rel = 0         (če v_rel=const vzdolž žleba)
4. a_Cor = 2ω·v_rel  (⊥ na v_rel)
5. a_abs = √(a_trans,n² + a_Cor²)  (vektorsko!)
```

---

# ═══════════════════════════════════
# SKLOP 4 — DINAMIKA
# ═══════════════════════════════════

## OSNOVA: Newton II — vzrok gibanja

$$\boxed{\sum \vec{F} = m\vec{a}} \qquad \text{(translacija)}$$

$$\boxed{\sum M_O = I_O \cdot \alpha} \qquad \text{(rotacija okrog fiksne osi)}$$

**D'Alembert:** Dodaj inercijsko silo $(-m\vec{a})$ → reši kot statiko:

$$\sum \vec{F} + (-m\vec{a}) = 0$$

---

## TIP D: NEWTON II — DVE KLADI (N6 — Poglavje Kin+Din)

**Postopek (sistem z vrvico čez škripec):**
```
1. FBD za vsako telo LOČENO
2. Kladivo m₁ (↓+): m₁g - S = m₁a         (1)
3. Kladica m₂ (→+): S - μm₂g = m₂a         (2)
4. Seštej (1)+(2): m₁g - μm₂g = (m₁+m₂)a
5. a = (m₁g - μm₂g)/(m₁+m₂)
6. S = m₁g - m₁a  (iz enačbe 1)
7. Kontrola: S = m₂a + μm₂g ✓
```

---

## TIP E: NEWTON II — KLANEC S TRENJEM (N7 — Poglavje Kin+Din)

```
N = mg·cosα
F_tr = μk·N = μk·mg·cosα
F_net = mg·sinα - F_tr = mg(sinα - μk·cosα)
a = g(sinα - μk·cosα)
v(t) = a·t  (začetek iz mirovanja)
s(t) = ½·a·t²
```

---

## MOMENTI INERCIJE TOGIH TELES

| Telo | Os | $I$ |
|------|----|-----|
| Točkasta masa $m$ na $r$ | os vrtenja | $mr^2$ |
| Palica $L$, masa $m$ | Skozi konec ⊥ | $\dfrac{mL^2}{3}$ |
| Palica $L$, masa $m$ | Skozi sredino ⊥ | $\dfrac{mL^2}{12}$ |
| Disk/valj $R$ | Os vrtenja | $\dfrac{mR^2}{2}$ |
| Obroč $R$ | Os vrtenja | $mR^2$ |
| Sfera $R$ | Premer | $\dfrac{2mR^2}{5}$ |

**Steinerjev stavek** (os izven težišča):

$$\boxed{I_O = I_T + m \cdot d^2}$$

---

## TIP F: DINAMIKA TOGEGA TELESA — ROTACIJA (N9 — Poglavje Kin+Din)

```
1. Izračunaj I_O (s Steinerjem, če treba)
2. Newton II za rotacijo: ΣM_O = I_O·α
3. α = M_navor/I_O
4. ω(t) = ω₀ + α·t
5. n = ω·60/(2π)  [obr/min]
```

⚠️ **ENOTE:** Masa MORA biti v **kg** (ne kN!). $F = ma \Rightarrow [kN] = [t\cdot m/s^2]$

---

## TIP G: ENERGETSKI ZAKONI (N8 — Poglavje Kin+Din)

**Izrek o delu:**

$$\boxed{A_{net} = \Delta E_k = E_{k2} - E_{k1}}$$

**Energijska ohranitev** (brez trenja, brez dušenja):

$$\boxed{E_{k1} + E_{p1} = E_{k2} + E_{p2}}$$

$$E_k = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2, \qquad E_{p,grav} = mgh, \qquad E_{p,vzmet} = \tfrac{1}{2}kx^2$$

**Vzmet sprošča iz stisnjenja $x_0$** (N8):

$$\tfrac{1}{2}kx_0^2 = \tfrac{1}{2}mv^2 \quad \Rightarrow \quad \boxed{v_{max} = x_0\sqrt{\frac{k}{m}} = x_0\cdot\omega_0}$$

| Metoda | Kdaj | Kar dobimo |
|--------|------|------------|
| Newton II | Iščemo sile ali pospeške | $F(t)$, $a(t)$ |
| Izrek o delu | Iščemo hitrosti (brez a) | $v$ direktno |
| Energijska ohranitev | Konzervativni sistem | $v$ pri dani legi |

---

## TIP H: NIHANJE — LASTNA FREKVENCA (N10, N11 — Poglavje Kin+Din)

**Izhodišče:** Masa na vzmeti (enodimenzionalni nihajnik):

$$m\ddot{x} + kx = 0$$

$$\boxed{\omega_0 = \sqrt{\frac{k}{m}}} \quad [\text{rad/s}], \qquad \boxed{f_0 = \frac{\omega_0}{2\pi}} \quad [\text{Hz}], \qquad \boxed{T_0 = \frac{2\pi}{\omega_0}} \quad [\text{s}]$$

**Vzporedne vzmeti:** $k_{eq} = k_1 + k_2 + \ldots$

**Zaporedne vzmeti:** $\dfrac{1}{k_{eq}} = \dfrac{1}{k_1} + \dfrac{1}{k_2} + \ldots$

**Nihanje z dušenjem:**

$$m\ddot{x} + c\dot{x} + kx = 0, \qquad \xi = \frac{c}{2\sqrt{km}}, \qquad \omega_d = \omega_0\sqrt{1-\xi^2}$$

---

## TIP I: RESONANCA (N11 — Poglavje Kin+Din)

**Prisilno nihanje:** $m\ddot{x}+kx = F_0\sin(\Omega t)$

$$\text{Resonanca}: \Omega = \omega_0 \quad \Rightarrow \quad A \to \infty \text{ (brez dušenja)}$$

**Praktično:** Priporoča se $|\Omega/\omega_0 - 1| > 20\%$

**Delovni obrati:** $\omega_{delo} = \dfrac{2\pi n}{60}$ → primerjaj z $\omega_0$

**Ukrepi:** sprememba $n$, dodaj maso ($\omega_0 \downarrow$), ojači vzmet ($\omega_0 \uparrow$), dušilnik.

---

# ═══════════════════════════════════
# HITRE FORMULE — IZPITNI LIST
# ═══════════════════════════════════

## STATIKA

$$\sum F_x=0,\ \sum F_y=0,\ \sum M_A=0 \quad \text{(2D)}$$

$$W_{tip} = I/e, \quad y_T = \frac{\sum A_iy_i}{\sum A_i}, \quad I = \sum\left(\frac{bh^3}{12}+A_id_i^2\right)$$

$$F_{tr} \leq \mu N, \quad \tan\alpha\leq\mu_s, \quad \frac{F_1}{F_2}=e^{\mu\theta}$$

## TRDNOST

$$M_{max}=A_y\cdot x_{T=0}-\ldots,\quad W_{min}=M/\sigma_{dop},\quad \sigma=M/W$$

$$S=\frac{\sigma_x+\sigma_y}{2},\ R=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau^2},\ \sigma_{1,2}=S\pm R$$

$$\sigma_{ekv,VM}=\sqrt{\sigma^2+3\tau^2},\quad \sigma_{ekv,T}=\sqrt{\sigma^2+4\tau^2}$$

$$F_k=\frac{\pi^2EI_{min}}{l_u^2},\quad \lambda=\frac{l_u}{i},\quad \lambda_E=\pi\sqrt{\frac{E}{\sigma_{dop}}},\quad \sigma_k=a_T-b_T\lambda$$

$$\tau=\frac{M_t}{W_t}\ \text{(polna)},\quad \tau=\frac{M_t}{2A_m t}\ \text{(Bredt)}$$

## KINEMATIKA + DINAMIKA

$$v=\omega R,\quad a_t=\alpha R,\quad a_n=\omega^2R,\quad a=\sqrt{a_t^2+a_n^2}$$

$$v_A=\omega\cdot r_{PA},\quad \text{Pol: presečišče ⊥ na }v$$

$$a_{Cor}=2\omega v_{rel}\quad (\omega\neq0,\ v_{rel}\neq0)$$

$$\sum F=ma,\quad \sum M_O=I_O\alpha,\quad I_O=I_T+md^2$$

$$A_{net}=\Delta E_k,\quad E_k+E_p=\text{const}$$

$$\omega_0=\sqrt{k/m},\quad T_0=2\pi/\omega_0,\quad f_0=\omega_0/(2\pi)$$

---

## Povezave

- [[Poglavje - Statika]] ← vse naloge 1. sklopa
- [[Poglavje - Trdnost]] ← vse naloge 2. sklopa
- [[Poglavje - Kinematika in Dinamika]] ← vse naloge 3.+4. sklopa
- [[Vaje - Statika - Vse vrste]] ← rešene statika vaje
- [[Vaje - NTM diagrami - Vse vrste]] ← rešene NTM vaje
- [[Vaje - Trdnost in dimenzioniranje]] ← rešene trdnostne vaje
- [[Vaje - Napetostni tenzor in Mohrova kroznica]] ← rešene tenzorske vaje
- [[Blok 0 - Statika]] | [[Blok 1 - NTM Diagrami]] | [[Blok 2 - Upogib]]
- [[Blok 3 - Napetostno Stanje]] | [[Blok 3.5 - Hipoteze Porusitve]]
- [[Blok 4 - Euler Uklon]] | [[Blok 5 - Torzija]]
- [[Blok 6 - Kinematika]] | [[Blok 7 - Dinamika Nihanje]]
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
