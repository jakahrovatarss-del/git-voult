---
tags: [fizika, poglavje-11, termodinamika, toplota]
predmet: Fizika
datum: 2026-06-10
---

# Toplota in Prenos Energije

![Termogram - macka](https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Thermogram-cat-659.jpg/250px-Thermogram-cat-659.jpg)

## Namen

Toplota kot prenos energije, specifična toplota, kalorimetrija, fazni prehodi, latentna toplota, prevajanje in sevanje toplote. Poglavje 11 skripta BF UNI 2025.

## Teorija / Glavne ideje

### Notranja energija vs. Toplota

| Pojam | Definicija |
|-------|------------|
| **Notranja energija** $E_n$ | kinetična + potencialna energija molekul — **lastnost sistema** |
| **Toplota** $Q$ | oblika prenosa energije zaradi temperaturne razlike — **prenos**, ne lastnost |

> Telo toplote ne *ima* — jo *odda* ali *prejme*. Temperatura je lastnost.

---

### Specifična toplota

$$\boxed{c = \frac{Q}{m\Delta T}} \quad \Rightarrow \quad Q = mc\Delta T \tag{11.1}$$

Enota: $\text{J/(kg·K)}$

| Snov | $c$ [J/(kg·K)] |
|------|----------------|
| Voda | 4200 |
| Led | 2100 |
| Beton/kamen | ~880 |
| Baker | 385 |
| Železo | 450 |

---

### Kalorimetrija

V izoliranem sistemu: vsota izmenjanih toplote = 0

$$\boxed{Q_1 + Q_2 = 0} \quad \Rightarrow \quad |Q_1| = |Q_2| \tag{11.2–3}$$

Prejeto toploto štejemo **pozitivno**, oddano **negativno**.

**Uporaba:** Iz ravnovesne temperature izmerimo neznano specifično toploto snovi.

---

### Fazni prehod — latentna toplota

Pri faznem prehodu se temperatura **ne spreminja**, kljub izmenjavi toplote.

$$\boxed{Q = \pm mq} \tag{11.4}$$

| Prehod | Konstanta | Vrednost za vodo |
|--------|-----------|-----------------|
| Taljenje (trdno → tekoče) | $q_t$ (specifična talilna toplota) | 333 kJ/kg |
| Izhlapevanje (tekoče → plin) | $q_i$ (specifična izparilna toplota) | 2260 kJ/kg |

**Diagram ogrevanja ledu od −40°C do pare:**
1. Led se segreva ($c_L = 2{,}1\ \text{kJ/kgK}$) → do 0°C
2. Taljenje pri 0°C (ravna črta) → $q_t = 333\ \text{kJ/kg}$
3. Voda se segreva ($c_V = 4{,}2\ \text{kJ/kgK}$) → do 100°C
4. Izhlapevanje pri 100°C (ravna črta) → $q_i = 2260\ \text{kJ/kg}$
5. Para se segreva

---

### Prevajanje toplote (kondukcija)

$$\boxed{P = -\frac{\lambda A \Delta T}{l}} \tag{11.4}$$

| Simbol | Pomen | Enota |
|--------|-------|-------|
| $P$ | toplotna moč | W |
| $\lambda$ | toplotna prevodnost | W/(m·K) |
| $A$ | površina stene | m² |
| $l$ | debelina stene | m |
| $\Delta T$ | temperaturna razlika | K |

**Toplotni upor:** $R = \frac{l}{\lambda A}$ — analogija z Ohmovim zakonom ($P = -\frac{\Delta T}{R}$)

Zaporedne stene: $R = R_1 + R_2$  
Vzporedne stene: $\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}$

Izolatorji: $\lambda < 1\ \text{W/(m·K)}$ (stiropor: 0,04). Kovine: $\lambda \gg 1$ (baker: 400).

---

### Sevanje (Stefan-Boltzmannov zakon)

$$\boxed{P = e\sigma A T^4} \tag{11.8}$$

**Neto oddana moč** (upošteva okolico pri temperaturi $T_0$):

$$P = e\sigma A(T^4 - T_0^4) \tag{11.9}$$

| Simbol | Pomen | Vrednost |
|--------|-------|---------|
| $\sigma$ | Stefan-Boltzmannova konstanta | $5{,}67 \times 10^{-8}\ \text{W/m}^2\text{K}^4$ |
| $e$ | emisivnost | $0 < e \leq 1$ |
| $T$ | absolutna temperatura | K |

Popolnoma črno telo: $e = 1$.

## Primeri / Naloge

**Kalorimetrija:** Železo ($m = 0{,}5\ \text{kg}$, $T_1 = 200°C$, $c = 450\ \text{J/kgK}$) potopimo v vodo ($m = 1\ \text{kg}$, $T_2 = 20°C$, $c = 4200\ \text{J/kgK}$). Ravnovesna temperatura?

$$Q_{\text{Fe}} + Q_{\text{H}_2\text{O}} = 0$$
$$0{,}5 \times 450 \times (T - 200) + 1 \times 4200 \times (T - 20) = 0$$
$$225T - 45000 + 4200T - 84000 = 0$$
$$4425T = 129000 \implies T \approx 29{,}2°C$$

## Flashcards

- **Q:** Enačba za specifično toploto?  
  **A:** $Q = mc\Delta T$, kjer $c$ v J/(kg·K).

- **Q:** Kaj je latentna toplota?  
  **A:** $Q = \pm mq$ — toplota faznega prehoda pri konstantni temperaturi.

- **Q:** Kateri mehanizmi prenašajo toploto?  
  **A:** Kondukcija (prevajanje), konvekcija (gibanje snovi), sevanje.

- **Q:** Stefan-Boltzmannov zakon?  
  **A:** $P = e\sigma A T^4$, $\sigma = 5{,}67 \times 10^{-8}\ \text{W/m}^2\text{K}^4$.

- **Q:** Izparilna toplota vode?  
  **A:** $q_i = 2260\ \text{kJ/kg}$ — ~7x večja od talilne toplote.

- **Q:** Razlika med toploto in notranjo energijo?  
  **A:** Toplota = prenos energije med sistemi. Notranja energija = lastnost sistema (kinetična + potencialna energija molekul).

## Povezave

- [[Specifična Toplota]] — razširjena nota o kalorimetriji (Q = mcΔT)
- [[Solarni Koncentrator]] — aplikacija prenosa toplote (konveksija, sevanje)
- [[Concept Crafted - DIY Solarni Koncentrator]] — praktičen primer (924W, beton)
- [[Fizika Hub]] — hub predmeta
- [[Mehanika Hub]] — nadrejena fizika nota
