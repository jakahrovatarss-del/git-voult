<%*
// ═══════════════════════════════════════════════════════════
// SUPPLEMENT LOGGER — VEČERJA
// Sprozi ko konças večerjati — izračuna CJC+IPA čas
// ═══════════════════════════════════════════════════════════

const inputTime = await tp.system.prompt(
    "🍽️ Ob kateri uri si večerjal? (HH:MM)",
    new Date().toTimeString().slice(0,5)
);

if (!inputTime || !inputTime.match(/^\d{2}:\d{2}$/)) {
    new Notice("❌ Neveljaven format. Uporabi HH:MM");
    return;
}

const today = new Date().toISOString().slice(0, 10);
const [dH, dM] = inputTime.split(":").map(Number);

const addMin = (h, m, mins) => {
    const total = h * 60 + m + mins;
    return `${String(Math.floor(total/60) % 24).padStart(2,"0")}:${String(total%60).padStart(2,"0")}`;
};

const cjc    = addMin(dH, dM, 180);   // +3 ure
const spanje = addMin(dH, dM, 225);   // +3h45min
const noFood = addMin(dH, dM, 240);   // +4h (1h po CJC)

const tasksFolder = "TaskNotes/Tasks";

async function updateTaskScheduled(filename, newTime, noteExtra = "") {
    const path = `${tasksFolder}/${filename}`;
    try {
        const file = app.vault.getAbstractFileByPath(path);
        if (!file) { new Notice(`⚠️ Ni najden: ${filename}`); return; }

        let content = await app.vault.read(file);
        const nowStamp = new Date().toISOString().slice(0,19) + ".000+02:00";

        content = content.replace(/^(scheduled:\s*)(.+)$/m, `$1${today}T${newTime}`);
        content = content.replace(/(⏰ \*\*Čas: )\d{2}:\d{2}(\*\*)/, `$1${newTime}$2`);
        content = content.replace(/^(dateModified:\s*)(.+)$/m, `$1${nowStamp}`);

        if (noteExtra) {
            content = content.replace(
                /(⏰ \*\*Čas: \d{2}:\d{2}\*\*)/,
                `$1\n> 🔄 **AUTO** ob ${new Date().toTimeString().slice(0,5)}: ${noteExtra}`
            );
        }
        await app.vault.modify(file, content);
    } catch(e) {
        new Notice(`❌ Napaka: ${e}`);
    }
}

// CJC+IPA — posodobi scheduled in "NIJ HRANE do X"
const cjcFilename = `${today} 09 CJC + IPA Injekcija.md`;
await updateTaskScheduled(cjcFilename, cjc, `3h po večerji (${inputTime} + 3h)`);

// Posodobi še NIJ HRANE čas v telesu CJC taska
const cjcFile = app.vault.getAbstractFileByPath(`${tasksFolder}/${cjcFilename}`);
if (cjcFile) {
    let c = await app.vault.read(cjcFile);
    c = c.replace(/(- \[ \] Po injekciji NIJ HRANE do )\d{2}:\d{2}/, `$1${noFood}`);
    await app.vault.modify(cjcFile, c);
}

// Spanje
await updateTaskScheduled(
    `${today} 10 Spanje.md`,
    spanje,
    `45min po CJC (${cjc} + 45min)`
);

// Vstani čas v Spanje tasku
const spanjeFile = app.vault.getAbstractFileByPath(`${tasksFolder}/${today} 10 Spanje.md`);
if (spanjeFile) {
    const [sH, sM] = spanje.split(":").map(Number);
    const vstani = addMin(sH, sM, 480); // +8h
    let c = await app.vault.read(spanjeFile);
    c = c.replace(/(- \[ \] Vstani ob )\d{2}:\d{2}/, `$1${vstani}`);
    await app.vault.modify(spanjeFile, c);
}

new Notice(
    `✅ Večerja ob ${inputTime}\n` +
    `💉 CJC+IPA: ${cjc}\n` +
    `😴 Spanje: ${spanje}\n` +
    `🚫 NIJ HRANE do: ${noFood}`,
    8000
);
_%>
Human: <% tp.date.now("YYYY-MM-DD") %> — Večerja ob <%inputTime%> ✅
