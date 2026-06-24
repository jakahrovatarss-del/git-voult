---
created: 2026-06-24
tags:
  - AI
  - hermes
  - modeli
  - optimizacija
  - tokens
type: reference
---

# Hermes — Modeli, Optimizacija Tokenov in Zastonjski Modeli

Ta dokument pokriva: kateri modeli so dostopni zastonj, kako optimizirati porabo tokenov, in kako nastaviti Hermes za najboljše delovanje.

---

## 1. DASHBOARD ANALIZA (http://127.0.0.1:9119)

### Stanje sej (junij 2026)
- **42 sej skupaj**, 2730 sporočil
- Platforme: TUI (25), cron (6), Telegram (1), CLI (1)
- Modeli v uporabi: `owl-alpha` (večina sej), `step-3.7-flash:free` (default), `nemotron-3-ultra-550b-a55b:free`

### Nous Portal (https://portal.nousresearch.com)
- **237 modelov** dostopnih prek Nous API / OpenRouter
- Registriran dashboard: "surface pro 7" (lokalni OAuth)
- Hermes-4-70B: **$0.05/1M input, $0.20/1M output** — najcenejši frontier model
- Hermes-4-405B: $0.09/1M input, $0.37/1M output

---

## 2. SKILLS IN PLUGINS

### Lokalni skills (~/.hermes/skills-local/)
Večina je **praznih shell map** brez vsebine:

| Skill | Stanje |
|-------|--------|
| `dogfood` | ✅ Aktiven — QA testiranje web appov |
| `yuanbao` | ✅ Aktiven — Yuanbao group @mentions |
| apple, creative, devops, education, email, github, media, mlops, note-taking, productivity, red-teaming, research, smart-home, social-media, software-development, work, data-science, autonomous-ai-agents | ❌ Prazne mape |

### Vgrajeni builtin skills (~/.hermes/skills/)
- `computer-use` — upravljanje namizja brez fokusa
- `dogfood` — enako kot lokalni
- `yuanbao` — enako kot lokalni
- `learning` — vgrajeni learning skill

### Plugins
- `disk-cleanup` — samodejno čiščenje diska
- `hermes-memory-store` — Holographic SQLite memory (aktiven, auto_extract: true)

### ⚡ Akcija: Zapolni prazne skills
Prioritetni skills za ustvariti glede na tvoj workflow:
1. `note-taking/SKILL.md` — Obsidian workflow (hub + koncepti + wikilinki)
2. `education/SKILL.md` — Mehanika/fizika workflow (korak 0, viri, shranjevanje)
3. `research/SKILL.md` — NotebookLM + vault workflow

---

## 3. ZASTONJSKI MODELI — KOMPLETNA MAPA

### Tvoje naročnine
| Naročnina | Vrednost | Modeli |
|-----------|----------|--------|
| Claude Pro | mesečna | claude-sonnet-4-6, claude-opus-4-8, claude-haiku-4-5 |
| Perplexity Student | mesečna | sonar, sonar-pro, sonar-reasoning |
| OpenRouter free | brezplačen | 15+ zastonjskih modelov (glej spodaj) |
| Nous Portal | €20 krediti | 237 modelov, Hermes-4-70B super poceni |

### Najboljši zastonjski modeli na OpenRouter (junij 2026)

| Model | Context | Najboljši za |
|-------|---------|-------------|
| **Owl Alpha** 🥇 | 1.05M | Agentic workloads, tool use, coding — #1 za Hermes |
| **NVIDIA Nemotron Ultra 550B** | 1M | Kompleksno razmišljanje, multi-agent orchestration |
| **Poolside Laguna M.1** | 262K | Coding agent, software engineering |
| **OpenAI gpt-oss-120b** | 131K | Splošno, tool use, structured output |
| **NVIDIA Nemotron Super 120B** | 1M | Hitrost + kakovost, MoE |
| **Gemma 4 31B** | 262K | Multimodal, function calling |
| **Poolside Laguna XS.2** | 262K | Hiter coding agent |

> **Že uporabljaš Owl Alpha in Nemotron Ultra** — odlična izbira!

### Konfiguracija za zastonjske modele

```bash
# V config.yaml — primary zastonjski model
hermes config set model.default openrouter/owl-alpha:free
hermes config set model.provider openrouter

# Ali direktno v config.yaml:
# model:
#   default: owl-alpha
#   provider: openrouter
```

### Claude Pro prek OpenRouter
```yaml
# V config.yaml — uporabi Claude Pro account prek OpenRouter
# Potrebuješ OPENROUTER_API_KEY in da povežeš Claude Pro
model:
  default: anthropic/claude-sonnet-4-6
  provider: openrouter
```

### Nous Portal — najboljša vrednost za €20
```yaml
# Hermes-4-70B — najboljše razmerje cena/kakovost
model:
  default: hermes-4-70b
  provider: nous
# ~€20 = ~80M input tokenov ali ~400 dolgih sej
```

### Priporočena strategija modelov

```
Enostavne naloge (formatiranje, iskanje, kratka vprašanja):
→ stepfun/step-3.7-flash:free (hitr, zastonj)

Agentne naloge, tool use, Obsidian workflow:
→ owl-alpha (zastonj, 1M context, #1 za Hermes)

Kompleksno razmišljanje, matematika, mehanika:
→ nemotron-3-ultra-550b-a55b:free (zastonj, 1M context)

Coding, software:
→ poolside/laguna-m.1:free (zastonj)

Dolge seje z resnim delom (izpiti, projekti):
→ hermes-4-70b prek Nous Portal ($0.05/1M) — iz €20 kredita

Claude Pro (najkompleksnejše):
→ anthropic/claude-sonnet-4-6 prek OpenRouter
```

---

## 4. OPTIMIZACIJA TOKENOV

### Zakaj token optimizacija šteje
Hermes injicira v vsako sporočilo: SOUL.md + MEMORY.md + USER.md + vse AGENTS.md datoteke. To so fiksni tokeni na vsako sporočilo — vsak znak šteje.

### A. Ne prekini prompt cache
```
✅ Ohranjaj stabilno: config files, memory files, model
❌ Ne menjaj modela sredi seje
❌ Ne urejaj SOUL.md med sejo
```
Ko prompt cache deluje → naslednja sporočila so bistveno cenejša.

### B. /compress pred limiti
```
Ko seja postaja dolga → /compress
Stisne conversation history za 50-80%
Ohrani ključni kontekst, izbriše redundantne izmenjave

Preveri porabo: /usage
Analiza zadnjih 30 dni: /insights
```

### C. Ohranjaj MEMORY.md in USER.md kratko
```yaml
# Trenutni limiti (config.yaml):
memory_char_limit: 2200   # MEMORY.md
user_char_limit: 1375     # USER.md
```
Ko se napolni → reci Hermesu: **"počisti memory"** ali **"konsolidiraj"**

### D. delegate_task za paralelno delo
```
Namesto: 3 zaporedna vprašanja v eni seji
Bolje: "Researchiraj tri teme vzporedno z delegate_task"
→ Vsak sub-agent ima svojo izoliran context
→ Glavna seja dobi samo povzetke (bistveno manj tokenov)
```

### E. execute_code za batch operacije
```
Namesto: 10 terminal ukazov enega za drugim
Bolje: "Napiši Python skript ki naredi vse skupaj in ga zaženi"
→ En tool call namesto 10
→ 5-10x manj tokenov
```

### F. AGENTS.md za ponavljajoče instrukce
Ustvari `/home/jaka/Zdaj Pa Zares Obsidian/AGENTS.md` z navodili ki jih vedno ponavljaš:
```markdown
# Obsidian Vault Context
- Vault root: /home/jaka/Zdaj Pa Zares Obsidian/
- Vedno preveri vault pred ustvarjanjem nove note
- Minimalno 5 wikilinkov per nota
- Sekcija ## Povezave obvezna
- Slovenščina, neformalno
```

### G. /model za menjavo modelov sredi seje
```
/model hermes-4-70b    → za kompleksne naloge
/model owl-alpha       → za agentne naloge
/model step-3.7-flash  → za preproste naloge
```

### H. Compression settings (config.yaml)
```yaml
compression:
  enabled: true
  threshold: 0.5      # stisni pri 50% context window
  target_ratio: 0.2   # stisni na 20% originalne dolžine
  protect_last_n: 20  # zadnjih 20 izmenjav ne stisni
  protect_first_n: 3  # prvih 3 ne stisni
```

---

## 5. HERMES OPTIMIZACIJA ZA TVOJ WORKFLOW

### Nastavitve za mehanika/fizika workflow
```yaml
# context_file_max_chars — omeji dolžino AGENTS.md
context_file_max_chars: 5000

# memory char limiti — optimizirano
memory:
  memory_char_limit: 2200
  user_char_limit: 1375
  flush_min_turns: 6    # shrani memory po 6 izmenjavah
  nudge_interval: 10    # opomni na memory po 10 izmenjavah
```

### Skills ki jih moraš ustvariti
```
/save-skill obsidian-mehanika  → za mehanika workflow (korak 0 + 4 viri)
/save-skill obsidian-fizika    → za fizika workflow (7 virov)
/save-skill obsidian-note      → generičen Obsidian note creation
```

### Kronski job optimizacija
Tvoj morning email cron (9:00) teče z `step-3.7-flash:free` — dobra izbira, ker je enostavna naloga.

### Priporočena finalna config.yaml sprememba
```yaml
model:
  default: owl-alpha          # zastonjski, 1M context, najboljši za Hermes
  provider: openrouter

fallback_model:
  provider: nous
  model: hermes-4-70b         # fallback ko owl-alpha ni dostopen

memory:
  provider: holographic       # ✅ že nastavljeno
  flush_min_turns: 6
```

---

## 6. SKILLS HUB — Skills Marketplace

### Kaj je Skills Hub
Skills Hub je vgrajen Hermes skills marketplace. Na voljo so skills iz več virov:

| Vir | Opis |
|-----|------|
| `official` | Uradni Hermes skills (Nous Research) |
| `skills-sh` | Community skills — Anthropic, Vercel, Microsoft, in drugi |
| `github` | Skills iz GitHub repozitorijev |
| `well-known`, `clawhub`, `lobehub`, `browse-sh` | Dodatni viri |

Skills Hub je **že povezan** — nobenih dodatnih tapov ne rabiš. Hermes privzeto išče po vseh virih.

### Ukazi za Skills Hub

```bash
hermes skills search <query>               # išči po vseh virih
hermes skills search <query> --source official   # samo uradni
hermes skills search <query> --source skills-sh  # samo skills.sh
hermes skills inspect <id>                 # predogled pred namestitvijo
hermes skills install <id>                 # namesti skill
hermes skills list                         # seznam nameščenih
hermes skills check                        # preveri posodobitve
hermes skills update                       # posodobi vse skills
hermes skills uninstall <id>               # odstrani skill
hermes skills tap add <repo>               # dodaj lasten GitHub repo kot vir
```

### Skills, ki so zanimivi zate

#### Iz official vira

| Skill | Kategorija | Opis |
|-------|-----------|------|
| `memento-flashcards` | productivity | Spaced-repetition flashcard sistem. Ustvarja kartice iz besedila, kvize iz YouTube transkriptov, adaptivno načrtovanje. **Odlično za izpite.** |
| `concept-diagrams` | creative | Izobraževalni SVG diagrami — flat, minimal, dark-mode aware. Devet semantičnih barvnih ramp. |
| `canvas` | productivity | Canvas LMS integracija — tečaji in naloge. |
| `code-wiki` | software-dev | Wiki docs + Mermaid diagrami za kodo. |
| `one-three-one-rule` | communication | Strukturiran decision-making framework za tehnične odločitve. |
| `excel-author` | finance | Gradi Excel delovne zvezke s formulami, named ranges, sensitivity tables. |
| `drug-discovery` | research | ChEMBL iskanje, Lipinski Ro5, drug-drug interakcije. |

#### Iz skills.sh vira

| Skill | Instalacij | Opis |
|-------|-----------|------|
| `academic-researcher` | 6.353 | Akademsko raziskovanje |
| `study-notes-creator` | 335 | Ustvarjanje študijskih zapiskov |
| `study-plan` | 263 | Študijski načrti (Anthropic) |
| `language-learning` | 370 | Učenje jezika |
| `literature-review-planner` | 117 | Pregled literature |

### Objava lastnih skills

Če želiš svoje skills deliti z drugimi:
1. Ustvari GitHub repo s skillsi v Hermes formatu (`SKILL.md` v kategorijskih mapah)
2. Dodaj ga kot tap: `hermes skills tap add tvoj-gh-username/ime-repa`
3. Drugi uporabniki ga lahko najdejo z `hermes skills search --source github`

Ali pa jih objavi na Skills Hub prek `hermes skills publish <path>`.

---

## 7. QUICK COMMANDS

```bash
hermes /compress              # stisni context
hermes /usage                 # poraba tokenov
hermes /insights              # analiza zadnjih 30 dni
hermes /model owl-alpha       # zamenjaj model
hermes /skills                # preglej skills
hermes config edit            # uredi config.yaml
```

Dodatno za skills:
```bash
hermes skills search <query>  # išči skills marketplace
hermes skills install <id>    # namesti iz huba
hermes skills tap add <repo>  # dodaj GitHub repo
```

---

## Povezave

- [[07_AI/Hermes - Vault Navodila]] — vault navodila za Hermes
- [[CLAUDE]] — AI navodila
- [[07_AI/AI Prompti]] — ready-made prompti
