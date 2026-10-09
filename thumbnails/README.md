# Okładki odcinków

Struktura pod szablony HTML/CSS i eksport okładek do PNG w Chromium.
Pierwszy roboczy szablon `hosts-split` umieszcza postacie po bokach i tekst
na środku. Renderer korzysta z lokalnych fontów i Chrome/Chromium przez Playwright.

## Skill dla Copilota

Skill [youtube-cover](../.github/skills/youtube-cover/SKILL.md) obsługuje
składanie i eksport gotowych obrazów. Przykładowe polecenia:

- „Wygeneruj okładkę odcinka 41 z tym tekstem i Piotrkiem po prawej”.
- „Przygotuj wszystkie kombinacje okładki odcinka 41 z podanymi pięcioma liniami”.

Osobny `youtube-thumbnail` nadal służy do propozycji samych tekstów.

## Prawdziwa okładka z bannerem do posta

Skill [episode-promo](../.github/skills/episode-promo/SKILL.md) pobiera
**opublikowaną okładkę odcinka ze strony lub YouTube** i dodaje pod nią
banner „link w komentarzu 👇”. Nie generuje ani nie odtwarza miniatury.
Przykład prośby: „Przygotuj prawdziwą okładkę odcinka 41 z bannerem do posta”.

Po pobraniu źródła do lokalnego pliku:

```bash
python3 thumbnails/render_promo.py thumbnails/output/041/source-youtube.jpg \
  --output thumbnails/output/041/promo-link-comment.png
```

Własne CTA podaj przez `--text "Obejrzyj — link w komentarzu 👇"`.
Okładka zachowuje oryginalny rozmiar i kadr; pasek jest dodawany poniżej,
nie nakładany na obraz. Dla 1280 × 720 wynik ma 1280 × 840 px.
Powstaje również HTML z lokalnym obrazem i fontami. Istniejące PNG/HTML
nie są nadpisywane — dla kolejnego wariantu wybierz nową nazwę.
Źródła i eksporty w `output/` nie trafiają do Git.

## Generowanie podglądu

```bash
python3 -m pip install -r thumbnails/requirements.txt
python3 thumbnails/render.py thumbnails/episodes/demo.json
python3 thumbnails/render.py thumbnails/episodes/demo-gestures.json
python3 thumbnails/render.py thumbnails/episodes/demo-gestures-split.json
```

W `thumbnails/output/` powstają PNG 1280 × 720 oraz małe pliki HTML,
które używają względnych ścieżek do wspólnych zdjęć i fontów zamiast Base64.
Można je otworzyć bez serwera i dostępu do Internetu, ale nie należy przenosić
samego HTML bez zasobów. Przycięte logo jest wspólne w `output/assets/`.
Tekst w konfiguracjach
`demo` jest przykładowy, nie jest tytułem rzeczywistego odcinka.

Renderer używa lokalnego `google-chrome` lub `chromium`. Jeśli ich nie ma,
zainstaluj przeglądarkę Playwright: `python3 -m playwright install chromium`.
Można też wskazać własną: `--browser /ścieżka/do/przeglądarki`.

Konfiguracja odcinka wybiera zdjęcia `people.left` i `people.right`, numer,
linie tekstu z kolorami z konfiguracji marki i rozmiar fontu. `grayscale`
przełącza kolor/czerń i biel; `titleTop` ustawia wysokość bloku tekstu.
Opcjonalne `gapAfter` w pojedynczej linii dodaje przerwę po niej, w pikselach.
W `demo-gestures-split` pierwsza linia jest nad dłonią, a pozostałe pod ręką:
gest wizualnie podkreśla górny fragment zamiast zabierać miejsce całemu tytułowi.
Zbyt szeroki tekst lub tekst wychodzący pod dolny margines powoduje błąd.

## Trzy kompozycje do dopracowania

Konfiguracje `layout-compact`, `layout-palm` i `layout-pointing` są
osobnymi propozycjami kompozycji na tym samym przykładowym tekście.
Renderowanie, np.:

```bash
python3 thumbnails/render.py thumbnails/episodes/layout-compact.json
```

Układ zwarty wykorzystuje większy tekst i mniej pustej przestrzeni.
Układ z dłonią ustawia górną frazę bezpośrednio nad gestem.
Układ wskazujący ustawia wyróżnione słowo w kierunku palca,
a pozostałe linie przesuwa, aby nie konkurowały z ręką.
Rozmiary 88–96 w tych propozycjach są eksperymentalne,
większe od początkowego rozmiaru 72–80 z Canvy.

`headCenters` ustawia poziome pozycje głów bez zmiany ich wyrównania w pionie.
`titleCenterX` i `titleWidth` kontrolują obszar tekstu.
Poszczególne linie mogą mieć własne `fontSize` i przesunięcie `offsetX`.
Generator kombinacji korzysta z tych trzech kompozycji i odbija układ tekstu
wraz ze zmianą strony gestu.

## Wszystkie kombinacje poz

```bash
python3 thumbnails/render_combinations.py
```

Bez argumentów używa demonstracyjnego tekstu i numeru 40.
Dla rzeczywistego odcinka podaj konfigurację:

```bash
python3 thumbnails/render_combinations.py \
  --config thumbnails/episodes/041.json \
  --output thumbnails/output/041/combinations
```

Plik wskazany przez `--config` musi zawierać `episode` i od jednej do sześciu
`lines`; może też ustawić `grayscale`. Zachowujemy słowa, emoji i kolory
podanych linii. Konfiguracje wygenerowanych wariantów trafiają do
`episodes/combinations/<nazwa-konfiguracji>/`, bez nadpisywania innych odcinków.
Renderer zachowuje również wielokrotne spacje wewnątrz linii tekstu.

Generuje wszystkie pary poz w obu ustawieniach stron na podstawie metadanych.
Obecnie to 24 warianty: 4 pozy Piotrka × 3 pozy Kajetana × 2 ustawienia stron.
Konfiguracje z przykładowym tekstem są w `episodes/combinations/`.
Galeria do porównania: `output/combinations/index.html`; zbiorczy PNG:
`output/combinations/contact-sheet.png`. Każda okładka ma osobny PNG i HTML.

Metadane `gesture` rozróżniają dłoń (`palm`) i wskazywanie palcem (`point`).
Układ bez gestów jest zwarty, dłoń podpiera górną frazę, a palec wskazuje
wyróżnione słowo. Jeśli obie pozy mają gest, używany jest układ z dłonią.
Emoji korzystają z pełnego lokalnego Noto Color Emoji, z licencją OFL:
nie ograniczamy zestawu do ⚡ i 🤦‍♂️. Font ma około 24 MB, ale istnieje tylko
w jednym wspólnym pliku, a nie w każdym HTML.

## Wyrównanie głów

Punkty odniesienia dla każdej pozy są w `assets/people/portraits.json`:
`headTop` (czubek głowy), `headCenterX` i `eyeY` (wysokość oczu), w pikselach
przygotowanego PNG. Są skalibrowane ręcznie dla obecnych zdjęć.

Renderer skaluje postacie do jednakowej odległości czubek głowy–oczy
(`eyeOffset`) i ustawia czubki głów na wspólnej wysokości (`headTop`
w konfiguracji odcinka). Szerokość zdjęcia i wyciągnięte ręce nie wpływają
na skalowanie. Przy wymianie zdjęcia lub zmianie przycięcia trzeba ponownie
skalibrować jego punkty odniesienia.

## Gdzie wgrać eksporty z Canvy

Wgraj osobne pliki do `thumbnails/assets/people/source/`.
Obecnie są cztery pozy Piotrka i trzy Kajetana. Nazwy wskazują stronę okładki,
na której używamy oryginału bez odbicia, np.:

```text
kajetan-01-prawo.png
piotrek-01-lewo.png
```

Można zastąpić numery opisem pozy, np. `kajetan-klawiatura.png`.
Każdy plik powinien zawierać jedną kolorową postać, bez filtra, obrysu,
cienia, tekstu ani logo.

- Projekt w Canvie: 1600 × 1600 px, z zachowaniem proporcji postaci.
- Kadr do pasa, ale z całymi dłońmi i rekwizytami.
- Minimum 40 px marginesu wokół postaci; nadmiar pustego miejsca można przyciąć później.
- Eksport PNG, najlepiej z przezroczystym tłem.
- Jeśli przezroczysty eksport jest niedostępny: jednolite tło `#FF00FF`,
  o ile tego koloru nie ma na postaci ani rekwizytach.

Zachowujemy oryginały w `source/`. Przygotowane wersje z przezroczystym tłem
i przyciętym płótnem trafią do `thumbnails/assets/people/ready/`.
Obróbkę magentowego tła wykonuje skrypt:

```bash
python3 -m pip install -r thumbnails/requirements.txt
python3 thumbnails/prepare_people.py
```

Skrypt usuwa jednolitą magentę, rekonstruuje półprzezroczyste krawędzie
i przycina płótno z marginesem 40 px. Nie rekonstruuje brakujących fragmentów
zdjęcia, np. ubytku przy dłoni. Oryginały pozostają bez zmian.

## Strona i odbicie postaci

Eksportuj każdą pozę tylko raz, w jej oryginalnej orientacji.
Nie trzeba przygotowywać osobnych plików na lewą i prawą stronę.
Konfiguracja określa stronę (`left` lub `right`).
Renderer dobiera odbicie na podstawie domyślnej strony zapisanej w metadanych
i stosuje je do samej postaci przez CSS `scaleX(-1)`,
bez odwracania tekstu i logo okładki.

Dobieramy orientację tak, aby spojrzenie lub gest pasowały do kompozycji,
zwykle w kierunku tekstu na środku. Wszystkie obecne zdjęcia można
odbijać; odwrócone napisy na koszulkach są akceptowane.

## Wygląd marki

Ustawienia znajdują się w `assets/branding/brand.json`.
Ścieżki do zasobów w tym pliku są względne wobec katalogu głównego repozytorium.

- Tytuł: Libre Franklin, rozmiar około 72–80.
- Numer odcinka: Open Sans, rozmiar 44.4, kolor biały `#ffffff`.
- Lokalne fonty w `assets/fonts/` pochodzą z Google Fonts; obok są licencje OFL.
- Rozmiary pochodzą z Canvy; dokładne dopasowanie do CSS wymaga porównania ze wzorcem.
- Główny kolor tekstu: `#f9fa30`; drugi kolor: `#ffffff`.
- Wyróżnienia: `#ff3131`.
- Obrys postaci: `#2ebef7`.
- Logo: istniejący `img/bdc-logo-backgroundless.png`, bez kopiowania.
- Tło: `assets/backgrounds/background.png`.

## Struktura

```text
thumbnails/
  assets/
    people/
      source/       oryginalne eksporty z Canvy
      ready/        postacie przygotowane do renderowania
    backgrounds/    tła i tekstury
    branding/       ustawienia marki; logo jest używane z img/
    fonts/          lokalne fonty z odpowiednimi licencjami
  templates/        szablony HTML/CSS
  episodes/         konfiguracje JSON odcinków
  output/           wygenerowane okładki, ignorowane przez Git
```

Docelowa okładka: 1280 × 720 px. Układ i efekty należą do szablonu;
tekst, numer odcinka i wybór poz należą do konfiguracji odcinka.
Obecne pliki `promo/poses-2.png` i `promo/poses-green.png` pozostają
wzorcami wyglądu i układu.
