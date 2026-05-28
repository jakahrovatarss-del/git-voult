---
created: 2026-05-29
tags:
  - note
  - cybersecurity
  - privacy
  - OSINT
  - OPSEC
---

# EXIF Metadata

EXIF (Exchangeable Image File Format) so skriti metapodatki, ki jih vsaka naprava avtomatično vstavi v datoteke ob nastanku. Neuvedeni uporabnik ne vidi ničesar — OSINT analitik vidi vse.

---

## Kaj EXIF Vsebuje

| Polje | Primer |
|-------|--------|
| GPS koordinate | 46.0514° N, 14.5060° E |
| Datum in čas nastanka | 2026-05-15 14:32:07 |
| Model naprave | iPhone 15 Pro |
| Nastavitve kamere | ISO 200, f/1.8, 1/500s |
| Verzija softwara | iOS 18.3.1 |
| Pot do datoteke | /Users/jaka/DCIM/photo.jpg |

**Dokumenti** (Word, PDF) vsebujejo: avtor, organizacija, datum urejanja, verzija programa, ime računalnika.

---

## Zakaj je To Problematično

- Objava fotografije s terena → nasprotnik ve točno lokacijo
- Objava dokumenta → razkrije interno infrastrukturo (ime serverja, OS verzija)
- Realni primer: 4chan "Burger King foot lettuce" — EXIF iz fotografije → GPS → McDonald's → delavec identificiran in odpuščen
- Realni primer: Epstein "surovi" videoposnetek — metadata razkril, da gre za montažo iz dveh MP4 datotek (Adobe Premiere Pro)

---

## Orodja za Čiščenje

| Orodje | Namenjeno za | Ukaz / Način |
|--------|-------------|-------------|
| **ExifTool** | Slike, splošno | `exiftool -all= datoteka.jpg` |
| **MAT2** | Večina formatov | CLI ali GUI |
| **FFmpeg** | Video | `ffmpeg -i input.mp4 -map_metadata -1 output.mp4` |
| **ImageMagick** | Batch slike | `mogrify -strip *.jpg` |

### Batch čiščenje celotne mape (ExifTool)

```bash
exiftool -all= -r /pot/do/mape/
```

### Python avtomatizacija

```python
import subprocess, os
for f in os.listdir('.'):
    if f.endswith(('.jpg', '.png', '.pdf')):
        subprocess.run(['exiftool', '-all=', f])
```

---

## Orodja za Branje (OSINT stran)

```bash
exiftool fotografija.jpg          # vse metapodatke
exiftool -GPS* fotografija.jpg    # samo GPS
exiftool -Make -Model foto.jpg    # naprava
```

Online alternativa: **Jeffrey's Exif Viewer** (ne zahteva namestitve).

---

## Pravilo

> Preden karkoli pošlješ ali objaviš → očisti metapodatke. Vedno. Brez izjeme.

Socialna omrežja (Instagram, Facebook, Twitter) večinoma **samodejno stripper EXIF** pri nalaganju — ampak to ni garancija in ne velja za direktno poslane datoteke.

---

## Povezave

- [[OPSEC - digitalna anonimnost]] — EXIF čiščenje kot del OPSEC protokola
- [[OSINT - odprtokodna inteligenca]] — branje EXIF za geolokacijo
