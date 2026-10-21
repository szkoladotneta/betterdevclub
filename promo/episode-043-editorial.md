# Better Dev Club #43 — pakiet do akceptacji

Status: nagrany odcinek, szkic redakcyjny. Bez publikacji. Data **2026-10-22** i długość **38:01** są robocze; długość pochodzi z końca ASR po normalizacji, a nie z finalnego montażu. Linki platform pozostają puste.

## Tytuł rekomendowany

**30 tys. zmian dziennie. Czy potrzebujesz następcy Gita? | Better Dev Club #43**

Alternatywy:
- **Anthropic zastępuje Gita. Ty też powinieneś? | Better Dev Club #43**
- **AI napisze ci narzędzie. Ale kto je utrzyma? | Better Dev Club #43**

Pierwszy tytuł opakowuje dominującą część rozmowy. Trzeci dotyczy drugiej części — lepszy, jeśli montaż przesunie nacisk na wybór własny kod/open source. To propozycje, nie obietnica wzrostu CTR.

## Obietnica dla widza

Dla programisty lub lidera zespołu, który widzi kolejne historie o skali agentów AI: rozróżnić realne wąskie gardło od pokusy kopiowania infrastruktury producenta modeli. Druga część daje konkretny kontrprzykład: Kajetan wybrał gotowy open source zamiast przepisywania mailingu.

Nowością wobec #40 (prawa inżynierii i agenci) i #41 (rzemiosło i generowany kod) jest konkretny przypadek Scion oraz decyzja Kajetana o mailingu. Nie sprzedajemy ponownie samej tezy „kod to nie wszystko”. Nie przypisujemy prowadzącym testów Scion — omawiają deklaracje Anthropic.

## Opis do publikacji

Opis i pełna agenda znajdują się w `episodes.json`. Nie dopisujemy odpowiedzi, których w nagraniu nie ma: prowadzący wprost chcą poznać proces stojący za liczbą commitów. Spekulacje o porządkowaniu slopu, danych treningowych i kopiowaniu rozwiązań nie są zweryfikowanymi ustaleniami redakcji.

## Miniatury — dokładnie 5 propozycji

Trzy konkretne haczyki i dwa ogólniejsze. Teksty do wyboru; nie wygenerowano grafik.

### A1 — rekomendowana: skala kontra potrzeba
---
30 TYS. 🤯
ZMIAN
DZIENNIE
PO CO?
---

### A2 — Scion
---
ANTHROPIC
ZASTĘPUJE
GITA 🤯
A TY?
---

### A3 — własne narzędzia
---
AI NAPISZE 🤖
TWÓJ MAILING
ALE PO CO?
---

### B1 — narzędzie a proces
---
NOWE NARZĘDZIE
CZY
STARY PROBLEM? 🤔
---

### B2 — koszt po wygenerowaniu kodu
---
KOD GOTOWY ✅
A KTO
TO UTRZYMA? 🔧
---

## Fragmenty do Shorts/Reels

Czasy poniżej to **surowa oś Riverside**, z zapasem 0,5 s przed i po. Wersja `transcriptions/043.json` odejmuje **0,718 s** od czasu pierwszego słowa; jej etykiety są dodatkowo obcięte do pełnych sekund. Finalny montaż może przesunąć całość i poszczególne fragmenty. Przed cięciem trzeba potwierdzić granice w audio. Cytowane krótkie hooki poniżej są parafrazami do opakowania, nie cytatami z nagrania. Dosłowny ASR każdego wycinka, autorzy i czasy poszczególnych słów są w `episode-043-shorts-words.json`.

1. **Chcesz być jak Anthropic? Musisz mieć ich problem**
   - Cięcie orientacyjne: **11:34.746–12:10.316**.
   - Treść: Kajetan tłumaczy, że rozwiązanie dotyczy problemu Anthropic, nie wszystkich firm. Piotrek domyka żartem o konsultancie.
   - Hook na ekranie: „Nie potrzebujesz infrastruktury firmy, której problemów nie masz”.
   - Uwaga: zachować końcowy żart i sprawdzić nakładanie głosów.
2. **Pokażcie proces, nie tylko narzędzie**
   - Cięcie orientacyjne: **24:15.111–24:44.723**.
   - Treść: Piotrek mówi, że cenny jest proces pracy na tej skali, którego sam nie zna.
   - Hook: „Nowe narzędzie to nie przepis na produktywność”.
   - Uwaga: koniec urywa przejście do następnej myśli; skrócić na odsłuchu lub poszerzyć, nie sklejać fikcyjnego zdania.
3. **Mailing: płacę za wysłane maile, nie za listę**
   - Cięcie orientacyjne: **33:34.138–33:52.354**.
   - Treść: Kajetan opisuje AWS SES i korzyść przy swojej skali wysyłki.
   - Hook: „Duża lista, rzadkie wysyłki? Sprawdź model rozliczeń”.
   - Uwaga: SES jest warstwą wysyłki, nie całym narzędziem marketingowym; nie obiecywać darmowego mailingu ani pełnego zamiennika beehiiv.
4. **Open source zamiast pisania wszystkiego od nowa**
   - Cięcie orientacyjne: **34:10.074–35:09.666**.
   - Treść: Kajetan wyjaśnia wybór gotowego produktu, koszt hostingu i potrzebę wiedzy technicznej mimo pomocy ChatGPT.
   - Hook: „Mogłem to napisać z AI. Wybrałem gotowe”.
   - Uwaga: początek segmentu nakłada się na poprzednią wypowiedź; potwierdzić odsłuch. Nie usuwać zastrzeżeń o hostingu i konfiguracji. Brak nazwy konkretnego produktu — nie dopisywać jej.

## Dodatkowe rolki nagrywane osobno — propozycje, nie materiał z #znaleziska

Brak dostępu do historii Discord #znaleziska. Poniższe to rozwinięcia tego odcinka, a nie rzekomo odczytane znaleziska.

### 1. Trzy pomiary przed zmianą Gita
- Hook: „Zanim skopiujesz Anthropic, zmierz swój problem”.
- Skrypt: „Przez jeden dzień zapisz, ile trwa przygotowanie środowiska agenta, ile aktualizacja repo i ile samo zadanie. Potem sprawdź, ile tego czasu to rzeczywiste czekanie. Jeśli kontrola wersji nie jest wąskim gardłem, jej wymiana nie rozwiąże głównego problemu. Nie znamy procesu Anthropic — ale własny możemy zmierzyć”.
- Proponowany eksperyment: 10 porównywalnych uruchomień na tym samym repo i maszynie; osobno zimny i ciepły cache. Raportować mediany oraz czas całego zadania; wynik dopiero po wykonaniu, bez wymyślonych oszczędności.

### 2. Napisz, kup czy wdroż open source?
- Hook: „To, że agent potrafi napisać narzędzie, nie znaczy, że warto je pisać”.
- Skrypt: „Dla jednej funkcji porównaj trzy opcje: kupić, wdrożyć open source albo napisać. Policz nie tylko start, ale hosting, aktualizacje, backup, awarie i swój czas. Kajetan przy mailingu wybrał open source oraz SES. To jego przypadek, nie uniwersalna recepta. Własne rozwiązanie ma sens, gdy rzeczywiście daje coś, czego nie dostajesz w gotowym”.
- Do nagrania: prowadzący mogą pokazać własny rachunek, ale bez kwot oszczędności, których tu nie policzyliśmy.

## Domknięcie i pytanie do komentarza

„Które narzędzie faktycznie napisaliście dla siebie z AI, a przy którym świadomie wybraliście gotowy produkt? Co przesądziło: brak funkcji, koszt czy utrzymanie?”

## Ważne rozbieżności ze źródłem

- Anthropic podaje **ponad 30 tys. scalonych zmian dziennie**, nie liczbę funkcji ani wszystkich commitów. W tytule i rekomendowanej miniaturze używamy „zmian”.
- **Siedem osób budowało Scion i Antique**, nie całe monorepo. Końcówka 37:30 wymaga odsłuchu i ewentualnego sprostowania, nie cichej zmiany wypowiedzi.
- **5,1 s** dla nowego worktree oraz **około 11 tys. zaoszczędzonych agentogodzin dziennie** to deklaracje Anthropic. Nie jest to nasz test.
- Oficjalna publikacja uznaje wcześniejszy dorobek Google/Meta. Nie potwierdziliśmy zarzutu kopiowania kodu Scion ani genezy REA związanej z Adobe. Nie używać tych tez jako haczyków.

## Kontrola przed publikacją

- Akceptacja tytułu, miniatury, daty i finalnej długości.
- Odsłuch niepewnych fragmentów z `episode-043-transcript-notes.md`; szczególnie liczba osób w monorepo na końcu.
- Weryfikacja źródeł i deklaracji w `episode-043-sources.md`.
- Dopasowanie agendy oraz Shorts do finalnej osi montażu.
- Uzupełnienie linków platform, dopiero potem publikacja za osobną zgodą.
- `notPublished: true` nie gwarantuje prywatności po wdrożeniu: obecny SSR obejmuje szkice. Draft PR jest publiczny, ale nie wdrażamy go na main.

## Jedna zmiana do sprawdzenia

Tytuł z jednym głównym pytaniem zamiast listy tematów. Jeśli będą dane Studio, porównać CTR w tych samych źródłach ruchu i przy tym samym wieku odcinka; pilnować retencji pierwszych 30/60 sekund, aby opakowanie nie obiecywało czegoś innego niż rozmowa. Bez danych nie diagnozujemy skuteczności.
