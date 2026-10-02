---
name: youtube-cover
description: "Tworzy i eksportuje gotowe okładki oraz miniatury YouTube Better Dev Club do PNG za pomocą szablonów HTML/CSS i lokalnego Chrome. Używaj, gdy użytkownik chce zobaczyć okładkę, wygenerować obraz, porównać pozy lub otrzymać zestaw kombinacji. Do samych propozycji tekstów służy osobny skill youtube-thumbnail."
---

# Generowanie okładek Better Dev Club

Wykonuj generowanie obrazów, nie tylko opisuj projekt. Używaj istniejącego
renderera i zasobów w `thumbnails/`; nie twórz nowego generatora ani osobnego
HTML z ręcznie osadzonymi zdjęciami.

Wszystkie poniższe ścieżki i komendy są względem katalogu głównego repozytorium.

## 1. Ustal treść i zakres

- Jeśli użytkownik podaje tekst, zachowaj jego słowa, emoji, kolejność i podział
  na linie. Renderer wyświetla tekst wersalikami.
- Jeśli chce propozycje tekstów, użyj `youtube-thumbnail`. Nie stosuj jego
  reguły pięciu propozycji do liczby generowanych obrazów.
- Ustal numer odcinka z prośby lub odpowiedniego wpisu w `episodes.json`.
  Jeśli jest niejasny, zapytaj; nie kopiuj bezmyślnie numeru 40 z przykładów.
- Domyślnie przygotuj jedną zwartą okładkę. Wszystkie kombinacje generuj,
  gdy użytkownik prosi o warianty wszystkich poz lub zestaw porównawczy.
- Nie publikuj obrazów, nie zmieniaj `episodes.json` i nie twórz commita,
  jeśli użytkownik prosi tylko o okładkę.

## 2. Wczytaj zasoby i wybierz kompozycję

Przeczytaj:

- `thumbnails/README.md`;
- `thumbnails/assets/branding/brand.json`;
- `thumbnails/assets/people/portraits.json`;
- odpowiedni przykład `thumbnails/episodes/layout-compact.json`,
  `layout-palm.json` albo `layout-pointing.json`.

Wybieraj tylko pozy obecne w metadanych i `assets/people/ready/`.
Nie zakładaj stałej liczby zdjęć.

| Kompozycja | Zastosowanie |
| --- | --- |
| `compact` | Bez gestów; największy, zwarty blok tekstu. Wariant domyślny. |
| `palm` | Wyciągnięta dłoń podpiera frazę nad ręką, dalsze linie są pod nią. |
| `pointing` | Wyróżnione słowo znajduje się w kierunku wskazującego palca. |

Generator kombinacji dobiera kompozycję z metadanych `gesture` i odbija
pozycje tekstu po zmianie strony gestu. Przy pojedynczej okładce zrób to samo:
nie wystarczy odbić zdjęcia, pozostawiając tekst w starej pozycji.

Zachowaj podobną wysokość i wielkość głów. `headTop` i `eyeOffset` sterują
wyrównaniem; `headCenters` pozycją poziomą. Nigdy nie skaluj postaci do
jednakowej szerokości plików PNG.

Zachowaj markę z `brand.json`: Libre Franklin dla tytułu, Open Sans dla numeru,
biały numer, żółty/biały/czerwony tekst i niebieski obrys postaci.
Nie zmieniaj wspólnego brandingu tylko dla jednego odcinka.

## 3. Zapisz konfigurację odcinka

Utwórz `thumbnails/episodes/<numer>.json`, kopiując wybraną kompozycję
i zastępując numer, tekst oraz wybrane pozy. Dla kilku propozycji użyj
osobnych nazw, np. `041-a.json` i `041-b.json`. Nie nadpisuj istniejącej
konfiguracji z inną treścią bez uzgodnienia.

Minimalny przykład treści dla zestawu wszystkich poz:

```json
{
  "episode": 41,
  "grayscale": true,
  "lines": [
    { "text": "TWÓJ TYTUŁ", "color": "primary" },
    { "text": "DRUGA LINIA", "color": "text" },
    { "text": "KONTRAST 🚀", "color": "highlight" }
  ]
}
```

Dla pojedynczego renderu konfiguracja musi dodatkowo zawierać
`people.left` i `people.right`; skopiuj je oraz ustawienia kompozycji
z istniejącego przykładu.

Kolory linii są nazwami z `brand.json`, nie dowolnymi nazwami CSS.
Pozycją tekstu sterują `titleTop`, `titleCenterX` i `titleWidth`.
Pojedyncza linia może mieć `fontSize`, `offsetX` i `gapAfter`.
Nie dodawaj pustych linii w celu zrobienia miejsca na rękę.

## 4. Wygeneruj obrazy

Pojedyncza okładka:

```bash
python3 thumbnails/render.py thumbnails/episodes/041.json \
  --output thumbnails/output/041/cover.png
```

Wszystkie kombinacje z tekstem i numerem użytkownika:

```bash
python3 thumbnails/render_combinations.py \
  --config thumbnails/episodes/041.json \
  --output thumbnails/output/041/combinations
```

Zestaw obejmuje każdą parę Piotrek–Kajetan w obu ustawieniach stron.
Generator zapisuje też konfiguracje w
`thumbnails/episodes/combinations/<nazwa-konfiguracji>/`.
Bez `--config` generuje wyłącznie demonstracyjny tekst i numer 40 —
nie używaj tego trybu do rzeczywistego odcinka.

Jeśli wybrana komenda zgłasza brak zależności, użyj
`thumbnails/requirements.txt` w środowisku Python repozytorium.
Nie instaluj niczego bez potrzeby ani nie omijaj ograniczeń systemowego pip.
Gdy brak Chrome/Chromium, użyj `python3 -m playwright install chromium`;
renderer obsługuje też `--browser`.

## 5. Sprawdź efekt, nie tylko kod zakończenia

- Obejrzyj PNG; przy zestawie obejrzyj `contact-sheet.png` i wybrane pełne
  okładki reprezentujące każdą kompozycję.
- Sprawdź czytelność w małym podglądzie, brak kolizji tekstu z twarzami
  i dłońmi oraz sens gestu. Nie nazywaj wskazującą pozy, która wskazuje
  w pustą przestrzeń.
- Wynik ma mieć dokładnie 1280 × 720 px; głowy mają być wyrównane.
- Nie ignoruj błędów ładowania zasobów ani przepełnienia tekstu.
  Popraw pozycję lub rozmiar i uruchom render ponownie.
  Nie usuwaj słów ani emoji użytkownika bez zgody.
- HTML ma korzystać ze wspólnych lokalnych plików; nie osadzaj Base64.
  Zachowaj pełny Noto Color Emoji, nie ograniczaj fontu do bieżących symboli.
- Nie czyść całego `output` bez wyraźnej prośby. Przy żądanym czyszczeniu
  zachowaj `output/.gitignore`; nie usuwaj zdjęć, fontów ani konfiguracji.

## Nowe zdjęcia

Oryginały trafiają do `thumbnails/assets/people/source/`, a przygotowane PNG
do `ready/`. Używaj istniejącego `prepare_people.py`; nie nadpisuj oryginałów.
Po dodaniu lub zmianie przycięcia zdjęcia skalibruj w `portraits.json`
`headTop`, `headCenterX` i `eyeY` na podstawie rzeczywistego obrazu.
`side` oznacza stronę bez odbicia. `gesture` dodawaj tylko dla rzeczywistego
gestu (`palm` albo `point`). Nie zgaduj punktów głowy z samej nazwy pliku.

## Wynik dla użytkownika

Podaj link do gotowego PNG, a dla zestawu do `index.html` i
`contact-sheet.png`. Krótko wskaż najlepszy wariant lub rzeczywiste ograniczenie.
Nie zastępuj gotowych obrazów listą instrukcji do samodzielnego wykonania.
