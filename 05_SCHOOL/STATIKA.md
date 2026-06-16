---
tags: [mehanika, statika, ravnotežje, FBD, reakcije, redukcija-sil, koncept]
predmet: Mehanika
datum: 2026-06-16
---

# Statika — Osnove

Statika je veja mehanike ki obravnava telesa v **mirovanju** ali gibanju s konstantno hitrostjo. Rezultanta vseh sil je vedno enaka 0.

## Temeljni pojmi (SL ↔ EN)

| Slovensko | English | Opomba |
|-----------|---------|--------|
| Togo telo | Rigid body | dimenzije upoštevamo, brez deformacij |
| Masna točka | Particle | dimenzije zanemarimo, sile se sekajo v točki |
| Diagram prostega telesa | Free-Body Diagram (FBD) | osnova vsake rešitve |
| Ravnotežne enačbe | Equations of equilibrium | ΣF=0, ΣM=0 |
| Redukcija sil | Force system resultants | zamenjaj sistem z rezultanto + momentom |
| Rezultanta | Resultant force R = ΣF | — |
| Dvojica sil | Couple moment | čisto vrtenje brez translacije |
| Reakcije podpor | Support reactions | nadomestijo podporo na FBD |

**Hibbeler reference:** Ch. 3 (Particle equilibrium) · Ch. 4 (Force resultants) · Ch. 5 (Rigid body equilibrium)

---

## Ravnotežne enačbe

### Masna točka (2D)
$$\sum F_x = 0 \qquad \sum F_y = 0$$

### Togo telo (2D) — 3 enačbe
$$\sum F_x = 0 \qquad \sum F_y = 0 \qquad \sum M_O = 0$$

> **Pravilo:** Vzemi moment okrog točke z največ neznankami → te se izničijo.

### Togo telo (3D) — 6 enačb
$$\sum F_{x,y,z} = 0 \qquad \sum M_{x,y,z} = 0$$

---

## Podpore in reakcije

| Podpora | Slovensko | Reakcije | Neznanke |
|---------|-----------|----------|----------|
| Pin / Zglob | Nepomični členek (tečaj) | $R_x$, $R_y$ | 2 |
| Roller / Valj | Pomični členek | $R_y$ (⊥ površini) | 1 |
| Fixed / Vpetje | Togo vpetje | $R_x$, $R_y$, $M_A$ | 3 |
| Free end | Prosti konec | — | 0 |
| Internal hinge | Notranji členek (Gerber) | doda pogoj $M=0$ | −1 |

**Statična določenost:** Σ reakcij = 3 za ravninski problem.

---

## Redukcija sistema sil

Sistem sil zamenjamo z ekvivalentnim v točki O:
$$\vec{R} = \sum \vec{F} \qquad \vec{M}_O = \sum (\vec{r} \times \vec{F}) + \sum \vec{M}$$

Tipična naloga: "Reduciraj sistem v točko O" → izračunaj R in M_O.

---

## Postopek reševanja — togo telo

```
1. Nariši FBD — odstrani podpore, nadomesti z reakcijami
2. Razstavi silo pod kotom: Fx = F·cosα, Fy = F·sinα
3. ΣMₐ = 0 → By (A se izniči)
4. ΣFy = 0 → Ay
5. Kontrola: ΣMB = 0 mora dati 0
```

---

## Ravnovesje delca — primer

Za obroček z dvema vrvema pod kotom:
$$T_{AC}\cos\alpha - T_{BC}\cos\beta = 0$$
$$T_{AC}\sin\alpha + T_{BC}\sin\beta - W = 0$$

→ [[ravnovesje delca]]

---

## Newtonovi zakoni

1. $\sum \vec{F} = 0 \iff \vec{v} = \text{konst.}$ (vztrajnost)
2. $\sum \vec{F} = m\vec{a}$ (osnovna enačba gibanja)
3. $\vec{F}_{12} = -\vec{F}_{21}$ (akcija = reakcija)

---

## Povezave

- [[ravnovesje delca]]
- [[Mehanika Hub]]
- [[Koncept - NTM Diagrami]]
- [[05_SCHOOL/School Hub]]
