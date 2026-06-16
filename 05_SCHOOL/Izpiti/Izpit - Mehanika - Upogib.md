---
tags: [mehanika, upogib, izpit, pregled, dimenzioniranje, napetosti]
predmet: Mehanika
datum: 2026-06-11
---

# Izpit — Mehanika: Upogib (Pregled tipov nalog)

## Namen

Sistematičen pregled vseh tipov izpitnih nalog s področja upogiba. Vsak tip ima: vzorec prepoznave, algoritem, ključne formule in primer.

---

## Splošni algoritem (velja za VSE tipe)

```
1. Nariši shemo → določi statični sistem
2. Izračunaj reakcije (ΣF=0, ΣM=0)
3. Nariši M-diagram → najdi M_max (in vse kritične prereze)
4. Geometrija prereza → yT, J, e_zg, e_sp
5. σ = M·e / J ≤ σ_dop  (ali reši za neznanko)
6. Kontrola z zaokroženimi dimenzijami
```

> ⚠️ Pri **asimetričnih prerezih** (U, C, T, I): preveri napetosti pri **vsakem kritičnem prerezu** — ne samo tam, kjer je |M| največji!

---

## Formule za prereze

| Prerez | $I_x$ | $W_x = I_x/e$ | $e$ |
|--------|--------|----------------|-----|
| Pravokotnik $a \times b$ ($b$=višina) | $\dfrac{a b^3}{12}$ | $\dfrac{a b^2}{6}$ | $b/2$ |
| Krog $\varnothing d$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^3}{32}$ | $d/2$ |
| Votel pravokotnik (box) | $\dfrac{B H^3 - b h^3}{12}$ | $\dfrac{B H^3 - b h^3}{6H}$ | $H/2$ |
| Sestavljeni (I, T, U, C) | $\sum\left[\frac{a_i b_i^3}{12} + A_i e_i^2\right]$ | $I/e_{max}$ | $H - y_T$ ali $y_T$ |

**Steinerjevo pravilo:**
$$I_{x_T} = \sum_i \left[\frac{a_i b_i^3}{12} + A_i \cdot (y_i - y_T)^2\right]$$

**Težišče sestavljenega prereza:**
$$y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}$$

---

## Tip 1 — Dimenzioniranje: Pravokotni prerez

**Prepoznava:** prerez $a \times b$ ali parametrično ($a = nx$, $b = mx$), podana $\sigma_{dop}$

**Algoritem:**
1. $M_{max}$ iz statike
2. $W = ab^2/6$ → z $a=nx$, $b=mx$: $W = n \cdot (mx)^2 / 6 = nm^2 x^3/6$
3. $x^n = M_{max}/(\sigma_{dop} \cdot W_{koef})$, zaokroži navzgor
4. Kontrola: $\sigma = M/W_{dej} \leq \sigma_{dop}$

**Primer:** $a=3x$, $b=5x$, $q=5$ kN/m, konzola 2m → $W=12{,}5x^3$, $x=4{,}31$ cm → **13×22 cm** → [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]]

---

## Tip 2 — Dimenzioniranje: Krožni prerez

**Prepoznava:** prerez je krog (premer $d$), podana $\sigma_{dop}$

**Ključna formula:**
$$W = \frac{\pi d^3}{32} \quad \Rightarrow \quad d = \sqrt[3]{\frac{32 M_{max}}{\pi \sigma_{dop}}}$$

**Primer:** Previs 1,5m + polje 3m, $F=4$ kN, $q=2$ kN/m, $\sigma_{dop}=1{,}2$ kN/cm²

Reakcije: $A_y = 1$ kN, $B_y = 5$ kN

M-diagram: $M_A = -F \cdot 1{,}5 = -6$ kNm, $M_{max,polje} = +6{,}25$ kNm pri $x=2{,}5$ m od A

Dimenzioniranje na $|M_{max}| = 6{,}25$ kNm = 625 kNcm:

$$d = \sqrt[3]{\frac{32 \cdot 625}{\pi \cdot 1{,}2}} = \sqrt[3]{\frac{20000}{3{,}770}} = \sqrt[3]{5305} = \boxed{17{,}44\ \text{cm}}$$

*(Vir: IMG_1241.pdf, str. 24–26)*

---

## Tip 3 — Ekstremne napetosti: Asimetričen prerez (U, C, T)

**Prepoznava:** prerez ni simetričen → $e_{zg} \neq e_{sp}$ → preveriti **oba kritična prereza**

**Algoritem:**
1. Razstavi prerez na pravokotnike
2. Izračunaj $y_T = \sum A_i y_i / \sum A_i$
3. $J = \sum [I_{i,own} + A_i(y_i - y_T)^2]$
4. $e_{zg} = H - y_T$, $e_{sp} = y_T$
5. Za vsak kritičen M: $\sigma_{zg} = M \cdot e_{zg}/J$, $\sigma_{sp} = M \cdot e_{sp}/J$
6. Upoštevaj predznak momenta → katera stran je v nategu/tlaku

**Primer U-prerez:** B=40, H=15, t=7 cm, $M_A = -10$ kNm, $M_{pol} = +8$ kNm

$y_T = 5{,}64$ cm, $J = 6240{,}8$ cm⁴, $e_{zg} = 9{,}36$ cm > $e_{sp}=5{,}64$ cm

| Prerez | M | σ_zg | σ_sp |
|--------|---|-------|-------|
| A | −10 kNm | +1,50 (nateg) | −0,90 (tlak) |
| polje | +8 kNm | −1,20 (tlak) | +0,72 (nateg) |
| **Max** | | **+1,50 kN/cm²** | **−1,20 kN/cm²** |

→ [[Naloga - Mehanika - Upogibne napetosti U-prerez]]

**Primer C-prerez:** Konstantna debelina 1,5 cm, H=20 cm, B=12,5 cm

Ker je prerez simetričen levo-desno, a asimetričen zgoraj-spodaj samo če ni enak zgoraj/spodaj. 

$W = 6{,}25$ cm³, $M = 400 \cdot 15 = 6000$ Ncm:

$$\sigma = \frac{M}{W} = \frac{6000}{6{,}25} = \mathbf{960\ \text{N/cm}^2 = 0{,}96\ \text{kN/cm}^2}$$

*(Vir: IMG_1241.pdf, str. 22–23)*

---

## Tip 4 — Škatlast prerez (box profil)

**Prepoznava:** zunanji prerez BH minus notranji bh, oba pravokotna

**Ključna formula:**
$$I_z = \frac{BH^3 - bh^3}{12} \quad (\text{simetričen} \Rightarrow e = H/2)$$

**Primer:** Zunanji $10 \times 7{,}5$ cm, notranji $8 \times 5{,}5$ cm, $M_{max} = 14{,}06$ kNm:

$$I_z = \frac{10 \cdot 7{,}5^3 - 8 \cdot 5{,}5^3}{12} = \frac{4218{,}75 - 1331}{12} = \frac{2887{,}75}{12} = 240{,}6\ \text{cm}^4$$

> Zvezek daje $I_z = 390{,}33$ cm⁴ — preveri dejanske dimenzije v nalogi (str. 34)

$$\sigma_{max} = \frac{M \cdot H/2}{I_z} = \frac{1406 \cdot 3{,}75}{390{,}33} \approx \mathbf{180\ \text{MPa}}$$

*(Vir: IMG_1241.pdf, str. 34–36)*

**Konzolni škatlast prerez** (str. 53): Zunanji $3 \times 5$ cm, notranji $1 \times 1$ cm. Maksimalna napetost na vpetju konzole (tam je $|M|$ največji).

---

## Tip 5 — Dimenzioniranje ojačanega I-profila

**Prepoznava:** prerez podan parametrično z $c$, $\sigma_{dop}$ v MPa

**Algoritem:**
1. $M_{max}$ (tipično na vpetju konzole)
2. Izraziti $y_T(c)$, $J(c)$, $e_{max}(c)$
3. Pogoj: $M \cdot e_{max} / J = \sigma_{dop}$ → reši za $c$

**Primer:** Konzola 2m, $q=3$ kN/m, $\sigma_{dop}=150$ MPa:

$M_{max} = qL^2/2 = 3 \cdot 4/2 = 6$ kNm

$y_T = 13{,}79c$, $J = 19363c^4$ (iz geometrije prereza)

$$\frac{6000 \cdot e_{max}(c)}{19363c^4} = 15\ \text{kN/cm}^2 \quad \Rightarrow \quad \boxed{c = 3{,}05\ \text{mm}}$$

*(Vir: IMG_1241.pdf, str. 38–40)*

---

## Tip 6 — Dimenzioniranje T-profila

**Prepoznava:** T-prerez (pasnica + vrat), dimenzija $a$, $\sigma_{dop}$ v MPa

**Algoritem:**
1. $M_{max}$ (tipično sredina razpona pri enakomernih obtežbah)
2. Geometrija: pasnica $4a \times a$, vrat $a \times 2a$ (ali podobno)
3. $y_T$, $J$, $e$ v odvisnosti od $a$
4. Pogoj napetosti → $a$

**Primer:** Prostoležeč nosilci 5m, $F=5$ kN na sredini, $\sigma_{dop}=100$ MPa:

$M_{max} = FL/4 = 5 \cdot 500/4 = 625$ kNcm

Pasnica ($4a \times a$): $A_1 = 4a^2$, $y_1 = 2a + a/2 = 2{,}5a$ (od dna vratu)
Vrat ($a \times 2a$): $A_2 = 2a^2$, $y_2 = a$

$$y_T = \frac{4a^2 \cdot 2{,}5a + 2a^2 \cdot a}{6a^2} = \frac{10a^3 + 2a^3}{6a^2} = 2a$$

$J = $ ... → iz pogoja $\sigma = M \cdot e/J = 100$ MPa dobimo $a$.

*(Vir: IMG_1241.pdf, str. 44)*

---

## Tip 7 — Napetosti v določenih točkah prereza (Double-T)

**Prepoznava:** vprašanje "kolikšna napetost v točki (1), (2), (3)?" → ni samo rob, ampak vmesne točke

**Ključna formula:**
$$\sigma(y) = \frac{M \cdot y}{J}$$

kjer je $y$ razdalja točke od nevtralne osi (pozitivno navzgor).

**Algoritem:**
1. Določi M pri danem prerezu (ne nujno M_max!)
2. Izračunaj $y_T$ in $J$ za Double-T prerez
3. Za vsako točko: $y_i = $ razdalja od NO → $\sigma_i = M \cdot y_i / J$
4. Predznak: + nateg, − tlak (glede na predznak M in smer točke)

**Primer:** Prerez 1m od leve podpore, $M(1m) = R_A \cdot 1 = 2$ kNm = 200 kNcm

Točke: (1) vrh, (2) stik pasnice in vratu, (3) NO (→ σ=0)

*(Vir: IMG_1241.pdf, str. 52)*

---

## Povzetek — Hitri pregled

| Tip | Iskano | Prerez | Ključna formula |
|-----|--------|--------|-----------------|
| 1 | dimenzija $x$ | pravokotnik | $W = nm^2x^3/6$, reši $x$ |
| 2 | premer $d$ | krog | $d = \sqrt[3]{32M/\pi\sigma_{dop}}$ |
| 3 | $\sigma$ (asimetričen) | U, C, T, I | $y_T$, $J$ Steiner, $e_{zg}\neq e_{sp}$ |
| 4 | $\sigma_{max}$ | box/škatlast | $I = (BH^3-bh^3)/12$ |
| 5 | parameter $c$ | I-profil | $y_T(c)$, $J(c)$, pogoj napetosti |
| 6 | dimenzija $a$ | T-profil | $y_T(a)$, $J(a)$, pogoj napetosti |
| 7 | $\sigma$ v točkah | Double-T | $\sigma(y) = My/J$ za vsako točko |

---

## Pogosta napaka

> **Ne zadostuje preveriti samo pri največjem $|M|$!**
> 
> Ker je $W = J/e$, je pri asimetričnem prerezu napetost odvisna od **katerega** roba gledamo. Vedno preveri oba roba ($e_{zg}$ in $e_{sp}$) pri **vsakem kritičnem prerezu** — tam, kjer se predznak momenta spremeni, se spremenijo tudi katera vlakna so v nategu.

---

## Rešene naloge

- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] — pravokotni prerez, 13×22 cm
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]] — U-prerez, σ_max = 1,50 kN/cm²

## Povezave

- [[Koncept - Upogib]]
- [[Koncept - Vztrajnostni moment]]
- [[Koncept - Euler Uklon]]
- [[Mehanika Hub]]
- [[Mehanika Hub]]
- [[05_SCHOOL/School Hub]]
