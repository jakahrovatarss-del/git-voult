# Domača naloga 1 — Notranje sile in navori v rezkalnem orodju

## Podatki

| Veličina | Vrednost |
|----------|----------|
| Dolžina stebla konzole | $L = 34{,}75\ \text{mm}$ |
| Polmer orodja | $r = 17{,}5\ \text{mm}$ |
| Aksialna sila | $F_a = -35{,}5\ \text{N}$ |
| Radialna sila | $F_r = 37{,}25\ \text{N}$ |
| Obodna (rezalna) sila | $F_c = 113\ \text{N}$ |

---

## 1. Koordinatni sistem

```
         y (radialno ↑)
         |
         |
A ———————● s=0          ● s=L  ←  sile Fa, Fr, Fc
 (vpetje)|______________|___→ x (vzdolž osi, s ∈ [0, L])
                              z (obodno, iz ravnine)
```

- **x-os** (= $s$): vzdolž osi stebla, od vpetja ($s=0$) do prostega konca ($s=L$)
- **y-os**: radialna smer ($F_r$ deluje v smeri $+y$)
- **z-os**: obodna smer ($F_c$ deluje v smeri $+z$)

Sile $F_a$, $F_r$, $F_c$ delujejo na prostem koncu, na polmeru $r$ od osi.

---

## 2. Redukcija obremenitve v os stebla

Obremenitev prenesemo v težišče prostega konca ($s = L$):

**Sile** (nespremenljene):
$$F_a = -35{,}5\ \text{N}, \quad F_r = 37{,}25\ \text{N}, \quad F_c = 113\ \text{N}$$

**Dodatni momenti** (nastanejo pri prenosu iz polmera $r$ na os):

Obodna sila $F_c$ povzroči torzijo:
$$M_t^{(0)} = F_c \cdot r = 113 \times 17{,}5 = 1977{,}5\ \text{N·mm}$$

Radialna sila $F_r$ povzroči dodaten upogibni moment v ravnini $x$-$z$:
$$M_{add} = F_r \cdot r = 37{,}25 \times 17{,}5 = 651{,}875\ \text{N·mm}$$

---

## 3. Metoda preseka

Presek na koordinati $s$ ($0 \le s \le L$). Obravnavamo **desni del** (od preseka do prostega konca).

### Ravnovesje sil

$$\sum F_x = 0: \quad N(s) + F_a = 0 \implies \boxed{N(s) = -F_a = 35{,}5\ \text{N}}$$

$$\sum F_y = 0: \quad T_n(s) + F_r = 0 \implies \boxed{T_n(s) = -F_r = -37{,}25\ \text{N}}$$

$$\sum F_z = 0: \quad T_b(s) + F_c = 0 \implies \boxed{T_b(s) = -F_c = -113\ \text{N}}$$

### Ravnovesje momentov (oko težišča preseka)

**Torzija** (moment okoli $x$-osi):
$$\sum M_x = 0: \quad M_t(s) + F_c \cdot r = 0$$
$$\boxed{M_t(s) = -F_c \cdot r = -113 \times 17{,}5 = -1977{,}5\ \text{N·mm}} \quad \text{(konstanta)}$$

**Upogibni moment v ravnini $x$-$y$** (moment okolid $z$-osi):
$$\sum M_z = 0: \quad M_b(s) + F_r \cdot (L - s) = 0$$
$$\boxed{M_b(s) = -F_r \cdot (L - s) = -37{,}25\,(34{,}75 - s)\ \text{N·mm}} \quad \text{(linearna)}$$

**Upogibni moment v ravnini $x$-$z$** (moment okoli $y$-osi):
$$\sum M_y = 0: \quad M_n(s) + F_c \cdot (L - s) + F_r \cdot r = 0$$
$$\boxed{M_n(s) = -F_c \cdot (L - s) - F_r \cdot r = -113\,(34{,}75 - s) - 651{,}875\ \text{N·mm}} \quad \text{(linearna)}$$

> **Opomba:** Člen $F_r \cdot r$ nastopi ker $F_r$ deluje na polmeru $r$ od osi in pri prenosu v os povzroči moment okoli $y$-osi.

---

## 4. Vrednosti funkcij

### Mejne vrednosti ($s = 0$ in $s = L$)

| Veličina | Pri $s=0$ (vpetje) | Pri $s=L$ (prost konec) |
|----------|-------------------|------------------------|
| $N$ | $+35{,}5\ \text{N}$ | $+35{,}5\ \text{N}$ |
| $T_n$ | $-37{,}25\ \text{N}$ | $-37{,}25\ \text{N}$ |
| $T_b$ | $-113\ \text{N}$ | $-113\ \text{N}$ |
| $M_t$ | $-1977{,}5\ \text{N·mm}$ | $-1977{,}5\ \text{N·mm}$ |
| $M_b$ | $-37{,}25 \times 34{,}75 = -1294{,}44\ \text{N·mm}$ | $0$ |
| $M_n$ | $-113 \times 34{,}75 - 651{,}875 = -4578{,}625\ \text{N·mm}$ | $-651{,}875\ \text{N·mm}$ |

---

## 5. Diagrami notranjih sil in navorov

> Diagrame generiraj z `DN1_diagrami.py` (v isti mapi).

### Shematični prikaz

```
N(s)  [N]
 35.5 |████████████████|
      0                L

T_n(s) [N]
      0                L
-37.25 |████████████████|

T_b(s) [N]
      0                L
 -113  |████████████████|

Mt(s) [N·mm]
      0                L
-1977.5 |███████████████|

Mb(s) [N·mm]
      0              / L=0
-1294.4 \___________/

Mn(s) [N·mm]
      0         ______/ -651.9
-4578.6 \______/
```

---

## 6. Verifikacija

- **Dimenzije:** $[N]\ =\ \text{N}$,  $[M]\ =\ \text{N·mm}$ ✓
- **Prost konec:** $M_b(L) = 0$, kar je pravilno (ni externega momenta $M_b$ na prostem koncu) ✓
- $M_n(L) = -651{,}875\ \text{N·mm} \ne 0$ — to je pričakovano, ker $F_r$ deluje izven osi (na polmeru $r$), kar pomeni, da obstaja preneseni moment $F_r \cdot r$ na prostem koncu ✓
- **Konstantne sile:** $N$, $T_n$, $T_b$ so konstantne, ker zunanja sila deluje le na enem mestu (prostem koncu) ✓
- **Torzija konstantna:** $M_t$ je konstantna vzdolž celotnega stebla ✓

---

## 7. Napetostno kritično mesto

Največje obremenitve nastopijo pri **vpetju** ($s = 0$):

$$|M_b(0)| = 1294{,}44\ \text{N·mm}, \quad |M_n(0)| = 4578{,}625\ \text{N·mm}$$

Skupni upogibni moment:
$$M_{up} = \sqrt{M_b^2 + M_n^2} = \sqrt{1294{,}44^2 + 4578{,}625^2} \approx 4757\ \text{N·mm}$$

Torzija: $|M_t| = 1977{,}5\ \text{N·mm}$

> Za dimenzioniranje prereza se upošteva kombinacija $M_{up}$ in $M_t$ po kriteriju (npr. HMH ali DE-Goodman).
