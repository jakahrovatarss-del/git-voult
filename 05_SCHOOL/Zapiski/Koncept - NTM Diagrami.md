---
tags: [mehanika, statika, NTM, notranje-sile, diagrami, izpit]
predmet: Mehanika
datum: 2026-06-14
---

# Koncept — N, T, M Diagrami (Notranje statične količine)

## Namen

Določiti potek osne sile N, prečne sile T in upogibnega momenta M vzdolž konstrukcije. **Pojavi se na VSAKEM izpitu iz Mehanike I.**

---

![[ntm_diagrami.svg|637]]

> **Vaje z rešenimi primeri (vsi tipi):** [[Vaje - NTM diagrami - Vse vrste]]

## Definicije in predznaki

| Količina | Simbol | Fizikalni pomen | Pozitiven predznak |
|----------|--------|-----------------|-------------------|
| Osna sila | $N$ | Nateg/tlak vzdolž osi | Nateg (vlečenje) |
| Prečna sila | $T$ | Strižna obremenitev ⊥ osi | Levi del: ↑, desni del: ↓ |
| Upogibni moment | $M$ | Upogibanje elementa | Sagging (upogib navzdol, spodaj nateg) |

> ⚠️ **Standardni dogovor za T:** ko seštevam sile na **levem** prerezu, je $T > 0$, če so sile usmerjene **navzgor**. Ko seštevam na **desnem**, je $T > 0$, če so sile usmerjene **navzdol**.

> ⚠️ **Standardni dogovor za M:** $M > 0$ (sagging) = vlakna spodaj v nategu, zgoraj v tlaku. Oziroma: desni del se vrti v smeri urinih kazalcev glede na prerez.

---

## Splošni algoritem

```
1. Nariši shemo → označi točke (A, B, C...), koordinate
2. Izračunaj reakcije (ΣFx=0, ΣFy=0, ΣM=0) — brez tega ne gre!
3. Razdeli konstrukcijo na PODROČJA (med karakterističnimi točkami)
4. Za vsako področje: naredi rez, seštej sile na ENI strani (levo ali desno, kar je enostavnejše)
5. N(x), T(x), M(x) zapiši kot funkcije koordinate x
6. Posebne vrednosti: rob, podpore, mesta obtežb
7. Nariši diagrame pod shemo
```

---

## Metoda prerezov (korak za korakom)

### Korak 1 — FBD in reakcije

Določi vse reakcije iz ravnotežnih enačb. **Brez tega ne moreš začeti.**

- Členek: $H, V$ (2 reakciji)
- Drsna podpora: $V$ (1 reakcija, smer ⊥ drsišču)
- Vpetje: $H, V, M$ (3 reakcije)

### Korak 2 — Rez in ravnotežje

Na mestu koordinate $x$ naredi rez. Na eni strani (npr. levi) seštej vse:

$$N(x) = \sum F_{x,levo}$$
$$T(x) = \sum F_{y,levo}$$
$$M(x) = \sum M_{levo} \text{ (momenti zunanjih sil glede na mesto reza)}$$

> 🔍 **Fizikalni pomen:** Interno sile v prerezu morajo uravnotežiti vse zunanje sile na levi strani.

### Korak 3 — Oblika diagrama

| Obtežba | N(x) | T(x) | M(x) |
|---------|------|------|------|
| Brez obtežbe | konstanta | konstanta | linearna (trikotnik) |
| Točkovna sila F | skok pri F | skok pri F | prelom (konica) |
| Porazdeljena q [kN/m] | linearna | linearna | parabolična |
| Točkovni moment M₀ | brez vpliva | brez vpliva | skok za M₀ |

### Korak 4 — Robni pogoji

| Tip podpore/konca | N | T | M |
|-------------------|---|---|---|
| Prosti konec | 0 | 0 | 0 |
| Členek | / | / | **0** ← ključno! |
| Drsna podpora | / | 0 | 0 |
| Vpetje | / | / | $\neq 0$ splošno |
| Notranja členkovita zveza | / | / | **0** |

> ⚠️ **Najpogostejša napaka:** pozabiti, da je $M = 0$ v členku!

---

## Zveze med T in M

$$T(x) = \frac{dM}{dx}$$
$$q(x) = -\frac{dT}{dx} = -\frac{d^2M}{dx^2}$$

**Posledici:**
- Kjer je $T = 0$ → $M$ ima **ekstrem** (iščemo lokalni maksimum/minimum!)
- Kjer je $q = 0$ → $T$ je **konstanten**
- Kjer je $q = 0$ → $M$ je **linearen**

> **glej:** [[Koncept - Upogib#Korak 2 — Diagram upogibnih momentov]]

---

## Vrste podpor — pregled

![[ntm_vrste_podpor.svg|637]]

| Podpora | Reakcije | Neznank | Pogoj |
|---------|----------|---------|-------|
| Nepomični členek (tečaj) | $R_x$, $R_y$ | 2 | — |
| Pomični členek (roller) | $R_y$ | 1 | x prost |
| Togo vpetje | $R_x$, $R_y$, $M_A$ | 3 | — |
| Prost konec | — | 0 | $T=0$, $M=0$ ✓ |
| Notranji členek (Gerber) | doda pogoj | −1 | $M=0$ ✓ |

> **Statična določenost:** $\sum \text{reakcij} = 3$ za ravninski problem.

> **zobacz:** [[STATIKA#Podpore in reakcije]]

---

## Primer 1 — Prostoležeč nosilec s točkovno silo

**Podatki:** $L = 6$ m, $F = 12$ kN na sredini ($a = 3$ m)

**Reakcije:** $A_y = B_y = 6$ kN (simetrija)

**Področje 1** ($0 \leq x \leq 3$ m, od A):

$$N(x) = 0$$
$$T(x) = +A_y = +6\ \text{kN}$$
$$M(x) = A_y \cdot x = 6x\ \text{kNm}$$

**Področje 2** ($3 \leq x \leq 6$ m, od A):

$$T(x) = A_y - F = 6 - 12 = -6\ \text{kN}$$
$$M(x) = A_y \cdot x - F \cdot (x-3) = 6x - 12(x-3) = -6x + 36\ \text{kNm}$$

**Vrednosti:**

| x | N | T | M |
|---|---|---|---|
| 0 | 0 | +6 kN | 0 ✓ (prosti konec) |
| 3 | 0 | skok +6→−6 | +18 kNm (max!) |
| 6 | 0 | −6 kN | 0 ✓ (prosti konec) |

> M_max = 18 kNm nastopi **pri sili F** (tam kjer T skoči)

> **glej:** [[Koncept - Upogib#Korak 1 — Statični sistem in reakcije]]

---

## Primer 2 — Konzola s porazdeljeno obtežbo

**Podatki:** $L = 4$ m, $q = 3$ kN/m, vpetje pri A (levo)

**Koordinata x od prostega konca** (pri B = 0):

$$T(x) = q \cdot x = 3x\ \text{kN}$$
$$M(x) = -\frac{q x^2}{2} = -1{,}5 x^2\ \text{kNm}$$

(negativen predznak ker hogging — konzola se upogiba navzgor)

**Vrednosti:**

| x | T | M |
|---|---|---|
| 0 (prosti konec B) | 0 ✓ | 0 ✓ |
| 4 m (vpetje A) | 12 kN | −24 kNm |

**Reakcije vpetja:** $A_y = 12$ kN ↑, $M_A = +24$ kNm ↗

---

## Primer 3 — L-profil (lomljeni nosilci, L-oblika)

Za L-profile ali ločne konstrukcije:

1. **Razdeli na horizontalni in vertikalni del** posebej
2. Vsak del ima svojo koordinato (npr. $x$ in $y$)
3. Pri spoju prenesi notranje sile: **$N$ enega dela postane $T$ drugega!**
4. M je v spoju **kontinuiren** (ni skoka)

> ⚠️ **Najpogostejša past:** Ko preidemo iz prečke v steber, se vlogi N in T zamenjata — kar je bilo vzdolžna (osna) sila v prečki, postane prečna sila v stebru in obratno!

**Primer (F = 8 kN vodoravno pri vrhu stebra):**

| Odsek | N | T | M |
|-------|---|---|---|
| Prečka AB | −8 kN (tlak) | +6 kN | 0 → 24 kNm |
| Steber BC | +6 kN (nateg) | +8 kN | 24 → 0 kNm |

> M = 24 kNm v točki B je enako v prečki in stebru — **M je v vozlišču enak!** ✓

> **zie:** [[Vaje - NTM diagrami - Vse vrste#NALOGA 3 — Lomljeni nosilci]]

---

## Primer 4 — Portalni okvir

> **Ključni koncept: statična nedoločenost in simetrija**

Portalni okvir (stebra + prečka) je pogosto **statično nedoločen**:
- Togo vpetje A (3 neznanke) + členek B (2 neznanki) = 5 neznank > 3 enačb → nedoločeno
- Rešitev na izpitu: poenostavitev na **oba členka** + **simetrija**

**Simetričen portal z $q$ na prečki:**

$$A_y = B_y = \frac{q \cdot L}{2}, \quad A_x = B_x = 0$$

| Odsek | N | T | M |
|-------|---|---|---|
| Steber CA | $-A_y$ (tlak) | 0 | 0 |
| Prečka CD | 0 | $A_y - qx$ (linear) | parabola, vrh $M_{max}$ |

$$M_{max} = \frac{q \cdot L^2}{8} \quad \text{(pri simetričnem portalu, na sredini prečke)}$$

> 💡 **V lesarstvu:** $M_{max}$ dimenzionira prerez prečke. Vogali (C, D) pri idealnem simetričnem portalu nimajo momenta — v realnosti (veter) postanejo **kritična mesta**.

> 💡 **Steber je v tlaku** — ugodno za les (dober v tlaku vzdolž vlaken).

> **zie:** [[Vaje - NTM diagrami - Vse vrste#NALOGA 4 — Portalni okvir]]

---

## Hitri pregled oblik

```
Samo reakcije (brez vmesne obtežbe):
N: ══════  (konstanta)
T: ══════  (konstanta)
M: ╱╲     (linearna, trikotnik)

Točkovna sila F:
T: ══╗    (skok pri F)
     ╚══
M: ╱ ╲   (prelom pri F)

Porazdeljena q:
T: ╱    (linearna)
M: ⌒    (parabola, max kjer T=0)

Točkovni moment M₀:
T: ══════ (brez vpliva)
M: ══╗   (skok za M₀)
     ╚══
```

---

## Pogosta napaka: predznak T na desni strani

Ko računam T iz **desne strani**:
$$T(x) = -\sum F_{y,desno}$$

(negativen predznak ker menjamo stran reza!)

Ali pa preprosto: **vedno računaj iz LEVE strani** — manj zmede.

---

## Rešene naloge

- [[Naloga - Mehanika - Dimenzioniranje krozni prerez upogib]] — M-diagram previsnega nosilca
- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] — M-diagram prostoležečega nosilca

---

## Povzetek — tipi nalog na izpitu

| Tip | Posebnost | Pazi na |
|-----|-----------|---------|
| Prosta greda | $N=0$, $M=0$ na obeh koncih | Razdalja rezultante $q$ |
| Nosilci s previsom | $A_y$ je lahko majhen ali negativen | Predznak $A_y$ |
| Lomljeni nosilci (L) | $N \neq 0$, N↔T zamenjata vlogi | Koordinatni sistem pri stebru |
| Portalni okvir | Simetrija → $A_y = B_y$, steber v tlaku | Statična nedoločenost |
| $F$ pod kotom + $M_0$ | Razstavi $F$, predznak $M_0$ v $\sum M$ | Preskok M pri $M_0$ |

---

## Povezave

- [[Vaje - NTM diagrami - Vse vrste]]
- [[Koncept - Upogib]]
- [[Koncept - Napetostno stanje]]
- [[Koncept - Euler Uklon]]
- [[STATIKA]]
- [[Mehanika Hub]]
- [[05_SCHOOL/School Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]
