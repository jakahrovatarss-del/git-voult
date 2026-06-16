---
tags: [mehanika, upogib, deformacije, poves, upogibnica, diferencialna-enačba, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 2.5 — Deformacije pri Upogibu

## VSE ENAČBE

```
DIFERENCIALNA ENAČBA UPOGIBNICE:
  EI · y''(x) = -M(x)    ali   EI · y'' = M(x)  (odvisno od dogovora o predznaku)

INTEGRACIJA:
  EI · y'(x) = ∫ -M(x) dx + C1      (zasuk)
  EI · y(x)  = ∬ -M(x) dx² + C1·x + C2  (poves)

ROBNI POGOJI:
  Vpetje:      y = 0,  y' = 0
  Članek/pin:  y = 0
  Prosti konec: M = 0, T = 0   (za C1, C2 ne neposredno)

TIPIČNI POVESI:
  Konzola, F na koncu:    ymax = FL³/3EI    (↓ na prostem koncu)
  Konzola, q:             ymax = qL⁴/8EI   (↓ na prostem koncu)
  Prostoležeč, F sr.:     ymax = FL³/48EI  (↓ na sredini)
  Prostoležeč, q:         ymax = 5qL⁴/384EI (↓ na sredini)
  Prostoležeč, F na a,b:  fi = Fi·ai²·bi² / (3EIL)

SUPERPOZICIJA:
  y_skupni = y1 + y2 + ... + yn   (velja za lin.-el. material)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "poves", "pomik", "deformacija", "zasuk"
- "za koliko se upogne", "upogibnica"
- "diferencialna enačba", "integracijska konstanta"
- "dopusten poves $f_{dop}$", "L/300", "L/500"

**Kaj je podano:**
- Nosilec z obtežbo ($q$, $F$)
- Material $E$ [kN/cm²], prerez → $I$ [cm⁴]
- Morda: omejitev povesa $f_{dop} = L/n$

**Kaj se sprašuje:**
- $y_{max}$ = maksimalni poves [cm ali mm]
- Zasuk $y'$ v točki
- Preverjanje dopustnega povesa

---

## Kako začeti reševati

**Metoda direktnih formul (hitrejša):**

1. Prepoznaj tip sistema (konzola, prostoležeč, kombinirano)
2. Vzemi formulo iz tabele
3. Vstavi vrednosti — pazi na enote!

> ⚠️ Enote: $F$ [kN], $L$ [cm], $E$ [kN/cm²], $I$ [cm⁴] → $y$ [cm]

---

**Metoda dvojne integracije (za nestandarden primer):**

**Korak 1:** Zapiši $M(x)$ (iz Blok 1, metoda preseka)

**Korak 2:** Integriraj — zasuk:
$$EI \cdot y'(x) = \int M(x)\, dx + C_1$$

**Korak 3:** Integriraj — poves:
$$EI \cdot y(x) = \iint M(x)\, dx^2 + C_1 x + C_2$$

**Korak 4:** Vstavi robne pogoje → določi $C_1$, $C_2$:
- Prostoležeč: $y(0) = 0$ in $y(L) = 0$
- Konzola: $y(0) = 0$ in $y'(0) = 0$

**Korak 5:** Poišči $y_{max}$ kjer $y'(x) = 0$:
$$y'(x_0) = 0 \quad \Rightarrow \quad x_0 \quad \Rightarrow \quad y_{max} = y(x_0)$$

---

## Robni pogoji — Tabela

| Podpora | Pogoji |
|---------|--------|
| Vpetje (clamped) 🧱 | $y = 0$, $y' = 0$ |
| Členek/pin △ | $y = 0$ |
| Premični/drsni ○ | $y = 0$ (normalno), $M = 0$ |
| Prosti konec | $M = 0$, $T = 0$ (ni direkten pogoj za $y$) |
| Notranje členkovito | $y$ neprekinjen, $M = 0$ |

---

## Tipični povesi — Hitri rezultati

| Sistem | Lega max | $y_{max}$ |
|--------|----------|-----------|
| Prostoležeč, $q$ | sredina | $\dfrac{5 q L^4}{384 EI}$ |
| Prostoležeč, $F$ na sredini | sredina | $\dfrac{F L^3}{48 EI}$ |
| Prostoležeč, $F$ na $a$, $b=L-a$ | pod $F$ | $\dfrac{F a^2 b^2}{3 EIL}$ |
| Konzola, $F$ na koncu | prost konec | $\dfrac{F L^3}{3 EI}$ |
| Konzola, $q$ | prost konec | $\dfrac{q L^4}{8 EI}$ |

---

## Zasuki pri tipičnih sistemih

| Sistem | Kraj | $\phi = y'$ |
|--------|------|-------------|
| Prostoležeč, $q$ | pri podpori | $\dfrac{q L^3}{24 EI}$ |
| Prostoležeč, $F$ sr. | pri podpori | $\dfrac{F L^2}{16 EI}$ |
| Konzola, $F$ | pri vpetju | $\dfrac{F L^2}{2 EI}$ |
| Konzola, $q$ | pri vpetju | $\dfrac{q L^3}{6 EI}$ |

---

## Superpozicija

Kadar deluje več sil hkrati:
$$y_{skupni}(x) = y_{F_1}(x) + y_{F_2}(x) + y_q(x) + \ldots$$

**Pogoj:** Linearno elastičen material (Hooke) + majhne deformacije.

**Primer:** Prostoležeč z $q$ in $F$ na sredini:
$$y_{max} = \frac{5qL^4}{384EI} + \frac{FL^3}{48EI}$$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Metoda |
|-----|----------------|--------|
| Standardni sistem | Konzola ali prostoležeč, $q$ ali $F$ | Direktna formula |
| Več sil hkrati | Dve ali več točkovnih sil | Superpozicija |
| Nestandarden sistem | Vmesni členek, nastavek | Dvojna integracija |
| Dopusten poves | "$f \leq L/300$" | Izračunaj $y_{max}$, preveri |
| Zasuk iskanje | "zasuk pri podpori" | Deriviraj $y(x)$ |

---

## Kombinacije z drugimi bloki

### Blok 2 + 2.5 (Napetosti + Deformacije) ← **Obe sočasno**
Dimenzioniranje: pogosto preverjamo tako napetost ($\sigma_{dop}$) kot poves ($f_{dop}$).

### Blok 1 + 2.5 (NTM → Deformacije)
$M(x)$ iz bloka 1 → vstavi v dif. enačbo.

### Blok 1.5 + 2.5 (Geometrija → Deformacije)
$I = bh^3/12$ iz prereza → izračunaj $EI$.

---

## Materialni podatki za $EI$

| Material | $E$ [kN/cm²] | $EI$ za $10 \times 20$ cm |
|----------|-------------|--------------------------|
| Les | 1 000 | $1000 \cdot 10 \cdot 8000/12 = 6{,}67 \times 10^6$ kNcm² |
| Jeklo | 21 000 | $\approx 140 \times 10^6$ kNcm² |

---

## Pogosta napaka

- Pozabiti predznak: $EI \cdot y'' = \pm M(x)$ — preveri dogovor!
- Enote: $L$ MORA biti v cm, ko je $E$ v kN/cm² in $I$ v cm⁴
- Superpozicija: sile morajo biti na ISTEM sistemu (podpore enake)
- $y_{max}$ ni nujno na sredini, če $F$ ni na sredini!

---

## Povezave

- [[Blok 2 - Upogib]] ← napetosti pri upogibu
- [[Blok 1 - NTM Diagrami]] ← $M(x)$ za integriranje
- [[Blok 1.5 - Geometrijske Karakteristike]] ← vrednost $EI$
- [[Blok 6 - Kinematika]] ← pomiki v mehanizmih
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
