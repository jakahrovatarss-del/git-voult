---
created: 2026-05-26
tags:
  - note
  - journal
  - cybersecurity
  - privacy
source: YouTube (Zuma channel) — OSINT deep dive video
---

```table-of-contents
title: 
style: nestedList
minLevel: 0
maxWidth: 0
includeLinks: true
hideWhenEmpty: false
debugInConsole: false
```

# OSINT — Odprtokodna Inteligenca

OSINT (Open Source Intelligence) je zbiranje, analiza in dokumentacija javno dostopnih informacij za odgovor na določeno obveščevalno vprašanje. Ni enkratno orodje — je disciplina in sklop tehnik.

> 87% ameriške populacije je enolično identificiranih samo iz: poštna številka + spol + datum rojstva.

Vse kar govoriš, objavljaš, všečkaš, kupiš online pusti **digitalni odtis**. OSINT je umetnost branja tega odtisa.

---

# Kratka Zgodovina

| Obdobje | Prelomnica |
|---------|-----------|
| ~500 BC | Sun Tzu: "Poznaj sovražnika in sebe" — filozofski prednik OSINT |
| 19. stol. | Masovni tisk — prvi "open source" zbiranje brez fizične prisotnosti |
| Zgodnje 1900s | Radio — zbiranje intel iz doma |
| 2. WW | ZDA: Foreign Broadcast Monitoring Service — sistematičen OSINT |
| Hladna vojna | Informacijska vojna → OSINT postane ključen |
| 1990 | CIA officer prvič uradno uporabi termin "OSINT" |
| Danes | Socialni mediji + AI = kdorkoli je OSINT analyst |

---

# Geolokacija iz Fotografij

Ena najpraktičnejših OSINT tehnik: določiti točno lokacijo fotografije samo z vizualno analizo.

## Metoda

1. **Arhitektura, prometni znaki, jezik** → zoži na državo/mesto
2. **Edinstveni elementi** (logotipi, specifični znaki) → obrni iskanje z Google Images / Yandex
3. **Google Street View** → ročno pregledaj kandidatna območja
4. **Satelitski pogled** → potrdi

**Primer iz videa:** Iskanje Bath & Body Works + arhitektura → New York. 10 lokacij v mestu → 1 Street View pregled → točen kotiček v minutah.

## Drevesa in Rastlinje

Celo fotografija v gozdu ni varna — identifikacija drevesnih vrst (npr. Acer platanoides + Prunus serrulata) skupaj s QGIS Python skriptom je locirala fotografijo med 39 možnimi lokacijami.

## Zaključek

Nikoli ne objavljaj fotografij javnih mest brez čiščenja [[EXIF Metadata|metapodatkov]] — geolokacija iz slike traja manj kot 30 minut.

---

# Metapodatki (EXIF)

Vsaka datoteka nosi **metapodatke** — skriti podatki o nastanku datoteke.

Kaj je mogoče najti: GPS koordinate, datum in čas, model naprave, nastavitve kamere, verzija compilerja, pot do datoteke na izvorni napravi.

**Realni primer**: Burger King foot lettuce — fotografija naložena na 4chan → EXIF → GPS koordinate → točen McDonald's in delavec identificiran in odpuščen.

**Epstein video**: metadata razkril, da je "surovi" videoposnetek iz zaporniškega zapora v resnici sestavljen iz dveh ločenih MP4 datotek, montiranih v Adobe Premiere Pro.

**Varnostno pravilo**: za [[OPSEC - digitalna anonimnost|OPSEC]] → ExifTool → očisti pred vsako objavo.

Podrobneje: [[EXIF Metadata]]

---

# Wayback Machine

Splet se nenehno briše in prepisuje. [[Wayback Machine]] arhivira snapshote spletnih strani skozi čas.

Kaj omogoča:
- Snapshote izbrisanih ali spremenjenjih strani
- Video/avdio arhive (novice, YouTube videi)
- Star software in digitalne aplikacije

**OSINT uporaba**: slediti spremembe na spletnih straneh, najti izbrisane objave, preveriti ali je podjetje spremenilo izjavo po incidentu.

**OPSEC pravilo**: preden karkoli objaviš online — razmisli. Internet je trajen zapis. Izbrisana objava je v Wayback Machine.

---

# HUMINT — Človeška Inteligenca

[[HUMINT]] je zbiranje informacij z lažjo in socialno manipulacijo, ne z javnimi podatki. Pogosto kombiniran z OSINT.

- **OSINT** = zbiranje iz javnih virov (pasivno)
- **HUMINT** = zbiranje z direktno interakcijo, pretvarjanjem (aktivno)

**Social engineering** izkoriča osnovno človeško zaupanje. Napadi vedno ciljajo na najšibkejši člen — ki je vedno človek, ne sistem.

**Obramba**: Zdravi skepticizem. Ne razkrivaj informacij, ki niso nujno potrebne. Verifikacija preden zaupanje.

---

# Vzorci in Identifikacija

Največja ranljivost pri ohranjanju anonimnosti: **nezavedni vzorci**.

## Tipi Vzorcev

| Vzorec | Kaj razkriva |
|--------|-------------|
| Časi aktivnosti online | Časovni pas, delovni urnik |
| Sleng, dialekt | Regija, starost, subkultura |
| Tipkarske navade | Edinstvene napake, fraze, struktura stavkov |
| Reused slike ali fraze | Poveže ločene identitete |

**Primer — Ted Kaczynski (Unabomber)**: 17 let anonimen. Ujeli ga ker je brat prepoznal njegovo edinstveno frazeologijo v manifestu: "You can't eat your cake and have it, too" namesto standardnega "You can't have your cake and eat it."

**Praktično**: Dialekt, čas pisanja, ponavljajoče napake — vse to tvori vzorec ki poveže različne identitete.

---

# Dokumentacija

OSINT brez dokumentacije je brezvreden. Zbrani dokazi morajo biti:
- **Ponovljivi** (nekdo drug jih mora moći reproducirati)
- **Sledljivi** (jasna veriga od vira do zaključka)
- **Preverljivi** (ne samo "to sem videl")

**Struktura OSINT dokumenta:**
1. Obveščevalno vprašanje (intelligence question)
2. Hipoteza
3. Zbrani viri + screenshoti + timestamps
4. Časovnica ugotovitev
5. Zaključek z omejitvami

---

# Orodja za Social Media OSINT

| Orodje | Platforma | Kaj dela |
|--------|----------|---------|
| **[[Sherlock]]** | Vsi | Najde vse račune z danim username |
| **SIG** | Instagram | Followerji, tagi, lokacije, vsebine |
| **Crosslink** | LinkedIn | Vse zaposlene v organizaciji |
| **Redfive/Redective** | Reddit | Subredditi, ključne besede, časovni vzorci |
| **OSINT Framework** | Vsi | Zbirka vseh OSINT orodij (kot Steam za OSINT) |
| **Snapchat Map Scraper** | Snapchat | Javne objave po lokaciji |

**OSINT Framework** (osintframework.com) — vstopna točka za vse orodje.

---

# Google Dorking

Napredni iskalni operatorji Google za odkrivanje skritih podatkov iz javno dostopnih strani.

Podrobneje: [[Google Dorking]]

---

# Dark Web OSINT

[[Tor Browser|Tor]] onion protokol (3 hop sistem: entry node → middle node → exit node) omogoča anonimno dostopanje do .onion strani. Dark web OSINT se ne ukvarja s deanonimizacijo uporabnikov — ampak z **varnostnim monitoringom**: sledenje novim ranljivostim, data breachesom, malware kampanjam.

Večina ujemov na darknetu ni iz OSINT analize — ampak iz OPSEC napak, ki povežejo darknet identiteto z realnim življenjem.

---

# Obramba pred OSINT

Najboljša obramba je **minimizacija podatkov**:
- Javna prisotnost na socialnih medijih → minimum
- Ko objaviš fotografijo → [[EXIF Metadata|očisti metapodatke]]
- Razumej: ko naložiš sliko na Instagram/Facebook, ni več tvoja lastnina — je njihova
- Nauči se [[OPSEC - digitalna anonimnost|OPSEC]] — razumeti napad je pogoj za dobro obrambo

---

# Etika

OSINT je legalen — zbiraš javno dostopne podatke. Kar je nezakonito je **uporaba** teh podatkov za:
- Doxing
- Identitetno goljufijo
- Nadlegovanje, izsiljevanje

Etična meja: OSINT za novinarstvo, varnostne raziskave, zakonito preiskovanje = OK. OSINT za škodovanje = ni OK.

---

# Prihodnost — AI in OSINT

AI bo masovno demokratiziral OSINT — povprečen uporabnik bo zmožen doxinga brez tehničnega znanja. Hkrati bo obramba lažja: generiranje milijonov prepričljivih lažnih profilov in podatkov bo oteže-valo validacijo.

**Najtežji del prihodnjega OSINT**: ne zbiranje podatkov — ampak **preverjanje resničnosti** podatkov.

---

# Povezave

- [[OPSEC - digitalna anonimnost]] — obratna stran kovanca: kako se zaščitiš pred OSINT
- [[EXIF Metadata]] — metapodatki in geolokacija
- [[Wayback Machine]] — internet arhiv
- [[Sherlock]] — username OSINT
- [[Google Dorking]] — napredni iskalniki
- [[HUMINT]] — človeška inteligenca
- [[Tor Browser]] — dark web dostop

---

## Viri

- Zuma (YouTube) — *The Most Comprehensive OSINT Video*
