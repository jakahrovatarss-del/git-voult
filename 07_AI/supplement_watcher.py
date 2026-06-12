#!/usr/bin/env python3
"""
Supplement Auto-Watcher
=======================
Teče v ozadju. Ko označiš Vyvanse ali Večerja kot DONE v Obsidianu,
avtomatsko posodobi vse odvisne taske s pravimi izračunanimi časi.

Zagon: python supplement_watcher.py
Ali pa dvoklikni: START_WATCHER.bat
"""

import time, re, os, sys
from datetime import datetime, timedelta
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ── CONFIG ────────────────────────────────────────────────────────────────────
VAULT = Path(__file__).parent.parent          # obsidian/
TASKS = VAULT / "TaskNotes" / "Tasks"
LOG   = VAULT / "07_AI" / "watcher_log.txt"
# ─────────────────────────────────────────────────────────────────────────────

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def today():
    return datetime.now().strftime("%Y-%m-%d")

def read_frontmatter(path):
    """Vrne dict frontmatter vrednosti iz .md datoteke."""
    text = Path(path).read_text(encoding="utf-8")
    fm = {}
    in_fm = False
    for line in text.splitlines():
        if line.strip() == "---":
            if not in_fm: in_fm = True
            else: break
        elif in_fm and ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"')
    return fm

def update_field(path, field, new_value):
    """Posodobi eno frontmatter polje v .md datoteki."""
    text = Path(path).read_text(encoding="utf-8")
    # Zamenjaj scheduled: ...
    pattern = rf'^({re.escape(field)}:\s*)(.+)$'
    new_text = re.sub(pattern, rf'\g<1>{new_value}', text, flags=re.MULTILINE)
    # Posodobi tudi dateModified
    now_stamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+02:00")
    new_text = re.sub(r'^(dateModified:\s*)(.+)$', rf'\g<1>{now_stamp}', new_text, flags=re.MULTILINE)
    Path(path).write_text(new_text, encoding="utf-8")

def update_scheduled_and_body(path, new_dt, note_extra=""):
    """Posodobi scheduled čas in opombo v telu taska."""
    new_scheduled = new_dt.strftime("%Y-%m-%dT%H:%M")
    new_time_str  = new_dt.strftime("%H:%M")

    text = Path(path).read_text(encoding="utf-8")

    # Posodobi frontmatter scheduled
    text = re.sub(r'^(scheduled:\s*)(.+)$', rf'\g<1>{new_scheduled}', text, flags=re.MULTILINE)
    # Posodobi "⏰ **Čas: HH:MM**" v telesu
    text = re.sub(r'(⏰ \*\*Čas: )\d{2}:\d{2}(\*\*)', rf'\g<1>{new_time_str}\g<2>', text)
    # Posodobi dateModified
    now_stamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000+02:00")
    text = re.sub(r'^(dateModified:\s*)(.+)$', rf'\g<1>{now_stamp}', text, flags=re.MULTILINE)
    # Dodaj opombo če je podana
    if note_extra:
        text = re.sub(r'(⏰ \*\*Čas: \d{2}:\d{2}\*\*)', rf'\g<1>\n\n> 🔄 **AUTO-POSODOBLJENO ob {datetime.now().strftime("%H:%M")}** — {note_extra}', text, count=1)

    Path(path).write_text(text, encoding="utf-8")
    log(f"  → Posodobljen: {Path(path).name} → {new_time_str}")

def recalculate_from_vyvanse(vyvanse_time: datetime):
    """Ko je Vyvanse označen done — posodobi vse zjutrajšnje taske."""
    d = today()
    log(f"🔄 Vyvanse ob {vyvanse_time.strftime('%H:%M')} → Računam odvisnosti...")

    zajtrk          = vyvanse_time + timedelta(minutes=15)
    zajtrk_deadline = vyvanse_time + timedelta(hours=1)
    theanine        = vyvanse_time + timedelta(hours=2, minutes=15)
    kosilo          = vyvanse_time + timedelta(hours=5, minutes=15)
    vitC_min        = vyvanse_time + timedelta(hours=2)

    tasks_to_update = [
        (f"{d} 04 Zajtrk + Suplementi", zajtrk,
         f"Vzemi do {zajtrk_deadline.strftime('%H:%M')}! (1h po Vyvanse)"),
        (f"{d} 05 L-Theanine 200mg", theanine,
         f"2h15m po Vyvanse"),
        (f"{d} 06 Kosilo + Baker 2mg", kosilo,
         f"5h15m po Vyvanse"),
    ]

    for name, new_dt, note in tasks_to_update:
        path = TASKS / f"{name}.md"
        if path.exists():
            update_scheduled_and_body(path, new_dt, note)
        else:
            log(f"  ⚠️  Ni najden: {name}.md")

    # Posodobi opombo v Vyvanse tasku z deadline
    vyvanse_path = TASKS / f"{d} 03 Vyvanse 40mg.md"
    if vyvanse_path.exists():
        text = vyvanse_path.read_text(encoding="utf-8")
        text = re.sub(
            r'(\| 🍳 Zajtrk OBVEZEN do \| \*\*)[\d:]+(\*\* \|)',
            rf'\g<1>{zajtrk_deadline.strftime("%H:%M")}\g<2>', text
        )
        text = re.sub(
            r'(\| 🍊 Vitamin C ne prej kot \| \*\*)[\d:]+(\*\* \|)',
            rf'\g<1>{vitC_min.strftime("%H:%M")}\g<2>', text
        )
        vyvanse_path.write_text(text, encoding="utf-8")

    log(f"✅ Vyvanse veriga posodobljena: Zajtrk {zajtrk.strftime('%H:%M')} | Theanine {theanine.strftime('%H:%M')} | Kosilo {kosilo.strftime('%H:%M')}")

def recalculate_from_vecerja(vecerja_time: datetime):
    """Ko je Večerja označena done — posodobi CJC+IPA in Spanje."""
    d = today()
    log(f"🔄 Večerja ob {vecerja_time.strftime('%H:%M')} → Računam CJC+IPA...")

    cjc    = vecerja_time + timedelta(hours=3)
    spanje = cjc + timedelta(minutes=45)
    no_food_until = cjc + timedelta(hours=1)

    # CJC task
    cjc_path = TASKS / f"{d} 09 CJC + IPA Injekcija.md"
    if cjc_path.exists():
        update_scheduled_and_body(cjc_path, cjc,
            f"3h po večerji ({vecerja_time.strftime('%H:%M')} + 3h)")
        # Posodobi tudi NIJ HRANE čas v telesu
        text = cjc_path.read_text(encoding="utf-8")
        text = re.sub(
            r'(- \[ \] Po injekciji NIJ HRANE do )\d{2}:\d{2}',
            rf'\g<1>{no_food_until.strftime("%H:%M")}', text
        )
        cjc_path.write_text(text, encoding="utf-8")
    else:
        log(f"  ⚠️  Ni najden: CJC task")

    # Spanje task
    spanje_path = TASKS / f"{d} 10 Spanje.md"
    if spanje_path.exists():
        update_scheduled_and_body(spanje_path, spanje,
            f"45min po CJC ({cjc.strftime('%H:%M')} + 45min)")
        text = spanje_path.read_text(encoding="utf-8")
        vstani = spanje + timedelta(hours=8)
        text = re.sub(
            r'(- \[ \] Vstani ob )\d{2}:\d{2}',
            rf'\g<1>{vstani.strftime("%H:%M")}', text
        )
        spanje_path.write_text(text, encoding="utf-8")

    log(f"✅ Večerja veriga posodobljena: CJC {cjc.strftime('%H:%M')} | Spanje {spanje.strftime('%H:%M')}")


class SupplementHandler(FileSystemEventHandler):
    def __init__(self):
        self._last_processed = {}   # path → zadnji obdelan čas (anti-spam)

    def on_modified(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix != ".md":
            return

        # Anti-spam: ignoriraj če smo isti file obdelali pred < 3s
        now = time.time()
        if self._last_processed.get(str(path), 0) > now - 3:
            return

        name = path.stem
        d = today()

        # Nas zanima samo današnje datume
        if not name.startswith(d):
            return

        try:
            fm = read_frontmatter(path)
        except Exception as e:
            return

        if fm.get("status") != "done":
            return

        self._last_processed[str(path)] = now

        # Kdaj je bil označen done? → dateModified
        date_modified_str = fm.get("dateModified", "")
        try:
            # Format: 2026-06-12T10:15:32.000+02:00
            taken_time = datetime.strptime(date_modified_str[:16], "%Y-%m-%dT%H:%M")
        except:
            taken_time = datetime.now()

        # ── Kateri task je bil označen? ──────────────────────────────────────
        if "03 Vyvanse" in name:
            log(f"\n🎯 VYVANSE označen done! Čas: {taken_time.strftime('%H:%M')}")
            recalculate_from_vyvanse(taken_time)

        elif "07 Vecerja" in name:
            log(f"\n🎯 VEČERJA označena done! Čas: {taken_time.strftime('%H:%M')}")
            recalculate_from_vecerja(taken_time)


def main():
    log("=" * 50)
    log("🚀 Supplement Watcher zagnan")
    log(f"📁 Opazujem: {TASKS}")
    log("=" * 50)
    log("Čaka na označitve v Obsidianu...")
    log("  → Označi Vyvanse done = posodobi zajtrk/theanine/kosilo")
    log("  → Označi Večerja done = posodobi CJC+IPA/spanje")
    log("  (Ctrl+C za zaustavitev)\n")

    handler  = SupplementHandler()
    observer = Observer()
    observer.schedule(handler, str(TASKS), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        log("👋 Watcher zaustavljen.")
    observer.join()

if __name__ == "__main__":
    main()
