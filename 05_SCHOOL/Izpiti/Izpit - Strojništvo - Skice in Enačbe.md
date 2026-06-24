---
tags: [izpit, strojništvo, enačbe, skice]
datum: 2026-06-20
---

# Izpit – Strojništvo: Skice in Enačbe

> Razlaga vseh 18 strani skic za izpit v ponedeljek. Vsak sklop vsebuje: **skico z dimenzijami**, **enačbe z izpeljavo** in **intuitivno razlago**.

---

## Povezave

Sorodni koncepti: [[Mehanika Hub]] · [[STATIKA]] · [[05_SCHOOL/School Hub]]  
Prerezi: [[vztrajnostni_moment_prerezi]] · [[upogib_krozni_prerez]] · [[upogib_c_prerez]]

---

## 📐 Opomba o dimenzijah za zvezek

Vse skice so narisane na črtastem papirju A4 (210×297 mm), razmak vrstic ≈ 8 mm.  
Ko rišeš v zvezek:
- **Vijaki (prečni prerez)**: ~6×8 cm
- **Sornik, gred**: ~10×4 cm (horizontalno)
- **Sklopke**: ~10×6 cm
- **Osi/gredi**: ~12×3 cm
- **Verige**: ~12×5 cm
- **Stroji (žagalni, skobelni)**: cela stran ~15×6 cm

Vse oznake so **simbolne** (d, l, b, h) – številske vrednosti dobiš iz katalogov ali naloge.

---

## SKLOP 1 – NAVOJI (Str. 1)

### Skica

```
SILE PRI PRIJANJANJU           SILE PRI ODVIJANJU

      F_tan                           F_tan
     /                               /
    / F                             / Ft
   /____                           /____
   \ α+φ                           \ α-φ
    \                               \
     \ F_n                           \ F_n
      ↓ F (aksialna)                  ↓ F
```

**Legenda:**
| Oznaka | Pomen | Tipična vrednost |
|--------|-------|-----------------|
| α | kot vzpona navoja | 2–5° |
| φ | kot trenja (φ = arctan μ) | ~6–10° |
| d₂ | srednji premer navoja | iz tabele |
| F | aksialna sila (prednapetje) | iz naloge |

### Enačbe in izpeljava

**Moment prijanjanja (zatezanje vijaka):**

Navoj je poševna ravnina navita v spiralo. Ko zatezamo vijak, premagujemo trenje in vzpon navoja.

$$M_f = F_{tan} \cdot r = F_{tan} \cdot \frac{d_2}{2}$$

Ker je $\tan\varphi = \frac{F_{tc}}{F_n} = \mu_g$ in tangencialna sila:

$$F_{tan} = F \cdot \tan(\alpha + \varphi)$$

Skupaj:

$$\boxed{M_f = F \cdot \tan(\alpha + \varphi) \cdot \frac{d_2}{2}}$$

**Moment odvijanja (sproščanje):**

Pri odvijanju trenje pomaga, zato je kot $-\varphi$:

$$F_t = F \cdot \tan(\alpha - \varphi)$$
$$M_f = F_t \cdot r = F \cdot \tan(\alpha - \varphi) \cdot \frac{d_2}{2}$$

> 💡 **Intuitivno:** Navoj je klina. Pri zatezanju plezaš navzgor po klinu (α+φ), pri odvijanju drsaš navzdol (α−φ). Če je α < φ, je zveza samozaporna (ne odvije se sama).

---

## SKLOP 2 – PRITRDILNI VIJAK (Str. 2)

### Skica

```
        ┌─────────┐
    ████│   ┌─┐   │████   ← privijačeni elementi
    ████│   │d│   │████
        │   │ │   │
        └───┴─┴───┘
             │ F (nateg)
             ↓

  Prerez navoja:
    ┌─────┐
    │  d₂ │  ← srednji premer (kjer se navoj "strga")
    │  d₃ │  ← jedro vijaka (najožji del)
    └─────┘
    d₂ = (d₂ + d₃) / 2
```

**Dimenzije za skico:**
- Glava vijaka: ~1.5× premer droga
- Dolžina droga: ~4× premer
- Navoj: valovita linija ob drogu

### Enačbe

**Natezna napetost jedra vijaka:**

$$\sigma = \frac{F}{A} = \frac{4F}{\pi d_2^2}$$

kjer je $d_2 = \frac{d_2 + d_3}{2}$ srednji premer navoja (ker jedro ni gladko).

**Pogoj:**
$$\sigma \leq \sigma_{dop} \approx 0{,}6 \cdot \sigma_{TDT}$$

kjer je $\sigma_{TDT}$ trajna dinamična trdnost materiala vijaka.

> 💡 **Intuitivno:** Vijak se razteguje kot gumijast. Kritičen je najožji del – jedro navoja (d₃). Ker je jedro neredno, računamo s "sredinskim" premerom d₂.

---

## SKLOP 3 – SPENJALNI VIJAK (Str. 3)

### Skica

```
       F ↓
   ┌───┴───┐
   │  ///  │  ← glava vijaka
   │       │
   │       │  Fn ←   premer podložke Fn = pn · πD²/4
   │  ///  │
   └───────┘
   d₂ = srednji premer navoja
```

**Dimenzije za skico:**
- Vijak gre skozi ploščo (prerez kaže: šrafura zgoraj + material spodaj)
- Podložka: D ≈ 2d (zunanji premer)

### Enačbe

**Moment ključa (skupni moment za zatezanje):**

$$M_{kl} = F \cdot \left[\tan(\alpha + \varphi') \cdot \frac{d_2}{2} + \mu \cdot \frac{d_{sr}}{2}\right]$$

Dva dela:
1. Navoj: $\tan(\alpha+\varphi') \cdot \frac{d_2}{2}$ — trenje na navoju
2. Podložka: $\mu \cdot \frac{d_{sr}}{2}$ — trenje pod glavo vijaka

**Sila na en vijak (ko jih je n):**

$$F_v = \frac{F_{cel}}{n}, \quad F_{cel} = p_n \cdot \frac{\pi D^2}{4}$$

**Natezna napetost vijaka:**

$$\sigma = \frac{F + F_v}{A} = \frac{F + F_v}{\frac{\pi d_2^2}{4}}$$

(skupna sila = zunanja F + prednapetje Fv)

**Vzvojna napetost vijaka:**

$$\tau_v = \frac{M_t}{W_p} = \frac{F \cdot \tan(\alpha+\varphi) \cdot \frac{d_2}{2}}{\frac{\pi d_2^3}{16}}$$

**Primerjalna napetost (von Mises):**

$$\boxed{\sigma_p = \sqrt{\sigma^2 + 3\tau_v^2} \leq \sigma_{dop} = 0{,}6 \cdot \sigma_{TDT}}$$

> 💡 **Intuitivno:** Vijak je obremenjen kombinirano – razteza se (σ) in zasuka ga (τ). Von Mises formula to združi v eno "ekvivalentno" napetost. Faktor 3 pri τ pride iz teorije plastičnosti (Tresca/von Mises).

---

## SKLOP 4 – PRILAGODNI VIJAK (Str. 4)

### Skica

```
  F/2 ←  ┌───┬───────────┬───┐  → F/2
          │l₁ │     D     │ l₂│
    ████  │///│  [===]    │///│  ████
    ████  │   │   vijak   │   │  ████
          └───┴───────────┴───┘
              ↑ b₁          ↑ b₂
              
  Prerez vijaka: krog premera d
```

**Dimenzije za skico:**
- Vijak: horizontalno skozi dve plošči in vmesni del
- l₁, l₂ = dolžini stikovnih mest
- D = premer vijaka
- Šrafure = material

### Enačbe

**Obremenitev na strig:**

$$\tau_s = \frac{F}{A} = \frac{F}{z \cdot \frac{\pi d^2}{4}} \leq \tau_{s,dop} \text{ (vijaka)}$$

kjer z = število strižnih prerezov (2 pri prikazanem primeru)

**Bočni tlak (3 mesta):**

$$p_1 = \frac{F}{A_1} = \frac{F}{1 \cdot l_1 \cdot D} \leq p_{dop}$$

$$p_2 = \frac{F}{A_2} = \frac{F}{2n \cdot l_1 \cdot D} \leq p_{dop}$$

$$p_3 = \frac{F}{A_3} = \frac{F}{2 \cdot n \cdot l_1 \cdot D} \leq p_{dop}$$

> 💡 **Intuitivno:** Prilagodni vijak ne nosi natega – nosi strig in bočni pritisk. Bočni tlak je kot pritisk pete ob steno – material se "zgnete", če je prevelik. Mehkejši material (običajno zunanje plošče) je kritičen.

---

## SKLOP 5 – SORNIK (Str. 5)

### Skica

```
  F/2↑        F/2↑
  ┌──────────────────┐
  │l₁│   l₂   │ l₃  │
  │██│ [sornik]│ ██  │
  │  │    d    │     │
  └──────────────────┘
       ↓ F (skupaj)

  Sornik = valj premera d, dolžine L = l₁+l₂+l₃
```

**Dimenzije za skico:**
- Sornik: horizontalna os, vidna od strani
- l₁, l₃ = stranski ušesi (~20% skupne dolžine vsak)
- l₂ = sredinski del (~60%)
- Sile F/2 navzgor na krajih, F navzdol na sredini

### Enačbe

**Strig (2 strižni prereza):**

$$\tau_s = \frac{F}{A} = \frac{2F}{2 \cdot \frac{\pi d^2}{4}} = \frac{F}{\frac{\pi}{4} d^2} \leq \tau_{s,dop}$$

**Upogib (kritičen!):**

$$\sigma_u = \frac{M_{max}}{W_u} = \frac{F \cdot (l_1 + l_2 + l_3)/4}{\frac{\pi d^3}{32}} = \frac{4F(l_1+l_2+l_3)}{\pi d^3}$$

(Moment je maksimalen na sredini sornika)

**Površinski tlak (na 3 mestih):**

$$p_1 = \frac{F}{2 l_1 \cdot d}, \quad p_2 = \frac{F}{d \cdot l_2}, \quad p_3 = \frac{F}{2 \cdot d \cdot l_3}$$

$$p_1 + p_2 + p_3 \leq p_{dop} \text{ (mehkejši material)}$$

> 💡 **Intuitivno:** Sornik je kot prečka na gugalnici. Sila na sredini ga hoče upogniti – to je pogosto kritičen kriterij, ne strig. Površinski tlak = koliko tlačijo ušesa sornik v stranske ploče.

---

## SKLOP 6 – ZVEZA GREDI IN PESTA Z MOSNIKOM (Str. 6)

### Skica

```
  ┌─────────────┐
  │  PESTO      │  ← zunanji del (vrti se skupaj z gredjo)
  │  ┌───┐      │
  │  │GRD│      │  ← gred
  │  │[M]│      │  ← moznik (pravokotnik v utoru)
  │  └───┘      │
  └─────────────┘

  Moznik:    ┌───────────────┐
   profil:   │ b             │  b = širina
             │      h_m      │  h_m = višina
             └───────────────┘
             ←── l_m ────→    l_m = dolžina moznika
             ←── l ──→        l = dolžina stika pesta in mosnika
```

**Dimenzije za skico:**
- b ≈ d/4, h_m ≈ d/4 (standardne vrednosti)
- l_m > l (moznik je daljši od pesta)

### Enačbe

**Strig** – ni kritičen (preskoči)

**Bočni tlak (moznik–pesto):**

$$p = \frac{F}{A} = k \cdot \frac{4 M_t}{d \cdot h_m \cdot l} \leq p_{dop} \text{ (mehk material)}$$

kjer:
- k = koeficient neenakomernosti
  - 1 moznik → k = 1
  - 2+ moznika → k = 1,35
- F = 2Mt/d (sila iz momenta)

> 💡 **Intuitivno:** Moznik je klin med gredjo in pestom – prenaša navor bočno. Bočni tlak je sila, ki stiska moznik ob stranico utora. Če jih je več, niso enakomerno obremenjeni – zato k=1,35 (en nosi več kot drugi).

---

## SKLOP 7 – UTORJENA GRED (Str. 7)

### Skica

```
  D ← zunanji premer pesta
  d ← premer gredi (dno utora)
  
  Gred s utorom (vzdolžni prerez):
  ┌─────────────────────────────┐
  │    [░░░░░░░░░░░░░░░]        │  ← utori (z zob = prebojev)
  │ d_sr          l    h        │
  └─────────────────────────────┘
  d_sr = (d + D) / 2  ← srednji premer
  h = (D - d) / 2    ← višina zoba
  z = število zob
```

**Dimenzije za skico:**
- Nariši pogled od strani: gred z vidnimi utorom
- Desno: prerez (krog z utori naokoli)
- z tipično = 4, 6, 8, 10

### Enačbe

**Površinski tlak:**

$$p = \frac{M_t}{d_{sr} \cdot h \cdot l_p \cdot \frac{z}{2}} \leq p_{dop} \text{ (mehk material)}$$

kjer $d_{sr} = \frac{d + D}{2}$ in $l_p$ = efektivna dolžina stika

> 💡 **Intuitivno:** Utorjena gred je moznik, ki ga je "razrezalo" na z kosov in razvrstilo naokoli. Prenaša večje navore (večja površina stika), a je dražja za izdelavo. Delimo z 2 ker samo polovica zob nosi obremenitev.

---

## SKLOP 8 – GUMIJASTE VZMETI (Str. 8)

### 8a – Tlačna vzmet

```
  ↓ F
  ┌───────┐
  │ guma  │  h = višina v mirovanju
  │       │  d = premer (ali b×l)
  └───────┘
  ↑↑↑↑↑↑↑  (podlaga)
  ←── d ──→
```

**Enačbe:**

Pomik:
$$f = \varepsilon \cdot h = \frac{\sigma}{E} \cdot h = \frac{F \cdot h}{A \cdot E_{tl}}$$

Statična togost:
$$c \approx \frac{F}{f} = \frac{A \cdot E_{tl}}{h}$$

Tlačna napetost:
$$\sigma_H = \frac{F}{A} = \frac{F}{d \cdot b}$$

### 8b – Strižna vzmet

```
  ↑ (fiksno)
  ┌───────┐
  │ guma  │  h = višina
  │       │
  └───────┘  → F (bočna sila)
  
  (deformira se v romb)
```

**Enačbe:**

Pomik:
$$f = \frac{F \cdot h}{A \cdot G}, \quad \gamma = \frac{\tau}{G} = \frac{F}{A \cdot G}$$

Statična togost:
$$c \approx \frac{A \cdot G}{h}$$

Strižna napetost:
$$\tau_s = \frac{F}{A} = \frac{F}{h \cdot b} \leq \tau_{s,dop} \text{ (vzmet)}$$

> 💡 **Intuitivno:** Tlačna vzmet = stisneš jo. Strižna vzmet = strižeš jo (ena ploskev klizi glede na drugo). Guma je dobra za blaženje vibracij ker je elastična in duši. E je modul za tlak, G za strig – pri gumi je G << E.

---

## SKLOP 9 – OSI IN GREDI (Str. 9)

### Skica

```
  F/2         F/2
   ↓           ↓
   A─────────────B
   ←── l₁ ──→←── l₂ ──→
   ←──────── l ──────────→
   
  Zasuk φ:
  φ ↙  ────────── gred ──────────→
```

### 3 kriteriji dimenzioniranja

#### 1. Poves in nagibni kot

$$f \leq f_{dop}$$
$$\beta_{1A} \leq \beta_{L,dop}, \quad \beta_{1B} \leq \beta_{L,dop}$$
$$\varphi \leq \varphi_{dop} = \frac{M_t \cdot L}{G \cdot I_t}$$

#### 2. Kritična vrtilna hitrost

$$n_{krit} = \frac{K}{2\pi} \sqrt{\frac{E}{\rho}}$$

K = koeficient vibriranja (odvisno od podpor)

**Graf obratovalnega področja:**
```
  amplituda
     ↑     /\
     │    /  \
     │   / resonanca
     │  /    \
     ─────────────→ n
       pod  nad
       krit krit
```

Delati je treba daleč od $n_{krit}$ (pod ali nad)!

#### 3. Induostni preračun (torzija)

$$G_x = \frac{M_u}{W_u}, \quad \tau_t = \frac{M_t}{W_t}$$

> 💡 **Intuitivno:** Gred mora biti toga (malo se upogibal), ne sme resonirati (kritična hitrost), in ne sme se plastično deformirati (napetosti). Tri neodvisna vprašanja, vse je treba preveriti.

---

## SKLOP 10 – DRSNI LEŽAJI (Str. 10)

### 10a – Radialni drsni ležaj

```
       F↓
   ┌────────────────┐
   │   ░░░░░░░░░░   │  ← ohišje
   │  (  gred d  )  │  ← gred se vrti
   │   ░░░░░░░░░░   │  ← drsni vložek
   └────────────────┘
        ←── B ──→    B = širina ležaja
```

**Kontrola tlaka:**
$$p = \frac{F}{A} = \frac{F}{d \cdot B}$$

**Zračnost:**
$$S = D - d \quad \text{(absolutna)}, \quad \psi = \frac{S}{d} \quad \text{(relativna)}$$

**Torna moč:**
$$P_t = F \cdot \omega \cdot \mu \quad \text{(koef. trenja = f(mazanje))}$$

**Prestop toplote:**
$$P_h = \alpha \cdot A \cdot (T_{max} - T_{okol})$$

### 10b – Aksialni drsni ležaj

```
       F↓
  ────[===]────  ← tekoči obrez
  ════[▓▓▓]════  ← drsni vložek (torus)
  ════[▓▓▓]════  ← tečaj
       ↑ F      
   dₐ, dᵢ = zunanji in notranji premer
```

**Kontrola tlaka:**
$$p = \frac{F}{A} = \frac{F}{\frac{\pi}{4}(d_a^2 - d_i^2)} \leq p_{dop}$$

> 💡 **Intuitivno:** Radialni ležaj nosi sile pravokotno na os (teža gredi). Aksialni nosi sile vzdolž osi (npr. vijak, ki potiska). Tlak je ključen – prevelik uniči mazalni film.

---

## SKLOP 11 – KOLOTNA SKLOPKA (s spenjalnim vijakom, Str. 11)

### Skica

```
  Mv ↺
   ┌─────────────────────────┐
   │  ┌──────────────────┐   │
Fv→│  │   DISK sklopke   │   │← Fv
   │  └──────────────────┘   │
   └─────────────────────────┘
       Rᵢ  Rsr  Rₐ
   
   n vijakov po obodu
   v ≤ 20 m/s → lijta  
   v > 20 m/s → stružena
```

### Enačbe

**Srednji radij (uteži po Rsr):**

$$R_{sr} = \frac{2}{3} \cdot \frac{R_a^3 - R_i^3}{R_a^2 - R_i^2}$$

**Moment trenja:**

$$M_{tr} = F_v \cdot \mu_g \cdot n \cdot R_{sr}^2$$

**Zahtevana sila vijaka:**

$$F_v = \frac{S \cdot M_{tr,min}}{\mu_g \cdot n \cdot R_{sr}}, \quad M_{tr} \geq M_{tr,min}$$

**Napetosti v vijakih (iste kot spenjalni vijak):**

$$\sigma = \frac{F_v}{\frac{\pi d_2^2}{4}}, \quad \tau = \frac{F_v \cdot \tan(\alpha+\varphi) \cdot \frac{d_2}{2}}{W_p}$$

$$\sigma_p = \sqrt{\sigma^2 + 3\tau^2} \leq \sigma_{dop}$$

> 💡 **Intuitivno:** Sklopka deluje na trenje – vijaki stisnejo dva diska skupaj, trenje med njima prenaša navor. Rsr je "efektivni" radij (ne preprosto sredina ker je obtežba porazdeljena po površini). Faktor varnosti S zagotavlja, da sklopka ne zdrsne ob sunkovnih obremenitvah.

---

## SKLOP 12 – KOLOTNA SKLOPKA (s prilagodnim vijakom, Str. 12)

### Skica

```
        b₁  b₂
   ─────[──|──]───────  ← skupaj b = b₁+b₂
       d₁  (vijak)
   Mv ↺               Dv/2 = polmer vijakov
   
   Fdi = Mtrmax / (Dv/2 · n)
```

### Enačbe

**Kontrola tlaka:**

$$p_1 = \frac{F_{c1}}{A_1} = \frac{F_{c1}}{d_1 \cdot b_1}, \quad F_{d1} = \frac{M_{tr,max}}{\frac{D_v}{2} \cdot n}$$

$$p_2 \geq \frac{F_{c2}}{A_2} = \frac{F_{c2}}{d_1 \cdot b_2}$$

$$p_1 + p_2 \leq p_{dop} \text{ (mehk mat.)}$$

**Kontrola striga:**

$$\tau_s = \frac{F_{c1}}{A} = \frac{F_{c1}}{\frac{\pi d_1^2}{4}} \leq \tau_{s,dop} \text{ (vijaka)}$$

---

## SKLOP 13 – JERMENSKA GONILA (Str. 13)

### Skica

```
  Pri mirovanju (n=0):       Pri obratovanju (n≠0):
  
    ───────────────           ─────────────────
   (   )         (   )       (   )            (   )
    ───────────────           ─────────────────
  
  F₁ = F₂ = F₀              F₁ > F₂
  
  Vektorski trikotnik:
  F_ao     F₀        F_h
    ╲      ↑         ╱
     ╲    │         ╱
      ╲   │        ╱
       ─────────────
         β = kot objetja
```

### Enačbe

**Sila pri mirovanju:**

$$\sin\frac{\beta}{2} = \frac{F_{a0}}{F_0 \cdot 2} \implies F_{a0} = 2 F_0 \sin\frac{\beta}{2}$$

**Sila pri obratovanju:**

$$F_h = \sqrt{F_1^2 + F_2^2 - 2 F_1 F_2 \cos\beta}$$

**Eytelweinova enačba (razmerje sil):**

$$\frac{F_1}{F_2} = e^{\mu \alpha} = m$$

kjer α = kot objetja (rad), μ = koef. trenja jermen/jermenica

> 💡 **Intuitivno:** Jermen deluje na trenje. Na strani, kjer drsi, je napetost večja (F₁). Na prosti strani je manjša (F₂). Eksponentna zveza pove, da z večjim kotom objetja (zavijanjem jermenice) hitro naraste razlika sil – zato je jermenica z majhnim kotom objetja kritična.

---

## SKLOP 14 – VERIGE (Str. 14)

### Tipi in področja uporabe

| Tip | Maks. hitrost | Maks. moč | Uporaba |
|-----|--------------|-----------|---------|
| **S kotalko** | v ≤ 60 m/s | P ≤ 500 kW | poljedeljstvo, gradbeni |
| **S pušo** | v ≤ 30 m/s | — | pogonske, transportne |
| **S sornikom** (str. 15) | v ≤ 2 m/s | — | bremenske (dvigala) |

### Skica (veriga s kotalko)

```
  ←────── t (korak) ──────→
  ┌──┐  ┌──┐  ┌──┐  ┌──┐
  │pl│══│ko│══│se│══│no│
  └──┘  └──┘  └──┘  └──┘
  puša  kotalk sornik notr.lamela
                      zunj.lamela (rdeče)
```

- **t** = korak verige (osnovna dimenzija, iz kataloga)
- Zeleno = zunanji člen, rdeče = notranji člen

---

## SKLOP 15 – VERIGE S SORNIKOM (Str. 15)

### Skica

```
  ┌──────────────────────┐
  │ sornik    zunanja lam│
  │      sortnik notr.lam│
  └──────────────────────┘
  Bremenska veriga (dvigala)
```

**Uporaba:** v ≤ 2 m/s, bremenske verige, dvigalne naprave

---

## SKLOP 16 – KROŽNI ŽAGALNI STROJ (Str. 16)

### Skica z oznakami

```
  ←─────────────────────────────────→
  
  [jermenica]─[fiksan ležaj]─[ohišje]─[prosti ležaj]─[podložka]─[matica]
                                              ↓
                                    [list kroži žage]
                                    (pritrjen z matico)
```

**Sestavni deli (za risanje):**
| Del | Položaj v skici |
|-----|----------------|
| Jermenica | levo, na osi |
| Fiksan ležaj | levo od center |
| Ohišje | sredina |
| Prosti ležaj | desno od centra |
| Podložka + matica | skrajno desno |
| List žage | konec osi (desno) |

> Fiksan ležaj = fiksira os vzdolžno, prosti ležaj = dopušča raztezanje.

---

## SKLOP 17 – SKOBELNI STROJ (Str. 17)

### Skica z oznakami

```
  [fiksan ležaj]─────[skobelno vreteno]─────[prosti ležaj]
        ↑                                          ↑
    (fiksira)                               (dopušča raztez)
                                         [jermenica]─ (za pogon)
```

**Sestavni deli:**
- Fiksan ležaj (levo) – aksialno pozicionira vreteno
- Skobelno vreteno – sredinska os, na njej so skobeljni noži
- Prosti ležaj (desno) – dopušča toplotno raztezanje
- Jermenica – za pogon (na koncu, desno)

---

## SKLOP 18 – SOLEŽNI ZVAR (Str. 18)

### Skica

```
  NATEZNA:    ── [ZVAR] ──→ F    
              σ_nz = F/A_zv

  STRIŽNA:    F→ ─────────
              ─────────── → F
              τ_s = F/A_zv
              
  UPOGIBNA:   F↓
               ──────────
                          
              σ_zu = Mz/Iz · y_zo
```

### Enačbe in pogoji

**Natezna napetost zvara:**
$$\sigma_{nz} = \frac{F}{A_{zv}} \leq \sigma_{zn,dop}$$

**Strižna napetost zvara:**
$$\tau_s = \frac{F}{A_{zv}} < \tau_{zn,dop}$$

**Upogibna napetost zvara:**
$$\sigma_{zu} = \frac{M_z}{I_z} \cdot y_{zo} \leq \sigma_{zu,dop}$$

**Skupna normalna napetost:**
$$\sigma_z = \sigma_{zN} + \sigma_{zU} \leq \sigma_{z0,dop}$$

**Skupna strižna napetost:**
$$\tau_z = \sqrt{\tau_{zS}^2 + \tau_z^2} \leq \tau_{zv,dop}$$

**Primerjalna napetost (soležni zvar):**

$$\boxed{\sigma_p = \sqrt{\sigma_z^2 + 3(\tau_{zS}^2 + \tau_{zU}^2)}} \leq \sigma_{dop}$$

$$\sigma_{dop} = \frac{\sigma_z}{k_1 \cdot k_2}$$

> 💡 **Intuitivno:** Zvar je "lepljeno" spajanje. Kritično je kombinacija normalnih in strižnih napetosti. Von Mises formula (kvadrat σ + 3× kvadrat τ) da ekvivalentno napetost, ki jo primerjamo z dopustno. k₁, k₂ sta faktorja varnosti za kakovost zvara.

---

## 📋 Povzetek: Katere enačbe se VEDNO pojavljajo

| Tip obremenitve | Enačba | Pogoj |
|----------------|--------|-------|
| Nateg/tlak | σ = F/A | σ ≤ σdop |
| Strig | τ = F/A | τ ≤ τdop |
| Upogib | σ = M/W | σ ≤ σdop |
| Torzija | τ = Mt/Wt | τ ≤ τdop |
| Bočni tlak | p = F/(l·d) | p ≤ pdop |
| Von Mises | σp = √(σ²+3τ²) | σp ≤ σdop |

## 📏 Prerezi (iz tvojih obstoječih not)

- [[vztrajnostni_moment_prerezi]] – I_z = bh³/12 (pravokotnik), πd⁴/64 (krog)
- [[upogib_krozni_prerez]] – W = πd³/32
- [[upogib_c_prerez]] – Steinerjeva formula: I_vzp = I_T + A·e²

---

*Vir: Skeniran zvezek (Opticno-prebrana-kopija_20200702-5.pdf), 18 strani*
