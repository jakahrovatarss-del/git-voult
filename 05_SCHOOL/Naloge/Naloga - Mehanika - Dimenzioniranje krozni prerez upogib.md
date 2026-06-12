---
tags: [mehanika, upogib, dimenzioniranje, krozni-prerez, naloga]
predmet: Mehanika
datum: 2026-06-11
vir: IMG_1241.pdf, str. 24 (naloga), str. 26 (rešitev)
---

# Naloga: Dimenzioniranje krožnega prereza na upogib

## Namen

Določiti minimalni premer $d$ krožnega prereza previsnega nosilca, obremenjenega s točkovno silo $F$ in enakomerno obtežbo $q$.

## Podatki
Human: 2026-06-12 — Vyvanse ob 11:00 ✅

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| F | 4 kN | točkovna sila (vodoraven, ročica 1,5 m) |
| q | 2 kN/m | enakomerna obtežba v polju A–B |
| L_previs | 1,5 m | ročica sile F do podpore A |
| L_AB | 3 m | razpon med podporama |
| σ_dop | 1,2 kN/cm² | dopustna napetost |
| d | ? | premer krožnega prereza |

## Shema konstrukcije

[[upogib_krozni_prerez.svg|1020]] 

- **A** = leva podpora (pri x = 0)
- **B** = desna podpora (pri x = 3 m)
- Obtežba $q = 2$ kN/m deluje na polju A–B
- Sila $F = 4$ kN deluje **vodorovno** z ročico 1,5 m → ustvari moment pri A, a **ne prispeva k navpičnim silam!**

---

## Korak 1 — Reakcije

### Zakaj?

Preden računamo napetosti, moramo poznati notranjo silo — upogibni moment $M(x)$. Za to potrebujemo reakcije iz **ravnotežnih enačb statično določene konstrukcije**.

### ⚠️ F je vodoravna sila!

Sila $F = 4$ kN deluje **vodoravno** (ne navpično!):
- **ustvarja moment** pri A z ročico 1,5 m
- **ne prispeva** k vsoti navpičnih sil → v $\sum F_y$ je **ne pišemo**

### Izpeljava

**Moment okrog B** (izniči $B_y$, ker je njena ročica = 0):

$$\sum M_B = 0: \quad -F \cdot 1{,}5 - A_y \cdot 3 + q \cdot 3 \cdot 1{,}5 = 0$$

$$A_y \cdot 3 = \underbrace{q \cdot 3 \cdot 1{,}5}_{= 9} - \underbrace{F \cdot 1{,}5}_{= 6} = 3$$

$$\boxed{A_y = 1\ \text{kN}\quad\uparrow}$$

**Vsota navpičnih sil** ($F$ vodoravna → izpusti!):

$$\sum F_y = 0: \quad A_y + B_y = q \cdot 3 = 6\ \text{kN}$$

$$\boxed{B_y = 6 - 1 = 5\ \text{kN}\quad\uparrow}$$

**Moment pri A** (od horizontalne sile F):

$$M_A = -F \cdot 1{,}5 = -4 \cdot 1{,}5 = -6\ \text{kNm} \quad \text{(hogging)}$$

> **glej:** [[Koncept - Upogib#Korak 1 — Statični sistem in reakcije]]

---

## Korak 2 — Diagram upogibnih momentov

### Zakaj?

M-diagram pokaže, kje je **največji upogibni moment** — merodajni prerez za dimenzioniranje. Iščemo absolutno največ, ker tam je napetost največja.

### Izpeljava

Koordinata $x$ od **B** v levo (B = 0, A = 3 m):

$$M(x) = B_y \cdot x - \frac{q \cdot x^2}{2} = 5x - x^2 \quad [\text{kNm}]$$

**Preveritev robnih vrednosti:**

| Mesto | $x$ [m] | Izračun | $M$ [kNm] |
|-------|---------|---------|-----------|
| Podpora B | 0 | $0 - 0$ | **0** ✓ |
| Podpora A | 3 | $15 - 9$ | **6** kNm |
| Prosti konec | — | — | **0** ✓ |

**Lokacija maksimuma** — M je ekstremen tam, kjer je strižna sila $T = 0$:

$$\frac{dM}{dx} = 5 - 2x = 0 \quad \Rightarrow \quad x_0 = 2{,}5\ \text{m od B}$$

$$M_{max} = 5 \cdot 2{,}5 - (2{,}5)^2 = 12{,}5 - 6{,}25 = \boxed{+6{,}25\ \text{kNm}}$$

**Oblika M-diagrama:**
- **Polje A–B**: parabola (porazdeljena obtežba $q$) — sagging (pozitiven, upogib navzdol)
- **Na A**: $M_A = -6$ kNm — hogging (negativen) — od horizontalne $F$
- Ker $6{,}25 > 6{,}00$, je **merodajni moment** iz polja:

$$M_{mer} = 6{,}25\ \text{kNm} = \mathbf{625\ \text{kNcm}}$$

> 🔍 **Fizikalni pomen:** Pozitiven M (sagging) = nosilci se upogiba navzdol. Zgornja vlakna v tlaku, spodnja v nategu.

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov]]

---

## Korak 3 — Geometrija krožnega prereza

### Zakaj?

Da bi pogoj $\sigma \leq \sigma_{dop}$ izrazili z neznano $d$, potrebujemo $W_x$ kot funkcijo $d$.

### Izpeljava iz osnov

Za polni krog s premerom $d$:

$$I_x = \frac{\pi d^4}{64}$$

Razdalja od nevtralne osi do najbolj oddaljenega vlakna:

$$e = \frac{d}{2}$$

Odpornostni moment (iz definicije $W = I/e$):

$$W_x = \frac{I_x}{e} = \frac{\pi d^4 / 64}{d/2} = \frac{\pi d^4}{64} \cdot \frac{2}{d} = \boxed{\frac{\pi d^3}{32}}$$

> 🔍 **Fizikalni pomen:** $W \propto d^3$ — podvojitev premera zmanjša napetost **8×**! Premer je zelo učinkovit parameter za dimenzioniranje.

> **glej:** [[Koncept - Vztrajnostni moment#Korak 1 — Enačbe za enostavne prereze]]

---

## Korak 4 — Pogoj dopustne napetosti → izpeljava d

### Zakaj?

Pogoj varnega delovanja zahteva $\sigma \leq \sigma_{dop}$. Iz tega izpeljemo $W_{min}$, nato $d_{min}$.

### Izpeljava — korak za korakom

**Pogoj dopustne napetosti:**

$$\sigma = \frac{M_{mer}}{W_x} \leq \sigma_{dop}$$

**Minimalni odpornostni moment:**

$$W_x \geq \frac{M_{mer}}{\sigma_{dop}} = \frac{625\ \text{kNcm}}{1{,}2\ \text{kN/cm}^2} = 520{,}83\ \text{cm}^3$$

**Vstavimo $W_x = \pi d^3 / 32$:**

$$\frac{\pi d^3}{32} \geq 520{,}83$$

**Izrazimo $d^3$:**

$$d^3 \geq \frac{32 \cdot 520{,}83}{\pi} = \frac{16666{,}7}{3{,}1416} = 5305{,}2\ \text{cm}^3$$

**Korenimo (kubični koren, ker $W \propto d^3$):**

$$\boxed{d \geq \sqrt[3]{5305{,}2} \approx 17{,}44\ \text{cm}}$$

> 🔍 **Zakaj kubični koren?** Ker je $W \propto d^3$, moramo vzeti $\sqrt[3]{\cdot}$. Kvadratni koren bi bil napačen!

> **glej:** [[Koncept - Upogib#Korak 5 — Dimenzioniranje]]

---

## Korak 5 — Rezultat in kontrola

### Rezultat

$$\boxed{d_{min} = 17{,}44\ \text{cm}}$$

> V praksi zaokrožimo **navzgor** na standardni premer → npr. $d = 18\ \text{cm}$.

### Kontrola z $d = 17{,}44$ cm

**Dejanski odpornostni moment:**

$$W_{dej} = \frac{\pi \cdot (17{,}44)^3}{32} = \frac{\pi \cdot 5302{,}0}{32} = 521{,}0\ \text{cm}^3$$

**Dejanska napetost:**

$$\sigma_{dej} = \frac{M_{mer}}{W_{dej}} = \frac{625\ \text{kNcm}}{521{,}0\ \text{cm}^3} = 1{,}20\ \text{kN/cm}^2$$

**Preverjanje:**

$$\sigma_{dej} = 1{,}20\ \text{kN/cm}^2 \leq \sigma_{dop} = 1{,}20\ \text{kN/cm}^2 \quad ✓$$

> 🔍 **Pomen kontrole:** Smo točno na meji dopustne napetosti — izračun je pravilen. V praksi vzamemo večji $d$ za varnostno rezervo.

> **glej:** [[Koncept - Upogib#Korak 4 — Napetosti in predznak]]

---

## Povzetek korakov

| Korak | Vsebina | Ključna enačba | Rezultat |
|-------|---------|----------------|---------|
| 1 | Reakcije (⚠️ F vodoraven!) | $\sum M_B = 0$ | $A_y = 1$ kN, $B_y = 5$ kN |
| 2 | M-diagram, M_max | $M(x) = 5x - x^2$, $dM/dx = 0$ | $M_{mer} = 625$ kNcm |
| 3 | Geometrija prereza | $W_x = \pi d^3 / 32$ | izraz za $W(d)$ |
| 4 | Pogoj σ ≤ σ_dop | $W \geq M/\sigma_{dop}$, $d^3 \geq \ldots$ | $d^3 \geq 5305$ cm³ |
| 5 | Rezultat + kontrola | $d = \sqrt[3]{5305}$ | $d_{min} = 17{,}44$ cm ✓ |

---

## Spremenljivke

| Simbol | Vrednost | Pomen |
|--------|----------|-------|
| A_y | 1 kN | reakcija pri podpori A |
| B_y | 5 kN | reakcija pri podpori B |
| M_A | −6 kNm = −600 kNcm | moment pri A (hogging) |
| M_max | +6,25 kNm = 625 kNcm | max moment v polju (sagging) |
| M_mer | 625 kNcm | merodajni moment za dimenzioniranje |
| W_min | 520,83 cm³ | minimalni zahtevan odpornostni moment |
| W_x | πd³/32 | odpornostni moment krožnega prereza |
| d³ | 5305,2 cm³ | izračunano iz pogoja σ ≤ σ_dop |
| **d** | **≥ 17,44 cm** | **minimalni premer** |
| W_dej | 521,0 cm³ | dejanski W pri d = 17,44 cm |
| σ_dej | 1,20 kN/cm² | dejanska napetost = σ_dop ✓ |

---

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]]
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]]
- [[Naloga - Mehanika - Upogibne napetosti C-prerez]]
- [[Naloga - Mehanika - Napetosti skatlaski profil]]
- [[Mehanika Hub]]
