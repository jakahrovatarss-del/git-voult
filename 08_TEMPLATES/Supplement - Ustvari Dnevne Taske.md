<%*
// ═══════════════════════════════════════════════════════════
// SUPPLEMENT DAILY GENERATOR
// Ustvari vse današnje supplement taske v TaskNotes
// Sprozi zjutraj enkrat — potem samo loggaj čase
// ═══════════════════════════════════════════════════════════

const today = tp.date.now("YYYY-MM-DD");
const tasksFolder = "TaskNotes/Tasks";

// Preveri če teski za danes že obstajajo
const existing = app.vault.getAbstractFileByPath(`${tasksFolder}/${today} 03 Vyvanse 40mg.md`);
if (existing) {
    new Notice(`ℹ️ Teski za ${today} že obstajajo!`);
    return;
}

// Privzeti časi (posodobijo se ko loggaš)
const DEF_VYVANSE = "07:45";
const DEF_DINNER  = "19:00";

const addMin = (timeStr, mins) => {
    const [h, m] = timeStr.split(":").map(Number);
    const total = h * 60 + m + mins;
    return `${String(Math.floor(total/60)%24).padStart(2,"0")}:${String(total%60).padStart(2,"0")}`;
};

const T = {
    tirozin:   addMin(DEF_VYVANSE, -45),
    injekcija: addMin(DEF_VYVANSE, -45),
    vyvanse:   DEF_VYVANSE,
    zajtrk:    addMin(DEF_VYVANSE,  15),
    theanine:  addMin(DEF_VYVANSE, 135),
    kosilo:    addMin(DEF_VYVANSE, 315),
    vecerja:   DEF_DINNER,
    vitC:      DEF_DINNER,
    cjc:       addMin(DEF_DINNER, 180),
    spanje:    addMin(DEF_DINNER, 225),
};

const nowStamp = () => new Date().toISOString().slice(0,19) + ".000+02:00";

function taskContent(title, time, priority, blockingArr, blockedByArr, notes) {
    const blocking  = blockingArr?.length  ? `blocking:\n${blockingArr.map(b=>`  - "[[${b}]]"`).join("\n")}\n` : "";
    const blockedBy = blockedByArr?.length ? `blockedBy:\n${blockedByArr.map(b=>`  - "[[${b}]]"`).join("\n")}\n` : "";
    return `---
title: ${title}
status: open
priority: ${priority}
scheduled: ${today}T${time}
due: ${today}
dateCreated: ${nowStamp()}
dateModified: ${nowStamp()}
tags:
  - task
  - supplement
  - health
contexts:
  - zdravje
projects:
  - Peptide Protocol
${blocking}${blockedBy}---

# ${title}

⏰ **Čas: ${time}**

${notes}
`;
}

const p = today;
const tasks = [
    [`${p} 01 L-Tirozin 500mg`,      "🧠 L-Tirozin 500mg",                    T.tirozin,   "high",
     [`${p} 03 Vyvanse 40mg`], null,
     `Na **prazen želodec**, 45 min pred Vyvanse.\n\n- [ ] Vzemi kapsulo z vodo`],

    [`${p} 02 Injekcija GLOW50 + RT`, "💉 Injekcija GLOW50 750mcg + RT 1mg SC", T.injekcija, "urgent",
     [`${p} 03 Vyvanse 40mg`], null,
     `**Tešče** (min 8h). SC trebuh, 45°.\n\n- [ ] GLOW50: 3.75 enot U100\n- [ ] RT: 20 enot U100\n- [ ] Počakaj 45min`],

    [`${p} 03 Vyvanse 40mg`,          "💊 Vyvanse 40mg",                        T.vyvanse,   "urgent",
     [`${p} 04 Zajtrk + Suplementi`],
     [`${p} 01 L-Tirozin 500mg`, `${p} 02 Injekcija GLOW50 + RT`],
     `⚠️ Vzemi šele ko sta 01 in 02 DONE!\n\n| Kaj | Kdaj |\n|-----|------|\n| 🍳 Zajtrk OBVEZEN do | **${addMin(T.vyvanse, 60)}** |\n| 🍊 Vitamin C ne prej kot | **${addMin(T.vyvanse, 120)}** |\n\n- [ ] Kapsula z vodo`],

    [`${p} 04 Zajtrk + Suplementi`,   "🍳 Zajtrk + Jutranji Suplementi",        T.zajtrk,    "urgent",
     [`${p} 05 L-Theanine 200mg`],
     [`${p} 03 Vyvanse 40mg`],
     `⚠️ **OBVEZNO do ${addMin(T.vyvanse, 60)}** — 40-50g beljakovin\n\n- [ ] Kreatin 5g\n- [ ] Omega-3 (2 kapsuli)\n- [ ] D3+K2\n- [ ] B-kompleks\n- [ ] Cink 25mg\n- [ ] CoQ10 200mg\n- [ ] Kolagenski peptidi 10g`],

    [`${p} 05 L-Theanine 200mg`,      "🍵 L-Theanine 200mg",                    T.theanine,  "normal",
     null, [`${p} 04 Zajtrk + Suplementi`],
     `- [ ] 1 kapsula (200mg)\n- [ ] Po potrebi še ena popoldne`],

    [`${p} 06 Kosilo + Baker 2mg`,    "🥗 Kosilo + Baker 2mg",                  T.kosilo,    "high",
     null, null,
     `40-50g beljakovin\n\n- [ ] Baker 2mg (LOČENO od cinka!)\n- [ ] L-karnitin 1-2g *(če NI vadbe)*\n- [ ] Elektroliti`],

    [`${p} 07 Vecerja`,               "🍽️ Večerja — ZAPIŠI ČAS",               T.vecerja,   "urgent",
     [`${p} 08 VitaminC + Magnezij`, `${p} 09 CJC + IPA Injekcija`], null,
     `⚠️ Po večerji NIJ HRANE — CJC zahteva 3h tešče!\n\n- [ ] Dejansi čas: ______\n- [ ] CJC = čas + 3h = ______`],

    [`${p} 08 VitaminC + Magnezij`,   "🍊 Vitamin C 1000mg + Magnezij 300mg",  T.vitC,      "high",
     null, [`${p} 07 Vecerja`],
     `Z večerjo:\n\n- [ ] Vitamin C 1000mg\n- [ ] Magnezij bisglicinat 300mg`],

    [`${p} 09 CJC + IPA Injekcija`,   "💉 CJC-1295 + Ipamorelin SC — 3H PO VEČERJI", T.cjc, "urgent",
     [`${p} 10 Spanje`],
     [`${p} 07 Vecerja`],
     `⏰ **3 URE PO VEČERJI** (privzeto ${DEF_DINNER} → ${T.cjc})\n\n- [ ] CJC: 4 enote U100\n- [ ] IPA: 6 enot U100\n- [ ] HA serum (obraz)\n- [ ] NIJ HRANE do ${addMin(T.cjc, 60)}`],

    [`${p} 10 Spanje`,                `😴 Spanje — ${T.spanje}`,                T.spanje,    "high",
     null, [`${p} 09 CJC + IPA Injekcija`],
     `- [ ] Posteljo ob ${T.spanje}\n- [ ] Vstani ob ${addMin(T.spanje, 480)}`],
];

let created = 0;
for (const [filename, title, time, priority, blocking, blockedBy, notes] of tasks) {
    const path = `${tasksFolder}/${filename}.md`;
    const content = taskContent(title, time, priority, blocking, blockedBy, notes);
    await app.vault.create(path, content);
    created++;
}

new Notice(`✅ ${created} supplement taskov ustvarjenih za ${today}!\n\nKo vzameš Vyvanse → zaženi "Supplement - Log Vyvanse"\nKo večerjaš → zaženi "Supplement - Log Vecerja"`, 8000);
_%>
