---
tags: [mehanika, vztrajnostni-moment, prerez, steiner, koncept]
predmet: Mehanika
datum: 2026-06-09
---

# Koncept: Vztrajnostni moment (I)

## Namen

Vztrajnostni moment prereza meri **odpornost telesa proti upogibanju in uklonu**. Večji I → bolj toga konstrukcija → večja kritična sila. Je geometrijska lastnost prereza — ne materiala.

## Fizikalni pomen

$$I = \int y^2 \, dA$$

Vsak delček površine $dA$ prispeva $y^2 \cdot dA$ — torej **oddaljenost od osi je kvadratna**. Material daleč od osi nosi veliko več kot material blizu osi. Zato so I-profili tako učinkoviti.

## Enačbe za najpogostejše prereze

![[vztrajnostni_moment_prerezi.svg]]

| Prerez | $I_z$ (ok. hor. osi) | $I_y$ (ok. vert. osi) | $A$ |
|--------|----------------------|-----------------------|-----|
| Pravokotnik $b \times h$ | $\dfrac{b \cdot h^3}{12}$ | $\dfrac{h \cdot b^3}{12}$ | $b \cdot h$ |
| Kvadrat $a \times a$ | $\dfrac{a^4}{12}$ | $\dfrac{a^4}{12}$ | $a^2$ |
| Krog $\varnothing d$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^4}{64}$ | $\dfrac{\pi d^2}{4}$ |
| Votel pravokotnik | $\dfrac{BH^3 - bh^3}{12}$ | $\dfrac{HB^3 - hb^3}{12}$ | $BH - bh$ |

> ⚠️ **Pazi na vrstni red b in h!**
> - $I_z = \frac{b \cdot h^3}{12}$ — **h** je dimenzija v smeri osi z (navpično)
> - $I_y = \frac{h \cdot b^3}{12}$ — **b** je dimenzija v smeri osi y (vodoravno)

## Šibka in močna os

Za pravokoten prerez $b \times h$ velja (če $b < h$):

$$I_{min} = \frac{h \cdot b^3}{12} \quad \text{(šibka os)} \qquad I_{max} = \frac{b \cdot h^3}{12} \quad \text{(močna os)}$$

Uklon vedno nastopi okoli **šibke osi** (najmanjši I → najlažja pot).

## Vztrajnostni polmer

$$i = \sqrt{\frac{I}{A}}$$

Meri, kako "daleč od osi" je porazdeljena masa prereza. Uporablja se za izračun vitkosti:

$$\lambda = \frac{l_u}{i}$$

## Steinerjeva formula (vzporedna os)

Če os ne gre skozi težišče, dodamo **Steinerjev člen**:

$$\boxed{I_{vzp} = I_T + A \cdot e^2}$$

| Simbol | Pomen |
|--------|-------|
| $I_T$ | I okoli osi skozi težišče |
| $A$ | površina prereza |
| $e$ | razdalja med osema |

**Uporaba:** sestavljeni prerezi (I-profil, T-profil, sovprežni nosilci) — vsak del posebej izračunamo in seštejemo.

## Primeri vrednosti

| Prerez | Dimenzije | $I_{min}$ |
|--------|-----------|-----------|
| Lesena deska | 2,5 × 20 cm | $h \cdot b^3/12 = 20 \cdot 2{,}5^3/12 = 26{,}04$ cm⁴ |
| Lesen steber | 12 × 12 cm | $a^4/12 = 12^4/12 = 1728$ cm⁴ |

## Povezave

- [[Koncept - Euler Uklon]]
- [[Naloga - Mehanika - Uklon lesene deske]]
- [[Naloga - Mehanika - Uklon leseni steber F_max]]
- [[mehanika]]
- [[Mehanika Hub]]
