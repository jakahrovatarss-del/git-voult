---
tags: [fizika, poglavje-2, kinematika]
predmet: Fizika
datum: 2026-06-10
---

# Premo Gibanje

![Galileo Galilei - prosti pad](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg/250px-Justus_Sustermans_-_Portrait_of_Galileo_Galilei%2C_1636.jpg)

## Namen

Opis premega gibanja (translacije) vzdolž osi x — lega, premik, hitrost, pospešek. Kinematika: **kaj** se giblje, ne **zakaj**.

## Teorija / Glavne ideje

### Lega in premik

Lega telesa = koordinata $x(t)$ glede na izhodišče.

Premik (sprememba lege):
$$\boxed{\Delta x = x_2 - x_1}$$

> ⚠️ Premik ≠ razdalja. Premik je vektorska količina (ima predznak).

### Hitrost

**Povprečna hitrost** v intervalu $\Delta t$:
$$v = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1} \tag{2.2}$$

**Trenutna hitrost** (odvod lege po času):
$$\boxed{v = \frac{dx}{dt}} \tag{2.3}$$

Na diagramu $x(t)$: trenutna hitrost = **strmina tangente** na krivuljo.

### Pospešek

**Povprečni pospešek:**
$$a = \frac{\Delta v}{\Delta t} \tag{2.4}$$

**Trenutni pospešek** (odvod hitrosti po času):
$$\boxed{a = \frac{dv}{dt}} \tag{2.5}$$

Na diagramu $v(t)$: pospešek = strmina tangente.

### Enakomerno pospešeno gibanje (EPG)

Velja, ko je $a = \text{konst.}$

| Enačba | Pomen |
|--------|-------|
| $v(t) = v_0 + at$ | hitrost v odvisnosti od časa (2.6) |
| $x(t) = x_0 + v_0 t + \frac{1}{2}at^2$ | lega v odvisnosti od časa (2.7) |
| $v^2 = v_0^2 + 2a\Delta x$ | brez časa (2.8) |

> Enakomerno gibanje ($v = \text{konst.}$) je poseben primer EPG z $a = 0$.

### Prosti pad

Telo pada s pospeškom $g = 9{,}81\ \text{m/s}^2$ (navzdol).

$$a = -g \quad \text{(os y navzgor)}$$

| Veličina | Enačba |
|----------|--------|
| Hitrost | $v_y(t) = v_{0y} - gt$ |
| Čas do vrha | $t_m = \frac{v_{0y}}{g}$ (2.11) |
| Maksimalna višina | $y_{max} = \frac{v_{0y}^2}{2g}$ (2.12) |

V najvišji točki: $v = 0$. Čas padanja = čas vzpenjanja.

## Simboli in enote

| Simbol | Pomen | Enota |
|--------|-------|-------|
| $x$, $y$ | lega | m |
| $\Delta x$ | premik | m |
| $v$ | hitrost | m/s |
| $a$ | pospešek | m/s² |
| $g$ | težni pospešek | 9,81 m/s² |
| $t$ | čas | s |

## Primeri / Naloge

**Prosti pad:** Telo pade z višine $h = 20\ \text{m}$. Kdaj udari v tla?

$$h = \frac{1}{2}gt^2 \implies t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{40}{9{,}81}} \approx 2{,}02\ \text{s}$$

**Hitrost ob udaru:** $v = gt = 9{,}81 \times 2{,}02 \approx 19{,}8\ \text{m/s}$

## Flashcards

- **Q:** Kako izračunamo trenutno hitrost iz $x(t)$?  
  **A:** $v = \frac{dx}{dt}$ — odvod lege po času.

- **Q:** Katere 3 enačbe opisujejo EPG?  
  **A:** $v = v_0 + at$, $x = x_0 + v_0t + \frac{1}{2}at^2$, $v^2 = v_0^2 + 2a\Delta x$

- **Q:** Kolikšen je pospešek prostega pada?  
  **A:** $g = 9{,}81\ \text{m/s}^2$ navzdol.

- **Q:** Kaj je razlika med premikom in razdaljo?  
  **A:** Premik je vektorski (ima predznak), razdalja je skalarna (vedno ≥ 0).

- **Q:** Kaj velja za hitrost v najvišji točki navpičnega meta?  
  **A:** $v = 0$.

## Povezave

- [[Mehanika Hub]] — nadrejena nota (kinematika, dinamika)
- [[Fizika Hub]] — hub predmeta
- [[Koncept - Zakoni Gibanja]] — naslednje poglavje (vzroki gibanja)
- [[Specifična Toplota]] — soroden fizika koncept
- [[SpaceX]] — aplikacija zakonov gibanja (rakete)
