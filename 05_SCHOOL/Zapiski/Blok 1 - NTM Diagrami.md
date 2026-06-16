---
tags: [mehanika, NTM, diagrami, notranje-sile, upogibni-moment, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 1 — N, T, M Diagrami

## VSE ENAČBE

```
REAKCIJE (3 statični pogoji):
  ΣFx = 0,  ΣFy = 0,  ΣMA = 0

NOTRANJE SILE (metoda preseka, pogled z LEVE):
  N(s) = ΣFx,levo
  T(s) = ΣFy,levo
  M(s) = Σmomentov_levo

DIFERENCIALNI ODNOSI (Schwerder/pravila):
  dT/ds = -q(s)     ← q navzdol = T pada
  dM/ds = T(s)      ← M je integral T!

OBLIKA DIAGRAMA:
  q=0:     T = const,  M = linearna
  q≠0:     T = linearna, M = parabola (2. stopnja)

Mmax: kjer T=0  →  T(s₀)=0  →  vstavi s₀ v M(s)

TIPIČNI Mmax:
  Prostoležeč, q:     Mmax = qL²/8   (sredina)
  Prostoležeč, F sr.: Mmax = FL/4    (sredina)
  Kombinacija q+F:    Mmax = qL²/8 + FL/4
  Konzola, F:         Mmax = F·L     (vpetje)
  Konzola, q:         Mmax = qL²/2  (vpetje)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "nariši diagrame notranjih sil", "diagram N, T, M"
- "upogibni moment", "prečna sila", "osna sila"
- "potek notranjih sil", "kvalitativno nariši"
- Podano: nosilec z obtežbo (q, F, M₀), podporami

**Kaj je podano:**
- Oblika nosilca (prostoležeč, konzola, okvir, lomljeni)
- Obtežba: $q$ [kN/m], $F$ [kN], $M_0$ [kNm]
- Podpore: členek, valj, vpetje

**Kaj se sprašuje:**
- Diagrame $N(s)$, $T(s)$, $M(s)$ za celo konstrukcijo
- Vrednost $M_{max}$, lega $M_{max}$
- Reakcije v podporah

---

## Kako začeti reševati

**Korak 1 — Reakcije:**

$$\sum F_x = 0, \quad \sum F_y = 0, \quad \sum M_A = 0$$

| Podpora | Reakcije |
|---------|----------|
| Nepremični členek | $A_x$, $A_y$ |
| Premični (drsni) členek | $B_y$ |
| Vpetje | $A_x$, $A_y$, $M_A$ |

> **Kontrola:** Vstavi v tretjo enačbo — mora biti = 0!

**Korak 2 — Polja:**
Razdeli nosilec na **področja** (med dvema sprememba obtežbe).

**Korak 3 — Metoda preseka:**
Za vsako področje na razdalji $s$ od levega konca:
$$T(s) = A_y - \sum F_{y,levo}(s), \qquad M(s) = A_y \cdot s - \sum M_{levo}(s)$$

**Korak 4 — $M_{max}$:**
$$T(s_0) = 0 \quad \Rightarrow \quad s_0 \quad \Rightarrow \quad M_{max} = M(s_0)$$

**Korak 5 — Riši:**
- Šrafura **pravokotno** na os
- Označi $M_{max}$ s številko
- Preveri robne pogoje!

---

## Diferencialne odvisnosti — Zlata pravila

$$\frac{dT}{ds} = -q(s), \qquad \frac{dM}{ds} = T(s)$$

| Obtežba na segmentu | $T(s)$ | $M(s)$ | Oblika |
|---------------------|--------|--------|--------|
| Ni obtežbe ($q=0$) | konstanta | linearna | ravna črta |
| $q$ enakomerna | linearna (pada) | parabola | 2. stopnja |
| Točkovna $F$ | **skok** za $F$ | lom (kink) | prelom |
| Točkovni moment $M_0$ | brez spremembe | **skok** za $M_0$ | |

---

## Robni pogoji — Obvezna kontrola

| Mesto | Pogoj | Zakaj |
|-------|-------|-------|
| Prosti konec | $M = 0$, $T = 0$ | Nič ne drži |
| Členek / tečaj | $M = 0$ | Ne prenaša momenta |
| Vpetje (konec konzole) | $M = M_A$, $T = A_y$ | Reakcija |
| Prostoležeč | $M = 0$ na obeh robih | |

> ⚠️ **M = 0 pri VSAKEM notranjem členku!** — najpogostejša past na izpitu.

---

## Posebnosti: Lomljeni nosilci in okviri

Na mestu **vogala (togega spoja)**:
- $M$ je **neprekinjen** (brez skoka)
- $N$ iz stebra postane $T$ v prečnici (in obratno!)
- Oba dela sta v ravnovesju z momentom v vogalu

**3D nosilci (gredi strojev):**
6 notranjih veličin: $N$, $T_y$, $T_z$, $M_t$ (torzija), $M_y$, $M_z$

---

## Prepoznavanje razlik med podtipi nalog

| Tip naloge | Kako prepoznaš | Posebnost |
|------------|----------------|-----------|
| Prostoležeč + $q$ | Dve podpori, enakomerna obtežba | $M_{max}$ na sredini, parabola |
| Konzola + $F$ | Eno vpetje, prosti konec | $M_{max}$ pri vpetju |
| Lomljeni / okvir | Horizontalni in vertikalni elementi | N/T se zamenjata v vogalu |
| Notranji členek | "Gerberjev nosilec" | $M = 0$ v členu! |
| Kombinacija $q + F$ | Oba hkrati | Superpozicija |

---

## Kombinacije z drugimi bloki

### Blok 0 + 1 (Statika → NTM) ← **OSNOVA VSEGA**
Vedno najprej reakcije (Blok 0), nato notranje sile.

### Blok 1 + 2 (NTM → Upogib napetosti)
$M_{max}$ iz tega bloka se vstavi v $\sigma = M/W$.

### Blok 1 + 2.5 (NTM → Deformacije)
$M(x)$ iz tega bloka je vhod za dif. enačbo $EI \cdot y'' = M(x)$.

### Blok 1 + 5 (NTM → Torzija)
Za gredi: v kritičnem prerezu vzamemo $M$ in $M_t$ hkrati.

---

## Hitri seznam formul

```
ΣFx=0, ΣFy=0, ΣM=0   ← reakcije

dT/ds = -q    dM/ds = T    Mmax: kjer T=0

OBLIKA:  q→parabola M,  F→lom,  M0→skok M
ROBNI:   M=0 pri pros. koncu, členu, prosti podpori
LOM. NOS: N↔T se zamenjata v vogalu!

Mmax tipični:
  qL²/8    FL/4    qL²/2+FL/4(konzola)
```

---

## Povezave

- [[Koncept - NTM Diagrami]] ← podrobna razlaga
- [[Vaje - NTM diagrami - Vse vrste]] ← rešene naloge
- [[Blok 0 - Statika]] ← predhodni blok (reakcije)
- [[Blok 1.5 - Geometrijske Karakteristike]] ← naslednji korak
- [[Blok 2 - Upogib]] ← uporaba M za napetosti
- [[Blok 2.5 - Deformacije pri Upogibu]] ← uporaba M(x)
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
