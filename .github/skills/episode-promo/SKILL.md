---
name: episode-promo
description: "Dodaje banner CTA do prawdziwej okładki odcinka."
version: 0.1.0
author: Piotrek Stapp, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [betterdevclub, promo, cover, html, social]
---

# Okładka odcinka z bannerem do posta

Używaj, gdy użytkownik chce promować odcinek obrazem z dolnym bannerem
„link w komentarzu 👇” lub własnym CTA. Wynikiem ma być gotowy PNG
oraz lokalny podgląd HTML, nie sam projekt ani instrukcje.
Wszystkie ścieżki są względem katalogu głównego repozytorium.

## Źródło — zawsze prawdziwa, opublikowana okładka

1. Ustal numer odcinka i odczytaj jego wpis w `episodes.json` przez `read_file`.
   Użyj `youtubeId` lub identyfikatora z `platforms.youtube`; nie zgaduj ID.
   Jeśli użytkownik wskazał konkretną opublikowaną okładkę, wybierz ją.
2. Pobierz istniejący obraz ze strony odcinka albo YouTube. Dla YouTube
   preferuj `https://i.ytimg.com/vi/<youtubeId>/maxresdefault.jpg`.
   Zapisz go w `thumbnails/output/<numer>/source-youtube.jpg`.
   Przykład przez `terminal`, po utworzeniu katalogu docelowego:
   ```bash
   curl --fail --location --max-time 30 \
     https://i.ytimg.com/vi/HertC6CwddA/maxresdefault.jpg \
     --output thumbnails/output/041/source-youtube.jpg
   ```
   To przykład dla #41, nie domyślny odcinek.
3. Obejrzyj pobrany obraz przez `vision_analyze` i sprawdź rozmiar przez Pillow.
   Potwierdź, że to okładka właściwego odcinka, nie placeholder YouTube.
   HTTP 200 nie wystarcza. Przy braku maxres spróbuj `sddefault.jpg`, potem
   `hqdefault.jpg`, albo obrazu ze strony; nie usuwaj ich marginesów.
   Jeśli nie możesz uzyskać prawdziwego obrazu, zgłoś blokadę i poproś o plik.
4. **Nie generuj ani nie odtwarzaj okładki.** Nie używaj `youtube-cover`,
   `render.py`, konfiguracji poz ani generatora AI do tworzenia zastępczej
   miniatury. Nie zmieniaj napisów, twarzy, numeru, kolorów ani kadru źródła.

## Render HTML/CSS

Zależności są istniejące: Pillow i Playwright z `thumbnails/requirements.txt`,
Chrome/Chromium albo Chromium Playwright. Użyj środowiska Python repozytorium;
nie omijaj PEP 668. Przy braku przeglądarki zainstaluj Chromium Playwright
w tym środowisku przez `terminal` (`python3 -m playwright install chromium`).

Uruchom przez `terminal`:

```bash
python3 thumbnails/render_promo.py thumbnails/output/041/source-youtube.jpg \
  --output thumbnails/output/041/promo-link-comment.png
```

Własny tekst (zachowaj go dosłownie, wraz z emoji i wielkością liter):

```bash
python3 thumbnails/render_promo.py thumbnails/output/041/source-youtube.jpg \
  --output thumbnails/output/041/promo-custom.png \
  --text "Obejrzyj odcinek — link w komentarzu 👇"
```

Opcjonalne `--browser` wskazuje lokalny Chrome/Chromium.
Domyślnie przygotuj jeden obraz. Nie dopisuj obietnic ani mocniejszego CTA
bez prośby użytkownika. Nie zmieniaj jego tekstu po cichu.

## Wygląd i ograniczenia

- Obraz źródłowy pozostaje w oryginalnych wymiarach, bez rozciągania,
  przycinania, retuszu ani bannera nakładanego na tytuł lub twarze.
- Banner jest **dodany pod okładką**: żółty kolor marki z `brand.json`,
  czarny napis Libre Franklin, lokalny pełny Noto Color Emoji.
- Okładka 1280 × 720 daje PNG **1280 × 840**; banner ma 120 px.
  Dla innych wymiarów jego wysokość i typografia skalują się z szerokością.
- HTML korzysta z istniejącego obrazu i lokalnych fontów, bez Base64 i sieci.
  Nie przenoś samego HTML bez źródła i fontów.
- Renderer odrzuca przepełniony tekst. Zapytaj o skrócenie własnego CTA,
  nie usuwaj słów samodzielnie.
- Nie nadpisuj istniejących PNG/HTML; dla kolejnego wariantu wybierz nową nazwę.
- Nie publikuj posta, nie zmieniaj `episodes.json` i nie commituj eksportów
  przy prośbie o sam obraz. `thumbnails/output/` jest ignorowany przez Git.

## Weryfikacja i wynik

1. Obejrzyj PNG przez `vision_analyze`: pełna prawdziwa okładka, czytelny
   banner pod nią, poprawne emoji, brak obcięcia.
2. Sprawdź wymiary oraz zachowanie źródła: dla PNG porównaj piksele górnej
   części; dla JPEG dopuszczalna jest drobna różnica dekodowania kolorów.
3. Podaj gotowy obraz (w Discordzie `MEDIA:/absolutna/ścieżka/do/pliku.png`),
   numer odcinka i źródło okładki. Nie zastępuj załącznika instrukcjami.

Testy renderera przez `terminal`:
`python3 -m unittest discover -s thumbnails -p 'test_render*.py' -v`.
