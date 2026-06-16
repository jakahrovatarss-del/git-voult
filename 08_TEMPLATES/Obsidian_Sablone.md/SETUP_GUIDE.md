# SETUP_GUIDE.md - Kako Integrirati AI Navodila v Vault

## ⚡ HITRI PREGLED

Ta navodila ti pokažejo, kako:
1. **Pravilno postaviti** CLAUDE.md datoteko
2. **Konfigurirati AI agente** (Claude Code, Cursor, drugi)
3. **Testirati delovanje** pred resnim uporabom
4. **Vzdrževati in posodabljati** navodila

---

## 🗂️ KAM POSTAVITI DATOTEKE

### Struktura, ki jo Trebaš

```
tvoj-vault/
├── CLAUDE.md                    ← GLAVNA navodila za AI
├── AI_QUICK_REFERENCE.md        ← Hitri cheatsheet
├── README.md                    ← Splošen opis vault-a
│
├── 04-Daily/
│   └── (dnevni zapisi)
│
├── 05-References/
│   ├── Muhammad_bin_Salman.md
│   ├── Jared_Kushner.md
│   └── (druge osebe, podjetja)
│
├── 06-Atlas/                    ← Evergreen notes
│   ├── Britanska_divide_and_conquer.md
│   ├── Donma_kot_infiltration_model.md
│   └── Faustov_dogovor.md
│
├── 08-Templates/                ← Sablone
│   ├── Person_Template.md
│   ├── Event_Template.md
│   ├── Theory_Template.md
│   ├── Daily_Template.md
│   └── Evergreen_Template.md
│
├── Las_Vegas_1_oktober_2017.md  ← V rootu!
├── Praxis-pametno_mesto.md      ← V rootu!
└── (drugi glavni članki)
```

### Kritični Detajli

**CLAUDE.md MORA biti v rootu vault-a** - to AI agenti samodejno preberejo.

**Razlog**: 
- Claude Code: bere `CLAUDE.md` iz delovne mape
- Cursor: bere `.cursorrules` ali `CLAUDE.md`
- Obsidian CLI: prebere ko se zažene

---

## 🤖 KONFIGURACIJA AI AGENTOV

### Opcija 1: Claude Code (Najpriporočanejša)

#### Korak 1: Inštalacija
```bash
# Na Mac/Linux
npm install -g @anthropic-ai/claude-code

# Preveri
claude --version
```

#### Korak 2: Avtorizacija
```bash
claude
# Sledi navodilom za prijavo
```

#### Korak 3: Odpri Vault s Claude Code
```bash
cd /pot/do/tvojega/vault
claude
```

Claude bo avtomatsko prebral `CLAUDE.md` in vedel kako delati.

#### Korak 4: Test
```
"Naredi nov članek o Donald Trumpu v stilu mojega vault-a"
```

Claude bo:
- ✓ Pogledal v CLAUDE.md
- ✓ Sledil tvojemu stilu
- ✓ Linkiral relevantne osebe
- ✓ Postavil v pravo mapo

---

### Opcija 2: Cursor (za VS Code uporabniki)

#### Korak 1: Naredi `.cursorrules` datoteko v root vault-a

```bash
cp CLAUDE.md .cursorrules
```

#### Korak 2: Odpri vault v Cursor
```bash
cursor /pot/do/vault
```

Cursor bo prebral `.cursorrules` in sledil navodilom.

---

### Opcija 3: Obsidian s Claude (Prek Plugina)

#### Korak 1: Inštaliraj "Smart Connections" ali "Text Generator" plugin

V Obsidian:
1. Settings → Community Plugins
2. Browse → Search: "Smart Connections"
3. Install + Enable

#### Korak 2: Konfiguriraj Plugin

V plugin settings:
1. Dodaj API key (Anthropic Claude)
2. **Pomembno**: V "System Prompt" pasti VSEBINO `CLAUDE.md`

#### Korak 3: Test v Obsidian

Odpri katerikoli članek → Use plugin command → Ask:
```
"Razširi ta članek v stilu mojih obstoječih zapiskov"
```

---

### Opcija 4: Claude Web (Najpreprostejša)

Če ne želiš inštalirati ničesar:

1. Pojdi na **claude.ai**
2. Ustvari nov projekt: "Obsidian Raziskave"
3. **Naloži CLAUDE.md** in **AI_QUICK_REFERENCE.md** v "Project Knowledge"
4. Po želji naloži tudi obstoječe članke

Sedaj vsakič ko se pogovarjaš s Claudom v tem projektu, bo poznala navodila.

---

## 📝 TESTIRANJE: ALI DELUJE?

### Test 1: Generiranje Novega Članka

**Prompt**:
```
Naredi članek o "Henry Kissinger" v stilu mojega vault-a.
```

**Pričakovan Rezultat**:
- ✓ Datoteka v `05-References/`
- ✓ Frontmatter s `categories: [[People]]`
- ✓ Naslov "Kdo je"
- ✓ Linki na druge osebe (`[[Donald Trump]]`, itd.)
- ✓ Slovenščina, neformalna
- ✓ Sekcija "Viri" na koncu

### Test 2: Razširjanje Obstoječega Članka

**Prompt**:
```
Razširi [[Muhammad bin Salman]] z novimi informacijami o Vision 2030.
```

**Pričakovan Rezultat**:
- ✓ Ohranja obstoječi stil
- ✓ Dodaja v relevantno sekcijo
- ✓ Linkira nove pojme
- ✓ Posodobi `updated` property
- ✓ Ne briše obstoječega

### Test 3: Identifikacija Vzorca

**Prompt**:
```
Analiziraj moje članke in poišči vzorce, ki bi lahko bili evergreen notes.
```

**Pričakovan Rezultat**:
- ✓ Predlaga 2-3 evergreen note ideje
- ✓ Pokaže konkretne primere
- ✓ Predlaga ime in strukturo

---

## 🔧 PRILAGAJANJE

### Spreminjanje CLAUDE.md

Če opazišč, da AI:
- **Ne uporablja tvoje slovenščine** → Dodaj več primerov v "STIL PISANJA"
- **Ne linkira dovolj** → Okrepi "LINKIRANJE PRAVILA"
- **Pretirano strukturira** → Dodaj v "ANTI-PATTERNS"
- **Pozablja na properties** → Okrepi "PROPERTIES SISTEM"

### Predlog: Različne Verzije CLAUDE.md

Lahko narediš **specializirane verzije** za različne tipe dela:

**`CLAUDE_research.md`** - za raziskovalno delo (geopolitika, zarote)
**`CLAUDE_health.md`** - za zdravstvene zapiske (peptidi, biologija)
**`CLAUDE_personal.md`** - za osebne zapiske

Potem v promptu lahko rečeš:
```
"Uporabi CLAUDE_research.md za to nalogo."
```

---

## 🚀 NAPREDNI WORKFLOW

### KJ Reads Sistem (Dva Sloja)

Po videoposnetku KJ Reads, lahko narediš:

#### Layer 1: Strategija (v rootu)
```
CLAUDE.md → splošna navodila
GOALS.md → tvoji raziskovalni cilji
ROADMAP.md → kaj raziskuješ naslednje
```

#### Layer 2: Projekti (po raziskovalnih temah)
```
projects/
├── geopolitika/
│   └── CLAUDE.md (specifična navodila)
├── peptidi/
│   └── CLAUDE.md (specifična navodila)
└── tehnologija/
    └── CLAUDE.md (specifična navodila)
```

Vsak projekt ima svoj **`CLAUDE.md`** s specifičnimi navodili.

---

### Vin Sistem (Commands)

Po Vinovem pristopu, lahko narediš **slash commands**:

V `08-Templates/commands/`:

**`/today.md`**:
```
Preveri dnevne zapise zadnjih 7 dni, identificiraj vzorce
in predlagaj 3 nova področja za raziskovanje danes.
```

**`/connect.md`**:
```
Vzemi dve osebi ali koncepta in poišči vse povezave med njima
preko obstoječih člankov v vault-u.
```

**`/evergreen.md`**:
```
Identificiraj 3 ponavljajoče se vzorce v mojih raziskavah
in predlagaj nove evergreen notes.
```

V Claude Code uporabiš:
```bash
claude --command today
claude --command connect "MBS in Kushner"
claude --command evergreen
```

---

## 📊 VZDRŽEVANJE NAVODIL

### Tedensko (5 min)

- [ ] Preveri, ali AI dela kvalitetno
- [ ] Dodaj nove primere v CLAUDE.md če rabita
- [ ] Posodobi categories indexe

### Mesečno (15 min)

- [ ] Preglej vse nove članke
- [ ] Identificiraj vzorce za evergreen notes
- [ ] Posodobi CLAUDE.md z novimi pravili
- [ ] Premakni datoteke v prave mape

### Letno (1 ura)

- [ ] Velik pregled vault strukture
- [ ] Refactor CLAUDE.md za novo leto
- [ ] Backup celotnega vault-a
- [ ] Razmisli o novih sistemih (npr. AI integracija)

---

## 🆘 PROBLEM SOLVING

### Problem: AI ne uporablja tvojega stila

**Rešitev**:
1. Dodaj več **konkretnih primerov** v CLAUDE.md (sekcija "STIL")
2. Vključi 2-3 obstoječe članke kot "exemplar"
3. Reci AI: "Preden začneš, preberi [[Muhammad bin Salman]] kot primer stila"

### Problem: AI naredi datoteko v napačni mapi

**Rešitev**:
1. Okrepi tabelo "KAM GRE KAJ?" v CLAUDE.md
2. V promptu eksplicitno reci: "V mapi 05-References/"

### Problem: AI dela duplikate

**Rešitev**:
1. Reci: "Najprej preveri, ali članek že obstaja"
2. Dodaj v CLAUDE.md pod "PRED PISANJEM": vedno search

### Problem: AI premalo linkira

**Rešitev**:
1. Dodaj v CLAUDE.md jasno pravilo: "Minimum 5 linkov na članek"
2. Reci: "Linkiraj vse imene, lokacije in koncepte"

---

## 🎯 KONKRETNI PRVI KORAKI

### Danes (15 min)

1. ✅ Skopiraj `CLAUDE.md` v root tvojega vault-a
2. ✅ Skopiraj `AI_QUICK_REFERENCE.md` v root
3. ✅ Skopiraj `Obsidian_Sablone.md` v `08-Templates/`
4. ✅ Naredi mapo `04-Daily/` in `06-Atlas/`

### Jutri (30 min)

1. ✅ Izberi AI orodje (Claude Code, Web, Cursor)
2. ✅ Konfiguriraj ga po zgornjih navodilih
3. ✅ Testiraj z enim novim člankom
4. ✅ Preveri, ali rezultat ustreza tvojemu stilu

### Ta Teden (1 ura)

1. ✅ Naredi prvi dnevni zapis v `04-Daily/`
2. ✅ Naredi prvo evergreen note v `06-Atlas/`
3. ✅ Premakni vsaj 3 osebne profile v `05-References/`
4. ✅ Ustvari `[[People]]` kategorijski index v rootu

### Naslednji Teden (2 uri)

1. ✅ Dodaj properties (confidence, rating) v 5 obstoječih člankov
2. ✅ Naredi 2-3 evergreen notes
3. ✅ Konfiguriraj hotkeyes v Obsidian
4. ✅ Testiraj AI workflow z transkripcijo videoposnetka

---

## 📚 DODATNI VIRI

### Branje
- **Steph Ango blog**: stephango.com (osnovna filozofija)
- **Nick Milo**: linkingyourthinking.com (LYT sistem)
- **Obsidian docs**: help.obsidian.md

### Videoposnetki (že analizirani)
- "How to Use Obsidian Like the CEO" - Steph Ango filozofija
- "Web Clipper for AI Second Brain" - Nick Milo
- "Essential 80% of Obsidian" - Nick Milo
- "Obsidian CLI + Claude Code" - Vin
- "AI Second Brain" - KJ Reads

### Skupnosti
- **Obsidian Discord**: za vprašanja in inspiracijo
- **r/ObsidianMD**: Reddit skupnost

---

## ✅ KONEC

Sedaj imaš:
1. **CLAUDE.md** - glavna navodila za AI
2. **AI_QUICK_REFERENCE.md** - hitri cheatsheet
3. **Obsidian_Sablone.md** - sablone za vse vrste člankov
4. **Analiza_Tvojega_Obsidian_Vault.md** - analiza in priporočila
5. **SETUP_GUIDE.md** - ta navodila

**Naslednji korak**: Izberi AI orodje in **začni testirati**!

---

## 🤝 SODELOVANJE Z AI

**Tvoja vloga**:
- Razmišljaš
- Raziskuješ
- Odločaš
- Daješ feedback

**AI vloga**:
- Sledi navodilom
- Pomaga pri pisanju
- Predlaga povezave
- Pripravi strukturo

**Skupaj**:
- Boljši zapiski
- Hitrejši pregled
- Globlje povezave
- **Drugi možgani, ki dejansko delajo**

---

*Vprašanja? Spreminjaj CLAUDE.md po potrebi. Ti si gospodar svojega vault-a.*
