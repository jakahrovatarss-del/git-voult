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

### Izračun reakcij

Za statično določene sisteme vedno dve enačbi:

$$\sum F_y = 0: \quad R_A + R_B = \sum F_{zunanji}$$

$$\sum M_{\text{točka}} = 0: \quad \text{(momenti vseh sil okoli izbrane točke)}$$

**Praktični nasvet:** Za $\sum M$ vedno izberi tisto podporo, ki ima dve neznani (npr. vpetje), ali pa točko, kjer ena od reakcij odpade.

**Predznaki pri $\sum M$:** Protiurno = pozitivno (po dogovoru).

**Enakomerna obtežba $q$** se nadomesti z rezultanto $Q = q \cdot L$ v težišču (na sredini obremenjenega dela).

---

## Korak 2 — Diagram upogibnih momentov

### Kaj je M-diagram?

M-diagram prikazuje, kako se **notranji upogibni moment** spreminja vzdolž nosilci. Je osnova za:
- določitev **mesta** max napetosti (kjer je |M| največji oz. kjer je M·e/J največji)
- določitev **predznaka** napetosti (katera vlakna so v nategu, katera v tlaku)

### Pravilo predznaka

![[m_diagram_predznak.svg|740]]

| Moment | Ukrivljanje | Zgornja vlakna | Spodnja vlakna |
|--------|-------------|----------------|----------------|
| **M > 0** (sagging ⌣) | navzdol | tlak (−) | nateg (+) |
| **M < 0** (hogging ⌢) | navzgor | nateg (+) | tlak (−) |

### Kako narisati M-diagram — postopek

1. **Izračunaj reakcije** (korak 1)
2. **Razreži nosilci** na odseke med karakterističnimi točkami (podpore, sile, začetek/konec q)
3. **Za vsak odsek izpiši M(x)** — vsota momentov vseh sil **levo** od prereza x:
   $$M(x) = \sum_{\text{levo}} F_i \cdot d_i - \sum_{\text{levo}} M_i$$
4. **Poišči ekstrema:**
   - Pri točkovnih silah: prelom v M-diagramu
   - Pri enakomernem q: parabola; ekstrem tam, kjer je $Q(x) = dM/dx = 0$ (prečna sila = 0)
5. **Preveri robne pogoje:**
   - Prosti konec → $M = 0$
   - Členek → $M = 0$
   - Vpetje → $M \neq 0$ (splošno)

### Ključna zveza: Prečna sila in moment

$$Q(x) = \frac{dM}{dx} \qquad \Leftrightarrow \qquad M(x) = \int Q(x)\,dx$$

- Kjer je $Q = 0$ → lokalni ekstrem M (max ali min)
- Kjer Q skoči (točkovna sila) → prelom v M-diagramu
- Pod enakomerno obtežbo q → Q linearen, M paraboličen

### M-diagram za tipične obtežbe — vizualno

![[m_diagram_tipi.svg|740]]

| Obtežba | Sistem | Oblika diagrama | $M_{max}$ | Mesto |
|---------|--------|-----------------|-----------|-------|
| $q$ po celem razponu $L$ | prostoležeč | parabola | $\dfrac{qL^2}{8}$ | sredina |
| $F$ na sredini $L$ | prostoležeč | trikotnik | $\dfrac{FL}{4}$ | sredina |
| $F$ na razdalji $a$ od A | prostoležeč | trikotnik | $\dfrac{F \cdot a \cdot b}{L}$ | pod F |
| $q$ na konzoli $L$ | konzola | parabola | $\dfrac{qL^2}{2}$ | vpetje |
| $F$ na koncu konzole $L$ | konzola | trikotnik | $F \cdot L$ | vpetje |
| $F$ na previsu $a$ | previsni | trikotnik | $F \cdot a$ (neg.) | podpora |

### Previsni nosilci — posebnost

Ko je previs obremenjen, nastane pri prvi podpori **negativen moment**:

$$M_A = -F \cdot a \quad \text{(pri točkovni sili na previsu dolžine } a\text{)}$$

V polju nato moment naraste in doseže maksimum tam, kjer je prečna sila Q = 0, nato pa pade na 0 pri drugi podpori.

**Primer** (previs 1m + polje 2,5m, F=10kN, q=16kN/m):
- $M_A = -F \cdot 1 = -10$ kNm (negativen pri A)
- $M_{max,polje} = +8$ kNm pri $\xi = 1{,}5$ m od A
- Enačba: $M(\xi) = -10 + 24\xi - 8\xi^2$

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

- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] — pravokotnik, konzola 2m, q=5kN/m → **13×22 cm**
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] — U-prerez, previs 1m + polje 2,5m → **σ_max = 1,50 kN/cm²**

Pregled vseh tipov: [[Izpit - Mehanika - Upogib]]

## Povezave

- [[Koncept - Vztrajnostni moment]]
- [[Koncept - Euler Uklon]]
- [[Izpit - Mehanika - Upogib]]
- [[mehanika]]
- [[STATIKA]]
- [[Mehanika Hub]]
