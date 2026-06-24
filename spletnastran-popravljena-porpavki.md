# ARSS Spletna Stran — Analiza in Popravki

**Datum:** 2026-06-24
**Vir:** koda repozitorija `spletna-stran-popravljena` (gh-pages branch)
**Pogled:** https://jakahrovatarss-del.github.io/spletna-stran-popravljena/

---

## 1. Kritične tehnične napake (fixaj takoj)

### 1.1 Malformed canonical/hreflang tagi (vse strani)
- `<link rel="canonical" href=".../">` — manjka zaključni `>` (odprt tag)
- `<link rel="alternate" hreflang="x-default" href=".../">>` — stray `>` na koncu
- Posledica: brskalnik/crawler zavrne hreflang="sl" ker ga vzame kot del canonical taga
- **Fix:** zaključi canonical z `>`, odstrani stray `>` na x-default

### 1.2 github.io domena namesto arss.si
- Vsi canonical, OG, sitemap, schema URL-ji kažejo na `jakahrovatarss-del.github.io/spletna-stran-popravljena/`
- Problema: ni domenne avtoriteti, URL vsebuje "popravljena" (slab zaupanje), arss.si ne dobi SEO equity
- **Fix:** migracija na arss.si custom domain (CNAME + DNS), 301 redirect, posodobi vse canonicale/sitemap/OG/schema

### 1.3 Render-blocking / velike slike
- `hero-bg.png` je 611 KB (obstaja `.webp` 83 KB — uporabi tega)
- `arss-comparison.png` je 665 KB
- `portal-overlay.webp` je 1024×1024 (LCP image)
- **Fix:** stisni/resize slike, da se .webp servira, ne .png

---

## 2. Vsebinske vrzeli (SEO)

### 2.1 Skrita primerjava
- `ARSS-2026-COMPARISON-TABLE-DEMO.html` obstaja, je Disallowed v robots.txt in brez linkov
- Naslov je "…Predlog" (draft) z emoji 🚀 — NI production-ready
- **Fix:** pusti blocked (je draft), ampak ustvari pravo "ARSS vs alternative" stran

### 2.2 Ni bloga / edukacijske vsebine
- 10 komercialnih strani, nobene informativne
- Manjkajo članki: "kako zaznati puščanje vode", "NB-IoT vs LoRaWAN", "koliko stane pametni vodomer"
- **Fix:** začni s 3–4 slovenskimi how-to članki

### 2.3 Samo 2 referenčni case study
- Obstajata `referenca-komunala` in `referenca-vecstanovanjski`
- **Fix:** razširi v "Reference" hub z kvantificiranimi rezultati (voda, puščanja, €)

---

## 3. UX popravki (konverzija)

### 3.1 Hero CTA ne ustreza obliki
- Hero gumb "Pošlji sliko vodomera" → navigira na `gospodinjstva.html#poslji-sliko` (dodatni page load)
- Homepage oblika spodaj nima file upload — je samo name/email/message
- **Fix:** inline photo-upload form v hero (ali modal), zmanjšaj required polja

### 3.2 Hero ima dve nasprotujoči naslovnici
- H1 "Pametno upravljanje z vodo" + H2 "Pošlji sliko vodomera" — dva focal points
- **Fix:** ali device image ali secondary headline se zmanjša, en CTA naj bo dominanten

### 3.3 Prazen footer
- Samo copyright vrstica
- **Fix:** dodaj naslov/telefon, link do reference, privacy/cookie policy, segment strani

---

## 4. Prioritiziran action plan

| # | Action | Effort | Impact |
|---|--------|--------|--------|
| 1 | Fix malformed canonical/hreflang na vseh straneh | XS | High |
| 2 | Migracija na arss.si custom domain | M | Very High |
| 3 | Stisni slike (hero, comparison) | S | Medium |
| 4 | Photo-upload form na homepage | S | High |
| 5 | Obogatitev footer (trust + linki) | S | Medium |
| 6 | 3–4 blog članka | M | Medium |

---

## 5. Kar je že dobro ✅

- Situacijska IA (gospodinjstva / vikendi / večstanovanjske / kmetije / industrija)
- Een dominanten CTA z jasno vrednostjo ("24h, brez klicanja, brez obveznosti")
- Skip-nav, :focus-visible, aria-hidden, breadcrumb markup, width/height na slikah (CLS)
- JSON-LD (Organization/LocalBusiness + FAQ + Speakable)
- Async fonti, inline critical CSS, lazy-loading
