# Better Dev Club #47 — pakiet redakcyjny

## Status i źródło

**SZKIC, NIE PUBLIKOWAĆ bez zatwierdzenia.** `notPublished: true`, identyfikatory i linki platform puste. Data **2026-11-19 jest robocza** (czwartek, tydzień po #46); prowadzący we wstępie nie rozstrzygają między czwartkiem a piątkiem. Datę trzeba zatwierdzić, nie wywodzić z daty pliku.

- Dokładny eksport Riverside: **Better Dev Club #47 - final**.
- Clip ID: `6afeeb177b03e227ce7bbefa`; RSTL edit ID `6afee8d6c4b8cb270526b1b2`, rewizja **21**.
- Finalny MP4: **2728.092993 s = 45:28**, pomiar ffprobe, nie ostatni timestamp ASR.
- Transkrypcja composed recording: HTTP **404**. Wykorzystano **ASR sesji przeliczony przez montaż finalnego klipu**, nie nową transkrypcję audio finalnego pliku.
- RSTL po odjęciu wspólnych cięć daje 2728.098667 s; różnica względem MP4 ok. **0.006 s**. To kontrola długości, nie dowód synchronizacji każdego słowa.
- Wszystkie klipy nagrań mają identyczne pozycje czasu źródła i ścieżki; obraz nakładki nie zmienia audio. Trzy wspólne cięcia: 0–1.5 s, 3.368–4.654 s, 12.836–15.118 s. Offset ASR: Kajetan 46 ms, Piotrek 0 ms. Nie odejmowano ponownie pierwszego słowa ASR.
- **Rozdziały i granice Shorts wymagają odsłuchu.** Per-track magic mutes nie zostały potraktowane jak globalne cięcia tekstu. ASR zawiera nakładające się wypowiedzi i nadal ma niejasne frazy.
- Surowy ASR zachowano bez korekt: `transcriptions/raw/047.json`; korekta nazw i terminów oraz metadane mapowania: `promo/047-transcription-audit.json`.
- Samo scalenie tego PR może ujawnić szkic w statycznym archiwum. Generator SSR nie filtruje `notPublished`, a bezpośrednia strona może mieć etykietę „Opublikowano”. PR ma pozostać draftem do decyzji redakcji.

## Obietnica i kierunek

**Dla kogo:** programiści i osoby planujące rozwój w IT, które nie wiedzą, w co inwestować czas po upowszechnieniu AI.

**Korzyść:** rozdzielenie kolejnego języka/frameworka od kompetencji pozwalających ocenić rozwiązanie: skala, koszty, sieci, wdrożenia i doświadczenie w rozwiązywaniu problemów. Odcinek pokazuje też różne sposoby uczenia się, nie jedną gwarantowaną ścieżkę kariery.

**Pytanie:** w co zainwestować tysiąc godzin nauki, gdy samo pisanie kodu przestaje wyróżniać?

**Konkretny własny przypadek:** Piotrek opisuje zbędny throttling w serwerze MCP; Kajetan wspomina poznanie SOLID po nieudanej rekrutacji. Są to relacje prowadzących, nie niezależnie odtworzone eksperymenty.

Nie sprzedawać odcinka jako dowodu, że „AI pisze lepiej od każdego” ani „w IT nie ma zwolnień”. Rozmówcy stawiają mocne tezy, ale też pokazują rozbieżności: książki kontra praktyka oraz to, ile przewagi zostaje w architekturze.

## Tytuły do wyboru

1. **Czego się uczyć, gdy AI pisze kod? | Better Dev Club #47** — roboczy wpis w bazie.
2. Tysiąc godzin na naukę. W co zainwestować w erze AI? | Better Dev Club #47
3. Kariera w IT to już nie tylko kod | Better Dev Club #47

## Teksty miniatur

Warianty do wyboru, nie gotowe obrazy ani obietnica wyższego CTR. Trzy konkretne haczyki i dwa ogólne; dokładnie pięć wariantów zgodnie z regułami miniatur.

### A1 — rekomendowany, tysiąc godzin

---
1000 GODZIN ⏳
NA NAUKĘ
ALE CZEGO? 🤔
---

### A2 — książki kontra praktyka

---
KSIĄŻKI 📚
CZY
PRAKTYKA? 🛠️
---

### A3 — doświadczenie

---
10 LAT
DOŚWIADCZENIA
CZY 10×
TEN SAM ROK? 🔁
---

### B1 — pytanie o kierunek nauki

---
AI PISZE KOD 🤖
A TY
CZEGO SIĘ
UCZYSZ? 🤔
---

### B2 — kod a praca

---
MNIEJ KODU 💻
WIĘCEJ
INŻYNIERII? 🛠️
---

## Uwagi do odsłuchu i decyzji przed publikacją

1. **00:00–06:42 — wstęp.** Główny temat pojawia się dopiero po ponad sześciu minutach. To obserwacja osi montażu i tekstu, nie diagnoza retencji. Jeżeli nie zmieniacie finalnego eksportu, zostawić rozdział 06:42 i nie obiecywać rozpoczęcia meritum od pierwszego zdania.
2. **Około 00:10 — GTA VI.** Rozmówcy mówią o premierze jako o fakcie; data zapowiedziana nie dowodzi odbytej premiery. Weryfikacja oficjalnego statusu osobno; opis nie opiera na tym głównej obietnicy.
3. **02:06–06:42 — Anthropic i konkurenci.** Rozdzielić IPO/złożenie dokumentów/plany debiutu. Wypowiedź o celowym podkopywaniu IPO przez innych producentów to interpretacja Kajetana, nie potwierdzona koordynacja działań. Nie zmieniano jej po cichu w transkrypcji.
4. **Około 14:11–14:42 — nazwy modeli.** ASR daje m.in. „Trussev, Stav, Frontier, Model, Fable, Astra” oraz „Argon, Carbon”. Bez pewności i oficjalnego potwierdzenia nie rozwijano ich do zmyślonych nazw modeli. Ten fragment pozostaje do odsłuchu.
5. **16:32–18:46 — Microsoft i rynek pracy.** Liczby 40 tys., 60 tys., 250 tys., 0% i −2% wymagają osobnego sprawdzenia okresów i definicji. Propozycja dobrowolnego odejścia nie oznacza skorzystania z niej przez wszystkich; płaski headcount nie dowodzi braku zwolnień. Z jednej firmy nie można wnioskować o całym rynku IT. Nie używać tego fragmentu w promocji bez sprostowania/źródła.
6. **25:13–27:59 — „AI pisze lepiej”.** Opinia prowadzących; odcinek nie zawiera własnego porównawczego benchmarku. Tytuł opisuje zmianę pracy, nie uniwersalną przewagę AI.
7. **31:07–33:04 — throttling.** Przykład konkretnego systemu i skali; nie ogólna rekomendacja usuwania limitów bezpieczeństwa. Przy wycinaniu Shorta koniecznie zachować kontekst.
8. **34:18–36:10 — niejasne terminy.** „crash na CPU” może być błędem ASR; nie poprawiano go arbitralnie na cache. Także „lock/load pointy”, „City of Morning Coffee” i nazwisko wspomnianego Sebastiana wymagają odsłuchu.
9. **44:50 — C# / Rust.** „raz” poprawiono kontekstowo na „Rust”; sprawdzić w audio. Nie jest to stwierdzenie, że Rust nie ma kosztów zarządzania pamięcią, tylko żart rozmówców o garbage collectorze.
10. **Data i publikacja.** Zatwierdzić datę, tytuł, odsłuchane rozdziały i linki platform przed zmianą `notPublished`.

## Dodatkowe rolki nagrywane osobno

Nie przygotowano fikcyjnych tematów z #znaleziska: ta sesja nie ma dostępu do historii kanału. Po otrzymaniu linków można dobrać 2–3 odrębne pomysły. Poniżej są wyłącznie fragmenty rzeczywiście obecne w odcinku.

## Jedna rzecz do sprawdzenia po publikacji

Sprawdzić retencję przed i po 06:42, kiedy zaczyna się główna obietnica tytułu. Porównać z duetowymi odcinkami w tym samym wieku publikacji. Bez danych Studio nie oceniać, czy długi wstęp faktycznie szkodzi; sam tekst i długość nie dowodzą utraty widzów.
