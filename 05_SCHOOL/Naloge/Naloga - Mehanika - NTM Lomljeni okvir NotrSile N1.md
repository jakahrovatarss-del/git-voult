---
tags: [mehanika, NTM, lomljeni-okvir, gerber, statika, vaje]
predmet: Mehanika
datum: 2026-06-18
vir: "NotrSileVaje (1).pdf — Naloga 1"
status: rešeno
---

# Naloga — NTM Lomljeni okvir z notranjim členkom

## Namen

Izračunaj N, T, M v ravninskem okvirju z notranjim Gerber členkom in nariši diagrame.

---

## Dano

![[ntm_lomljeni_okvir_n1.svg|697]]

| Oznaka | Vrednost |
|--------|---------|
| $F_1$ | 1 kN (navpično navzdol, pri D) |
| $F_2$ | 2 kN (vodoravno v desno, na AC pri $y = 2$ m) |
| $q$ | 0,125 kN/m (enakomerna navpična, na prečki CD) |
| Dolžina AC | 4 m (navpična) |
| Dolžina CD | 4 m (vodoravna) |
| Dolžina DB | 2 m (navpična) |
| A, B | Nepremični členek (2 reakciji vsak) |
| C | **Notranji Gerber členek** ($M_C = 0$!) |
| D | Togi spoj |

---

## KORAK 1 — Analiza konstrukcije (FBD)

**Tri palice:**
- **Steber AC** (navpično, 4 m): A = nepremičen členek, C = notranji členek, $F_2 = 2$ kN pri $y = 2$ m
- **Prečka CD** (vodoravno, 4 m): enakomerna obtežba $q = 0{,}125$ kN/m, rezultanta $Q = 0{,}5$ kN
- **Steber DB** (navpično, 2 m): D = togi spoj, B = nepremičen členek

**Problem:** 4 neznane reakcije ($A_x, A_y, B_x, B_y$), le 3 enačbe ravnotežja → statično nedoločen!

**Rešitev — notranji členek C** doda 4. enačbo:
$$\sum M_C^{levo} = 0 \quad \text{(moment okrog C gledano z leve = 0)}$$

---

## KORAK 2 — Reakcije

**Na levem delu (steber AC) — moment okrog C:**

$$\sum M_C^{levo} = 0: \quad A_x \cdot 4 + F_2 \cdot 2 = 0 \quad \Rightarrow \quad \boxed{A_x = -1\ \text{kN}}$$

**Globalno $\sum F_x = 0$:**

$$A_x + F_2 + B_x = 0 \quad \Rightarrow \quad \boxed{B_x = -1\ \text{kN}}$$

**Globalno $\sum M_A = 0$** (moment okrog A, ročice: $F_2$ pri 2 m, $Q$ pri 2 m, $F_1$ pri 4 m, $B_x$ pri 2 m, $B_y$ pri 4 m):

$$2 \cdot 2 + 0{,}5 \cdot 2 + 1 \cdot 4 + 1 \cdot 2 - B_y \cdot 4 = 0 \quad \Rightarrow \quad \boxed{B_y = 2{,}75\ \text{kN}}$$

**Globalno $\sum F_y = 0$:**

$$A_y + B_y - Q - F_1 = 0 \quad \Rightarrow \quad \boxed{A_y = -1{,}25\ \text{kN}}$$

> ⚠️ $A_y = -1{,}25$ kN pomeni, da kaže **navzdol** — steber AC je v **nategu**!

---

## KORAK 3 — Notranje sile po poljih

### Steber AC ($s = 0$ pri A, navzgor do C)

**N (osna sila):** $A_y = -1{,}25$ kN vleče navzdol → steber se razteza → **nateg**

$$\boxed{N_{AC} = +1{,}25\ \text{kN}} \quad \text{(konstanten po celotnem stebru)}$$

**T (prečna sila):** $A_x = -1$ kN deluje levo, $F_2 = 2$ kN pri $s = 2$ m:

| Odsek | $T(s)$ |
|-------|--------|
| $0 \leq s \leq 2$ m | $T = -1$ kN |
| pri $s = 2$ m | **Skok za $+F_2 = +2$ kN** |
| $2\ \text{m} \leq s \leq 4\ \text{m}$ | $T = +1$ kN |

**M (moment):** integriramo T (brez $q$ → linearen):

| Točka | $M$ |
|-------|-----|
| A ($s = 0$) | $M = 0$ kNm |
| $s = 2$ m | $M = -1 \cdot 2 = -2$ kNm |
| C ($s = 4$ m, **členek!**) | $M = 0$ kNm ← **mora biti 0** |

---

### Prečka CD ($s = 0$ pri C, levo → desno)

V točki C se sile "prelijejo": $C_x = 1$ kN → osna sila prečke, $C_y = 1{,}25$ kN → prečna sila.

$$\boxed{N_{CD} = -C_x = -1\ \text{kN}} \quad \text{(tlak, konstanten)}$$

$$T(s) = -C_y - q \cdot s = -1{,}25 - 0{,}125 \cdot s$$

| $s$ | $T$ |
|-----|-----|
| 0 (pri C) | $-1{,}25$ kN |
| 4 m (pri D) | $-1{,}75$ kN |

$$M(s) = -C_y \cdot s - \frac{q \cdot s^2}{2} = -1{,}25s - 0{,}0625s^2$$

| $s$ | $M$ |
|-----|-----|
| 0 (pri C) | 0 kNm |
| 2 m | $-2{,}75$ kNm |
| 4 m (pri D) | $-6{,}00$ kNm |

Potek: **parabola** (ker $q \neq 0$). Ekstrem izven območja — ni lokalne nič T → ni vmesnega ekstrema M.

---

### Steber DB ($s = 0$ pri B, navzgor do D)

$$\boxed{N_{DB} = -B_y = -2{,}75\ \text{kN}} \quad \text{(tlak)}$$

$$\boxed{T_{DB} = +1\ \text{kN}} \quad \text{(konstanten, od } B_x\text{)}$$

$$M_{DB}(s=0) = 0 \ \text{kNm}, \quad M_{DB}(s=2\ \text{m}) = 2\ \text{kNm}$$

> **Togi spoj D:** Moment iz prečke CD = $-6$ kNm. Moment iz stebra DB = $+2$ kNm. Razlika $4$ kNm je reakcijski moment togega spoja.

---

## KORAK 4 — Kontrola in intuicija

**Kontrolni pogoji:**

| Kontrola | Vrednost | Status |
|----------|---------|--------|
| M v A (prosta podpora) | $M_A = 0$ | ✅ |
| M v B (prosta podpora) | $M_B = 0$ | ✅ |
| M v C (notranji členek) | $M_C = 0$ | ✅ |
| $\sum F_x = 0$ | $-1+2-1 = 0$ | ✅ |
| $\sum F_y = 0$ | $-1{,}25+2{,}75-0{,}5-1=0$ | ✅ |

**Ključna opažanja:**
1. **Osna sila se prelevi v vogalu:** $N_{AC} = 1{,}25$ kN (navpično) → postane $T_{CD} = 1{,}25$ kN (vodoravno pri C)
2. **Skok v T** natanko pri točkovni sili $F_2$
3. **Parabola v M** natanko tam, kjer je $q \neq 0$ (na CD)
4. **Negativni $A_y$** → steber AC je **nategnjen** — presenečenje!

---

## Flashcards

Q: Zakaj je sistem statično nedoločen in kako to rešimo?
A: 4 neznanke, 3 enačbe. Notranji členek C doda pogoj M_C=0 → 4. enačba.

Q: Kakšen je predznak N v stebru AC?
A: +1,25 kN (nateg) — Ay kaže navzdol, kar steber razteza.

Q: Zakaj je M paraboličen na prečki CD?
A: q≠0 → T linearna → M = ∫T = kvadratna funkcija (parabola).

Q: Kaj pomeni togi spoj D za moment?
A: Moment je zvezen (ne skokuje) — oba dela D prenašata isti moment. Razlika med -6 in +2 je v reakcijskem momentu spoja.

---

## Povezave

- [[Blok 0 - Statika]] — reakcije, Gerber memberki
- [[Blok 1 - NTM Diagrami]] — N, T, M postopek
- [[Vaje - NTM diagrami - Vse vrste]] — TIP A2: lomljeni nosilci
- [[Cheat Sheet - Mehanika Celotna]] — TIP A2 in A3
- [[Koncept - NTM Diagrami]]
