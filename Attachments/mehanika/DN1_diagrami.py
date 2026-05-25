"""
DN1 - Diagrami notranjih sil in navorov v rezkalnem orodju
Konzola dolžine L = 34.75 mm, sile na polmeru r = 17.5 mm
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")   # non-interactive backend – ne potrebuje zaslona
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── Podatki ──────────────────────────────────────────────
L = 34.75   # mm  – dolžina stebla
r = 17.5    # mm  – polmer orodja
Fa = -35.5  # N   – aksialna (negativna = tlak)
Fr = 37.25  # N   – radialna
Fc = 113.0  # N   – obodna (rezalna)

s = np.linspace(0, L, 500)

# ── Notranje sile/navori (metoda preseka, desni del) ──────
N   =  -Fa * np.ones_like(s)                    # aksialna sila
Tn  =  -Fr * np.ones_like(s)                    # strižna y
Tb  =  -Fc * np.ones_like(s)                    # strižna z
Mt  =  -Fc * r * np.ones_like(s)                # torzija (konst.)
Mb  =  -Fr * (L - s)                            # upogib ok. z
Mn  =  -Fc * (L - s) - Fr * r                   # upogib ok. y

# ── Mejne vrednosti (za oznake) ───────────────────────────
vals = {
    "N":  (N[0],   N[-1]),
    "Tn": (Tn[0],  Tn[-1]),
    "Tb": (Tb[0],  Tb[-1]),
    "Mt": (Mt[0],  Mt[-1]),
    "Mb": (Mb[0],  Mb[-1]),
    "Mn": (Mn[0],  Mn[-1]),
}

# ── Risanje ───────────────────────────────────────────────
fig = plt.figure(figsize=(14, 16))
fig.suptitle(
    "Notranje sile in navori – rezkar (konzola)\n"
    f"$L = {L}$ mm,  $r = {r}$ mm,  "
    f"$F_a = {Fa}$ N,  $F_r = {Fr}$ N,  $F_c = {Fc}$ N",
    fontsize=13, fontweight="bold"
)

gs = gridspec.GridSpec(3, 2, figure=fig, hspace=0.55, wspace=0.35)

datasets = [
    (gs[0, 0], s, N,  "N(s)  [N]",   "Aksialna sila N",   "tab:blue"),
    (gs[0, 1], s, Tn, "T_n(s)  [N]", "Strižna sila $T_n$", "tab:orange"),
    (gs[1, 0], s, Tb, "T_b(s)  [N]", "Strižna sila $T_b$", "tab:green"),
    (gs[1, 1], s, Mt, "M_t(s)  [N·mm]", "Torzija $M_t$",  "tab:red"),
    (gs[2, 0], s, Mb, "M_b(s)  [N·mm]", "Upogibni moment $M_b$", "tab:purple"),
    (gs[2, 1], s, Mn, "M_n(s)  [N·mm]", "Upogibni moment $M_n$", "tab:brown"),
]

for spec, xs, ys, ylabel, title, color in datasets:
    ax = fig.add_subplot(spec)
    ax.plot(xs, ys, color=color, linewidth=2)
    ax.fill_between(xs, ys, 0, alpha=0.15, color=color)
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_xlabel("s  [mm]", fontsize=9)
    ax.set_ylabel(ylabel, fontsize=9)
    ax.set_title(title, fontsize=10, fontweight="bold")
    ax.set_xlim(0, L)

    # Oznake vrednosti na začetku in koncu
    y0, yL = float(ys[0]), float(ys[-1])
    yrange = float(np.ptp(ys)) if float(np.ptp(ys)) != 0 else max(abs(y0), abs(yL), 1)
    offset = 0.12 * yrange
    sign0 = 1 if y0 >= 0 else -1
    signL = 1 if yL >= 0 else -1
    ax.text(0.5, y0 + offset * sign0, f"{y0:.1f}", fontsize=8, ha="left", color=color)
    ax.text(L - 0.5, yL + offset * signL, f"{yL:.1f}", fontsize=8, ha="right", color=color)

    ax.grid(True, alpha=0.3, linestyle="--")

out_path = "DN1_diagrami.png"
plt.savefig(out_path, dpi=150, bbox_inches="tight")
plt.close()
print(f"Slika shranjena: {out_path}")

# ── Izpis povzetka ────────────────────────────────────────
print("\n=== Povzetek vrednosti ===")
print(f"N(s)   = {N[0]:.2f} N  (konst.)")
print(f"Tn(s)  = {Tn[0]:.2f} N  (konst.)")
print(f"Tb(s)  = {Tb[0]:.2f} N  (konst.)")
print(f"Mt(s)  = {Mt[0]:.2f} N·mm  (konst.)")
print(f"Mb(0)  = {Mb[0]:.2f} N·mm,  Mb(L) = {Mb[-1]:.2f} N·mm")
print(f"Mn(0)  = {Mn[0]:.2f} N·mm,  Mn(L) = {Mn[-1]:.2f} N·mm")

Mup = np.sqrt(Mb[0]**2 + Mn[0]**2)
print(f"\nSkupni upogibni moment pri vpetju: M_up = sqrt(Mb²+Mn²) = {Mup:.2f} N·mm")
