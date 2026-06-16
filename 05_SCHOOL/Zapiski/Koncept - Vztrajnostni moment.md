---
tags: [mehanika, vztrajnostni-moment, prerez, steiner, težišče, koncept]
predmet: Mehanika
datum: 2026-06-11
---

# Koncept: Vztrajnostni moment (I)

## Namen

Vztrajnostni moment prereza meri **odpornost telesa proti upogibanju in uklonu**. Je **geometrijska** lastnost prereza — ne materiala. Večji $I$ → bolj toga konstrukcija → manjše napetosti pri isti obtežbi.

> **Fizikalni pomen:** $I = \int y^2 \, dA$ — vsak delček površine prispeva sorazmerno s **kvadratom** razdalje od osi. Material daleč od osi prispeva enormno. Zato so I-profili tako učinkoviti: max materiala je daleč od osi.

---

## Korak 1 — Enačbe za enostavne prereze

![[vztrajnostni_moment_prerezi.svg|585]]

| Prerez | $I_z$ (ok. hor. osi) | $I_y$ (ok. vert. osi) | $A$ |
|--------|----------------------|-----------------------|-----|
| Pravokotnik $b \times h$ | $\dfrac{b \cdot h^3}{12}$ | $\dfrac{h \cdot b^3}{12}$ | $b \cdot h$ |
| Kvadrat $a \times a$ | $\dfrac{a^4}{12}$ | $\dfrac{a^4}{12}$ | $a^2$ |
| Krog $\varnothing d$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^2}{4}$ |
| Votel pravokotnik | $\dfrac{BH^3 - bh^3}{12}$ | $\dfrac{HB^3 - hb^3}{12}$ | $BH - bh$ |

> ⚠️ **Pazi na vrstni red $b$ in $h$!**
> - $I_z = \dfrac{b \cdot h^3}{12}$ — $h$ je dimenzija v smeri osi z (**navpično**)
> - $I_y = \dfrac{h \cdot b^3}{12}$ — $b$ je dimenzija v smeri osi y (**vodoravno**)

---

## Korak 2 — Šibka in močna os

Za pravokoten prerez $b \times h$ (kjer $b < h$):

$$I_{max} = \frac{b \cdot h^3}{12} \quad \text{(močna os)} \qquad I_{min} = \frac{h \cdot b^3}{12} \quad \text{(šibka os)}$$

- **Upogib** → vrtimo prerez tako, da je $I_{max}$ v smeri obtežbe (npr. pravokotnik stoječe, ne ležeče)
- **Uklon** → nastopi vedno okoli šibke osi (palica se ukloni v "najlažji" smeri)

---

## Korak 3 — Steinerjev izrek (vzporedna os)

Ko os **ne** gre skozi težišče prereza, dodamo Steinerjev člen:

$$\boxed{I_{vzp} = I_T + A \cdot e^2}$$

| Simbol | Pomen |
|--------|-------|
| $I_T$ | vztrajnostni moment glede na težiščno os elementa |
| $A$ | površina elementa |
| $e$ | razdalja med težiščno osjo elementa in skupno osjo |

> **Ključno:** Steinerjev člen $A \cdot e^2$ je **vedno pozitiven** — nikoli ga ne odštevaj, ne glede na smer.

---

## Korak 4 — Sestavljeni prerezi (I, T, U, C)

Ko prerez sestavimo iz več pravokotnih delov, sledimo postopku:

### Korak 4a — Razstavi prerez

| Profil | Razstavi na | Opomba |
|--------|-------------|--------|
| U-profil | 2 navpični steni + spodnja pasnica | 3 pravokotniki |
| C-profil | zgornja pasnica + stojina + spodnja pasnica | 3 pravokotniki |
| T-profil | vrat + zgornja pasnica | 2 pravokotnika |
| I-profil | 2 pasnici + stojina | 3 pravokotniki |
| Box (škatlast) | zunanji − notranji pravokotnik | odšteješ notranjost |

### Korak 4b — Izračunaj površine in težišča posameznih delov

Referenčna ravnina: tipično **spodnji rob** celotnega prereza.

| Del $i$ | $A_i$ [cm²] | $y_i$ [cm od spodaj] | $A_i \cdot y_i$ |
|---------|-------------|----------------------|-----------------|
| del 1 | ... | ... | ... |
| del 2 | ... | ... | ... |
| **Σ** | $\sum A_i$ | — | $\sum A_i y_i$ |

### Korak 4c — Skupno težišče

$$\boxed{y_T = \frac{\sum A_i \cdot y_i}{\sum A_i}}$$

### Korak 4d — Steinerjev izrek za vsak del

$$I_{x_T} = \sum_i \left[\underbrace{\frac{a_i \cdot b_i^3}{12}}_{\text{lastni } I} + \underbrace{A_i \cdot (y_i - y_T)^2}_{\text{Steiner}}\right]$$

### Korak 4e — Razdalji skrajnih vlaken

$$e_{zg} = H_{total} - y_T \qquad e_{sp} = y_T$$

> Ker $e_{zg} \neq e_{sp}$ pri asimetričnih prerezih, sta odpornostna momenta različna:
> $$W_{zg} = \frac{I}{e_{zg}} \qquad W_{sp} = \frac{I}{e_{sp}}$$

---

## Primer: U-prerez B=40, H=15, t=7 cm

**Korak 4b — Tabela:**

| Del | Dimenzije | $A_i$ | $y_i$ (od spodaj) | $A_i y_i$ |
|-----|-----------|-------|--------------------|-----------|
| leva stena | 7×15 | 105 | 7,5 | 787,5 |
| desna stena | 7×15 | 105 | 7,5 | 787,5 |
| spodnja pasnica | 26×7 | 182 | 3,5 | 637,0 |
| **Σ** | | **392** | | **2212** |

**Korak 4c:**
$$y_T = \frac{2212}{392} = 5{,}643 \text{ cm}$$

**Korak 4d:**
$$I = 2\left[\frac{7\cdot15^3}{12} + 105(7{,}5-5{,}643)^2\right] + \left[\frac{26\cdot7^3}{12} + 182(3{,}5-5{,}643)^2\right] = 6240{,}8 \text{ cm}^4$$

**Korak 4e:**
$$e_{zg} = 15 - 5{,}643 = 9{,}357 \text{ cm} \qquad e_{sp} = 5{,}643 \text{ cm}$$

→ Polna naloga: [[Naloga - Mehanika - Upogibne napetosti U-prerez]]

---

## Vztrajnostni polmer

$$i = \sqrt{\frac{I_{min}}{A}}$$

Meri, kako "daleč od osi" je porazdeljena masa prereza. Uporablja se za izračun vitkosti pri uklonu:

$$\lambda = \frac{l_u}{i}$$

---

## Odpornostni moment (W) — povezava z upogibom

$$W_x = \frac{I_x}{e}$$

kjer je $e$ razdalja od nevtralne osi do skrajnega vlakna.

| Prerez | $W_x$ |
|--------|--------|
| Pravokotnik $a \times b$ ($b$=višina) | $\dfrac{ab^2}{6}$ |
| Krog $\varnothing d$ | $\dfrac{\pi d^3}{32}$ |
| Box $BH$ − $bh$ | $\dfrac{BH^3-bh^3}{6H}$ |

Pogoj upogibne trdnosti: $\sigma = M / W_x \leq \sigma_{dop}$

→ Podrobno pri [[Koncept - Upogib]]

---

## Tipične vrednosti

| Prerez | Dimenzije | $I$ |
|--------|-----------|-----|
| Lesena deska (uklon) | 2,5 × 20 cm | $I_{min} = 20\cdot2{,}5^3/12 = 26{,}04$ cm⁴ |
| Lesen steber | 12 × 12 cm | $I = 12^4/12 = 1728$ cm⁴ |
| U-profil 40×15×7 | — | $J = 6240{,}8$ cm⁴ |

---

## Povezave

- [[Koncept - Euler Uklon]] — uporaba $I_{min}$ za uklon
- [[Koncept - Upogib]] — uporaba $I$, $W$ za upogibne napetosti
- [[Naloga - Mehanika - Uklon lesene deske]]
- [[Naloga - Mehanika - Uklon leseni steber F_max]]
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]]
- [[Naloga - Mehanika - Upogibne napetosti U-prerez]]
- [[Mehanika Hub]]
- [[Mehanika Hub]]
