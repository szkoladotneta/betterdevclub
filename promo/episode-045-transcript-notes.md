# Odcinek 45 — korekta i uwagi do odsłuchu

## Pochodzenie i oś czasu

- Dokładny eksport Riverside: `Better Dev Club #45 - final`, clip `6aeb08faca4a739dce99e659`, composed recording `6aeb08faca4a739dce99e65a`.
- Długość MP4 sprawdzona przez ffprobe: **2265.208333 s = 37:45**, obraz 1920×1080. Długość RSTL: 2265.2083333333335 s, zgodna w granicy zaokrąglenia.
- Endpoint transkrypcji composed recording zwrócił **404**. Użyto jawnego fallbacku do ASR sesji `18129a34-cd4d-4ec6-afcf-ddd8d60a91e5`, nie transkrypcji finalnego MP4.
- Każda ścieżka ma jeden klip, `trackTime=0`, brak clip cuts i syncedCuts. Początki źródłowe są różne: Kajetan 1.5416666667 s, Piotrek 1.625 s. ASR offset Kajetana wynosi 96 ms, Piotrka 0 ms.
- Mapowanie słów: od timestampu ASR odejmujemy offset rozmówcy i początek lokalnego źródła. Efektywne początki: Kajetan 1.6376666667 s, Piotrek 1.625 s. Nie odejmujemy dodatkowo czasu pierwszego słowa.
- Mapowanie sprawdzono strukturalnie i względem zgodności długości MP4; nie przeprowadzono weryfikacji odsłuchem. Magic-mutes nie traktowano jako usunięcia wspólnego tekstu.
- `transcriptions/raw/045.json` zachowuje pobraną odpowiedź ASR bez korekty. Hash SHA-256, wersja RSTL, zakresy źródeł i audyt każdej zamiany: `episode-045-source-map.json`. Bez prywatnych URL mediów, ciastek i danych logowania.
- Transkrypcja po korekcie: 82 segmenty. Korekta nazw i oczywistych fonetycznych błędów nie oznacza redakcji wszystkich zdań ani napisów zweryfikowanych audio.

## Miejsca wymagające uwagi

- **01:48–02:36:** subiektywna ocena szybkości Deno, jawnie bez benchmarków. Nie zamieniać jej w obiektywny wynik ani zapewnienie pełnej kompatybilności Node.js.
- **02:37–04:50:** nazwa projektu Cloudflare rozpoznana fonetycznie jako „Sell D”. Wymaga porównania z oficjalnym źródłem i odsłuchu; podobnie fragmenty „Słuchaj, czemu rozwalił kolejny…” i „To chyba bardzo oprzeczam…”. Harmonogramy runtime i hostingu sprawdzić w raporcie źródeł.
- **08:18–12:38:** reverse engineering a portowanie to nie to samo; nie potwierdzono reprodukcji Need for Speed ani Cyberpunka. Nie linkować pirackich buildów. Dostępność Cyberpunka prowadzący sami oznaczają jako niepewną.
- **11:05, 24:33:** twierdzenie o blokadach Anthropic wymaga konkretnego ogłoszenia. Nie zamieniać go w fakt w opisie.
- **12:11–13:58:** kategoryczne wypowiedzi o prawach autorskich to opinie rozmówców, nie zweryfikowana analiza prawna. Klon funkcjonalny, skopiowanie kodu/zasobów i port wymagają osobnej oceny.
- **12:38:** „Artcraft jako przeniesiony cały pakiet Adobe” jest skrótem rozmówców, nie dowodem kompletnej zgodności produktów. Materiały promocyjne mówią o alternatywach/demo, nie o pełnym zastąpieniu.
- **14:24–14:46:** niepewność o obsługiwanych systemach i rozwoju Paint.NET — nie poprawiać wypowiedzi na przeciwną bez oznaczenia; sprawdzić dokumentację w raporcie źródeł.
- **15:16:** „odtworzyć z Apple” prawdopodobnie „odtworzyć apkę”, ale pozostawiono do odsłuchu zamiast rekonstruować na pewniaka.
- **16:25–17:08:** pytanie o klon Visual Studio jest hipotetyczne. Piotrek nie raportuje próby odtworzenia IDE. Krótkie wtrącenia ASR („No, obcocie.”) do odsłuchu.
- **17:36:** uszkodzony fragment o ReSharperze; poprawiono markę, nie rekonstruowano sensu zdania.
- **17:59–21:20:** Cal.com i Cal.diy poprawiono jako nazwy. Nie utożsamiać zmiany licencji/otwartości z zamknięciem firmy; argument bezpieczeństwa przedstawiać jako deklarację firmy.
- **21:20–22:18:** własny kalendarz Kajetana: ok. 20 minut i średnie działanie to jego relacja, nie nasz pomiar. To najmocniejszy fragment z własnej praktyki w odcinku.
- **22:46–24:33:** porównanie tempa znajdowania i łatania luk jest oceną rozmówców. Nie ma w nagraniu pomiaru ani dowodu dla całej branży. PHP — brak wskazanych CVE.
- **24:52:** uogólnienie o Chińczykach i prawach autorskich nie jest ustaleniem o politykach konkretnych dostawców. Nie powielać w opisie/rolkach jako faktu.
- **25:36–27:29:** silnie uszkodzone ASR („Kazu Salona”, „Grogbocie”, „badbite”) i niezweryfikowana anegdota o Elonie, Opusie i wypowiedzi Sama Altmana. Pozostawiono niepewne fragmenty bez wymyślania nazw lub linków. Do odsłuchu albo wycięcia po decyzji redakcji.
- **27:29–33:12:** Pico CSS — oddzielić deklarację autora, dług technologiczny i interpretacje prowadzących. „Popularniejsze” nie znaczy „lepsze”; zachować kontrargument Piotrka. Sassa, Tailwinda i Polly skorygowano jako nazwy.
- **28:49–29:46:** niepewna nazwa mechanizmu finansowania („open source contributor license”). Nie zastępować konkretną licencją bez źródła. 20 USD dla Polly to relacja Piotrka o procesie w jego organizacji, nie weryfikacja obecnego cennika.
- **35:05–36:31:** Oskar Dudycz jest propozycją zaproszenia, nie potwierdzonym gościem. Nie obiecywać jego udziału.
- **37:07:** prośba o tort i rocznica podcastu zostają; nie skracać opisu w sposób sugerujący potwierdzoną datę założenia kanału.

## Wyniki sprawdzenia źródeł

Pełny raport i cytaty: `episode-045-sources.md`.

- Nazwę „Sell D” poprawiono na **`celld`** na podstawie oficjalnego komunikatu Cloudflare; pozostałych uszkodzonych zdań nie rekonstruowano. Plan dotyczy połączenia kodu i pomysłów istniejącego celld z workerd, nie budowy od zera. Okresy roku dla runtime i sześciu miesięcy Deploy potwierdzone.
- Zmiana Cal.com pochodzi z **14–15 kwietnia 2026**, czyli około pół roku przed nagraniem, nie z ostatnich dwóch–trzech miesięcy. To rozbieżność do sprostowania, a nie błąd fonetyczny do ukrytej korekty.
- **Cal.diy ostrzega przed użyciem produkcyjnym** i zaleca użytek osobisty. Własny pomysł Kajetana na migrację kalendarza konsultacji nie jest rekomendacją redakcji do wdrożenia dla klientów.
- Autor Pico CSS podaje zarówno kontekst AI, jak i potrzebę przepisania na modern CSS. Interpretacja „naturalna śmierć” jest stanowiskiem prowadzących, nie pełnym streszczeniem uzasadnienia autora. Dokładnej daty ogłoszenia nie ustalono.
- PhotoCraft jest nadal early alpha. Brak potwierdzenia pełnej równoważności z pakietem Adobe.
- Oficjalny wpis Paint.NET z **24 października 2026** opisuje eksperymentalną betę 5.2 dla Wine/Linux, z możliwym działaniem na Macu. Nie mówić bezwarunkowo „tylko Windows”, ale też nie obiecywać natywnej stabilnej wieloplatformowości. Rozwój projektu trwa.

## Przed cięciem Shorts

Dokładne czasy z zapasem 0,5 s i słowa ASR są w `episode-045-shorts-words.json`. Przy montażu odsłuchać oba końce, nie ucinać początku na podstawie zaokrąglenia czasu w górę. Napisy skorygować po odsłuchu. Hooki z pakietu redakcyjnego są parafrazami, nie cytatami.
