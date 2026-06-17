---
tags: [mehanika, vir, kanal, statics, strength-of-materials, dynamics, drawings]
predmet: Mehanika
datum: 2026-06-17
vir: "The Efficient Engineer — YouTube kanal"
url: "https://youtube.com/theefficientengineer"
spletna-stran: "https://efficientengineer.com"
---

# Vir — The Efficient Engineer (YouTube kanal)

> Kanal za strojne in gradbene inženirje. Misija: poenostaviti inženirske koncepte, en video naenkrat.  
> Zelo relevanten za **mehaniko, statiko, trdnost materialov in tehnično risanje**.

---

## Pokrita področja

| Področje | Slovensko | Relevantnost za mehaniko |
|----------|-----------|--------------------------|
| **Statics** | Statika | ⭐⭐⭐ Neposredno |
| **Strength of Materials** | Trdnost materialov | ⭐⭐⭐ Neposredno |
| **Dynamics** | Dinamika | ⭐⭐⭐ Neposredno |
| **Mechanical Design & Drafting** | Tehnično risanje | ⭐⭐⭐ Neposredno |
| **Material Properties** | Lastnosti materialov | ⭐⭐ Delno |
| **Materials Science** | Veda o materialih | ⭐ Splošno |
| **Fluid Mechanics** | Mehanika tekočin | ⭐ Ločen predmet |
| **Heat Transfer** | Prenos toplote | ⭐ Ločen predmet |

---

## Statika — ključne teme s kanala

### Strižna sila in moment (Shear Force & Bending Moment Diagrams)
Diagrami, ki prikazujejo porazdelitev strižnih sil in upogibnih momentov vzdolž nosilca.

**Algoritem:**
```
1. Izračunaj podporne reakcije (ΣF=0, ΣM=0)
2. Nariši diagram strižnih sil V(x)
3. Nariši diagram upogibnih momentov M(x)
4. M_max je tam, kjer V = 0 (ničla)
```
→ [[Koncept - Upogib]] | [[Koncept - NTM Diagrami]]

### Paličja (Trusses)
Konstrukcije (mostovi, strehe) iz palic, ki prenašajo samo tlačne ali natezne osne sile.

**Metode:**
- **Metoda vozlišč** (Method of Joints) — analiziraj vsako vozlišče posebej
- **Metoda presekov** (Method of Sections) — prereži paličje za neznane sile

**Pogoji:**
- Paličje je statično določeno: $m = 2j - 3$ (m = palic, j = vozlišč)
- Vsako vozlišče: $\sum F_x = 0$, $\sum F_y = 0$

### Mehanski prenos sile (Mechanical Advantage)
Ojačanje vhodne sile z vzvodom ali škripci:

$$MA = \frac{F_{out}}{F_{in}} = \frac{d_{in}}{d_{out}}$$

Primeri: vzvod, škripec, vijak, zobnik

### Površinski vztrajnostni moment (Area Moment of Inertia)
Opisuje, kako je material prereza porazdeljen glede na upogibno os.

| Prerez | Formula | |
|--------|---------|--|
| Pravokotnik (osa x) | $I_x = \frac{bh^3}{12}$ | b = širina, h = višina |
| Krog (osa x) | $I_x = \frac{\pi d^4}{64}$ | d = premer |
| Splošno (Steiner) | $I = I_0 + A \cdot e^2$ | e = razdalja od OS do težišča |

→ [[Koncept - Vztrajnostni moment]]

---

## Trdnost materialov — ključne teme

### Napetost in deformacija
$$\sigma = \frac{F}{A} \qquad \varepsilon = \frac{\Delta L}{L_0} \qquad E = \frac{\sigma}{\varepsilon} \quad \text{(Youngov modul)}$$

### Strižna napetost
$$\tau = \frac{V \cdot S}{I \cdot b}$$

### Upogib
$$\sigma = \frac{M \cdot e}{I} \qquad \text{max pri } e = e_{max}$$

→ [[Koncept - Upogib]]

### Uklon (Euler)
$$F_{kr} = \frac{\pi^2 E I}{l_u^2} \qquad l_u = \beta \cdot L$$

→ [[Koncept - Euler Uklon]]

---

## Dinamika — ključne teme

| Tema | Ključna enačba |
|------|----------------|
| Kinetika delca | $\sum F = ma$ |
| Delo in energija | $W = \Delta KE = \frac{1}{2}mv_2^2 - \frac{1}{2}mv_1^2$ |
| Impulz in gibalna količina | $\sum F \cdot \Delta t = m(v_2 - v_1)$ |
| Rotacijska dinamika | $\sum M = I\alpha$ |
| Harmonično nihanje | $\omega_n = \sqrt{k/m}$ |

---

## Tehnično risanje — ključne teme

→ [[Vir - Tehnično Risanje in GDT]]

---

## Koristni resursi s spletne strani

- **Quizzi:** https://efficientengineer.com/practice/
- **Summary Sheets (PDF):** https://efficientengineer.com/summary/
- **Statics:** https://efficientengineer.com/statics/
- **Strength of Materials:** https://efficientengineer.com/strength-of-materials/
- **Dynamics:** https://efficientengineer.com/dynamics/

> 💡 Summary Sheets so odlični za hiter pregled pred izpitom!

---

## Priporočen vrstni red gledanja (za mehaniko)

1. Statics — Shear Force and Bending Moment Diagrams
2. Statics — Trusses
3. Strength of Materials — Stress and Strain
4. Strength of Materials — Bending Stress
5. Mechanical Design — Understanding Engineering Drawings ← **že pogledano**
6. Dynamics — Introduction

---

## Povezave

- [[Mehanika Hub]]
- [[STATIKA]]
- [[Koncept - Upogib]]
- [[Koncept - Euler Uklon]]
- [[Koncept - Vztrajnostni moment]]
- [[Vir - Tehnično Risanje in GDT]]
- [[05_SCHOOL/School Hub]]
