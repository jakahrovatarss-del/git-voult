---
tags: [mehanika, upogib, dimenzioniranje, napetost, M-diagram, reakcije, Steiner, koncept]
predmet: Mehanika
datum: 2026-06-11
---

# Koncept: Upogib (Bending)

## Namen

Upogib nastopi, ko prečna obtežba povzroči ukrivljanje nosilca. Vzdolž prereza nastanejo **normalne napetosti** — tlačne na eni strani in natezne na drugi nevtralne osi (NO).

**Osnovna enačba:**

$$\boxed{\sigma = \frac{M \cdot e}{J} = \frac{M}{W} \leq \sigma_{dop}}$$

---

## Korak 1 — Statični sistem in reakcije

### Tipi statičnih sistemov

| Sistem | Opis | Prosto. konci | Neznanke |
|--------|------|---------------|----------|
| Prostoležeč nosilci | 2 členkasti podpori (A, B) | 2 | R_A, R_B |
| Konzola | 1 vpetje | 0 | R, M_vpetje |
| Previsni nosilci | 2 podpori + previs(i) | 1–2 | R_A, R_B |

### Splošni postopek — korak za korakom

**1. Nariši prosto telo** (FBD) — vrisaj vse zunanje sile in nadomesti podpore z reakcijami.

**2. Identificiraj smer vsake sile:**
- Navpične sile → prispevajo k $\sum F_y$ in $\sum M$
- Vodoravne sile → prispevajo k $\sum F_x$ in $\sum M$ (ampak **NE** k $\sum F_y$!)
- Momenti → prispevajo direktno k $\sum M$

**3. Vzemi moment okrog podpore** z **dvema** neznanima — tako odpade ena enačba:

$$\sum M_B = 0 \quad \Rightarrow \quad A_y = \ldots \quad \text{(B se izniči)}$$

**4. Navpično ravnotežje** (vodoravnih sil NE vključuj!):

$$\sum F_y = 0 \quad \Rightarrow \quad B_y = \sum F_y^{zunaj} - A_y$$

**5. Preveri** z momentom okrog A (rezultat mora biti 0).

### ⚠️ Najpogostejše napake

| Napaka | Posledica | Kako se izogniti |
|--------|-----------|-----------------|
| Vodoravno silo $F_H$ vključiš v $\sum F_y$ | Napačna $B_y$ | Vedno preverti smer sile |
| Napačen predznak momenta | Napačen predznak reakcije | Določi konvencijo: ↺ = + ali ↻ = + in se drži |
| Rezultanta $q$ na napačnem mestu | Napačen $M$ | $Q = q \cdot L$ deluje na **sredini** razpona $L$ |
| Pozabiš na moment previsne sile | Napačna reakcija | Previsna sila ustvari moment pri **bližnji podpori** |

### Enačbi ravnotežja

$$\sum F_y = 0: \quad R_A + R_B = \sum F_{zunanji,\,navpično}$$

$$\sum M_{\text{točka}} = 0: \quad \text{(vsota momentov vseh sil okrog izbrane točke)}$$

**Enakomerna obtežba $q$** → nadomesti z rezultanto $Q = q \cdot L$ v težišču razpona.

---

### 📌 PRIMER 1 — Prostoležeči nosilci s točkovno silo

**Naloga:** Nosilci razpona $L = 6$ m, sila $F = 12$ kN na razdalji $a = 2$ m od A.

```
     F=12kN
       ↓
A──────●──────────B
|← 2m →|←── 4m ──|
△                 ○
A_y               B_y
```

**Korak 1a — Moment okrog A** (izniči $A_y$):

$$\sum M_A = 0: \quad -F \cdot 2 + B_y \cdot 6 = 0$$

$$B_y = \frac{12 \cdot 2}{6} = \boxed{4\ \text{kN}}$$

**Korak 1b — Vsota sil:**

$$\sum F_y = 0: \quad A_y + B_y = F$$

$$A_y = 12 - 4 = \boxed{8\ \text{kN}}$$

**Kontrola** (moment okrog B):

$$\sum M_B = A_y \cdot 6 - F \cdot 4 = 48 - 48 = 0 \quad ✓$$

---

### 📌 PRIMER 2 — Previsni nosilci z enakomerno obtežbo + vodoraven F

**Naloga:** Nosilci A–B razpona 3 m, previs levo 1,5 m. $q = 2$ kN/m na A–B, $F = 4$ kN vodoravno z ročico 1,5 m (enako kot v [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]]).

```
F=4kN →    q=2kN/m
       ←←←←←←←←←←←←←
C──────A────────────────B
|←1.5m→|←────3 m──────→|
       △                ○
       A_y              B_y
```

**Korak 1a — ⚠️ F je vodoravna** → ne prispeva k $\sum F_y$, ampak ustvari moment!

**Moment okrog B** (izniči $B_y$):

$$\sum M_B = 0: \quad \underbrace{-F \cdot 1{,}5}_{\text{ročica F od B}} - \underbrace{A_y \cdot 3}_{\text{A_y · razpon}} + \underbrace{q \cdot 3 \cdot 1{,}5}_{\text{q → rezultanta v sredini}} = 0$$

$$A_y \cdot 3 = 9 - 6 = 3 \quad \Rightarrow \quad \boxed{A_y = 1\ \text{kN}}$$

**Korak 1b — Vsota navpičnih sil** ($F$ izpusti!):

$$A_y + B_y = q \cdot 3 = 6\ \text{kN}$$

$$\boxed{B_y = 5\ \text{kN}}$$

**Moment pri A od previsne sile $F$:**

$$M_A = -F \cdot 1{,}5 = -6\ \text{kNm} \quad \text{(negativen — hogging)}$$

---

## Korak 2 — Diagram upogibnih momentov

### Kaj je M-diagram?

M-diagram prikazuje, kako se **notranji upogibni moment** spreminja vzdolž nosilci. Je osnova za:
- določitev **mesta** max napetosti (kjer je |M| največji)
- določitev **predznaka** napetosti (katera vlakna so v nategu, katera v tlaku)

### Pravilo predznaka

![[m_diagram_predznak.svg|740]]

| Moment | Ukrivljanje | Zgornja vlakna | Spodnja vlakna |
|--------|-------------|----------------|----------------|
| **M > 0** (sagging ⌣) | navzdol | tlak (−) | nateg (+) |
| **M < 0** (hogging ⌢) | navzgor | nateg (+) | tlak (−) |

### Splošni postopek — korak za korakom

**1. Določi reakcije** (Korak 1) — brez tega ne moreš nadaljevati.

**2. Razreži nosilci na odseke** med:
- podporami (A, B)
- točkovnimi silami
- začetkom/koncem enakomerne obtežbe $q$
- vpetji (moment M₀)

**3. Za vsak odsek izpiši $M(x)$** — seštej momente vseh sil **levo** od reza na razdalji $x$:

$$M(x) = \sum_{\text{levo od x}} F_i \cdot d_i$$

> **Konvencija:** Reakcija navzgor · razdalja levo = **pozitivno**. Sila navzdol · razdalja levo = **negativno**.

**4. Poišči ekstrema:**

| Tip obtežbe v odseku | Oblika $M(x)$ | Ekstrem — kje? |
|---------------------|---------------|----------------|
| Brez obtežbe | linearna | na robu odseka |
| Točkovna sila $F$ | prelom | točno pod silo |
| Enakomerna $q$ | parabola | kjer $dM/dx = Q = 0$ |

**5. Preveri robne pogoje:**

| Robni pogoj | Vrednost M |
|-------------|-----------|
| Prosti konec | $M = 0$ ✓ |
| Členek (pin) | $M = 0$ ✓ |
| Vpetje | $M \neq 0$ (splošno) |

**6. Nariši M-diagram:**
- Pozitivne vrednosti rišemo **pod** bazno linijo (sagging)
- Negativne vrednosti rišemo **nad** bazno linijo (hogging)
- Označi vse kritične vrednosti in lokacije

### Ključna zveza: Prečna sila in moment

$$Q(x) = \frac{dM}{dx} \qquad \Leftrightarrow \qquad M(x) = \int Q(x)\,dx$$

- Kjer je $Q = 0$ → **lokalni ekstrem** M
- Kjer Q skoči (točkovna sila) → **prelom** v M-diagramu
- Pod $q$ → Q linearen, M paraboličen

### M-diagram za tipične obtežbe

![[m_diagram_tipi.svg|740]]

| Obtežba | Sistem | Oblika | $M_{max}$ | Mesto |
|---------|--------|--------|-----------|-------|
| $q$ po celem $L$ | prostoležeč | parabola | $qL^2/8$ | sredina |
| $F$ na sredini $L$ | prostoležeč | trikotnik | $FL/4$ | sredina |
| $F$ na razdalji $a$ od A | prostoležeč | trikotnik | $F \cdot a \cdot b/L$ | pod F |
| $q$ na konzoli $L$ | konzola | parabola | $qL^2/2$ | vpetje |
| $F$ na koncu konzole $L$ | konzola | trikotnik | $F \cdot L$ | vpetje |
| $F$ na previsu $a$ | previsni | trikotnik | $F \cdot a$ (neg.) | podpora |

### ⚠️ Previsni nosilci — posebnost

Ko je previs obremenjen, nastane pri prvi podpori **negativen moment** (hogging):

$$M_A = -F \cdot a \quad \text{(točkovna sila na previsu)}$$

V polju moment naraste do maksimuma (tam kjer Q = 0), nato pade na 0 pri B.

---

### 📌 PRIMER 1 — Prostoležeči nosilci s točkovno silo

**Nadaljevanje Korak 1, Primer 1:** $L = 6$ m, $F = 12$ kN pri $a = 2$ m od A. Reakcije: $A_y = 8$ kN, $B_y = 4$ kN.

**Odsek 1:** $x \in [0,\ 2\ \text{m}]$ od A

$$M(x) = A_y \cdot x = 8x \quad [\text{kNm}]$$

| $x$ | $M$ |
|-----|-----|
| 0 (A) | 0 ✓ |
| 2 m (pod F) | 16 kNm |

**Odsek 2:** $x \in [2,\ 6\ \text{m}]$ od A

$$M(x) = A_y \cdot x - F \cdot (x-2) = 8x - 12(x-2) = -4x + 24$$

| $x$ | $M$ |
|-----|-----|
| 2 m (pod F) | $-8+24=16$ kNm ✓ (zveznost) |
| 6 m (B) | $-24+24=0$ ✓ |

**M-diagram:** Trikotnik z vrhom 16 kNm pod silo F. Oblika: linearno narašča od A do F, potem linearno pada do B.

$$\boxed{M_{max} = 16\ \text{kNm} \quad \text{pri}\ x = 2\ \text{m od A}}$$

```
     16 kNm
       ▲
      /|\
     / | \
    /  |  \
A──/───●───\──B
   0  2m  6m
```

---

### 📌 PRIMER 2 — Previsni nosilci z enakomerno obtežbo + vodoraven F

**Nadaljevanje Korak 1, Primer 2:** $A_y = 1$ kN, $B_y = 5$ kN, $M_A = -6$ kNm. Koordinata $x$ od B v levo.

**Odsek A–B** ($x \in [0,\ 3\ \text{m}]$ od B, $q = 2$ kN/m):

$$M(x) = B_y \cdot x - \frac{q \cdot x^2}{2} = 5x - x^2 \quad [\text{kNm}]$$

**Lokacija maksimuma** — tam kjer $Q = dM/dx = 0$:

$$\frac{dM}{dx} = 5 - 2x = 0 \quad \Rightarrow \quad x_0 = 2{,}5\ \text{m od B}$$

$$M_{max} = 5 \cdot 2{,}5 - (2{,}5)^2 = 12{,}5 - 6{,}25 = \boxed{+6{,}25\ \text{kNm}}$$

**Kontrola robnih pogojev:**

| Mesto | $x$ od B | $M$ |
|-------|----------|-----|
| B | 0 | 0 ✓ |
| A | 3 | $15-9 = 6$ kNm |
| Prosti konec (od $M_A$) | — | 0 ✓ |

**Primerjava kritičnih momentov:**

$$|M_{max,\,polje}| = 6{,}25\ \text{kNm} > |M_A| = 6{,}00\ \text{kNm}$$

→ **Merodajni moment:** $M_{mer} = 6{,}25$ kNm

**M-diagram ima dve kritični vrednosti:**
- $M_A = -6$ kNm (hogging, pri podpori A)
- $M_{max} = +6{,}25$ kNm (sagging, v polju)
- Ničla med njima — tam se predznak napetosti obrne

```
        +6.25
           ▲ (sagging)
          / \
M=0 ──–/–––\–– M=0
       |      \
  -6.0 ▼       \ (hogging)
       A    2.5m  B
```

### Previsni nosilci — posebnost

Ko je previs obremenjen, nastane pri prvi podpori **negativen moment** (hogging):

$$M_A = -F \cdot a \quad \text{(točkovna sila na previsu)}$$

V polju moment naraste do maksimuma (tam kjer Q = 0), nato pade na 0 pri B.

---

## Korak 3 — Geometrija prereza

### Simetričen prerez (NO = simetrijska os)

Nevtralna os je na sredini. $e_{zg} = e_{sp} = H/2$.

| Prerez | $J_x$ | $W_x = J/e$ |
|--------|--------|-------------|
| Pravokotnik $a \times b$ ($b$=višina) | $\dfrac{ab^3}{12}$ | $\dfrac{ab^2}{6}$ |
| Kvadrat $a \times a$ | $\dfrac{a^4}{12}$ | $\dfrac{a^3}{6}$ |
| Krog $\varnothing d$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^3}{32}$ |
| Votel pravokotnik (box) | $\dfrac{BH^3 - bh^3}{12}$ | $\dfrac{BH^3 - bh^3}{6H}$ |

### Asimetričen prerez — postopek s Steinerjem

Ko prerez ni simetričen (U, C, T, I, L...), nevtralna os ni na sredini.

**Korak 3a — Težišče:**
$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}$$

kjer $y_i$ merimo od **iste referenčne ravnine** (tipično spodnji rob).

**Korak 3b — Vztrajnostni moment (Steinerjevo pravilo):**
$$J_{x_T} = \sum_i \left[\underbrace{\frac{a_i \cdot b_i^3}{12}}_{\text{lastni}} + \underbrace{A_i \cdot (y_i - y_T)^2}_{\text{Steiner}}\right]$$

**Korak 3c — Razdalji skrajnih vlaken:**
$$e_{zg} = H - y_T \qquad e_{sp} = y_T$$

> Ker velja $e_{zg} \neq e_{sp}$, sta odpornostna momenta za zgornji in spodnji rob **različna**:
> $$W_{zg} = \frac{J}{e_{zg}} \neq W_{sp} = \frac{J}{e_{sp}}$$

### Tabela: Razstavljanje prerezov

| Profil | Razstavi na | Opomba |
|--------|-------------|--------|
| U-profil | 2 navpični steni + spodnja pasnica | 3 pravokotniki |
| C-profil | zgornja pasnica + stojina + spodnja pasnica | 3 pravokotniki |
| T-profil | vrat + zgornja pasnica | 2 pravokotnika |
| I-profil | 2 pasnici + stojina | 3 pravokotniki |
| Box (škatlast) | zunanji − notranji pravokotnik | odšteješ notranjost |

**Tip za Steiner:** Kvadratni člen $A_i(y_i-y_T)^2$ je **vedno pozitiven** — nikoli ga ne odštevaj.

---

## Korak 4 — Izračun napetosti

### Osnovna formula

$$\sigma(y) = \frac{M \cdot y}{J}$$

kjer je $y$ razdalja od nevtralne osi (pozitivno navzgor).

Na skrajnih vlaknih:
$$\sigma_{zg} = \frac{M \cdot e_{zg}}{J} \qquad \sigma_{sp} = \frac{M \cdot e_{sp}}{J}$$

### Predznak napetosti

| M | Vlakno | Napetost |
|---|--------|----------|
| $M > 0$ (sagging) | zgornji rob | tlak (−) |
| $M > 0$ (sagging) | spodnji rob | nateg (+) |
| $M < 0$ (hogging) | zgornji rob | nateg (+) |
| $M < 0$ (hogging) | spodnji rob | tlak (−) |

### Kateri prerez je kritičen?

Za **simetričen prerez**: vedno pri $|M|_{max}$.

Za **asimetričen prerez**: preveri oba robova pri vsakem kritičnem M:

$$\sigma_{max} = \max\left\{\frac{|M_i| \cdot e_{zg}}{J},\ \frac{|M_i| \cdot e_{sp}}{J}\ \forall i\right\}$$

> **Primer U-prerez:** $e_{zg}=9{,}36$ cm, $e_{sp}=5{,}64$ cm.  
> Pri $M_A=-10$ kNm: $\sigma_{zg}=+1{,}50$, $\sigma_{sp}=-0{,}90$ kN/cm²  
> Pri $M_{pol}=+8$ kNm: $\sigma_{zg}=-1{,}20$, $\sigma_{sp}=+0{,}72$ kN/cm²  
> → Max nateg **+1,50** (pri A, zgoraj), max tlak **−1,20** (v polju, zgoraj)

---

## Korak 5 — Dimenzioniranje (iskanje dimenzije)

Postopek ko iščeš dimenzijo prereza:

1. Določi $M_{max}$
2. Izrazi $W$ v odvisnosti od neznanke: $W(x)$ ali $W(d)$
3. Postavi pogoj: $\sigma_{dop} = M_{max} / W$
4. Reši za neznanko
5. Zaokroži **navzgor** (na celo število ali tržno dimenzijo)
6. Kontrola z zaokroženimi dimenzijami

**Krog:**
$$d = \sqrt[3]{\frac{32 \cdot M_{max}}{\pi \cdot \sigma_{dop}}}$$

**Pravokotnik $a \times b = nx \times mx$:**
$$x = \sqrt[3]{\frac{6 \cdot M_{max}}{nm^2 \cdot \sigma_{dop}}}$$

---

## Dopustne napetosti (tipične vrednosti)

| Material | $\sigma_{dop}$ [kN/cm²] | $\sigma_{dop}$ [MPa] |
|----------|------------------------|----------------------|
| Les (iglavci) — upogib | 1,0–1,2 | 10–12 |
| Jeklo (S235) | 16 | 160 |
| Konstrukcijsko jeklo | 15 | 150 |
| Aluminij | ~10 | ~100 |

> Les ima **višjo** dopustno napetost za upogib kot za tlak (~0,8 kN/cm²) — vlakna so boljša v nategu.

---

## Napetosti v specifičnih točkah prereza

Ko naloga sprašuje po napetosti v **vmesni točki** (ne samo na robu):

$$\sigma(y_i) = \frac{M \cdot y_i}{J}$$

kjer je $y_i$ razdalja točke od nevtralne osi — pozitivna v eno smer, negativna v drugo.

Točke tipično v: vrhu pasnice, stiku pasnice in stojine, nevtralni osi (σ=0).

---

## Asimetričen prerez — pozor!

Če prerez **ni simetričen** (npr. U-profil, T-profil), velja $e_{zg} \neq e_{sp}$. Takrat je treba preveriti napetosti pri **vsakem kritičnem prerezu posebej** — maksimalni |M| ni nujno merodajen za oba roba!

$$\sigma_{max} = \max\left(\frac{|M_i| \cdot e_{max}}{J}\right)$$

---

## Primer nalog

| Naloga | Sistem | M_max | Prerez | Rezultat |
|--------|--------|-------|--------|---------|
| [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] | konzola, q | $qL^2/2$ | pravokotnik | 13×22 cm |
| [[Naloga - Mehanika - Upogibne napetosti U-prerez]] | previs+polje | parabola | U-prerez | σ_max = 1,50 kN/cm² |
| [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]] | previs+polje, F vodoraven | 6,25 kNm | krog | d_min = 17,44 cm |
| [[Naloga - Mehanika - Upogibne napetosti C-prerez]] | konzola, F | F·a = 6 kNcm | pravokotnik | ±9,6 MPa |
| [[Naloga - Mehanika - Napetosti skatlaski profil]] | prostoležeč, q (pol) | 14,06 kNm | škatlast | 180 MPa > σ_dop ❌ |

Pregled vseh tipov: [[Izpit - Mehanika - Upogib]]

## Povezave

- [[Koncept - Vztrajnostni moment]]
- [[Koncept - Euler Uklon]]
- [[Izpit - Mehanika - Upogib]]
- [[Mehanika Hub]]
- [[STATIKA]]
- [[Mehanika Hub]]
