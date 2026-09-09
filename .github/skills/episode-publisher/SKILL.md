---
name: episode-publisher
description: Kompleksowy workflow publikacji nowego odcinka podcastu Better Dev Club. Wykonuje po kolei: 1) korektę transkrypcji (nazwy własne, tech stack), 2) dodanie wpisu do episodes.json (tytuł, agenda, opis, tagi, resources), 3) propozycje tekstów na miniaturkę YouTube (konkretne + ogólne motywy). Używaj, gdy użytkownik prosi o przygotowanie, obrobienie, publikację odcinka lub przetworzenie nowej transkrypcji.
---

# Workflow Publikacji Nowego Odcinka (Better Dev Club)

Ten skill automatyzuje kompletny proces przygotowania odcinka na podstawie pliku transkrypcji (`transcriptions/XXX.json` lub `transcriptions/raw/XXX.json`).

---

## Krok 1: Korekta transkrypcji JSON (`transcriptions/XXX.json`)

1. **Wczytaj plik transkrypcji:**
   - Jeśli plik jest w `transcriptions/raw/XXX.json`, utwórz lub zaktualizuj wersję docelową w `transcriptions/XXX.json`.
2. **Popraw błędy fonetyczne, techniczne i nazwy własne:**
   - **Modele i narzędzia AI:** `OpenAI`, `ChatGPT`, `Claude`, `Anthropic`, `Cursor`, `xAI`, `DeepSeek`, `Qwen`, `Gemini`, `Copilot`, `MCP (Model Context Protocol)`, `Hugging Face`, `Midjourney`, `DALL-E`, `Imagen`.
   - **Sprzęt i technologie:** `Mac Studio`, `Mac Mini`, `Apple Silicon`, `Nvidia`, `RTX 5090`, `.NET`, `C#`, `Polly`, `GitHub`, `RAM`, `LLM / LLM-y`.
   - **Słownictwo techniczne i żargon:** `hurtowo`, `stanieje`, `infrę`, `offtopa`, `release'y`, `harnessy`, `Maintenance Fee`, `wrapper`, `storage'owy`, `prompt / prompcie`.
   - **Prowadzący i marka:** `Kajetan Duszyński` (Kajtek), `Piotrek Stapp`, `Better Dev Club`.
   - **Interpunkcja i stylistyka:** Rozbijanie sklejonych zdań, poprawne wielkie litery, brakujące przecinki.

---

## Krok 2: Aktualizacja bazy odcinków (`episodes.json`)

Dodaj nowy obiekt na początku tablicy w `episodes.json` zgodnie z poniższą strukturą:

```json
{
  "id": <numer_odcinka_jako_int>,
  "num": "<numer_odcinka_string>",
  "title": "Better Dev Club #<nr> - <Chwytliwy, konkretny tytuł z 2-3 głównymi tematami>",
  "date": "YYYY-MM-DD",
  "duration": "MM:SS",
  "desc": "Dwuparagrafowy, wciągający opis. Pierwszy akapit nakreśla główny wątek i kontekst. Drugi akapit streszcza pozostałe tematy, dyskusje i wnioski.",
  "agenda": [
    "00:00 - [Nazwa Sekcji] Krótki opis...",
    "01:23 - [Kolejny Temat] Opis..."
  ],
  "tags": [
    "betterdevclub",
    "ai",
    "<kluczowe-tagi-z-odcinka>"
  ],
  "platforms": {
    "youtube": "https://www.youtube.com/@BetterDevClub",
    "spotify": "https://open.spotify.com/show/2vFp58L1h9l5jP6bZ5mH3j",
    "apple": "https://podcasts.apple.com/us/podcast/better-dev-club/id1848840540"
  },
  "resources": [
    {
      "type": "link",
      "url": "https://...",
      "label": "Nazwa źródła",
      "description": "Krótki opis linku"
    }
  ],
  "youtubeId": ""
}
```

- **Agenda:** Wyciągnij kluczowe momenty i tematy bezpośrednio ze znaczników czasu `time` w transkrypcji.
- **Data:** Wyznacz kolejny czwartek lub bieżącą datę publikacji.

---

## Krok 3: Generowanie propozycji tekstów na miniaturkę YouTube

Wygeneruj teksty na okładkę w dwóch kategoriach (zgodnie z regułami `.github/skills/youtube-thumbnail/SKILL.md`):

### Kategoria A: Konkretne haczyki z odcinka (3-4 warianty)
- Oparte o najmocniejsze newsy, liczby i kontrasty (np. `90K PLN`, `$13B`, `VS`, konkrety technologiczne).

### Kategoria B: Wspólny motyw / Haczyk ogólny (3-4 warianty)
- Synteza tematu przewodniego lub prowokacyjne pytanie (np. powrót po wakacjach, koniec darmowych narzędzi, szaleństwo na rynku).

### Format miniaturki:
- Krótkie linie (1-3 słowa), ALL CAPS.
- Łamanie na 3-5 wierszy.
- Wymowne emotikony na końcu wierszy (🔥, 💸, 🤯, 🛑, 🚀, 🤖).
- Wyróżnienie blokowe ze znacznikami `---`.

---

## Podsumowanie dla użytkownika
Na koniec wyświetl użytkownikowi:
1. Status wykonania korekty transkrypcji.
2. Podgląd dodanego wpisu w `episodes.json` (tytuł, data, wygenerowana agenda).
3. Zestaw gotowych propozycji na okładkę YT.
