---
tags: [fizika, poglavje-4, dinamika, Newton]
predmet: Fizika
datum: 2026-06-10
---

# Zakoni Gibanja (Newton)

![Isaac Newton](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/GodfreyKneller-IsaacNewton-1689.jpg/250px-GodfreyKneller-IsaacNewton-1689.jpg)

## Namen

Razlaga **zakaj** se telesa gibljejo — Newtonovi zakoni, gravitacija, sila prožnosti (Hooke), sila trenja, sile na klancu. Dinamika = sile → gibanje.

## Teorija / Glavne ideje

### Sila

Sila $\vec{F}$ opisuje vpliv enega telesa na drugo. Enota: $\text{N} = \text{kg} \cdot \text{m/s}^2$.

**4 osnovne sile v naravi:** močna jedrska, elektromagnetna, šibka jedrska, gravitacijska.

---

### 1. Newtonov zakon — zakon vztrajnosti

Telo miruje ali se giblje premo enakomerno, ko je **vsota sil enaka nič**:

$$\boxed{\sum_{i=1}^{N} \vec{F}_i = 0 \iff \vec{v} = \text{konst.}} \tag{4.1}$$

---

### 2. Newtonov zakon — osnovna enačba gibanja

$$\boxed{\sum \vec{F} = m\vec{a}} \tag{4.2}$$

Pospešek je sorazmeren z rezultanto sil, obratno sorazmeren z maso.

---

### 3. Newtonov zakon — akcija in reakcija

$$\boxed{\vec{F}_{12} = -\vec{F}_{21}} \tag{4.3}$$

Sile vedno nastopajo v parih — enako veliki, nasprotno usmerjeni.

---

### Gravitacijski zakon

$$\boxed{F_g = G\frac{m_1 m_2}{r^2}} \tag{4.4}$$

| Simbol | Pomen | Vrednost/Enota |
|--------|-------|----------------|
| $G$ | gravitacijska konstanta | $6{,}674 \times 10^{-11}\ \text{N m}^2/\text{kg}^2$ |
| $r$ | razdalja med telesoma | m |

**Teža telesa** blizu Zemljine površine:
$$F_g = mg, \quad g_0 = G\frac{m_Z}{R_Z^2} = 9{,}81\ \text{m/s}^2 \tag{4.5}$$

Na višini $h$ nad površino:
$$g(r) = g_0 \left(1 + \frac{h}{R_Z}\right)^{-2} \tag{4.7}$$

---

### Hookov zakon (sila prožnosti)

$$\boxed{F = k\Delta x} \tag{4.6}$$

$k$ = koeficient vzmeti (N/m), $\Delta x$ = raztezek/skrček.

---

### Sila trenja

| Tip | Enačba | Pogoj |
|-----|--------|-------|
| Statično trenje | $F_s \leq \mu_s F_n$ | telo miruje |
| Kinetično trenje | $F_t = \mu_t F_n$ | telo drsi |

> V splošnem $\mu_t < \mu_s$ — lažje je ohranjati gibanje kot ga začeti.

Smer sile trenja je vedno **nasprotna smeri gibanja**.

---

### Sile na klancu (kot $\varphi$)

Razstavimo težo na dve komponenti:
- $F_d = F_g \sin\varphi$ — vzdolž klanca (dinamična)
- $F_s = F_g \cos\varphi$ — pravokotno na klanec (statična)

**Pospešek pri drsenju navzdol:**

$$\boxed{a_x = g(\sin\varphi - \mu_t \cos\varphi)} \tag{4.17}$$

**Pospešek pri gibanju navzgor** (pojemek):

$$a_{x,\text{gor}} = -g(\sin\varphi + \mu_t \cos\varphi) \tag{4.18}$$

## Primeri / Naloge

**Klanec:** Telo mase 5 kg drsi po klancu pod kotom 30°. $\mu_t = 0{,}2$. Kolikšen je pospešek?

$$a = g(\sin 30° - 0{,}2 \cdot \cos 30°) = 9{,}81(0{,}5 - 0{,}2 \times 0{,}866) = 9{,}81 \times 0{,}327 \approx 3{,}2\ \text{m/s}^2$$

## Flashcards

- **Q:** Zapiši 2. Newtonov zakon.  
  **A:** $\sum \vec{F} = m\vec{a}$

- **Q:** Kaj pravi 3. Newtonov zakon?  
  **A:** $\vec{F}_{12} = -\vec{F}_{21}$ — akcija = reakcija, nasprotne smeri.

- **Q:** Razlika med statičnim in kinetičnim trenjem?  
  **A:** $F_s \leq \mu_s F_n$ (telo miruje), $F_t = \mu_t F_n$ (telo drsi). Vedno $\mu_t < \mu_s$.

- **Q:** Kako izračunamo težo telesa blizu Zemlje?  
  **A:** $F_g = mg$, kjer $g = 9{,}81\ \text{m/s}^2$.

- **Q:** Komponenti teže na klancu pod kotom $\varphi$?  
  **A:** Vzdolž: $F_g \sin\varphi$. Pravokotno: $F_g \cos\varphi$.

- **Q:** Hookov zakon?  
  **A:** $F = k\Delta x$ — sila prožnosti sorazmerna raztezku.

## Povezave

- [[Mehanika Hub]] — nadrejena nota (kinematika, dinamika, statika)
- [[Fizika Hub]] — hub predmeta
- [[Koncept - Premo Gibanje]] — predhodno poglavje (kinematika)
- [[STATIKA]] — statika teles (ravnovesje)
- [[ravnovesje delca]] — aplikacija 1. Newtonovega zakona
- [[SpaceX]] — aplikacija 3. Newtonovega zakona (reaktivni pogon)
