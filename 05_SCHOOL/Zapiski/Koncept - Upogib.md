---
tags: [mehanika, upogib, dimenzioniranje, napetost, koncept]
predmet: Mehanika
datum: 2026-06-11
---

# Koncept: Upogib (Bending)

## Namen

Upogib nastopi, ko prečna obtežba povzroči ukrivljanje nosilca. Vzdolž prereza nastanejo **normalne napetosti** — tlačne na eni strani in natezne na drugi nevtralne osi (NO).

## Osnovna enačba upogiba

$$\boxed{\sigma = \frac{M}{W_x} \leq \sigma_{dop}}$$

kjer je $W_x$ **odpornostni moment** prereza.

## Odpornostni moment

$$W_x = \frac{I_x}{e}$$

- $I_x$ = vztrajnostni moment prereza glede na nevtralno os
- $e$ = razdalja od nevtralne osi do skrajnega vlakna

### Pravokotni prerez ($a \times b$, $b$ = višina)

$$I_x = \frac{a \cdot b^3}{12}, \quad e = \frac{b}{2}$$

$$\boxed{W_x = \frac{a \cdot b^2}{6}}$$

### Krožni prerez (premer $d$)

$$I_x = \frac{\pi d^4}{64}, \quad e = \frac{d}{2} \quad \Rightarrow \quad W_x = \frac{\pi d^3}{32}$$

## Upogibni moment $M$

Moment je odvisen od obtežbe in statičnega sistema.

| Obtežba | Sistem | $M_{max}$ |
|---------|--------|-----------|
| Enakomerna $q$ na konzoli $L$ | konzola | $M = \dfrac{q L^2}{2}$ |
| Enakomerna $q$ na razponu $L$ | prostoležeč | $M = \dfrac{q L^2}{8}$ |
| Točkovna $F$ na sredini | prostoležeč | $M = \dfrac{F L}{4}$ |
| Točkovna $F$ na koncu konzole | konzola | $M = F \cdot L$ |

## Postopek dimenzioniranja

1. **Določi $M_{max}$** — iz statičnega sistema in obtežbe
2. **Izrazi prerez parametrično** — npr. $a = 3x$, $b = 5x$
3. **Izrazi $W_x$** — za pravokotnik: $W = ab^2/6 = 3x \cdot (5x)^2 / 6 = 12{,}5x^3$
4. **Postavi pogoj** $\sigma = M / W \leq \sigma_{dop}$
5. **Izračunaj $x$** in zaokroži navzgor
6. **Kontrola** z zaokroženimi dimenzijami

## Nevtralna os in porazdelitev napetosti

```
  +----+
  |    |  ← tlak (-)
  |    |
  ======  ← nevtralna os (σ = 0)
  |    |
  |    |  ← nateg (+)
  +----+
```

- Na nevtralni osi: $\sigma = 0$
- Na skrajnih vlaknih: $\sigma = \pm M/W$ (max vrednost)
- **Uklon** ni nevarnost pri upogibu — le ko je element v tlaku/pritisku vzdolžno

## Varnostni faktor pri lesu

Za les (iglavci): $\sigma_{dop} = 1{,}0\ \text{kN/cm}^2$ (upogib), ki je višja od tlačne dopustne (~0,8 kN/cm²).

> Primerjaj: pri [[Koncept - Euler Uklon|uklonu]] je varnostni faktor ν=3 (kritična sila se deli z ν).  
> Pri upogibu varnosti ni treba posebej upoštevati — $\sigma_{dop}$ jo že vsebuje.

## Primer nalog

- [[Naloga - Mehanika - Dimenzioniranje leseni nosilec upogib]] — konzola 2m + razpon 3m, q=5kN/m, 13×22 cm

## Povezave

- [[Koncept - Vztrajnostni moment]]
- [[Koncept - Euler Uklon]]
- [[mehanika]]
- [[STATIKA]]
- [[Mehanika Hub]]
