---
tags: [mehanika, kinematika, pol-hitrosti, hitrost, mehanizem, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — Kinematika mehanizmov (pol hitrosti)

## Namen

Za dano gibanje mehanizma določiti hitrosti točk, kotno hitrost telesa in pol hitrosti (trenutni pol). Pojavlja se na izpitih iz Mehanike I.

---

![[pol_hitrosti.svg]]

## Osnove kinematike togega telesa

Za togo telo (rigid body) velja:

$$\vec{v}_B = \vec{v}_A + \vec{\omega} \times \vec{r}_{AB}$$

- $\vec{v}_A$, $\vec{v}_B$ = hitrost točk A, B
- $\vec{\omega}$ = kotna hitrost telesa [rad/s]
- $\vec{r}_{AB}$ = vektor od A do B

V 2D (ravninsko gibanje):

$$v_B = v_A + \omega \cdot r_{AB}$$

kjer je $r_{AB}$ = razdalja med točkama, smer $v_A + \omega \times r_{AB}$ pa ⊥ na $r_{AB}$.

---

## Pol hitrosti (trenutni pol)

**Definicija:** Točka $P$ telesa (ali njene razširitve), ki ima v danem trenutku **hitrost nič** ($v_P = 0$). Telo se v tistem trenutku vrti okoli pola.

$$v_A = \omega \cdot r_{PA}$$

kjer je $r_{PA}$ = razdalja od pola P do točke A.

> 🔍 **Fizikalni pomen:** Telo se v vsakem trenutku "obrača" okoli nekega pola. Za prostoležeče telo je pol v neskončnosti (translacija), za kolesečo se kolo je pol na talni točki.

---

## Iskanje pola hitrosti

**Metoda:** Pol leži na sečišču **pravokotnic na smeri hitrosti** posameznih točk.

### Korak za korakom:

1. Določi smer hitrosti točke A (iz pogoja gibanja: npr. kolesanje, drsanje po vodni podlagi)
2. Nariši pravokotnico na $\vec{v}_A$ skozi A
3. Določi smer hitrosti točke B
4. Nariši pravokotnico na $\vec{v}_B$ skozi B
5. **Presečišče = pol P**

```
     v_A ↑        v_B ↑
      |             |
  ----A-----------  B----
      |    telo    |
      |             |
      ↓             ↓
  pravokotnica   pravokotnica
  skozi A        skozi B
        \         /
         \       /
          \     /
           P (pol!)
```

---

## Algoritem

```
1. Nariši shemo z vsemi vezmi in danimi hitrostmi
2. Določi smer gibanja vsake točke (iz kinematičnih pogojev)
3. Nariši pravokotnice na smeri hitrosti → najdi pol P
4. Izmeri razdalje r_PA, r_PB, r_PC ...
5. ω = v_A / r_PA  (kotna hitrost)
6. v_B = ω · r_PB  (hitrosti ostalih točk)
7. Smer v_B: ⊥ na r_PB, v smeri vrtenja (kot ω)
```

> **Enota:** $\omega$ [rad/s], $v$ [m/s], $r$ [m]

> **Preveritev:** Računaj hitrost iste točke iz dveh smeri → morata se ujemati!

---

## Primer 1 — Drsnik na vodoravni površini

**Podatki:** Ročica AB, $|AB| = L$. Točka A drsi vodoravno (hitr. $v_A$ →), točka B se giblje navpično (hitr. $v_B$ ↑).

**Smer hitrosti:**
- $v_A$ je vodoravna → pravokotnica na $v_A$ je **navpična** (skozi A)
- $v_B$ je navpična → pravokotnica na $v_B$ je **vodoravna** (skozi B)

**Pol P:** presečišče navpičnice (skozi A) in vodoravnice (skozi B).

Razdalje: $r_{PA} = $ navpična razdalja A–P = $y_A$, $r_{PB} = $ vodoravna razdalja B–P = $x_B$.

$$\omega = \frac{v_A}{r_{PA}}, \qquad v_B = \omega \cdot r_{PB}$$

---

## Primer 2 — Kolo, ki se kotali po tleh

**Pogoj:** Kotalna točka $C$ (stična točka kolo-tla) ima hitrost **nič** → pol je pri $C$!

$$\omega = \frac{v_{sr}}{R} \quad \text{(hitrost središča / polmer)}$$

$$v_{vrha} = \omega \cdot 2R = 2 v_{sr}$$

$$v_A = \omega \cdot r_{CA} \quad \text{(splošna točka A)}$$

Smer $v_A$: ⊥ na daljico CA.

---

## Primer 3 — Štirivezni mehanizem

Za telo z dvema vezema (npr. ročica AF vpeta pri A, ročica BG vpeta pri B):

1. Točka F (na ročici AF, ki se vrti pri A): $v_F$ ⊥ AF
2. Točka G (na ročici BG, ki se vrti pri B): $v_G$ ⊥ BG
3. Pol telesa FG = presečišče pravokotnic skozi F in G (usmeritev ⊥ $v_F$ in ⊥ $v_G$)

> **Posebnost:** Ročice AF in BG se sami vrtita → vsaka ima svoj pol (pri A in B)!

---

## Primer 4 — Iz izpita (kinematika z maso)

**Podatki:** Masa $m$ na krogu polmera $R$ = 9,3 m, $f$ = frekvenca

Nihanje: $v = R \cdot \omega = R \cdot 2\pi f$

To je dinamika, ne kinematika mehanizmi — glejte [[Koncept - Zakoni Gibanja]].

---

## Pogosta napaka

> **Napaka:** Pravokotnice narisati na **daljico** AB namesto na smer **hitrosti**!
> 
> Pravokotnica teče skozi točko A **⊥ na vektor $\vec{v}_A$** — ne ⊥ na telo.

> **Napaka:** Zamešanje pola hitrosti (trenutni pol, $v=0$) s težiščem. Pol se premika s časom!

---

## Posebni primeri

| Gibanje | Pol |
|---------|-----|
| Čista translacija | Pol v neskončnosti (vse točke enake $v$) |
| Čisto vrtenje | Pol = os vrtenja |
| Kotaljenje brez zdrsavanja | Pol = stična točka |
| Splošno ravninsko | Pol = presečišče pravokotnic |

---

## Hitrost in pospešek

Za **pospešek** točke B glede na A:

$$\vec{a}_B = \vec{a}_A + \vec{\alpha} \times \vec{r}_{AB} - \omega^2 \vec{r}_{AB}$$

- $\vec{\alpha}$ = kotni pospešek
- $-\omega^2 \vec{r}_{AB}$ = centripetalni pospešek (kaže od B proti A)

> Centripetalni pospešek je **vedno** prisoten pri krogilijočem gibanju (≠ 0, razen ko ω=0)!

> **glej:** [[Koncept - NTM Diagrami]]

---

## Rešene naloge

- Primer iz izpita Statike (28.1.2005) — iskanje pola in hitrosti

---

## Povezave

- [[Koncept - Zakoni Gibanja]]
- [[Koncept - Premo Gibanje]]
- [[Koncept - NTM Diagrami]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]
