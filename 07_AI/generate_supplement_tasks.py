#!/usr/bin/env python3
"""
Supplement Daily Task Generator za Obsidian TaskNotes
Uporaba: python3 generate_supplement_tasks.py [VYVANSE_TIME] [DINNER_TIME] [DATE]
Primer:  python3 generate_supplement_tasks.py 07:45 19:00 2026-06-12
"""
from datetime import datetime, timedelta
import os, sys

VAULT = "/sessions/elegant-trusting-feynman/mnt/obsidian"
TASKS_DIR = os.path.join(VAULT, "TaskNotes", "Tasks")

def parse_time(date_str, time_str):
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")

def fmt_dt(dt):   return dt.strftime("%Y-%m-%dT%H:%M")
def fmt_date(dt): return dt.strftime("%Y-%m-%d")
def stamp(dt):    return dt.strftime("%Y-%m-%dT%H:%M:%S.000+02:00")

def write_task(filename, title, sched, priority, blocking=None, blocked_by=None, notes="", status="open"):
    now = stamp(datetime.now())
    def links(lst): return "\n".join(f'  - "[[{x}]]"' for x in lst) if lst else ""
    
    blocking_block  = f"blocking:\n{links(blocking)}\n"  if blocking  else ""
    blockedby_block = f"blockedBy:\n{links(blocked_by)}\n" if blocked_by else ""

    content = f"""---
title: {title}
status: {status}
priority: {priority}
scheduled: {fmt_dt(sched)}
due: {fmt_date(sched)}
dateCreated: {now}
dateModified: {now}
tags:
  - task
  - supplement
  - health
contexts:
  - zdravje
projects:
  - Peptide Protocol
{blocking_block}{blockedby_block}---

# {title}

⏰ **Čas: {sched.strftime('%H:%M')}**

{notes}
"""
    path = os.path.join(TASKS_DIR, filename + ".md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {filename}.md")

def main():
    vyvanse_time = sys.argv[1] if len(sys.argv) > 1 else "07:45"
    dinner_time  = sys.argv[2] if len(sys.argv) > 2 else "19:00"
    date_str     = sys.argv[3] if len(sys.argv) > 3 else datetime.now().strftime("%Y-%m-%d")

    v = parse_time(date_str, vyvanse_time)
    d = parse_time(date_str, dinner_time)

    # === VSI IZRAČUNANI ČASI ===
    t_tirozin   = v - timedelta(minutes=45)
    t_inj_am    = v - timedelta(minutes=45)
    t_vyvanse   = v
    t_zajtrk    = v + timedelta(minutes=15)
    t_zajtrk_deadline = v + timedelta(hours=1)
    t_theanine  = v + timedelta(hours=2, minutes=15)
    t_kosilo    = v + timedelta(hours=5, minutes=15)
    t_vecerja   = d
    t_vitC_mag  = d
    t_cjc       = d + timedelta(hours=3)
    t_spanje    = t_cjc + timedelta(minutes=45)
    t_vitC_min  = v + timedelta(hours=2)  # Vitamin C ne sme biti prej od tega

    p = date_str  # prefix

    print(f"\n🔧 Generiram taske za {date_str}...")
    print(f"   Vyvanse: {vyvanse_time} | Večerja: {dinner_time}")
    print(f"   → Zajtrk do: {t_zajtrk_deadline.strftime('%H:%M')} | CJC ob: {t_cjc.strftime('%H:%M')}\n")

    # ─── TASK 01: L-Tirozin ───────────────────────────────────────────────────
    write_task(
        f"{p} 01 L-Tirozin 500mg",
        f"🧠 L-Tirozin 500mg",
        t_tirozin,
        priority="high",
        blocking=[f"{p} 03 Vyvanse 40mg"],
        notes=f"""Na **prazen želodec** — 45 min pred Vyvanse.

- [ ] Vzemi kapsulo z vodo
- [ ] Nastavi timer na {t_vyvanse.strftime('%H:%M')} za Vyvanse

> ⚠️ Ne jej nič do zajtrka ob {t_zajtrk.strftime('%H:%M')}"""
    )

    # ─── TASK 02: Injekcija zjutraj ───────────────────────────────────────────
    write_task(
        f"{p} 02 Injekcija GLOW50 + RT",
        f"💉 Injekcija GLOW50 750mcg + RT 1mg SC",
        t_inj_am,
        priority="urgent",
        blocking=[f"{p} 03 Vyvanse 40mg"],
        notes=f"""**Tešče** (min 8h od zadnjega obroka). SC v trebuh, 45° kot.

- [ ] Dezinficiraj mesto injekcije
- [ ] GLOW50: 750mcg = 3.75 enot U100
- [ ] RT: 1mg = 20 enot U100
- [ ] Počakaj 45 min → NIJ HRANE do {t_vyvanse.strftime('%H:%M')}

> ⚠️ RT + insulin = blokirano delovanje. Tešče je nujno."""
    )

    # ─── TASK 03: Vyvanse ─────────────────────────────────────────────────────
    write_task(
        f"{p} 03 Vyvanse 40mg",
        f"💊 Vyvanse 40mg",
        t_vyvanse,
        priority="urgent",
        blocked_by=[f"{p} 01 L-Tirozin 500mg", f"{p} 02 Injekcija GLOW50 + RT"],
        blocking=[f"{p} 04 Zajtrk + Suplementi"],
        notes=f"""⚠️ **Vzemi šele ko sta 01 in 02 označena kot DONE!**

- [ ] Kapsula z vodo

**Po Vyvanse — pomembni roki:**
| Kaj | Kdaj |
|-----|------|
| 🍳 Zajtrk OBVEZEN do | **{t_zajtrk_deadline.strftime('%H:%M')}** |
| 🍊 Vitamin C ne prej kot | **{t_vitC_min.strftime('%H:%M')}** |
| 💊 Vse zajtrk supl. | **{t_zajtrk.strftime('%H:%M')}** |

> ⚠️ Vyvanse + RT = dvojna supresija apetita. Nastavi alarm za zajtrk!"""
    )

    # ─── TASK 04: Zajtrk + suplementi ────────────────────────────────────────
    write_task(
        f"{p} 04 Zajtrk + Suplementi",
        f"🍳 Zajtrk + Jutranji Suplementi",
        t_zajtrk,
        priority="urgent",
        blocked_by=[f"{p} 03 Vyvanse 40mg"],
        blocking=[f"{p} 05 L-Theanine 200mg"],
        notes=f"""⚠️ **OBVEZNO do {t_zajtrk_deadline.strftime('%H:%M')}** (1h po Vyvanse) — brez obroka se razgrajujejo mišice!

**40-50g beljakovin** (3 jajca + 150g jogurt + 50g oves)

S hrano vzemi:
- [ ] Kreatin 5g
- [ ] Omega-3 (2 kapsuli) — 800mg EPA+DHA
- [ ] D3+K2 (1 kapsula)
- [ ] B-kompleks (1 kapsula)
- [ ] Cink 25mg
- [ ] CoQ10 200mg (z maščobo!)
- [ ] Kolagenski peptidi 10g (v napitek/kavo)

> 🚫 Cink in Baker NIKOLI skupaj → baker je ob kosilu!"""
    )

    # ─── TASK 05: L-Theanine ─────────────────────────────────────────────────
    write_task(
        f"{p} 05 L-Theanine 200mg",
        f"🍵 L-Theanine 200mg",
        t_theanine,
        priority="normal",
        blocked_by=[f"{p} 04 Zajtrk + Suplementi"],
        notes=f"""Po zajtrku — umiritev Vyvanse efekta, boljši fokus brez anksioznosti.

- [ ] 1 kapsula (200mg)
- [ ] Po potrebi še ena kapsula popoldne (~15:00)"""
    )

    # ─── TASK 06: Kosilo + Baker ──────────────────────────────────────────────
    write_task(
        f"{p} 06 Kosilo + Baker 2mg",
        f"🥗 Kosilo + Baker 2mg",
        t_kosilo,
        priority="high",
        notes=f"""**40-50g beljakovin** (piščanec/riba/govedina)

S kosilom vzemi:
- [ ] Baker 2mg ← LOČENO od cinka (cink je bil ob {t_zajtrk.strftime('%H:%M')}!)
- [ ] L-karnitin 1-2g *(SAMO če danes NI vadbe — sicer prestavi na 15:00)*
- [ ] Elektroliti v vodi (natrij + kalij + magnezij)

> 🔬 Zakaj baker? Dolgotrajno jemanje cinka brez bakra → pomanjkanje bakra."""
    )

    # ─── TASK 07: Večerja ─────────────────────────────────────────────────────
    write_task(
        f"{p} 07 Vecerja",
        f"🍽️ Večerja — ZAPIŠI ČAS",
        t_vecerja,
        priority="urgent",
        blocking=[f"{p} 08 VitaminC + Magnezij", f"{p} 09 CJC + IPA Injekcija"],
        notes=f"""**40-50g beljakovin**

- [ ] Dejansi čas večerje: ______:______
- [ ] CJC+IPA = 3h po tem času = ______:______

⚠️ **Po večerji NIJ HRANE** — CJC+IPA zahteva 3h tešče!

> 📌 Ko označiš večerjo, nastavi alarm: dejansi_čas + 3h = CJC+IPA"""
    )

    # ─── TASK 08: Vitamin C + Magnezij ───────────────────────────────────────
    write_task(
        f"{p} 08 VitaminC + Magnezij",
        f"🍊 Vitamin C 1000mg + Magnezij 300mg",
        t_vitC_mag,
        priority="high",
        blocked_by=[f"{p} 07 Vecerja"],
        notes=f"""Vzemi Z večerjo (ne moti več Vyvanse ker je dovolj časa minilo):

- [ ] Vitamin C 1000mg (Bioflavonoids)
- [ ] Magnezij bisglicinat 300mg

> Vitamin C podpira kolagen sintezo (GHK-Cu sinergija).
> Magnezij → globoki spanec + mišična regeneracija."""
    )

    # ─── TASK 09: CJC + IPA ───────────────────────────────────────────────────
    write_task(
        f"{p} 09 CJC + IPA Injekcija",
        f"💉 CJC-1295 + Ipamorelin SC — 3H PO VEČERJI",
        t_cjc,
        priority="urgent",
        blocked_by=[f"{p} 07 Vecerja"],
        blocking=[f"{p} 10 Spanje"],
        notes=f"""⏰ **3 URE PO VEČERJI** (privzeto: večerja {dinner_time} → injekcija {t_cjc.strftime('%H:%M')})

⚠️ Če si večerjal ob drugem času → posodobi scheduled čas tega taska!

- [ ] Dezinficiraj mesto injekcije
- [ ] CJC-1295: 200mcg = 4 enote U100
- [ ] Ipamorelin: 300mcg = 6 enot U100
- [ ] SC v trebuh, 45° kot
- [ ] Hialuronska kislina serum (topikalno na obraz)
- [ ] Po injekciji NIJ HRANE do {(t_cjc + timedelta(minutes=60)).strftime('%H:%M')}

> 🔬 Zakaj tešče? Insulin blokira GH sproščanje. Tešče = čisti GH pulz ponoči."""
    )

    # ─── TASK 10: Spanje ──────────────────────────────────────────────────────
    write_task(
        f"{p} 10 Spanje",
        f"😴 Spanje — {t_spanje.strftime('%H:%M')}",
        t_spanje,
        priority="high",
        blocked_by=[f"{p} 09 CJC + IPA Injekcija"],
        notes=f"""45 min po CJC+IPA injekciji (inzulin pade, GH pulz se sproži med globokim spancem).

- [ ] V posteljo ob {t_spanje.strftime('%H:%M')}
- [ ] Cilj: 7-9 ur spanja
- [ ] Vstani ob {(t_spanje + timedelta(hours=8)).strftime('%H:%M')}

> 💡 CJC+IPA maksimizira naravni GH pulz med spanjem. Kvaliteta spanca = ključna."""
    )

    print(f"\n✅ Ustvarjenih 10 taskov za {date_str}")
    print(f"📅 Urnik: L-Tirozin {t_tirozin.strftime('%H:%M')} → Injekcija {t_inj_am.strftime('%H:%M')} → Vyvanse {vyvanse_time} → Zajtrk {t_zajtrk.strftime('%H:%M')} (do {t_zajtrk_deadline.strftime('%H:%M')})")
    print(f"🍽️  Večerja {dinner_time} → VitC+Mag {t_vitC_mag.strftime('%H:%M')} → CJC+IPA {t_cjc.strftime('%H:%M')} → Spanje {t_spanje.strftime('%H:%M')}")

if __name__ == "__main__":
    main()
