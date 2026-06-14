---
tags: [mehanika, torzija, Bredt, škatlast-prerez, tankostenska, naloga, izpit]
predmet: Mehanika
datum: 2026-06-14
vir: Izpit iz Mehanike BTF, Lesarstvo UN, 5. 2. 2019 / 3. 9. 2025, Naloga 4
---

# Naloga: Torzija škatlastega prereza (Bredt) — Izpit Feb 2019

## Podatki

![[torzija_skatlast_prerez.svg]]

- Dolžina palice: $L = 4a = 4 \cdot 0{,}3 = 1{,}2\ \text{m}$
- Sila na koncu: $F = 10\ \text{kN}$, z ročico $a = 0{,}3\ \text{m}$ (ekscentrično)
- Škatlast prerez (pravokotna cev): $15 \times 10\ \text{cm}$, debelina sten $t = 1\ \text{cm}$

---

## Korak 1 — Torzijski moment $M_t$

### Zakaj?

Sila F deluje z ročico $a$ glede na os palice → ustvari torzijski moment.

$$M_t = F \cdot a = 10\ \text{kN} \cdot 0{,}3\ \text{m} = \boxed{3\ \text{kNm} = 3 \cdot 10^6\ \text{Nmm}}$$

> ℹ️ $M_t$ je **konstanten** vzdolž celotne dolžine palice (ni porazdeljenega torzijskega momenta).

> **glej:** [[Koncept - Torzija#Osnovna enačba torzije]]

---

## Korak 2 — Ploščina srednje linije $A_m$

### Zakaj?

Bredt-Bathoova formula zahteva ploščino, ki jo obkroži **srednja linija** stene (ne zunanja, ne notranja kontura!).

Srednja linija je $t/2 = 0{,}5\ \text{cm}$ od roba. Dimenzije srednje linije:

$$b_m = 10 - t = 10 - 1 = 9\ \text{cm}$$
$$h_m = 15 - t = 15 - 1 = 14\ \text{cm}$$

$$A_m = b_m \cdot h_m = 9 \cdot 14 = \boxed{126\ \text{cm}^2 = 12\,600\ \text{mm}^2}$$

> ⚠️ **Pogosta napaka:** Vzamejo zunanjo ploščino $10 \times 15 = 150\ \text{cm}^2$ — to je napačno! Vzeti je treba ploščino znotraj **srednje linije**.

---

## Korak 3 — Strižna napetost (Bredt)

### Zakaj?

Za zaprti tankosteni profil velja **Bredt-Bathoova formula** (ne Wt za polne prereze!):

$$\boxed{\tau = \frac{M_t}{2 \cdot A_m \cdot t}}$$

Vstavimo:

$$\tau = \frac{3 \cdot 10^6\ \text{Nmm}}{2 \cdot 12\,600\ \text{mm}^2 \cdot 10\ \text{mm}}$$

$$\tau = \frac{3\,000\,000}{252\,000} = \boxed{11{,}9\ \text{MPa}}$$

> ℹ️ Ker je $t = \text{konst.}$ po vsem obodu → $\tau = \text{konst.}$ po vsem obodu prereza.

> **glej:** [[Koncept - Torzija#Tankosteni zaprti prerezi — Bredt-Bathoova formula]]

---

## Korak 4 — Polje napetosti vzdolž palice

### Zakaj se vprašajo za "polje napetosti"?

Ker torzijska napetost ni nujno konstantna vzdolž palice — odvisno od obremenitve.

### V tej nalogi:

$$M_t(x) = F \cdot a = \text{konst.} = 3\ \text{kNm} \quad \forall x \in [0, L]$$

Ker je $M_t$ konstanten vzdolž celotne dolžine, je tudi:

$$\tau(x) = \frac{M_t}{2 A_m t} = \text{konst.} = 11{,}9\ \text{MPa} \quad \text{vzdolž palice}$$

**Polje napetosti:**
- Po **obodu prereza**: $\tau = \text{konst.}$ (ker $t = \text{konst.}$ povsod)
- Po **dolžini palice**: $\tau = \text{konst.}$ (ker $M_t = \text{konst.}$)

> 🔍 **Fizikalni pomen:** Torzijski tok $q = \tau \cdot t = M_t/(2A_m)$ je konstanten po obodu zaprtega prereza (Bredt: $q = \text{konst.}$ ne glede na t). Ko je t=konst → τ=konst.

---

## Korak 5 — Kontrola (primerjava z dopustno napetostjo)

Če je $\tau_{dop}$ podan (npr. $\tau_{dop} = 60\ \text{MPa}$):

$$\tau = 11{,}9\ \text{MPa} \leq \tau_{dop} = 60\ \text{MPa} \quad ✓$$

---

## Povzetek

| Korak | Vsebina | Rezultat |
|-------|---------|---------|
| 1 | Torzijski moment | $M_t = F \cdot a = 3\ \text{kNm}$ |
| 2 | Ploščina srednje linije | $A_m = 9 \cdot 14 = 126\ \text{cm}^2$ |
| 3 | Bredt: strižna napetost | $\tau = M_t/(2A_m t) = \boxed{11{,}9\ \text{MPa}}$ |
| 4 | Polje napetosti | $\tau = \text{konst.}$ po obodu IN vzdolž palice |

---

## Razlika: Bredt vs. klasična torzija

| | Polni krog | Škatlast (Bredt) |
|--|------------|------------------|
| Formula | $\tau = M_t/W_t$, $W_t = \pi d^3/16$ | $\tau = M_t/(2A_m t)$ |
| Porazdelitev τ | Linearno od 0 do max | Konstantno po obodu |
| Velja za | Polne prereze | Zaprte tankostene prereze |

---

## Povezave

- [[Koncept - Torzija]]
- [[Naloga - Mehanika - Izpit Feb2019 - Tresca Von Mises]]
- [[Koncept - Napetostno stanje]]
- [[Mehanika Hub]]
- [[Izpit - Mehanika - Celoletni 2026]]
