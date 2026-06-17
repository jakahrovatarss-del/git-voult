---
tags: [mehanika, upogib, napetosti, dimenzioniranje, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 2 — Upogib: Napetosti in Dimenzioniranje

## VSE ENAČBE

```
NORMALNA NAPETOST PRI UPOGIBU:
  σ(z) = My / Iy · z
  σmax = Mmax / W  ≤ σdop

ODPORNOSTNI MOMENTI:
  Pravokotnik b×h:   W = b·h²/6
  Krog d:             W = π·d³/32
  h=2b:               W = 2b³/3

DIMENZIONIRANJE:
  Wmin = Mmax / σdop
  h=2b:  b = ∛(3Wmin/2)
  krog:  d = ∛(32M / π·σdop)

STRIG PRI UPOGIBU (Žuravski):
  τ = T·S / (I·b)
  Pravokotnik: τmax = 1.5·T/A   (v nevtralni osi)

EKSCENTRIČNO (N + M):
  σmax = N/A - M/W   (stran sile = VEČJA tlačna)
  σmin = N/A + M/W   ⚠ mogoč NATEG!

MATERIALNI PODATKI:
  Les:   E=1000 kN/cm²,  σdop = 1.0–1.2 kN/cm²
  Jeklo: E=21000 kN/cm², σdop = 16 kN/cm²
```

---

## Intuicija

### Fizikalna slika — "Vlakna se raztegujejo in krčijo"

Ko upogneš nosilci, vlakna nad nevtralno osjo se **stlačijo** (tlak), vlakna pod njo se **raztegnejo** (nateg). Nevtralna os je ravno na sredini — tam deformacija = 0, napetost = 0.

> *Vizualizacija:* Upogni ravnilo. Rob, ki se skrajša = tlak. Rob, ki se podaljša = nateg. Ravno v sredini se nič ne zgodi — to je nevtralna os.

**Analogija — knjiga v roki:** Ko upogneš knjigo, hrbet se raztegne, spredaj se stisne. Listi na sredini se komaj premaknejo. Če bi bila knjiga iz jekla — tisti najdaljši list (najdlje od sredine) bi bil najbolj obremenjen.

---

### Miselni eksperiment — "Povečaj višino prereza"

Pravokotnik $b \times h$. Podvoji $h$ (višino):
- $W = bh^2/6$ → $W$ se poveča **4×**
- $\sigma_{max} = M/W$ → napetost pade **4×** pri istem momentu!

Podvoji $b$ (širino):
- $W$ se poveča le **2×**

**Sklep:** Višina prereza je daleč bolj učinkovita kot širina. Zato so nosilci visoki in ozki, ne nizki in široki.

---

### Zakaj enačba izgleda tako?

$$\sigma(y) = \frac{M \cdot y}{I}, \qquad \sigma_{max} = \frac{M}{W} = \frac{M \cdot e_{max}}{I}$$

**Zakaj $M \cdot y$?** Ker pri upogibu se prerez zavrti za kot $\kappa$ (ukrivljenost). Fiber na razdalji $y$ od osi se raztegne za $y \cdot \kappa$ → deformacija $\varepsilon = y \cdot \kappa$ → napetost $\sigma = E \cdot y \cdot \kappa$. Konstanta $M/(EI)$ zamenja $\kappa$.

**Zakaj delimo z $I$ (in ne z $A$)?** Ker $A$ opisuje površino, $I$ pa opisuje, kako je ta površina porazdeljena. Pri upogibu ni važno, koliko materiala je — važno je, **kje** je.

> *Enote:* $[M/W] = \frac{\text{kNm}}{\text{m}^3} = \frac{\text{kN}}{\text{m}^2} = \text{MPa}$ ✓

---

### Mejni primeri (sanity check)

| Situacija | Pričakuješ |
|---|---|
| $y = 0$ (nevtralna os) | $\sigma = 0$ — nič napetosti |
| $y = e_{max}$ (rob prereza) | $\sigma = \sigma_{max}$ — maksimalna napetost |
| $M = 0$ (ni obremenitve) | $\sigma = 0$ povsod |
| Asimetričen prerez (T, L) | $\sigma_{nateg} \neq \sigma_{tlak}$ — kritičen je manjši $W$! |

> ⚠️ **Za asimetričen prerez:** Izračunaj oba $W_{zg} = I/e_{zg}$ in $W_{sp} = I/e_{sp}$. Manjši je kritičen!

---

### Veriga vzrokov → Blok 3 in Blok 2.5

Ko imaš $\sigma_{max}$:
- → [[Blok 3 - Napetostno Stanje|Blok 3]]: sestavi napetostni tenzor ($\sigma_x = \sigma$, $\tau_{xy}$ iz Žuravski)
- → [[Blok 2.5 - Deformacije pri Upogibu|Blok 2.5]]: izračunaj poves $y_{max}$ (iste enačbe, samo integrirane)
- → [[Blok 3.5 - Hipoteze Porusitve|Blok 3.5]]: preveri trdnost z Von Mises ali Tresca

> **Povzetek:** M → napetost ($\sigma = M/W$) → tenzor → porušitev.

> **glej:** [[Blok 3 - Napetostno Stanje#Intuicija]]

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "preveri trdnost", "dimenzioniranje prereza"
- "dopustna napetost $\sigma_{dop}$"
- "določi $b$ in $h$", "minimalni prerez"
- "pravokoten prerez $h = 2b$"
- Podano: $M_{max}$ ali celoten nosilec z obtežbo

**Kaj je podano:**
- $M_{max}$ [kNm ali kNcm] — ali računamo sami iz bloka 1
- Oblika prereza: $h = 2b$, krog, T-prerez...
- Material: $\sigma_{dop}$ [kN/cm²]

**Kaj se sprašuje:**
- Minimalne dimenzije prereza ($b$, $h$, $d$)
- Maksimalna napetost $\sigma_{max}$
- Ali je prerez ustrezen ($\sigma_{max} \leq \sigma_{dop}$)

---

## Kako začeti reševati

**Korak 1 — Poišči $M_{max}$** (iz Blok 1 ali formula):

| Sistem | $M_{max}$ |
|--------|-----------|
| Prostoležeč $q$ | $qL^2/8$ |
| Prostoležeč $F$ sr. | $FL/4$ |
| Konzola $F$ | $FL$ |
| Konzola $q$ | $qL^2/2$ |

> ⚠️ **Enote:** $M$ v kNcm (prevedi m→cm, krat 100)!

**Korak 2 — Izračunaj $W_{min}$:**
$$W_{min} = \frac{M_{max}}{\sigma_{dop}}$$

**Korak 3 — Dimenzioniranje iz oblike prereza:**

| Prerez | Enačba | Rešitev |
|--------|--------|---------|
| $h = 2b$ | $W = 2b^3/3$ | $b = \sqrt[3]{3W_{min}/2}$ |
| Krog $d$ | $W = \pi d^3/32$ | $d = \sqrt[3]{32W_{min}/\pi}$ |

**Korak 4 — Zaokroži navzgor** (na mm ali cm) in **kontroliraj:**
$$\sigma_{dej} = \frac{M_{max}}{W_{dej}} \leq \sigma_{dop} \quad ✓$$

---

## Asimetričen prerez — Steiner postopek

Velja za T-, L-, U-prereze:

1. $y_T = \sum A_i y_i / \sum A_i$
2. $J = \sum (b_i h_i^3/12 + A_i d_i^2)$, kjer $d_i = y_i - y_T$
3. $W_{sp} = J / e_{sp}$, $W_{zg} = J / e_{zg}$
4. Preveri **oba roba**: $\sigma = M / W$ — kritičen je **manjši $W$**!

---

## Strižne napetosti pri upogibu (Žuravski)

$$\tau = \frac{T \cdot S}{I \cdot b}$$

- $S$ = statični moment dela prereza nad točko
- Za **pravokotnik** — maksimum v nevtralni osi:

$$\tau_{max} = 1{,}5 \cdot \frac{T}{A}$$

- Za **I-profil** — maksimum v stojini:

$$\tau_{max} = \frac{T \cdot S_{max}}{I \cdot t_{stojine}}$$

---

## Ekscentrična obremenitev (N + M)

$$\sigma = \frac{N}{A} \pm \frac{M}{W}$$

| Stran | Enačba | Opomba |
|-------|--------|--------|
| Stran sile (večji tlak) | $\sigma_{max} = N/A - M/W$ | Tlak = negativno |
| Nasprotna stran | $\sigma_{min} = N/A + M/W$ | Lahko NATEG! |

> ⚠️ Kljub tlačni sili $N$ se na nasprotni strani pojavi **nateg** — morda nevaren za beton/les!

---

## Diferencialna enačba upogibnice

$$EI \cdot y'' = M(x) \quad \Rightarrow \quad y(x) = \frac{1}{EI} \iint M(x)\, dx^2 + C_1 x + C_2$$

Konstanti iz robnih pogojev:
- Prostoležeč: $y = 0$ pri obeh podporah
- Vpetje: $y = 0$, $y' = 0$

→ **Podrobneje:** [[Blok 2.5 - Deformacije pri Upogibu]]

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Posebnost |
|-----|----------------|-----------|
| Dimenzioniranje $h=2b$ | "pravokoten prerez", "les" | $b = \sqrt[3]{3W/2}$ |
| T-prerez Steiner | "varjeni prerez", "T-profil" | OBA $W$! |
| Ekscentrično N+M | "steber", "ekscentrično" | NATEG možen! |
| Strig preverjanje | "strižna napetost", "strig" | Žuravski |
| Krog $d$ | "okrogel", "gredi" | $W = \pi d^3/32$ |

---

## Kombinacije z drugimi bloki

### Blok 1 + 2 (NTM → Upogib) ← **OSNOVA**
Najpogostejši zaporedje:
1. Reakcije (Blok 0)
2. $M_{max}$ (Blok 1)
3. $W_{min}$, dimenzije (Blok 2)

### Blok 1.5 + 2 (Steiner + Upogib)
T-prerez: najprej Steiner → $J$, $W_{sp}$, $W_{zg}$, nato $\sigma$.

### Blok 2 + 3.5 (Upogib + VM/Tresca)
Gredi: $\sigma = M/W$ iz upogiba, $\tau = Mt/Wt$ iz torzije → VM.

### Blok 2 + 4 (Upogib + Euler Uklon)
Steber z ekscentrično obremenitvijo: N+M kombinacija + uklon kontrola.

---

## Materialni podatki

| Material | $\sigma_{dop}$ [kN/cm²] | $E$ [kN/cm²] |
|----------|------------------------|--------------|
| Les (iglavci) | 1,0 – 1,2 | 1 000 |
| Jeklo S235 | 16 | 21 000 |
| Beton (tlak) | 1,5 – 2,5 | 3 000 |

---

## Profesorjev »ček-list«

1. ⚠️ **Enote:** $M$ v kNcm, $W$ v cm³, $\sigma$ v kN/cm² — ne mešaj m in cm!
2. $M_{max}$: tam kjer $T = 0$ (iščemo $x_0$: $dM/dx = 0$)
3. Asimetričen prerez: **oba** $W$, kritičen je **manjši**
4. $h = 2b$: najpogostejša lesarska naloga — $W = 2b^3/3$
5. ⚠️ **Vodoravna sila** $F_x$ ne prispeva k $\sum F_y$ — samo k momentu!
6. ⚠️ **U-prerez (asimetričen):** $e_{zg} \neq e_{sp}$ → zgornji rob je kritičen pri **OBEH** predznaknih momentih — ne samo pri večjem $|M|$!
7. **Votli prerez** (škatlast, cevi): $I = I_{zun} - I_{not}$ (metoda odštevanja!)
8. **Navierjev zakon** (porazdelitev σ po višini): $\sigma(y) = M \cdot y / I_z$ — linearna, max na robu!

---

## Primer iz izpita — U-prerez (asimetričen)

Previs z $F = 10$ kN in poljem z $q = 16$ kN/m, U-prerez $B = 40$ cm, $H = 15$ cm, $t = 7$ cm:

$$y_T = 5{,}64\ \text{cm od spodnjega roba}, \quad e_{zg} = 9{,}36\ \text{cm} > e_{sp} = 5{,}64\ \text{cm}$$

$$J = 6240{,}8\ \text{cm}^4, \quad M_A = -10\ \text{kNm}, \quad M_{max} = +8\ \text{kNm v polju}$$

| Prerez | $M$ [kNm] | Vlakno | $\sigma$ [kN/cm²] |
|--------|-----------|--------|-------------------|
| Podpora A | $-10$ | zgornji (nateg) | **+1,50** ← max nateg! |
| Polje | $+8$ | zgornji (tlak) | $-1,20$ |
| Polje | $+8$ | spodnji (nateg) | $+0,72$ |

> ⚠️ **Ključna ugotovitev:** Zgornji rob je kritičen pri obeh momentih! Samo primerjava $|M_A|$ vs $|M_{max}|$ ni dovolj — preveriti σ pri vsakem prerezu posebej.

> **Primer:** [[Naloga - Mehanika - Upogibne napetosti U-prerez]]

---

## Primer iz izpita — Dimenzioniranje (krožni prerez)

Za previsni nosilci $F = 4$ kN (vodoraven!), $q = 2$ kN/m, $\sigma_{dop} = 1{,}2$ kN/cm²:

**Ključno:** F vodoravna → ne prispeva k $\sum F_y$, samo ustvari moment $M_A = -6$ kNm pri A.

$$M_{mer} = 6{,}25\ \text{kNm} = 625\ \text{kNcm}$$

$$W_{min} = M_{mer}/\sigma_{dop} = 625/1{,}2 = 520{,}83\ \text{cm}^3$$

$$\frac{\pi d^3}{32} \geq 520{,}83 \quad \Rightarrow \quad d \geq \sqrt[3]{5305} = \boxed{17{,}44\ \text{cm}}$$

> **Primer:** [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]]

---

## Povezave

- [[Koncept - Upogib]] ← podrobna razlaga
- [[Blok 1.5 - Geometrijske Karakteristike]] ← I in W prereza
- [[Blok 2.5 - Deformacije pri Upogibu]] ← povesi
- [[Blok 3 - Napetostno Stanje]] ← kombinirana napetostna stanja
- [[Blok 3.5 - Hipoteze Porusitve]] ← VM, Tresca
- [[Vaje - Trdnost in dimenzioniranje]] ← N1 (h=2b), N3 (T-prerez), N4 (N+M)
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] ← asimetričen prerez, oba M
- [[Naloga - Mehanika - Upogibne napetosti C-prerez]] ← konzola, Navierjev zakon
- [[Naloga - Mehanika - Napetosti skatlaski profil]] ← votli prerez, σ > σdop primer
- [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]] ← vodoravna F, d_min
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] ← a×b iz x³=80
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
