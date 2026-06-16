---
tags: [mehanika, dinamika, nihanje, Newton, inercija, blok]
predmet: Mehanika
datum: 2026-06-16
---

# Blok 7 — Dinamika in Nihanje

## VSE ENAČBE

```
NEWTON II (translacija):
  ΣF = m·a   [kN = kg·m/s² → m v tonah ali kg!]

NEWTON II (rotacija — okrog fiksne osi):
  ΣM_O = I_O · α
  I_O = m·r²  (za točkasto maso)
  I_O = I_T + m·d²  (Steiner za togo telo)

MOMENTI INERCIJE TOGIH TES:
  Homogen palica (okrog konca):    I = mL²/3
  Homogen palica (okrog sredine):  I = mL²/12
  Disk/valj (okrog osi):           I = mR²/2
  Sfera:                           I = 2mR²/5

PROSTO NIHANJE:
  m·ẍ + k·x = 0
  ω₀ = √(k/m)    [rad/s]
  f₀ = ω₀/(2π)   [Hz]
  T₀ = 2π/ω₀     [s]

NIHANJE POD DUŠENJEM:
  m·ẍ + c·ẋ + k·x = 0
  ξ  = c/(2√(km))   dušilno razmerje
  ωd = ω₀·√(1-ξ²)

RESONANCA: Fmax ko ω_vzb ≈ ω₀

NIHALO (matematično):
  ω₀ = √(g/L)

KINETIČNA ENERGIJA:
  Ek = ½·m·v² + ½·I·ω²

POTENCIALNA ENERGIJA:
  Ep = m·g·h   (gravitacijska)
  Ep = ½·k·x²  (vzmetna)

ENERGIJSKA METODA (nihanje):
  Emax = const → Ek,max = Ep,max
  ½·m·v²max = ½·k·x²max → ω₀ = √(k/m)
```

---

## Kako prepoznamo nalogo tega bloka

**Ključne besede v besedilu:**
- "dinamika", "nihanje", "frekvenca"
- "gibalna enačba", "diferencialna enačba gibanja"
- "lastna frekvenca", "resonanca"
- "masa in vzmet", "ω₀"
- "d'Alembert", "D'Alembert"
- Podano: masa $m$, togost $k$, začetni pogoji

**Kaj je podano:**
- Masa $m$ [kg ali t]
- Togost vzmeti $k$ [N/m ali kN/cm]
- Morda dušenje $c$ [Ns/m]
- Sila vzbujevanja $F(t) = F_0 \sin(\omega t)$

**Kaj se sprašuje:**
- Lastna frekvenca $\omega_0$, $f_0$, $T_0$
- Amplituda nihanja
- Ali je resonanca možna
- Gibalna enačba $m\ddot{x} + k x = F(t)$

---

## Kako začeti reševati

**Nihanje mase na vzmeti:**

**Korak 1:** Nariši FBD (free body diagram) mase v splošnem položaju $x$

**Korak 2:** Zapiši Newton II:
$$m\ddot{x} + kx = 0 \quad \text{(prosto)} \quad \text{ali} \quad = F(t) \quad \text{(prisilno)}$$

**Korak 3:** Odčitaj $\omega_0$:
$$\omega_0 = \sqrt{\frac{k}{m}}$$

**Korak 4:** Izračunaj $f_0$, $T_0$:
$$f_0 = \frac{\omega_0}{2\pi}, \quad T_0 = \frac{1}{f_0} = \frac{2\pi}{\omega_0}$$

---

**Rotacijska dinamika:**

**Korak 1:** Določi os vrtenja

**Korak 2:** Izračunaj $I_O$ (s Steinerjem, če ni v težišču):
$$I_O = I_T + m \cdot d^2$$

**Korak 3:** Zapiši Newton II za rotacijo:
$$\sum M_O = I_O \cdot \alpha$$

---

**Energijska metoda (za nihanje):**

Kadar je sila konservativna, enačba gibanja iz $E = const$:
$$\frac{d}{dt}(E_k + E_p) = 0$$

---

## Prepoznavanje razlik med podtipi nalog

| Tip | Kako prepoznaš | Metoda |
|-----|----------------|--------|
| Prosto nihanje | Masa + vzmet, brez sile | $\omega_0 = \sqrt{k/m}$ |
| Prisilno nihanje | Zunanji $F(t)$ | Partikularna rešitev + homogena |
| Nihanje z dušenjem | Dano $c$ ali dušilno razmerje | $\xi$, $\omega_d = \omega_0\sqrt{1-\xi^2}$ |
| Togo telo, rotacija | Dano togo telo (palica, disk) | $I \cdot \alpha = \sum M$ |
| Rotacijsko nihanje | Togo telo + vzmet/gravitacija | Energija ali Newton |
| Resonanca | Vprašanje o max amplitudi | $\omega_{vzb} = \omega_0$ |

---

## Kombinacije z drugimi bloki

### Blok 7 + 6 (Dinamika + Kinematika)
Najosnovnejša kombinacija — kinematika da $a$, dinamika ga poveže s silo.
1. Iz kinematike: $\alpha$, $a$ (Blok 6)
2. Newton II: $F = ma$, $M = I\alpha$

### Blok 7 + 0 (D'Alembert + Statika)
D'Alembertov princip: dodaj inercijsko silo $-ma$ in problem reši statično.
$$\sum F + (-m\vec{a}) = 0 \quad \Rightarrow \quad \text{statični problem!}$$

### Blok 7 + 5 (Torzijsko nihanje)
Gredi z diskom — torzijsko nihanje:
$$I\ddot{\phi} + k_t\phi = 0, \quad \omega_0 = \sqrt{k_t/I}$$

---

## Momenti inercije — Tabela

| Telo | Os | $I$ |
|------|----|-----|
| Palica dolžine $L$ | Skozi konec, ⊥ | $\frac{mL^2}{3}$ |
| Palica dolžine $L$ | Skozi sredino, ⊥ | $\frac{mL^2}{12}$ |
| Disk/valj, polmer $R$ | Os vrtenja | $\frac{mR^2}{2}$ |
| Obroč, polmer $R$ | Os vrtenja | $mR^2$ |
| Sfera, polmer $R$ | Diameter | $\frac{2mR^2}{5}$ |
| Pravokotna plošča $a \times b$ | Skozi težišče, || z $a$ | $\frac{mb^2}{12}$ |

---

## Pogosta napaka

- Enote mase: masa v **kg** (ne kN!) → $F = ma$ → $[kN] = [t \cdot m/s^2]$
- Moment inercije ni skalaren pri 3D — Steiner obvezno!
- Resonanca: amplituda → ∞ samo pri nedušenem sistemu
- $\omega_0$ je kotna frekvenca [rad/s], $f_0$ je frekvenca [Hz], $T_0$ je perioda [s]

---

## Povezave

- [[Blok 6 - Kinematika]] ← predhodni korak (hitrosti, pospešek)
- [[Blok 0 - Statika]] ← D'Alembert (statični pristop)
- [[Blok 5 - Torzija]] ← torzijsko nihanje
- [[Izpit - Mehanika - Celoletni 2026]]
- [[Mehanika Hub]]
