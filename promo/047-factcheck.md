> Czasy w tym raporcie to sekundy surowego ASR. Czasy finalnego eksportu podaje `047-editorial.md`; po wstępnych cięciach różnica to 5.068 s dla Piotrka oraz 5.114 s dla Kajetana.
> Kontrola nadrzędna: ponownie pobrano źródła Microsoft FY2025/FY2026, Anthropic IPO, Rockstar VI i Google Gemini; wskazane liczby, daty i atrybucję Argon/Carbon potwierdzono w treści. Pozostałe źródła opisano w raporcie z ograniczeniami.

# BDC 47 — fact-check redakcyjny

Stan odniesienia: **19 listopada 2026** (data wskazana w zadaniu). Sprawdzono rzeczywiście pobrane oficjalne strony, nie wiedzę modelu. Materiał wejściowy: `raw-readable.txt`; bez odsłuchu audio. „Niepotwierdzone” nie oznacza „fałszywe”.

## Microsoft — 997–1112 s

| Twierdzenie | Werdykt i bezpieczna korekta |
|---|---|
| „Na początku tego roku 250 tys.” (1092 s) | **Niepotwierdzone dla początku 2026 r.** Oficjalne porównywalne stany to 228 tys. na 30.06.2025 oraz 223 tys. na 30.06.2026; strona korporacyjna podaje również 223 tys. na 30.09.2026. Żadna z tych dat nie jest 1 stycznia; nie przedstawiać 250 tys. jako zweryfikowanej bazy.[1][2][15] |
| „40 tys. dostało opcję dobrowolnego odejścia” (998 s), później „40 tys. będzie zwolnionych” (1062 s) | **Niepotwierdzone.** Brak takiej liczby/programu w przejrzanych raportach i brak potwierdzenia w oficjalnej wyszukiwarce Microsoft dla `voluntary 2026`. Zakres przeszukania jest ograniczony. Uprawnienie do programu, skorzystanie z niego i przymusowe zwolnienie to różne wielkości; transkrypt zamienia je bez uzasadnienia.[unverified] |
| „W zeszłym roku 60 tys. zwolnili i 60 tys. zatrudnili” (1062 s) | **Niepotwierdzone przepływy brutto.** Porównanie stanów zatrudnienia nie ustala liczby zwolnień ani rekrutacji. Nie znaleziono w przejrzanych oficjalnych materiałach potwierdzenia obu liczb; usunąć albo zażądać źródła od prowadzącego.[unverified] |
| „W zeszłym roku headcount zmienił się o 0%” | **Tak, jeśli chodzi o rok fiskalny FY2025:** około 228 tys. zarówno na 30.06.2024, jak i 30.06.2025, czyli 0% na opublikowanych zaokrąglonych danych. To nie jest potwierdzenie bilansu kalendarzowego 2025 ani 60 tys. zwolnień/rekrutacji.[7][1] |
| „W tym roku 2% niższy” (1112 s) | **Z grubsza zgodne dla porównania FY2026/FY2025:** 228 → 223 tys., obliczeniowo **−2,19%**. Stan wrześniowy nadal wynosi 223 tys. Nie dowodzi to zmiany od początku stycznia do listopada. Przy bazie 250 tys. i stanie 223 tys. spadek wyniósłby **10,8%**, a nie 2%.[1][2][15] |

**Wniosek redakcyjny:** zdanie „więc nie ma zwolnień w IT, realnie” nie wynika z headcountu pojedynczej firmy. Stabilny stan netto może współistnieć ze zwolnieniami; dane nie dowodzą też przesunięć konkretnie między rolami technicznymi.

## GTA VI — początek odcinka

**Potwierdzono zapowiedzianą datę 19.11.2026.** Oficjalna strona Rockstar wyświetla „Coming November 19, 2026”. Nie zastępować tej daty wcześniejszymi terminami z pamięci. Źródło nadal używa „Coming” i „Pre-Order”, więc samo w sobie **nie potwierdza**, że gra już faktycznie wystartowała, że premiera była o północy ani jednocześnie we wszystkich strefach. Bezpiecznie: „GTA VI ma oficjalnie zapowiedzianą premierę na 19 listopada”.[3]

## Anthropic IPO — 131–377 s

**Potwierdzone IPO, ale rozdzielić jego etapy.** Oficjalny komunikat z 18.11.2026 podaje ustalenie ceny **83 USD za akcję**, oczekiwany początek notowań na **Nasdaq Global Select Market 19.11.2026**, ticker **ANT**, oraz oczekiwane zamknięcie oferty **20.11.2026**, warunkowe. Potwierdza to kontekst „ma IPO / wejdą na giełdę”; nie dowodzi jeszcze rozpoczęcia handlu, kursu debiutu ani zrealizowanego zarobku inwestorów.[5]

Sugestia, że konkurenci celowo zsynchronizowali premiery, aby „podkopać IPO/wycenę”, jest **spekulacją o intencjach**, nie ustalonym faktem. Zapowiedź nieuchronnej zmiany cen subskrypcji po IPO jest prognozą; w sprawdzonym komunikacie IPO brak takiej deklaracji.[unverified]

## Nazwy modeli — 857–878 s

Nie poprawiać całego wyliczenia automatycznie: zapis ASR nie dowodzi, jakie słowa rzeczywiście padły.

- **„Trussev”, „Stav”** — **nierozpoznane**. Nie udało się przypisać tych dokładnych tokenów do modeli w przejrzanych oficjalnych materiałach. Wymagają odsłuchu/pytania do autora, nie zgadywanego rozwinięcia.[unverified]
- **„Frontier, Model”** — nie potwierdzono osobnego produktu o takiej nazwie. Może to być ogólne określenie „frontier model”, a nie dwa elementy listy; bez audio nie rozstrzygać.[unverified]
- **Fable** — nazwa rzeczywista: **Claude Fable 5.2**, ogłoszony przez Anthropic razem z Claude Mythos 5.2 **9.11.2026**. To potwierdzenie nazwy, nie tego, że w nagraniu podano tę wersję.[6]
- **Astra** — nazwa rzeczywista w rodzinie OpenAI: dokumentacja wskazuje **GPT-6.2 Astra**; oficjalny RSS zawiera premierę „Introducing GPT-6.2 Astra and Sol” z **17.11.2026**. Pełny artykuł był zablokowany, więc nie przypisuję mu dodatkowych ustaleń.[13][12]
- **Argon / Carbon** — oficjalny katalog Google wymienia **Gemini 4 Argon** i **Gemini 4 Carbon**. Jeżeli fragment przypisuje te nazwy Microsoftowi, jest to **błąd atrybucji**; źródło potwierdza Google, nie Microsoft. Samą fonetykę musi rozstrzygnąć odsłuch.[9]
- Microsoft rzeczywiście ogłosił **17.11.2026** rodzinę nowych modeli, m.in. **MAI Code 2 / Code 2 Flash**, **MAI Cyber 2 Flash** i **MAI Image 2.7**, oraz **MAI Licensed Weights**. Ogólny wątek o nowych modelach i większej kontroli ma podstawę w komunikacie producenta; jego benchmarki/ceny pozostają deklaracjami producenta, nie niezależnym testem.[14]

## Dostępność i ograniczenia źródeł

- **HTTP 200 i odczytana treść:** raporty Microsoft FY2024/25/26, Rockstar VI, komunikaty Anthropic o IPO i Fable, katalog Google Gemini, dokumentacja modeli OpenAI oraz oficjalny RSS OpenAI.
- **HTTP 403 przez requests, odzyskano aktualną treść w przeglądarce:** dokładny artykuł Microsoft Ignite i „Facts About Microsoft”. Cytowane treści zapisano w `msignite-browser.txt` i `msfacts-browser.txt`; narzędzie przeglądarkowe nie zwróciło kodu HTTP.
- **Ograniczenia:** `https://openai.com/news/` — requests 403, przeglądarka „Just a moment…”; pełny artykuł `https://openai.com/index/introducing-gpt-6-2-astra-sol` — 403. Zamiast udawać odczyt, wykorzystano oficjalną dokumentację i RSS. `https://www.take2games.com/ir/news` — 404; nie użyto jako dowodu.
- Wyszukiwanie Google zwracało ekran zgody, a próba Bing dała wyniki niezwiązane z zapytaniem — nie były dowodem. Oficjalna wyszukiwarka Microsoft była dostępna w przeglądarce, ale nie dała potwierdzenia programu 40 tys. Brak wyniku nie dowodzi braku programu.
- Kopie pobrań i rejestr `retrieval.json` pozostawiono obok raportu. Weryfikacja obejmuje treści dostępne w tej sesji, nie audyt kompletności wszystkich historycznych komunikatów.

## Sources

[1] https://www.microsoft.com/investor/reports/ar25/index.html — ms2025
    > "As of June 30, 2025, we employed approximately 228,000 people on a full-time basis"
[2] https://www.microsoft.com/investor/reports/ar26/index.html — ms2026
    > "As of June 30, 2026, we employed approximately 223,000 people on a full-time basis"
[3] https://www.rockstargames.com/VI — gta
    > "Coming November 19, 2026"
[5] https://www.anthropic.com/news/anthropic-prices-initial-public-offering — ipo
    > "The shares are expected to begin trading on the Nasdaq Global Select Market on November 19, 2026 under the symbol “ANT.”"
    > "Today Anthropic, PBC priced its initial public offering of its Class A common stock at $83.00 per share."
    > "The offering is expected to close on November 20, 2026, subject to the satisfaction of customary closing conditions."
[6] https://www.anthropic.com/claude-fable-and-mythos-5-2 — fable
    > "November 9, 2026 Claude Fable 5.2 and Mythos 5.2"
[7] https://www.microsoft.com/investor/reports/ar24/index.html — ms2024
    > "As of June 30, 2024, we employed approximately 228,000 people on a full-time basis"
[9] https://deepmind.google/models/gemini — gemini
    > "Gemini 4 Argon: Built to solve your hardest problems"
    > "Gemini 4 Carbon: Our next frontier model"
[12] https://openai.com/news/rss.xml — oairss
    > "Introducing GPT-6.2 Astra and Sol"
    > "Tue, 17 Nov 2026 17:45:00 GMT"
[13] https://developers.openai.com/api/docs/models — oaimodels
    > "If you're not sure where to start, use GPT-6.2 Astra , our flagship model for complex reasoning and coding."
[14] https://microsoft.ai/news/microsoft-ignite-2026 — Microsoft Ignite 2026 — browser
    > "That’s why today we’re releasing a family of seven new world class models at a truly exceptional price-performance."
    > "Today, we’re taking a big step forward with MAI Licensed Weights: models under your control."
[15] https://news.microsoft.com/facts-about-microsoft — Facts About Microsoft — browser
    > "Worldwide	223,000

As of September 30, 2026"
