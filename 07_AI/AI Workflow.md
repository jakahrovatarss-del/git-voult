---
created: 2026-05-25
tags:
  - AI
  - workflow
  - system
---

# 🤖 AI Workflow

Kako delati z AI v tem vaultu. Vse kar AI zna in kam spada.

---

## Kaj AI Naredi pri Novem Zapisku

Ko prineseš surov zapis, AI:
1. Prepozna glavne koncepte
2. Predlaga `[[wikilinks]]` za vse pomembne pojme
3. Preveri, ali tema spada v [[05_SCHOOL/School Hub|School]], [[06_LEARNING/Learning Hub|Learning]], [[03_PROJECTS/Projects Hub|Projects]] ali [[04_RESOURCES/Resources Hub|Resources]]
4. Predlaga pravo mapo
5. Predlaga naslednji korak

---

## Prompti — Šola

Kopiraj in prilagodi:

```
Pretvori ta surov zapis v pregledno note za [[PREDMET]].
Izlušči glavne koncepte in jih poveži z obstoječimi notami.
Naredi povzetek za test.
Naredi 10 vprašanj za samopreverjanje.
Katere note bi morale biti linkane sem?
```

```
Naredi exam review sheet za [[PREDMET]] — [[TEMA]].
Poveži vse ključne koncepte z obstoječimi notami v vaultu.
```

---

## Prompti — Solo Učenje

```
Razbij temo [[TEMA]] na učne module.
Naredi [[Study Plan]] za 14 dni.
Kateri koncepti morajo biti znani prej?
Predlagaj mini projekt za [[Projekt]] utrditev.
Pretvori temo v [[Skill Tree]].
```

```
Analiziraj moje zapiske za [[TEMA]].
Kje so luknje v razumevanju?
Generiraj self-test vprašanja po [[Feynmanova Tehnika|Feynmanovi tehniki]].
```

---

## Prompti — Viri

```
Povzemi ta članek/video v uporabno noto.
Izpiši actionable ideje.
Poveži vir z obstoječimi koncepti v vaultu.
Katere [[Projekt|projekte]] ali naloge podpira ta vir?
```

---

## AI Naloge v Vaultu

AI lahko pomaga pri:
- preoblikovanju surovih zapiskov v strukturirane note
- iskanju manjkajočih [[wikilinks]] v obstoječih notah
- ustvarjanju indeksnih not in dashboardov
- načrtovanju učenja ([[Study Plan]], [[Skill Tree]])
- pretvorbi virov v povzetke
- generiranju vprašanj in nalog
- pripravi recapov za test
- pretvorbi projektov v učne artefakte

---

## Kako Povedati AI Kaj Hočeš

Dovolj je reči:
- "Naredi noto za [[KONCEPT]]" → AI ustvari strukturirano concept noto z linki
- "Kaj manjka v [[NOTA]]?" → AI preveri povezave in strukturo
- "Povezi [[A]] in [[B]]" → AI poišče skupne koncepte in predlaga evergreen
- "Pripravi me na izpit iz [[PREDMET]]" → AI naredi review sheet

---

## Pravila za AI pri Linkanju

Iz [[01_SYSTEM/Vault Pravila|Vault Pravila]]:
- Vsak nov koncept → `[[wikilink]]`
- Vsaka nota → vsaj 2–5 relevantnih povezav
- Šolske note → poveži s `[[Predmet]]`, `[[Izpit]]`, `[[Vir]]`
- Learning note → poveži s `[[Tema]]`, `[[Skill Tree]]`, `[[Study Plan]]`, `[[Refleksija]]`

---

## Datoteke za AI Kontekst

Ko delaš z AI, mu daj v kontekst:
- [[CLAUDE]] — osnovna navodila
- [[01_SYSTEM/Vault Pravila|Vault Pravila]] — struktura in pravila
- Relevantne obstoječe note za temo

---

## Povezave

- [[CLAUDE]] — AI navodila
- [[07_AI/AI Prompti|AI Prompti]] — zbirka promptov
- [[01_SYSTEM/Vault Pravila|Vault Pravila]]
- [[09_DASHBOARDS/Dashboard|Dashboard]]
