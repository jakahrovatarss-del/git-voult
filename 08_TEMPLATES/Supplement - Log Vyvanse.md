<%*
// ═══════════════════════════════════════════════════════════
// SUPPLEMENT LOGGER — VYVANSE
// Sprozi preko: Command palette → "Templater: Open Insert Template Modal"
// Ali nastavi hotkey direktno na ta template
// ═══════════════════════════════════════════════════════════

const inputTime = await tp.system.prompt(
    "🕐 Ob kateri uri si vzel Vyvanse? (HH:MM)",
    new Date().toTimeString().slice(0,5)
);

if (!inputTime || !inputTime.match(/^\d{2}:\d{2}$/)) {
    new Notice("❌ Neveljaven format časa. Uporabi HH:MM");
    return;
}

const today = new Date().toISOString().slice(0, 10);
const [vH, vM] = inputTime.split(":").map(Number);

// ── Izračun vseh odvisnih časov ──────────────────────────────
const addMin = (h, m, mins) => {
    const total = h * 60 + m + mins;
    return `${String(Math.floor(total/60) % 24).padStart(2,"0")}:${String(total%60).padStart(2,"0")}`;
};

const times = {
    zajtrk:          addMin(vH, vM, 15),
    zajtrk_deadline: addMin(vH, vM, 60),
    theanine:        addMin(vH, vM, 135),
    kosilo:          addMin(vH, vM, 315),
    vitC_min:        addMin(vH, vM, 120),
};

// ── Posodobi TaskNotes datoteke ──────────────────────────────
const tasksFolder = "TaskNotes/Tasks";

async function updateTaskScheduled(filename, newTime, noteExtra = "") {
    const path = `${tasksFolder}/${filename}`;
    try {
        const file = app.vault.getAbstractFileByPath(path);
        if (!file) { new Notice(`⚠️ Ni najden: ${filename}`); return; }

        let content = await app.vault.read(file);
        const newScheduled = `${today}T${newTime}`;
        const nowStamp = new Date().toISOString().slice(0,19) + ".000+02:00";

        // Posodobi frontmatter scheduled
        content = content.replace(
            /^(scheduled:\s*)(.+)$/m,
            `$1${newScheduled}`
        );
        // Posodobi čas v telesu
        content = content.replace(
            /(⏰ \*\*Čas: )\d{2}:\d{2}(\*\*)/,
            `$1${newTime}$2`
        );
        // Posodobi dateModified
        content = content.replace(
            /^(dateModified:\s*)(.+)$/m,
            `$1${nowStamp}`
        );
        // Dodaj opombo
        if (noteExtra) {
            content = content.replace(
                /(⏰ \*\*Čas: \d{2}:\d{2}\*\*)/,
                `$1\n> 🔄 **AUTO** ob ${new Date().toTimeString().slice(0,5)}: ${noteExtra}`
            );
        }

        await app.vault.modify(file, content);
    } catch(e) {
        new Notice(`❌ Napaka pri ${filename}: ${e}`);
    }
}

// Posodobi vse odvisne taske
await updateTaskScheduled(
    `${today} 04 Zajtrk + Suplementi.md`,
    times.zajtrk,
    `Vzami do ${times.zajtrk_deadline} (1h po Vyvanse!)`
);
await updateTaskScheduled(
    `${today} 05 L-Theanine 200mg.md`,
    times.theanine,
    `2h15m po Vyvanse`
);
await updateTaskScheduled(
    `${today} 06 Kosilo + Baker 2mg.md`,
    times.kosilo,
    `5h15m po Vyvanse`
);

// Posodobi opombi v Vyvanse tasku
const vyvansePath = `${tasksFolder}/${today} 03 Vyvanse 40mg.md`;
const vyvanseFile = app.vault.getAbstractFileByPath(vyvansePath);
if (vyvanseFile) {
    let c = await app.vault.read(vyvanseFile);
    c = c.replace(/(🍳 Zajtrk OBVEZEN do \| \*\*)[\d:]+(\*\* \|)/, `$1${times.zajtrk_deadline}$2`);
    c = c.replace(/(🍊 Vitamin C ne prej kot \| \*\*)[\d:]+(\*\* \|)/, `$1${times.vitC_min}$2`);
    await app.vault.modify(vyvanseFile, c);
}

// ── Prikaži potrdilo ─────────────────────────────────────────
new Notice(
    `✅ Vyvanse ob ${inputTime}\n` +
    `🍳 Zajtrk: ${times.zajtrk} (do ${times.zajtrk_deadline})\n` +
    `🍵 Theanine: ${times.theanine}\n` +
    `🥗 Kosilo: ${times.kosilo}`,
    8000
);
_%>
Human: <% tp.date.now("YYYY-MM-DD") %> — Vyvanse ob <%inputTime%> ✅
