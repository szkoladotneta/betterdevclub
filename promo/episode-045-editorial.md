# Better Dev Club #45 — pakiet redakcyjny

Status: szkic do zatwierdzenia, bez publikacji. Źródło: dokładnie `Better Dev Club #45 - final`, clip `6aeb08faca4a739dce99e659`, nie roboczy Magic episode. Długość MP4 sprawdzona przez ffprobe: 2265.208333 s (37:45), 1920×1080. Robocza premiera: 2026-11-05.

## Obietnica i rekomendowany tytuł

**Czy AI naprawdę zabija open source? | Better Dev Club #45**

Dla programistów wybierających zależności i budujących własne narzędzia: oddzielamy przejęcie zespołu, zamknięcie kodu i koniec utrzymania projektu od jednej prostej opowieści o AI. Co oznaczają te zmiany dla użytkownika bibliotek — i kiedy szybki klon nie zastąpi produktu, za który warto zapłacić?

Warianty do wyboru, nie wyniki testu CTR:
1. Czy AI naprawdę zabija open source? | Better Dev Club #45
2. Możesz sklonować aplikację. Ale czy chcesz ją utrzymywać? | Better Dev Club #45
3. Open source się kończy czy tylko zmienia? | Better Dev Club #45

Nie obiecujemy benchmarków ani własnej reprodukcji klonów gier czy Artcraft. Piotrek opisuje subiektywne używanie Deno bez pomiarów; Kajetan opisuje własny prosty kalendarz konsultacji, który działa średnio.

## Opis

Czy AI naprawdę zabija open source, czy pod jedną etykietą wrzucamy zupełnie różne historie? Piotrek Stapp i Kajetan Duszyński rozmawiają o Deno i Cloudflare, zmianach w Cal.com oraz końcu utrzymania Pico CSS. Rozdzielają przejęcie zespołu, argumenty bezpieczeństwa i zwykłe starzenie się bibliotek — bez uznawania każdego z tych przypadków za dowód na tę samą tezę.

Przechodzimy też od gier przenoszonych do przeglądarki i alternatyw dla Photoshopa do praktycznego pytania: skoro możesz odtworzyć aplikację z pomocą AI, czy naprawdę chcesz to zrobić zamiast za nią zapłacić? Jest własny przykład Kajetana z kalendarzem konsultacji, dyskusja o odpowiedzialności za utrzymanie i bezpieczeństwo oraz pytanie do maintainerów. Na końcu świętujemy rok Better Dev Club — zostawcie tort w komentarzu! 🎂

## Rozdziały

Czasy na osi finalnego eksportu, wyprowadzone z ASR i montażu; do odsłuchu przed publikacją.

00:00 - [Open source i remont] Jeszcze jedna mała poprawka i pytanie o zmianę.
01:24 - [Deno i Cloudflare] Przejęcie zespołu: sukces twórców czy kłopot użytkowników?
08:18 - [Gry w przeglądarce] Reverse engineering, portowanie i pytania o prawa autorskie.
12:38 - [Photoshop w weekend?] Artcraft, efektowne demo i faktyczne potrzeby użytkownika.
16:10 - [Klon czy abonament?] Czy z nielimitowanymi tokenami odtworzylibyśmy własne IDE?
17:59 - [Cal.com i Cal.diy] Otwarty kod, model biznesowy i argument bezpieczeństwa.
21:20 - [Kalendarz w 20 minut] Własny przykład Kajetana i koszt niedopracowanego narzędzia.
22:46 - [Luki i agenci] Znajdowanie błędów, łatanie oraz granice blokad modeli.
27:29 - [Koniec Pico CSS] Dług technologiczny, popularność bibliotek i pieniądze na utrzymanie.
33:12 - [Co zostaje z open source?] Wnioski, kraftowy kodzik i pytanie do maintainerów.
37:07 - [Rok Better Dev Club] Tort w komentarzu i do zobaczenia za tydzień.

## Teksty miniatur

Pięć wariantów zgodnie z regułą miniatur: trzy konkretne, dwa ogólne. To propozycje tekstów, nie wygenerowane grafiki.

### A1 — konkret: decyzja użytkownika
---
KLONOWAĆ 🤖
CZY
ZAPŁACIĆ? 💸
---

### A2 — konkret: granice demonstracji
---
PHOTOSHOP
W WEEKEND? 🤯
A POTEM CO?
---

### A3 — konkret: przypadki z odcinka
---
DENO
CAL.COM
CO SIĘ
ZMIENIA? 🔍
---

### B1 — motyw przewodni
---
AI ZABIJA
OPEN SOURCE?
CZY NA PEWNO? 🤔
---

### B2 — motyw przewodni
---
KOD JEST 🤖
KTO GO
UTRZYMA? 🔧
---

## Trzy fragmenty na Shorts / Reels

Pełny surowy tekst i dokładne znaczniki słów: `episode-045-shorts-words.json`. Czasy poniżej zawierają 0,5 s zapasu; nie są zweryfikowane odsłuchem. Napisy wymagają korekty fonetycznych błędów ASR. Hooki są propozycją opakowania, nie dosłownym cytatem.

1. **Nielimitowane tokeny czy własna karta?** — około 16:25–17:08, dialog Kajetana i Piotrka. Hook: „Czy odtworzyłbyś własne IDE zamiast za nie zapłacić?”. Pytanie o Visual Studio i odpowiedź, że Piotrek raczej kupiłby narzędzie. Nie przedstawiać tego jako testu klonowania IDE.
2. **Zwaibowałem kalendarz. Działa bardzo średnio.** — około 21:20–22:19, Kajetan, z krótkim wtrąceniem Piotrka. Hook: „Szybkie napisanie aplikacji to jeszcze nie gotowy produkt”. Własny przykład Kajetana, ok. 20 minut pracy i zainteresowanie gotowym Cal.diy. Nie uogólniać jednego przykładu na wszystkie produkty AI.
3. **Popularniejsze nie znaczy lepsze** — około 30:57–31:42, Kajetan i Piotrek. Hook: „Czy AI wybiera najlepszą bibliotekę, czy tę najbardziej znaną?”. Fragment o Pico, bibliotekach CSS i sprostowaniu słowa „lepsze”. Zachować kontrargument Piotrka.

## Rolki nagrywane osobno — propozycje, nie newsy z #znaleziska

Brak dostępu do historii Discord #znaleziska; poniższe pomysły wynikają wyłącznie z odcinka.

- **Solo Kajetan: „Kalendarz z AI kontra gotowiec”**. Pokazać własny działający fragment kalendarza i jeden rzeczywisty problem. Następnie porównać wymagania z Cal.diy. Ważny kontrargument: dokumentacja Cal.diy zaleca wyłącznie osobisty, nieprodukcyjny użytek, więc nie proponować go bezwarunkowo do obsługi klientów. Nie obiecywać migracji ani jej wyników przed wykonaniem.
- **Duet: „Kiedy klonować, kiedy kupić?”**. Dwa przypadki: jednorazowa prosta obróbka obrazka i codzienne IDE. Ocenić utrzymanie, niezawodność oraz ryzyko prawne, bez udawania porady prawnej.

## Domknięcie i pomiar

Pytanie do widzów: **Którego narzędzia używasz codziennie i mimo dostępu do AI nadal wolisz za nie płacić — dlaczego?**

Do przetestowania jedna zmiana: tytuł z konkretnym pytaniem zamiast listy newsów. Bez danych Studio brak diagnozy CTR. Po publikacji porównać CTR według źródeł ruchu i wieku filmu; nie przypisywać samej zmianie tytułu przyczynowości.

## Przed publikacją

- Zatwierdzić tytuł, miniaturę i datę; uzupełnić rzeczywiste linki platform.
- Przejrzeć `episode-045-transcript-notes.md` oraz raport źródeł.
- Odsłuchać miejsca z niejasnym ASR, nazwy własne i granice rozdziałów/Shorts.
- Nie publikować ogólnych opinii o prawach autorskich jako ustaleń prawnych.
- Nie obiecywać udziału Oskara Dudycza; prowadzący dopiero proponują zaproszenie.
- `notPublished: true` nie zapewnia prywatności po scaleniu: SSR generuje również szkice. Pozostawić draft PR do akceptacji.
