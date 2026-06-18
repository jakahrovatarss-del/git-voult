---
tags: [mehanika, dinamika, vztrajnostni-moment, steiner, navor, rotacija]
predmet: Mehanika
datum: 2026-06-18
vir: "Profesor — 2. letnik, les"
status: rešeno
---

# Naloga — Dinamika mešala (Steiner + navor)

## Namen

Izračunaj vztrajnostni moment jeklene mešalne glave in potreben navor za pospeševanje iz mirovanja na $2800\ \text{obr/min}$ v 3 sekundah.

---

## Dano

![[dinamika_mesalo_steiner.svg|697]]

| Oznaka | Vrednost |
|--------|---------|
| Gostota jekla $\rho$ | $8\ \text{kg/dm}^3$ |
| Dolžina rezila $L$ | 120 mm |
| Širina rezila $w$ | 80 mm |
| Debelina rezila $t$ | 10 mm |
| Premer gredi $d$ | 20 mm → polmer $r = 10\ \text{mm}$ |
| Višina gredi $H$ | 200 mm *(zanemarimo)* |
| Hitrost $n$ | 2800 obr/min |
| Čas pospeševanja $\Delta t$ | 3 s |

**Iskano:** Vztrajnostni moment $I_z$ in potreben navor $M_z$.

---

## KORAK 1 — Masa rezila

$$V_R = L \cdot w \cdot t = 1{,}2 \cdot 0{,}8 \cdot 0{,}1 = 0{,}096\ \text{dm}^3$$

$$\boxed{m_R = \rho \cdot V_R = 8 \cdot 0{,}096 = 0{,}768\ \text{kg}}$$

---

## KORAK 2 — Lastni vztrajnostni moment rezila ($I_{z,lastni}$)

Rezilo je **pravokotna plošča** — vrtimo ga okoli osi, ki leži v ravnini plošče vzporedno s kratico $w$:

$$\boxed{I_{z,lastni} = \frac{m_R}{12}(L^2 + w^2) = \frac{0{,}768}{12}(0{,}12^2 + 0{,}08^2) = 0{,}001331\ \text{kg·m}^2}$$

---

## KORAK 3 — Steinerjev stavek

Rezilo se ne vrti okoli svojega težišča, temveč **okoli osi gredi** — odmaknjeno za:

$$e = r + \frac{L}{2} = 10\ \text{mm} + 60\ \text{mm} = 70\ \text{mm} = 0{,}07\ \text{m}$$

$$I_{Steiner} = m_R \cdot e^2 = 0{,}768 \cdot 0{,}07^2 = 0{,}003763\ \text{kg·m}^2$$

$$I_{rezilo} = I_{z,lastni} + I_{Steiner} = 0{,}001331 + 0{,}003763 = \boxed{0{,}005094\ \text{kg·m}^2}$$

> 💡 **Steinerjev stavek:** $I_{Steiner} = m \cdot e^2$ — odmik od osi bistveno poveča vztrajnost (faktor $e^2$). Tukaj Steiner prispeva **73 %** skupnega momenta!

---

## KORAK 4 — Skupni vztrajnostni moment mešala

Dve rezili, gred zanemarimo ($r \approx 0$, $I_{gred} \approx 0$):

$$\boxed{I_{tot} = 2 \cdot I_{rezilo} = 2 \cdot 0{,}005094 = 0{,}01019\ \text{kg·m}^2}$$

---

## KORAK 5 — Dinamika: kotna hitrost in pospešek

$$\omega = \frac{2\pi \cdot n}{60} = \frac{2\pi \cdot 2800}{60} \approx 293{,}2\ \text{rad/s}$$

$$\alpha = \frac{\Delta\omega}{\Delta t} = \frac{293{,}2}{3} \approx 97{,}7\ \text{rad/s}^2$$

---

## KORAK 6 — Potreben navor (Newton II za rotacijo)

$$\sum M_z = I_z \cdot \alpha$$

$$\boxed{M_z = I_{tot} \cdot \alpha = 0{,}01019 \cdot 97{,}7 \approx 0{,}995\ \text{Nm}}$$

---

## Povzetek in pasti

| Korak | Formula | Vrednost |
|-------|---------|---------|
| Masa rezila | $m = \rho V$ | 0,768 kg |
| Lastni $I$ (plošča) | $m(L^2+w^2)/12$ | 0,001331 kg·m² |
| Odmik težišča | $e = r + L/2$ | 0,07 m |
| Steiner | $m \cdot e^2$ | 0,003763 kg·m² |
| $I$ enega rezila | $I_{lastni} + I_{St}$ | 0,005094 kg·m² |
| $I_{tot}$ (2 rezili) | $2 \cdot I_{rezilo}$ | 0,01019 kg·m² |
| $\omega$ | $2\pi n / 60$ | 293,2 rad/s |
| $\alpha$ | $\Delta\omega / \Delta t$ | 97,7 rad/s² |
| **$M_z$** | $I \cdot \alpha$ | **0,995 Nm** |

**Pogoste napake:**
- ⚠️ Enote: masa v **kg** (ne kN!), razdalje v **m** (ne mm!) pri $I$
- ⚠️ $e$ = razdalja od **osi vrtenja** do **težišča** dela — ne do roba!
- ⚠️ $I_{plošča} = m(L^2+w^2)/12$ samo ko os ⊥ plošči in gre skozi težišče
- ⚠️ Ta $M_z$ je **minimalni navor** — ne upošteva upora tekočine!

---

## Flashcards

Q: Zakaj je Steinerjev dodatek tako velik (73 % $I$)?
A: Ker narašča s $e^2$ — majhen odmik e pomeni velik prispevek. Tukaj e=7cm je velik glede na dimenzije.

Q: Katera formula za $I$ velja za pravokotno ploščo pri vrtenju pravokotno nanjo?
A: $I = m(a^2+b^2)/12$ (osi vzdolž stranic skozi težišče).

Q: Enačba Newton II za rotacijo?
A: $\sum M_z = I_z \cdot \alpha$, kjer je $\alpha = \Delta\omega/\Delta t$.

Q: Kaj pomeni, da je ta $M_z$ minimalen?
A: Premaguje samo vztrajnost jekla (pospeševanje mase). V realnosti dodaš še upor tekočine.

---

## Povezave

- [[Blok 7 - Dinamika Nihanje]] — Newton II za rotacijo
- [[Koncept - Vztrajnostni moment]] — Steinerjev stavek, prerezi
- [[Cheat Sheet - Mehanika FORMULE]] — Blok 7, momenti inercije
- [[Naloga - Mehanika - NTM Lomljeni okvir NotrSile N1]] — sestrska naloga (NTM)
