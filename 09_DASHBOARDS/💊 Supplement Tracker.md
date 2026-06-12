---
tags:
  - dashboard
  - supplement
  - tracker
cssclasses:
  - wide-page
---

```dataviewjs
// ═══════════════════════════════════════════════════════════════════════
// 💊 SUPPLEMENT TRACKER
// • Bere status iz TaskNotes (avtomatsko)
// • Shranjuje počutje/energijo/stranske učinke v localStorage
// • SVG grafi za trende
// ═══════════════════════════════════════════════════════════════════════

const TASKS = "TaskNotes/Tasks";
const today = moment().format("YYYY-MM-DD");
const LS_KEY = d => `sptrk_${d}`;

// ── localStorage helpers ─────────────────────────────────────────────
const loadDay = d => {
    try { return JSON.parse(localStorage.getItem(LS_KEY(d)) || "{}"); }
    catch { return {}; }
};
const saveDay = (d, data) => {
    const existing = loadDay(d);
    localStorage.setItem(LS_KEY(d), JSON.stringify({...existing, ...data}));
};

// ── TaskNotes reader ─────────────────────────────────────────────────
async function getSupp(filename) {
    const file = app.vault.getAbstractFileByPath(`${TASKS}/${filename}`);
    if (!file) return null;
    const c = await app.vault.read(file);
    return {
        status:    c.match(/^status:\s*(.+)$/m)?.[1]?.trim(),
        planned:   c.match(/^scheduled:\s*.+T(\d{2}:\d{2})$/m)?.[1],
        completed: c.match(/^completedDate:\s*(.+)$/m)?.[1]?.trim(),
        modified:  c.match(/^dateModified:\s*(.+T)(\d{2}:\d{2}):/m)?.[2],
    };
}

const SUPPS = [
    { id:"tirozin",  label:"🧠 L-Tirozin 500mg",          file:`${today} 01 L-Tirozin 500mg.md` },
    { id:"glow",     label:"💉 GLOW50 + RT",               file:`${today} 02 Injekcija GLOW50 + RT.md` },
    { id:"vyvanse",  label:"💊 Vyvanse 40mg",              file:`${today} 03 Vyvanse 40mg.md` },
    { id:"zajtrk",   label:"🍳 Zajtrk + Suplementi",       file:`${today} 04 Zajtrk + Suplementi.md` },
    { id:"theanine", label:"🍵 L-Theanine 200mg",          file:`${today} 05 L-Theanine 200mg.md` },
    { id:"kosilo",   label:"🥗 Kosilo + Baker 2mg",        file:`${today} 06 Kosilo + Baker 2mg.md` },
    { id:"vecerja",  label:"🍽️ Večerja",                   file:`${today} 07 Vecerja.md` },
    { id:"vitc",     label:"🍊 Vitamin C + Magnezij",      file:`${today} 08 VitaminC + Magnezij.md` },
    { id:"cjc",      label:"💉 CJC-1295 + Ipamorelin",    file:`${today} 09 CJC + IPA Injekcija.md` },
    { id:"spanje",   label:"😴 Spanje",                    file:`${today} 10 Spanje.md` },
];

// Pre-load all today's tasks
const suppData = {};
for (const s of SUPPS) { suppData[s.id] = await getSupp(s.file); }

const nowHHMM = moment().format("HH:mm");
const nowMin  = parseInt(moment().format("HH"))*60 + parseInt(moment().format("mm"));

// ── CSS ──────────────────────────────────────────────────────────────
const css = document.createElement("style");
css.textContent = `
.st{font-family:var(--font-interface);max-width:100%;}
.st-h1{font-size:1.4em;font-weight:800;color:var(--color-accent);margin:0 0 4px;}
.st-sub{font-size:0.85em;color:var(--text-muted);margin-bottom:14px;}
.st-grid2{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:18px;}
.st-grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:16px;}
.st-card{background:var(--background-secondary);border-radius:10px;padding:14px 16px;}
.st-ch{font-size:0.78em;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.05em;margin:0 0 8px;}
.st-row{display:flex;align-items:center;gap:8px;padding:5px 8px;border-radius:6px;margin:2px 0;transition:background .1s;}
.st-row:hover{background:var(--background-modifier-hover);}
.st-ico{font-size:1.1em;width:22px;text-align:center;}
.st-lbl{flex:1;font-size:0.86em;}
.st-t{font-size:0.82em;font-weight:600;color:#7c3aed;min-width:40px;}
.st-done{opacity:.45;text-decoration:line-through;}
.st-done .st-t{text-decoration:none;opacity:1;}
.st-late{background:rgba(239,68,68,.07);border-left:2px solid #ef4444;}
.st-now{background:rgba(124,58,237,.08);border-left:2px solid #7c3aed;}
.st-inp{background:var(--background-primary);border:1px solid var(--background-modifier-border);border-radius:5px;padding:4px 8px;font-size:0.88em;color:var(--text-normal);width:100%;box-sizing:border-box;font-family:var(--font-interface);}
.st-inp:focus{outline:none;border-color:#7c3aed;box-shadow:0 0 0 2px rgba(124,58,237,.15);}
.st-label{font-size:0.8em;color:var(--text-muted);margin:6px 0 2px;display:block;}
.st-range{width:100%;accent-color:#7c3aed;}
.st-rval{font-size:1.1em;font-weight:700;color:#7c3aed;text-align:center;min-width:24px;}
.st-rrow{display:flex;align-items:center;gap:8px;margin:4px 0;}
.st-rname{font-size:0.85em;flex:1;}
.st-emoji-row{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0;}
.st-em{font-size:1.3em;cursor:pointer;padding:4px 8px;border-radius:6px;border:2px solid transparent;transition:all .15s;}
.st-em:hover,.st-em.sel{border-color:#7c3aed;background:rgba(124,58,237,.1);}
.st-btn{border:none;border-radius:6px;padding:6px 16px;font-size:0.85em;font-weight:700;cursor:pointer;transition:all .15s;}
.st-save{background:#7c3aed;color:white;width:100%;margin-top:10px;}
.st-save:hover{background:#6d28d9;}
.st-saved{background:#059669;color:white;width:100%;margin-top:10px;}
.st-sep{border:none;border-top:1px solid var(--background-modifier-border);margin:14px 0;}
.st-stat{text-align:center;padding:8px;}
.st-stat-n{font-size:1.8em;font-weight:800;color:#7c3aed;}
.st-stat-l{font-size:0.75em;color:var(--text-muted);margin-top:2px;}
.st-badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:0.78em;font-weight:600;margin:1px;}
.st-miss{background:#fee2e2;color:#991b1b;}
`;
dv.container.appendChild(css);

const root = dv.container.createEl("div", {cls:"st"});

// ── Title ────────────────────────────────────────────────────────────
root.createEl("div", {cls:"st-h1", text:"💊 Supplement Tracker"});
root.createEl("div", {cls:"st-sub", text:`${moment().format("dddd, DD. MMMM YYYY")} · Posodobljeno ob ${nowHHMM}`});

// ── Count today's done ───────────────────────────────────────────────
const doneCount = Object.values(suppData).filter(s => s?.status === "done").length;
const totalCount = Object.values(suppData).filter(s => s !== null).length;
const pct = totalCount ? Math.round((doneCount/totalCount)*100) : 0;

// ── Stats row ────────────────────────────────────────────────────────
const statsRow = root.createEl("div", {cls:"st-grid3"});
const statItems = [
    {n: `${doneCount}/${totalCount}`, l: "Vzeto danes"},
    {n: `${pct}%`,                   l: "Adherence danes"},
    {n: totalCount === 0 ? "—" : (pct >= 80 ? "🟢" : pct >= 50 ? "🟡" : "🔴"), l: "Status"},
];
for (const {n, l} of statItems) {
    const c = statsRow.createEl("div", {cls:"st-card st-stat"});
    c.createEl("div", {cls:"st-stat-n", text: n});
    c.createEl("div", {cls:"st-stat-l", text: l});
}

// ═══════════════════════════════════════════════════
// DVOKOLONSKI LAYOUT: Urnik | Dnevni Vnos
// ═══════════════════════════════════════════════════
const mainGrid = root.createEl("div", {cls:"st-grid2"});
const colUrnik = mainGrid.createEl("div");
const colVnos  = mainGrid.createEl("div");

// ── LEFT: Urnik za danes ─────────────────────────────────────────────
const urnikCard = colUrnik.createEl("div", {cls:"st-card"});
urnikCard.createEl("div", {cls:"st-ch", text:"📋 Urnik za danes — avtomatsko iz TaskNotes"});

if (totalCount === 0) {
    urnikCard.createEl("div", {
        cls:"st-miss",
        attr:{style:"padding:8px 12px;border-radius:6px;font-size:0.88em;"},
        text:"⚠️ Teski niso ustvarjeni. Pritisni Ctrl+Shift+S."
    });
} else {
    for (const s of SUPPS) {
        const d = suppData[s.id];
        if (!d) continue;
        const isDone = d.status === "done";
        const tMin   = d.planned ? parseInt(d.planned.split(":")[0])*60 + parseInt(d.planned.split(":")[1]) : null;
        const isLate = !isDone && tMin && tMin < nowMin;
        const isCurr = !isDone && tMin && Math.abs(tMin - nowMin) <= 30;

        let cls = "st-row";
        if (isCurr) cls += " st-now";
        else if (isLate) cls += " st-late";
        if (isDone) cls += " st-done";

        const row = urnikCard.createEl("div", {cls});
        row.createEl("span", {cls:"st-ico", text: isDone ? "✅" : isLate ? "⚠️" : isCurr ? "▶️" : "⬜"});
        row.createEl("span", {cls:"st-lbl", text: s.label});
        const doneTime = isDone && d.modified ? d.modified : null;
        row.createEl("span", {cls:"st-t",   text: doneTime ? `✓ ${doneTime}` : (d.planned || "—")});
    }
}

// ── RIGHT: Dnevni Vnos ───────────────────────────────────────────────
const vnosCard = colVnos.createEl("div", {cls:"st-card"});
vnosCard.createEl("div", {cls:"st-ch", text:`📝 Vnos za danes — ${moment().format("DD.MM.YYYY")}`});

const saved = loadDay(today);
let pendingSave = {...saved};

// Helper: labeled range input
function addRange(parent, key, label, emoji1, emoji2, min=1, max=10) {
    parent.createEl("span", {cls:"st-label", text:label});
    const rrow = parent.createEl("div", {cls:"st-rrow"});
    rrow.createEl("span", {text:emoji1, attr:{style:"font-size:1.1em;"}});
    const inp = rrow.createEl("input");
    inp.type="range"; inp.min=min; inp.max=max;
    inp.value = pendingSave[key] ?? Math.round((min+max)/2);
    inp.className="st-range";
    inp.style.flex="1";
    const valSpan = rrow.createEl("span", {cls:"st-rval", text:inp.value});
    rrow.createEl("span", {text:emoji2, attr:{style:"font-size:1.1em;"}});
    inp.addEventListener("input", () => { valSpan.textContent=inp.value; pendingSave[key]=parseInt(inp.value); });
    return inp;
}

addRange(vnosCard, "feeling", "💜 Splošno počutje", "😞", "😄");
addRange(vnosCard, "energy",  "⚡ Energija",        "🪫", "⚡");
addRange(vnosCard, "focus",   "🎯 Fokus",            "😵","🎯");
addRange(vnosCard, "sleep",   "😴 Spanec (prejšnja noč)", "😴","✨");

vnosCard.createEl("span", {cls:"st-label", text:"🍽️ Apetit"});
const apRow = vnosCard.createEl("div", {cls:"st-emoji-row"});
const apOptions = [["1","😐 Zmanjšan"],["2","😊 Normalen"],["3","😋 Povečan"]];
let apSel = pendingSave.apetit ?? "2";
const apBtns = [];
for (const [val, lbl] of apOptions) {
    const b = apRow.createEl("button", {text:lbl, cls:"st-em"+(apSel===val?" sel":"")});
    apBtns.push({b, val});
    b.addEventListener("click", () => {
        apSel=val; pendingSave.apetit=val;
        apBtns.forEach(({b:bb,val:vv}) => bb.classList.toggle("sel", vv===val));
    });
}

vnosCard.createEl("span", {cls:"st-label", text:"⚠️ Stranski učinki (prazno = brez)"});
const seInp = vnosCard.createEl("input", {cls:"st-inp"});
seInp.type="text"; seInp.placeholder="npr. glavobol, suha usta, palpitacije...";
seInp.value = pendingSave.sideEffects ?? "";
seInp.addEventListener("input", () => { pendingSave.sideEffects = seInp.value; });

vnosCard.createEl("span", {cls:"st-label", text:"📝 Opombe"});
const notesInp = vnosCard.createEl("textarea", {cls:"st-inp"});
notesInp.rows=3; notesInp.placeholder="Kakšen dan je bil? Kaj si opazil?";
notesInp.value = pendingSave.notes ?? "";
notesInp.style.resize="vertical";
notesInp.addEventListener("input", () => { pendingSave.notes = notesInp.value; });

const saveBtn = vnosCard.createEl("button", {cls:"st-btn st-save", text:"💾 Shrani vnos za danes"});
saveBtn.addEventListener("click", () => {
    pendingSave.timestamp = new Date().toISOString();
    saveDay(today, pendingSave);
    saveBtn.textContent = "✅ Shranjeno!";
    saveBtn.className = "st-btn st-saved";
    setTimeout(() => { saveBtn.textContent="💾 Shrani vnos za danes"; saveBtn.className="st-btn st-save"; }, 2500);
});

// Pre-fill if already saved today
if (saved.feeling) { saveBtn.textContent = `✅ Zadnjič shranjeno ob ${saved.timestamp ? new Date(saved.timestamp).toLocaleTimeString("sl-SI",{hour:"2-digit",minute:"2-digit"}) : "—"}`; saveBtn.className="st-btn st-saved"; }

root.createEl("hr", {cls:"st-sep"});

// ═══════════════════════════════════════════════════════════════════
// SVG GRAFI — zadnjih 14 dni
// ═══════════════════════════════════════════════════════════════════
root.createEl("div", {cls:"st-ch", text:"📈 TREND — ZADNJIH 14 DNI"});

const DAYS = 14;
const days = Array.from({length:DAYS}, (_,i) => moment().subtract(DAYS-1-i,"days").format("YYYY-MM-DD"));
const dayLabels = days.map(d => moment(d).format("DD.MM"));

// Load historical data
const hist = days.map(d => loadDay(d));

// TaskNotes adherence per day (count done tasks)
const adherence = [];
for (const d of days) {
    const files = app.vault.getMarkdownFiles().filter(f => f.path.startsWith(`${TASKS}/${d}`));
    if (files.length === 0) { adherence.push(null); continue; }
    let done=0;
    for (const f of files) {
        const c = await app.vault.read(f);
        if (/^status:\s*done$/m.test(c)) done++;
    }
    adherence.push(Math.round((done/files.length)*100));
}

// ── SVG helper ────────────────────────────────────────────────────────
function makeSVG(width, height) {
    const el = document.createElementNS("http://www.w3.org/2000/svg","svg");
    el.setAttribute("viewBox", `0 0 ${width} ${height}`);
    el.setAttribute("width","100%");
    el.setAttribute("preserveAspectRatio","xMidYMid meet");
    return el;
}
function svgLine(svg, x1,y1,x2,y2, color="#7c3aed", w=2) {
    const l = document.createElementNS("http://www.w3.org/2000/svg","line");
    l.setAttribute("x1",x1); l.setAttribute("y1",y1);
    l.setAttribute("x2",x2); l.setAttribute("y2",y2);
    l.setAttribute("stroke",color); l.setAttribute("stroke-width",w);
    svg.appendChild(l); return l;
}
function svgPath(svg, pts, color="#7c3aed", w=2.5, fill="none") {
    if (pts.filter(p=>p).length < 2) return;
    const d = pts.map((p,i) => {
        if (!p) return null;
        return `${i===0 || !pts[i-1] ? "M" : "L"}${p[0]},${p[1]}`;
    }).filter(Boolean).join(" ");
    const path = document.createElementNS("http://www.w3.org/2000/svg","path");
    path.setAttribute("d",d); path.setAttribute("stroke",color);
    path.setAttribute("stroke-width",w); path.setAttribute("fill",fill);
    path.setAttribute("stroke-linejoin","round"); path.setAttribute("stroke-linecap","round");
    svg.appendChild(path);
}
function svgCircle(svg, cx,cy, r=4, fill="#7c3aed") {
    const c = document.createElementNS("http://www.w3.org/2000/svg","circle");
    c.setAttribute("cx",cx); c.setAttribute("cy",cy);
    c.setAttribute("r",r); c.setAttribute("fill",fill);
    svg.appendChild(c); return c;
}
function svgText(svg, x,y, text, size=10, color="#6b7280", anchor="middle") {
    const t = document.createElementNS("http://www.w3.org/2000/svg","text");
    t.setAttribute("x",x); t.setAttribute("y",y);
    t.setAttribute("font-size",size); t.setAttribute("fill",color);
    t.setAttribute("text-anchor",anchor); t.setAttribute("font-family","Arial,sans-serif");
    t.textContent = text; svg.appendChild(t); return t;
}
function svgRect(svg, x,y,w,h, fill) {
    const r = document.createElementNS("http://www.w3.org/2000/svg","rect");
    r.setAttribute("x",x); r.setAttribute("y",y);
    r.setAttribute("width",w); r.setAttribute("height",h);
    r.setAttribute("fill",fill); r.setAttribute("rx","3");
    svg.appendChild(r); return r;
}

// ── CHART 1: Počutje / Energija / Fokus ──────────────────────────────
const W=760, H=180, PL=40, PR=20, PT=20, PB=40;
const plotW = W-PL-PR, plotH = H-PT-PB;

const chartBox1 = root.createEl("div", {cls:"st-card", attr:{style:"margin-bottom:14px;"}});
chartBox1.createEl("div", {cls:"st-ch", text:"Počutje · Energija · Fokus (1–10)"});
const svg1 = makeSVG(W, H);
chartBox1.appendChild(svg1);

// Grid lines
for (let v of [2,4,6,8,10]) {
    const y = PT + (1 - v/10) * plotH;
    svgLine(svg1, PL, y, W-PR, y, "#e5e7eb", 1);
    svgText(svg1, PL-4, y+4, v, 9, "#9ca3af", "end");
}

// X axis labels
days.forEach((d,i) => {
    const x = PL + (i/(DAYS-1))*plotW;
    if (i%2===0) svgText(svg1, x, H-6, dayLabels[i], 9, "#9ca3af");
});

// Data lines
const series = [
    {key:"feeling", color:"#7c3aed", label:"Počutje"},
    {key:"energy",  color:"#f59e0b", label:"Energija"},
    {key:"focus",   color:"#2563eb", label:"Fokus"},
];
for (const {key, color} of series) {
    const pts = hist.map((h,i) => {
        const v = h[key];
        if (!v) return null;
        return [PL + (i/(DAYS-1))*plotW, PT + (1 - v/10)*plotH];
    });
    svgPath(svg1, pts, color, 2.5);
    pts.forEach(p => { if (p) svgCircle(svg1, p[0], p[1], 4, color); });
}

// Legend
const legX = PL + 10;
series.forEach(({color,label},i) => {
    svgLine(svg1, legX+i*90, PT+8, legX+i*90+18, PT+8, color, 2.5);
    svgText(svg1, legX+i*90+22, PT+12, label, 10, "#374151", "start");
});

// ── CHART 2: Adherence ───────────────────────────────────────────────
const chartBox2 = root.createEl("div", {cls:"st-card", attr:{style:"margin-bottom:14px;"}});
chartBox2.createEl("div", {cls:"st-ch", text:"% Vzeto po dnevu (adherence iz TaskNotes)"});
const svg2 = makeSVG(W, H);
chartBox2.appendChild(svg2);

const barW = Math.floor(plotW / DAYS) - 4;
const barPad = Math.floor(plotW / DAYS);

// Grid lines
for (let v of [25,50,75,100]) {
    const y = PT + (1 - v/100)*plotH;
    svgLine(svg2, PL, y, W-PR, y, "#e5e7eb", 1);
    svgText(svg2, PL-4, y+4, `${v}%`, 9, "#9ca3af", "end");
}

// Bars
adherence.forEach((val, i) => {
    if (val === null) return;
    const x = PL + i*barPad + 2;
    const barH = (val/100)*plotH;
    const y = PT + plotH - barH;
    const color = val >= 80 ? "#059669" : val >= 50 ? "#f59e0b" : "#ef4444";
    svgRect(svg2, x, y, barW, barH, color);
    if (i%2===0) svgText(svg2, x+barW/2, H-6, dayLabels[i], 9, "#9ca3af");
});

root.createEl("hr", {cls:"st-sep"});

// ═══════════════════════════════════════════════════════════════════
// STATISTIKE — zadnjih 14 dni
// ═══════════════════════════════════════════════════════════════════
root.createEl("div", {cls:"st-ch", text:"📊 POVZETEK — ZADNJIH 14 DNI"});
const statGrid = root.createEl("div", {cls:"st-grid3"});

function avg(arr, key) {
    const vals = arr.map(d=>d[key]).filter(v=>v!=null&&v!==undefined);
    if (!vals.length) return null;
    return (vals.reduce((a,b)=>a+b,0)/vals.length).toFixed(1);
}
const avgAdh = adherence.filter(v=>v!==null);
const avgAdhPct = avgAdh.length ? Math.round(avgAdh.reduce((a,b)=>a+b,0)/avgAdh.length) : null;

const summaries = [
    {n: avg(hist,"feeling") ?? "—", l:"Ø Počutje",   sub:"zadnjih 14 dni"},
    {n: avg(hist,"energy")  ?? "—", l:"Ø Energija",   sub:"zadnjih 14 dni"},
    {n: avg(hist,"focus")   ?? "—", l:"Ø Fokus",      sub:"zadnjih 14 dni"},
    {n: avg(hist,"sleep")   ?? "—", l:"Ø Spanec",     sub:"zadnjih 14 dni"},
    {n: avgAdhPct !== null ? `${avgAdhPct}%` : "—", l:"Ø Adherence", sub:"iz TaskNotes"},
    {n: hist.filter(d=>d.sideEffects&&d.sideEffects.trim()).length, l:"Dni s str. učinki", sub:"od 14"},
];
for (const {n,l,sub} of summaries) {
    const c = statGrid.createEl("div", {cls:"st-card st-stat"});
    c.createEl("div", {cls:"st-stat-n", text:String(n)});
    c.createEl("div", {cls:"st-stat-l", text:l});
    if (sub) c.createEl("div", {attr:{style:"font-size:0.72em;color:var(--text-muted);"},text:sub});
}

// ── Stranski učinki log ───────────────────────────────────────────────
const seLog = hist.map((h,i)=>({date:dayLabels[i],se:h.sideEffects})).filter(x=>x.se&&x.se.trim());
if (seLog.length > 0) {
    root.createEl("hr", {cls:"st-sep"});
    root.createEl("div", {cls:"st-ch", text:"⚠️ STRANSKI UČINKI — ZADNJIH 14 DNI"});
    const seCard = root.createEl("div", {cls:"st-card"});
    for (const {date, se} of seLog) {
        const row = seCard.createEl("div", {attr:{style:"display:flex;gap:10px;padding:4px 0;border-bottom:1px solid var(--background-modifier-border);font-size:0.85em;"}});
        row.createEl("span", {attr:{style:"color:#7c3aed;font-weight:600;min-width:56px;"}, text:date});
        row.createEl("span", {text:se});
    }
}
```

---

> 💡 **Navodila:** Vsak dan zvečer vnesi počutje, energijo, fokus in spanje. Tracker avtomatsko bere, kdaj si vzel suplemente iz TaskNotes.
> 
> 🔗 [[09_DASHBOARDS/🏠 Dnevni Dashboard|← Dnevni Dashboard]] · [[02_AREAS/Peptidni Dnevnik/Dnevni Urnik - Peptide Protocol|💊 Peptide Urnik]]
