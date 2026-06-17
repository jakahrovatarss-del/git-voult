# Vaje — N, T, M diagrami (vse vrste za izpit)

**Predmet:** Mehanika (LE007) · **Tema:** Notranje sile — N, T, M  
**Namen:** Obvladati vse tipe nalog ki se pojavijo na izpitu BTF Lesarstvo UN

---

## Vrste podpor — katere reakcije ima vsaka

![[ntm_vrste_podpor.svg]]

| Podpora | Simbol | Reakcije | Število neznank |
|---------|--------|----------|-----------------|
| **Nepomični členek** (tečaj) | △ na tleh | $R_x$, $R_y$ | 2 |
| **Pomični členek** (roller) | △ + kolesca | $R_y$ | 1 |
| **Togo vpetje** (konzola) | □ v steni | $R_x$, $R_y$, $M_A$ | 3 |
| **Prost konec** | — | nič | 0 → $T=0$, $M=0$ ✓ |
| **Notranji členek** (Gerber) | ○ na gredi | doda pogoj: $M=0$ | −1 |

> **Pravilo statične določenosti:** Σ reakcij = 3 za ravninski problem.  
> Nepomični členek (2) + pomični členek (1) = 3 ✓ → statično določena greda.

> **zobacz:** [[STATIKA#Podpore in reakcije]]

---

## SPLOŠNI POSTOPEK — 6 korakov za vsako nalogo

> Nauči se to zaporedje. Na izpitu ga sledi mehanično, ne improvizira.

### KORAK 0 — Prepoznaj tip konstrukcije

Poglej skico in odgovori:
- Koliko podpor? Koliko reakcij skupaj?
- Statično določena? → $\text{št. reakcij} = 3$ (ravninski problem)
- Je lomljena os (L, T oblika)? → bo $N \neq 0$!
- Je portalni okvir? → simetrija pomaga

### KORAK 1 — Nariši prosti diagram telesa (FBD)

Vrisaj **vse** sile:
- Zunanje obtežbe ($q$, $F$, $M_0$)
- Reakcije v podporah (puščice s smermi, ki jih predpostavljaš)
- Silo $F$ pod kotom **takoj razstavi** na $F_x$ in $F_y$

### KORAK 2 — Izračunaj reakcije

Vedno v tem vrstnem redu:
$$\sum F_x = 0 \implies A_x$$
$$\sum M_A = 0 \implies B_y \quad \text{(moment okoli podpore A eliminira } A_x, A_y\text{)}$$
$$\sum F_y = 0 \implies A_y$$

**Kontrola:** $\sum M_B = 0$ mora dati $A_y$ ki si ga dobil.

### KORAK 3 — Določi območja

Postavi oznake na osi $x$ kjer se obremenitev **spremeni**:
- Vsaka točkovna sila $F$ → meja območja
- Vsak točkasti moment $M_0$ → meja območja
- Začetek/konec porazdeljene obtežbe $q$ → meja območja
- Vsaka podpora → meja območja

### KORAK 4 — Presečna metoda (za vsako območje)

Za vsak odsek naredi rez in narišei prosti diagram **levega dela**. Piši ravnotežne enačbe:

$$N(x) = -\sum F_{\text{vzdolž osi, levo od reza}}$$
$$T(x) = +\sum F_{\text{prečno na os, levo od reza}}$$
$$M(x) = +\sum M_{\text{okoli reza, levo}}$$

> 💡 **Trik:** Začni od tistega konca kjer je manj sil (pogosto od prostega konca ali od konca z $B$).

### KORAK 5 — Poišči $T = 0$ (mesto $M_{max}$)

Za vsak odsek reši $T(x) = 0$ → preveri ali je $x$ v območju odseka → izračunaj $M$ pri tem $x$.

### KORAK 6 — Nariši diagrame + kontrola

- $N(x)$: konstantna na vsakem odseku (brez porazdeljenih osnih sil)
- $T(x)$: linearna kjer je $q$, konstanta kjer ni $q$, skoki pri $F$
- $M(x)$: parabola kjer je $q$, linearna kjer ni $q$, preskok pri $M_0$

**Kontrola:**
- Na prostem koncu: $T = 0$ in $M = 0$
- Pri členku (podpori brez momenta): $M = 0$
- $\frac{dM}{dx} = T$ (odvod momenta = prečna sila)

---

## Teorija (hitri povzetek pred vajami)

### Konvencija predznakov

| Sila/moment | Pozitiven predznak |
|-------------|-------------------|
| $N$ (normalna) | nateg (vlak) |
| $T$ (prečna) | desni del gre navzgor |
| $M$ (upogibni) | vlakna na spodnji strani so nategno obremenjena |

### Grafična pravila

| Obremenitev | $T$ | $M$ |
|-------------|-----|-----|
| Porazd. obremenitev $q$ | linearna | parabola |
| Točkovna sila $F$ | skok za $F$ | lom (kink) |
| Točkasti moment $M_0$ | brez spremembe | preskok za $M_0$ |

> $M_{max}$ je **vedno tam kjer $T = 0$**  
> Na prostem koncu: $T = 0$ in $M = 0$  
> Na vpetju: $M \neq 0$, reakcijski moment

---

## NALOGA 1 — Prosta greda: točkovna sila + porazdeljena obtežba

![[ntm_naloga1.svg|697]]

### Podatki

```
        F = 10 kN        q = 2 kN/m
             ↓       ↓↓↓↓↓↓↓↓↓
 A ──────────┼────────────────── B
[△]          2m          4m    [△]
             ←     6 m →
```

- $F = 10\ \text{kN}$ (navpična, na razdalji 2 m od A)
- $q = 2\ \text{kN/m}$ (na desni polovici, dolžina 4 m)
- Razpon: $L = 6\ \text{m}$
- Podpori A in B: **členki** (vodoravna + navpična reakcija v A, samo navpična v B)

### KORAK 1 — Reakcije

Obremenitve pretvorimo v rezultante:

$$Q_q = q \cdot 4 = 2 \times 4 = 8\ \text{kN} \quad \text{(deluje na sredini desne polovice, x = 2+2 = 4 m od A)}$$

**Ravnotežne enačbe:**

$$\sum F_x = 0: \quad A_x = 0$$

$$\sum M_A = 0: \quad B_y \cdot 6 - F \cdot 2 - Q_q \cdot 4 = 0$$
$$B_y = \frac{10 \cdot 2 + 8 \cdot 4}{6} = \frac{20 + 32}{6} = \frac{52}{6} = \boxed{8{,}67\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y + B_y - F - Q_q = 0$$
$$A_y = 10 + 8 - 8{,}67 = \boxed{9{,}33\ \text{kN}}$$

### KORAK 2 — Metoda preseka

Greda ima **3 karakteristična območja**:
- **Območje I:** $x \in [0,\ 2]$ — od A do sile F
- **Območje II:** $x \in [2,\ 6]$ — od F do B (tu deluje $q$)

#### Območje I: $0 \leq x \leq 2$ m

Prosti diagram od **leve** (vsebuje samo $A_y = 9{,}33$ kN):

$$N(x) = 0 \quad (A_x = 0, \text{ ni vodoravnih sil})$$
$$T(x) = A_y = +9{,}33\ \text{kN} \quad \text{(konstanta)}$$
$$M(x) = A_y \cdot x = 9{,}33\,x\ \text{kN·m} \quad \text{(linearna)}$$

Vrednosti:
- $x=0$: $T=9{,}33$, $M=0$
- $x=2$: $T=9{,}33$, $M=18{,}67\ \text{kN·m}$

#### Območje II: $2 \leq x \leq 6$ m

Po sili $F$ (od leve, upoštevamo $A_y$ in $F$):

$$T(x) = A_y - F - q(x-2) = 9{,}33 - 10 - 2(x-2) = -0{,}67 - 2(x-2)$$

$$M(x) = A_y \cdot x - F(x-2) - q\frac{(x-2)^2}{2} = 9{,}33x - 10(x-2) - (x-2)^2$$

Vrednosti:
- $x=2^+$: $T = -0{,}67\ \text{kN}$ (skok navzdol za $F=10$ kN)
- $x=6$: $T = -0{,}67 - 2\cdot4 = -8{,}67\ \text{kN}$ ✓ (= $-B_y$, kontrola!)

**Kje je $T=0$?** (= mesto $M_{max}$ na območju II)
$$-0{,}67 - 2(x-2) = 0 \implies x - 2 = -0{,}335 \implies \text{negativno!}$$

Torej $T$ je na celotnem območju II negativen → $M_{max}$ je pri $x=2$ m:
$$M_{max} = M(x=2) = 9{,}33 \cdot 2 = \boxed{18{,}67\ \text{kN·m}}$$

### KORAK 3 — Diagrami (shematsko)

```
N:  ────────────────────────── 0
    (ni osnih sil)

T:  ┌──────────┐
    │  +9.33   │ -0.67
    │          └─────────────────── (pada do -8.67)
    0          2                  6

M:  (narašča linearno do x=2, nato pada parabolično)
         18.67 kNm
        /
       /           \
      /              \
    0                  0
    A    2m    4m      B
```

> **Kontrola:** $M(6) = 9{,}33\cdot6 - 10\cdot4 - 2\cdot\frac{16}{2} = 56 - 40 - 16 = 0$ ✓

---

## NALOGA 2 — Nosilci s previsom (konzola + prosta greda)

![[ntm_naloga2.svg]]

### Podatki

```
    q = 3 kN/m           F = 6 kN
    ↓↓↓↓↓↓↓↓              ↓
 A ──────────── B ──────── C
[△]     3m    [△]    2m
              ←     5 m →
```

- $q = 3\ \text{kN/m}$ na odseku AB (3 m)
- $F = 6\ \text{kN}$ na prostem koncu C (previs 2 m za B)
- Podpori A in B sta **členki**

### KORAK 1 — Reakcije

$$Q_q = 3 \times 3 = 9\ \text{kN} \quad \text{(težišče pri } x = 1{,}5\ \text{m od A)}$$

$$\sum M_A = 0: \quad B_y \cdot 3 - Q_q \cdot 1{,}5 - F \cdot 5 = 0$$
$$B_y = \frac{9 \cdot 1{,}5 + 6 \cdot 5}{3} = \frac{13{,}5 + 30}{3} = \frac{43{,}5}{3} = \boxed{14{,}5\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y = Q_q + F - B_y = 9 + 6 - 14{,}5 = \boxed{0{,}5\ \text{kN}}$$

> ⚠️ $A_y$ je majhen — tipično za nosilci s previsom. Preverimo predznak: pozitiven = navzgor ✓

### KORAK 2 — Metoda preseka

**3 območja:** $[0,3]$, $[3,5]$ ... toda v B je podpora, zato:
- **Območje I:** $0 \leq x \leq 3$ (AB, deluje $q$)
- **Območje II:** $3 \leq x \leq 5$ (BC, previs, samo $F$ na koncu)

#### Območje I (od leve): $0 \leq x \leq 3$

$$T(x) = A_y - qx = 0{,}5 - 3x$$
$$M(x) = A_y \cdot x - q\frac{x^2}{2} = 0{,}5x - 1{,}5x^2$$

Kje $T=0$?
$$0{,}5 - 3x = 0 \implies x = \frac{0{,}5}{3} = 0{,}167\ \text{m}$$

$$M_{max}^{I} = 0{,}5 \cdot 0{,}167 - 1{,}5 \cdot 0{,}167^2 = 0{,}0835 - 0{,}0418 = \boxed{0{,}042\ \text{kN·m}}$$

Vrednosti na mejah:
- $x=0$: $T=0{,}5$, $M=0$
- $x=3^-$: $T = 0{,}5 - 9 = -8{,}5\ \text{kN}$, $M = 1{,}5 - 13{,}5 = -12\ \text{kN·m}$

Skok v $T$ pri $x=3$ (podporna sila $B_y = 14{,}5$ kN navzgor):
- $x=3^+$: $T = -8{,}5 + 14{,}5 = +6\ \text{kN}$

#### Območje II (od desne!): $3 \leq x \leq 5$

Lažje od desne (samo $F$ na koncu C):

$$T(x) = -F = -6\ \text{kN} \quad \text{(konstanta)}$$
$$M(x) = -F \cdot (5-x) = -6(5-x)$$

Vrednosti:
- $x=5$ (C): $T=-6$, $M=0$
- $x=3^+$ (B): $T=-6$, $M=-6\cdot2 = -12\ \text{kN·m}$ ✓ (sklada se z območjem I)

### KORAK 3 — Diagrami

```
N:  ─────────────────── 0

T:  0.5                    +6
     \     /──────────────────
      \   / (skok +14.5 pri B)
       \ /
       -8.5        -6
       B

M:   (majhen + vrh pri x=0.167)
    0  ↗ 0.042 ↘              0
                 \────────────
                 -12 (pri B)
    ← neg. vrh pri B = -12 kNm
```

> **Ključna opazka:** Negativni $M$ pri podpori B pomeni, da so vlakna na **zgornjem robu** nategno obremenjena — pri lesu to pomeni nevarnost razcepa!

---

## NALOGA 3 — Lomljen nosilci (L-oblika) — pojavi se N ≠ 0!

![[ntm_naloga3.svg|697]]

### Podatki

```
        C
        │  ← F = 8 kN (vodoravna)
        │
        │ 3 m (steber)
        │
 A ─────┤ B
[△]  4m  [△]
```

- Vodoravna sila $F = 8\ \text{kN}$ v točki C
- Steber BC je **navpičen**, dolžine 3 m
- Prečka AB je **vodoravna**, dolžine 4 m
- A: členek, B: členek

### KORAK 1 — Reakcije (pozor: lomljena os!)

$$\sum M_A = 0: \quad B_y \cdot 4 - F \cdot 3 = 0 \implies B_y = \frac{8 \cdot 3}{4} = \boxed{6\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y + B_y = 0 \implies A_y = \boxed{-6\ \text{kN}} \quad \text{(navzdol!)}$$

$$\sum F_x = 0: \quad A_x = F = \boxed{8\ \text{kN}} \quad \text{(v levo)}$$

### KORAK 2 — Ločimo po odsekih

#### Odsek AB (prečka, vodoravna): $0 \leq x \leq 4$ m (x meri od A)

Lokalni koordinatni sistem: x vzdolž AB (vodoravno), y navzgor.

Reakciji v A: $A_x = 8$ kN (vodoravna), $A_y = -6$ kN (navzdol).

$$N(x) = -A_x = -8\ \text{kN} \quad \text{(tlak v prečki!)}$$
$$T(x) = -A_y = +6\ \text{kN} \quad \text{(konstanta)}$$
$$M(x) = A_y \cdot x \cdot (-1) = 6x\ \text{kN·m}$$

> Pozor na predznak: $A_y = -6$ kN navzdol, torej prečna sila na levi strani preseka = $+6$ kN ↑

- $x=0$ (A): $N=-8$, $T=6$, $M=0$
- $x=4$ (B): $N=-8$, $T=6$, $M=24\ \text{kN·m}$

#### Odsek BC (steber, navpičen): $0 \leq z \leq 3$ m (z meri od B navzgor)

V točki B deluje reakcija $B_y = 6$ kN navzgor.

Vzdolž stebra (z-os navzgor): $B_y$ postane **osna** sila.

$$N(z) = +B_y = +6\ \text{kN} \quad \text{(nateg v stebru)}$$
$$T(z) = F = 8\ \text{kN} \quad \text{(toda F deluje na vrhu, gledamo od spodaj)}$$

Iz ravnovesja stebra (od spodaj):
$$T(z) = F = 8\ \text{kN} \quad \text{(konstanta)}$$
$$M(z) = F \cdot (3 - z) = 8(3-z)\ \text{kN·m}$$

- $z=0$ (B): $N=6$, $T=8$, $M=24\ \text{kN·m}$ ✓ (sklada z M na koncu prečke!)
- $z=3$ (C): $N=6$, $T=8$, $M=0$ ✓ (prosti konec)

### KORAK 3 — Diagrami

```
STEBER BC (z navzgor):
N:  ─── +6 kN (konstanta, nateg)
T:  ─── +8 kN (konstanta)
M:  24 kNm pri B → 0 pri C (linearno pada)

PREČKA AB (x od A):
N:  ─── -8 kN (konstanta, tlak!)
T:  ─── +6 kN (konstanta)
M:  0 pri A → 24 kNm pri B (linearno narašča)
```

> **Ključ:** Pri lomljenih konstrukcijah: sila vzdolž osi = N, sila prečno = T. Ko preidemo iz prečke v steber, se vlogi zamenjata!

---

## NALOGA 4 — Portalni okvir ← **tip izpita 2018!**

![[ntm_naloga4.svg|697]]

### Podatki

```
     q = 1.5 kN/m
   ↓↓↓↓↓↓↓↓↓↓↓↓↓
C ─────────────── D
│                 │
│                 │
│  4 m            │ 4 m
│                 │
A                 B
[▽]              [▽]
    ←── 6 m ──→
```

- Porazdeljena obtežba $q = 1{,}5\ \text{kN/m}$ na prečki CD (dolžina 6 m)
- Stebri CA in DB so visoki 4 m
- A: **togi vpetje** (3 reakcije: $A_x, A_y, M_A$)
- B: **členek** (2 reakciji: $B_x, B_y$)

### KORAK 1 — Reakcije

Skupaj 5 neznank ($A_x, A_y, M_A, B_x, B_y$) — statično **nedoločena** konstrukcija!

> ⚠️ Portalni okvir je pogosto **statično nedoločen**. Na izpitu pa ponavadi poenostavijo: oba konca sta **členka** (ne vpetja), ali pa je okvir z notranjo articulacijo.

**Poenostavitev za izpit:** Oba A in B sta **členki** (brez momenta).

Potem: 4 neznank ($A_x, A_y, B_x, B_y$) — še vedno nedoločen!

Rešimo s **simetrijo** (simetričen portal, simetrična obtežba):
$$A_y = B_y = \frac{Q_q}{2} = \frac{q \cdot 6}{2} = \frac{1{,}5 \cdot 6}{2} = \boxed{4{,}5\ \text{kN}}$$

Ker ni vodoravnih obtežb in je simetrija:
$$A_x = B_x = 0$$

### KORAK 2 — Notranje sile

#### Steber CA (dolžina 4 m, od A navzgor):

$$N = -A_y = -4{,}5\ \text{kN} \quad \text{(tlak)}$$
$$T = A_x = 0$$
$$M = 0 \quad \text{(v celotnem stebru pri simetričnem portalu brez hor. sil!)}$$

#### Prečka CD (dolžina 6 m, od C do D):

Pri C: prečna sila $T_C = A_y = 4{,}5\ \text{kN}$, $M_C = 0$.

$$T(x) = A_y - qx = 4{,}5 - 1{,}5x$$
$$M(x) = A_y \cdot x - q\frac{x^2}{2} = 4{,}5x - 0{,}75x^2$$

$T = 0$ pri: $x = \frac{4{,}5}{1{,}5} = 3\ \text{m}$ (sredina — simetrija ✓)

$$M_{max} = 4{,}5 \cdot 3 - 0{,}75 \cdot 9 = 13{,}5 - 6{,}75 = \boxed{6{,}75\ \text{kN·m}}$$

### KORAK 3 — Diagrami

```
STEBER CA:
N: ─── -4.5 kN (tlak, konstanta)
T: ─── 0
M: ─── 0

PREČKA CD:
N: ─── 0
T:     +4.5 → 0 → -4.5  (pada linearno)
       C         sredina    D
M:    0 ────────── 6.75 ────────── 0
        (parabolično, vrh na sredini)
```

> **Zakaj je to na izpitu:** Leseni portalni okviri so tipičen konstrukt v lesarstvu (okvirji hiš, garažna vrata). Moment 6,75 kN·m v sredini prečke dimenzionira prereze!

### 🎓 Profesorjeva razlaga — portalni okvir (konceptualno)

> **Korak 0 — Uvod: statična (ne)določenost**
>
> Portalni okvir je pogosto **statično nedoločen**: togo vpetje (A) + členek (B) dá 5 neznank, a imamo le 3 enačbe ravnotežja. Na izpitu to rešimo s **poenostavitvijo na oba členka** in **simetrijo** → $A_y = B_y$.
>
> **Splošno pravilo:**
> - Togo vpetje: 3 neznanke
> - Členek: 2 neznanki
> - Skupaj > 3 → statično nedoločeno (rešujemo s simetrijo ali notranjo articulacijo)

> **Korak 1 — Navpične reakcije iz simetrije**
>
> Ker je portal simetričen in obtežba $q$ simetrična:
> $$A_y = B_y = \frac{q \cdot L}{2} = \frac{1{,}5 \cdot 6}{2} = 4{,}5\ \text{kN}$$
> Vodoravnih sil ni → $A_x = B_x = 0$.
>
> **Korak 2 — Steber CA** (od A navzgor do C)
>
> Reakcija $A_y$ pritiska neposredno v steber → steber je v **tlaku**:
> $$N = -4{,}5\ \text{kN}$$
> Ker $A_x = 0$: ni prečnih sil → $T = 0$ in $M = 0$ v celotnem stebru.
>
> 💡 V lesarstvu je to ugodno — les dobro prenaša tlak vzdolž vlaken.

> **Korak 3 — Prečka CD** (x od C proti D)
>
> V vogalu C se **osna sila iz stebra prelije v prečno silo v prečki**:
> $$T(x) = 4{,}5 - 1{,}5x$$
> $$M(x) = 4{,}5x - 0{,}75x^2$$
>
> Ekstremen moment tam kjer $T = 0$: $x = 3\ \text{m}$ (sredina — simetrija ✓)
> $$\boxed{M_{max} = 6{,}75\ \text{kNm}}$$
>
> **Napaka, na katero pazi:** Vogala C in D v *idealnem simetričnem* primeru nimata momenta ($M_C = M_D = 0$). V realnosti (veter, nesimetrično breme) postanejo vogali **kritična mesta** — tam bi bila potrebna ojačitev spoja!

> **Inženirski zaključek:**
>
> $M_{max} = 6{,}75\ \text{kNm}$ **dimenzionira prerez prečke** — iz tega izračunamo potreben $W_{min}$ in izberemo dimenzijo tramov. Če bi les bil prešibak, bi prečka razpokala na spodnji strani (nateg vlaken v sredini).
>
> **Diagram — kako brati:**
> - $N$: dva polna pravokotnika na stebrih ($-4{,}5$), prečka prazna
> - $T$: trikotnika nad prečko: $+4{,}5 \to 0 \to -4{,}5$
> - $M$: simetrična parabola pod prečko z vrhom $6{,}75\ \text{kNm}$; stebra sta čista (ničle)
>
> **→ glej:** [[STATIKA#Portalni okvir]] | [[Mehanika Hub]]

---

## NALOGA 5 — Kombinacija q + F pod kotom + točkasti moment M₀

![[ntm_naloga5.svg|697]]

### Podatki (najtežja varianta — izpitni nivo!)

```
     M₀=12 kNm    F=10 kN pod 30°
         ↺              ↗
 A ──────┼──────────────┼────── B
[△]      2m            2m    [△]
         ←       4 m        →

    q = 2 kN/m celoten razpon
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
 A ────────────────────────── B
```

- $q = 2\ \text{kN/m}$ po celotnem razponu $L = 4\ \text{m}$
- $M_0 = 12\ \text{kN·m}$ pri $x = 2\ \text{m}$
- $F = 10\ \text{kN}$ pod kotom $30°$ pri $x = 3\ \text{m}$ (od A)

**Razstavi F:**
$$F_x = F\cos 30° = 10 \cdot 0{,}866 = 8{,}66\ \text{kN}$$
$$F_y = F\sin 30° = 10 \cdot 0{,}5 = 5\ \text{kN}$$

### KORAK 1 — Reakcije

$$\sum F_x = 0: \quad A_x = -F_x = -8{,}66\ \text{kN} \quad \text{(v levo)}$$

$$Q_q = 2 \times 4 = 8\ \text{kN} \quad \text{(pri } x=2\ \text{m)}$$

$$\sum M_A = 0: \quad B_y \cdot 4 - Q_q \cdot 2 + M_0 - F_y \cdot 3 = 0$$

> ⚠️ **Predznak $M_0$:** Na sliki je $M_0$ narisan kot protiurna smer (↺ pozitivna). Upoštevamo ga pozitivno v enačbi momentov.

$$B_y = \frac{Q_q \cdot 2 - M_0 + F_y \cdot 3}{4} = \frac{8\cdot2 - 12 + 5\cdot3}{4} = \frac{16 - 12 + 15}{4} = \frac{19}{4} = \boxed{4{,}75\ \text{kN}}$$

$$\sum F_y = 0: \quad A_y = Q_q + F_y - B_y = 8 + 5 - 4{,}75 = \boxed{8{,}25\ \text{kN}}$$

### KORAK 2 — Metoda preseka (4 območja!)

**Točke diskontinuitete:** $x=2$ ($M_0$), $x=3$ ($F$) → **3 območja** vzdolž osi.

#### Območje I: $0 \leq x \leq 2$

$$N(x) = -A_x = +8{,}66\ \text{kN} \quad \text{(nateg, konstanta)}$$
$$T(x) = A_y - qx = 8{,}25 - 2x$$
$$M(x) = A_y \cdot x - q\frac{x^2}{2} = 8{,}25x - x^2$$

- $x=0$: $T=8{,}25$, $M=0$
- $x=2^-$: $T = 8{,}25-4 = 4{,}25$, $M = 16{,}5-4 = 12{,}5\ \text{kN·m}$

Skok $M$ pri $x=2$ (točkasti moment $M_0 = 12$ kN·m):
- $x=2^+$: $M = 12{,}5 - 12 = 0{,}5\ \text{kN·m}$ ← preskok za 12 kNm!

#### Območje II: $2 \leq x \leq 3$

$$T(x) = A_y - qx = 8{,}25 - 2x \quad \text{(M₀ ne vpliva na T!)}$$
$$M(x) = 8{,}25x - x^2 - M_0 = 8{,}25x - x^2 - 12$$

- $x=2^+$: $M = 16{,}5 - 4 - 12 = 0{,}5$ ✓
- $x=3^-$: $T = 8{,}25-6 = 2{,}25$, $M = 24{,}75 - 9 - 12 = 3{,}75\ \text{kN·m}$

Skok pri $x=3$ (sila $F$):
- $T$ skok: $F_y = -5$ kN (navzdol → $T$ pade za 5)
- $x=3^+$: $T = 2{,}25 - 5 = -2{,}75\ \text{kN}$

#### Območje III: $3 \leq x \leq 4$

$$T(x) = A_y - qx - F_y = 8{,}25 - 2x - 5 = 3{,}25 - 2x$$
$$M(x) = 8{,}25x - x^2 - 12 - F_y(x-3) = 8{,}25x - x^2 - 12 - 5(x-3)$$
$$= 3{,}25x - x^2 + 3$$

- $x=3^+$: $M = 9{,}75 - 9 + 3 = 3{,}75$ ✓
- $x=4$: $T = 3{,}25-8 = -4{,}75 = -B_y$ ✓, $M = 13-16+3 = 0$ ✓

**Kje $T = 0$ na območju I?**
$$8{,}25 - 2x = 0 \implies x = 4{,}125\ \text{m} \quad \text{→ zunaj območja I!}$$

**Kje $T = 0$ na območju II?** $x=4{,}125$ → zunaj II.

**Kje $T = 0$ na območju III?**
$$3{,}25 - 2x = 0 \implies x = 1{,}625 \quad \text{→ zunaj III!}$$

Zaključek: $T$ je na območjih I in II **pozitiven** ($M$ narašča), na območju III **negativen** → $M_{max}$ je pri $x=3$ m!

$$M_{max} = 3{,}75\ \text{kN·m}$$

### KORAK 3 — Diagrami

```
N:  ──── +8.66 kN ────────────────── (skok nazaj pri x=3, ker Fx!)
    [0──────────────3] → potem 0

    Točneje:
    x∈[0,3]: N = +8.66 kN
    x∈[3,4]: N = +8.66 - F_x·... hmm

    *** Pozor: F_x = 8.66 kN deluje pri x=3 navzgor/desno ***
    Pri x>3: N = 8.66 - 8.66 = 0 kN

T:  +8.25
    \
     \  (pada linearno)
      4.25  ←(pri x=2, skok M₀ ne vpliva)
        \
         2.25 (x=3-)
              -2.75 (x=3+, skok za -5)
               \
                -4.75 (x=4) = -By ✓

M:  0              preskok pri x=2 (za -12)
      ↗ 12.5 → 0.5 ↗ 3.75 ↘ 0
     (par.)      (par.)  (par.)
```

---

## Povzetek — Kaj moraš znati za vsak tip

| Tip naloge | Ključni korak | Pogosta napaka |
|------------|--------------|----------------|
| Prosta greda | $\sum M_A = 0$ za $B_y$ | Pozabiti na razdaljo $Q_q$ |
| Nosilci s previsom | Preveriti predznak $A_y$ | Misliti da je vedno ↑ |
| Lomljeni nosilci | Ločiti N in T po odseku | Zamešati os (vzdolž ≠ prečno) |
| Portalni okvir | Simetrija → $A_y = B_y$ | Pozabiti na $N$ v stebrih |
| F pod kotom + $M_0$ | Razstavi F; predznak $M_0$! | Napačen predznak $M_0$ v $\sum M$ |

---

## Povezave

- [[STATIKA]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Junij 2026]]
- [[Koncept - Krožni žagalni stroj]]
- [[05_SCHOOL/School Hub]]
