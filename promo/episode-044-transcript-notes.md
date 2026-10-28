# Odcinek 44 — źródło, korekta ASR i oś finalnego eksportu

## Źródło

- Riverside, projekt `6ae1d6512bc53e2e156cf6eb`.
- Wybrano dokładny tytuł **Better Dev Club #44 - final**, klip `6ae1e4186c10430c50c5e066`, composed recording `6ae1e4186c10430c50c5e067`.
- Długość MP4 sprawdzona przez ffprobe: **2016.000000 s = 33:36**.
- ASR pobrano z sesji `9e35fdad-60ef-48a8-8cd6-742f70ee460a`; finalny eksport ma własną, zapisaną wersję `rstlTimeline`. Nie użyto późniejszych zmian roboczego Magic episode 01.
- Endpointy gotowej transkrypcji composed recording zwróciły 404. Plik wynikowy powstał z ASR sesji, po zastosowaniu początku/końca oraz wspólnego cięcia finalnego eksportu. Nie jest to transkrypcja potwierdzona odsłuchem.
- Surowego `transcriptions/raw/044.json` nie korygowano. Zapisano hash, metadane montażu i pełną listę zamian w `episode-044-source-map.json`, bez prywatnych URL do pobierania ani danych logowania.

## Mapowanie czasu

- Surowe pierwsze słowo: **0,878 s**.
- Standardowy formatter odejmuje tę wartość i ucina etykiety do sekund. **W odcinku #44 nie stosujemy jego normalizacji**: posługujemy się osią finalnego eksportu.
- Finalny montaż zaczyna się od **0,8333333333 s** surowej osi; przed wspólnym cięciem ma **2019,88 s**.
- Wspólne cięcie na osi montażowej przed kompresją: **1781,5436666667–1785,4236666667 s**, długość **3,88 s**. Odpowiada surowemu zakresowi **1782,377–1786,257 s**.
- Po kompresji długość wynosi dokładnie **2016 s**, zgodnie z ffprobe.
- Z tekstu odpadają cztery słowa objęte cięciem: surowy ASR „Bo nie facy, uważaj.”. Nie jest to samowolna korekta wypowiedzi; fragmentu nie ma w finalnym montażu.
- Przed cięciem: `final = raw - 0,8333333333`; po cięciu dodatkowo odjąć **3,88 s**. W środku cięcia nie ma materiału do cytowania.
- Etykiety segmentów wynikają z pierwszego zachowanego, niepustego słowa; mogą różnić się od standardowego formattera także dlatego, że ten wybiera timestamp pustego tokenu szumu przed wypowiedzią.
- Nie interpretowano magic-mutes na ścieżkach jako usuwania tekstu. To wyciszenia toru, nie wspólne cięcia montażowe. Wymagany odsłuch przy nakładaniu głosów.

## Zakres korekty

Przeczytano całą transkrypcję. Zachowano 35 grup wypowiedzi i autorów, ale przeliczono ich czasy na finalny eksport. Korekty tekstowe dotyczą 17 grup. Zachowano potoczne wypowiedzi, liczby, wahania i nierozstrzygnięte miejsca.

Najważniejsze poprawki:
- Nazwy i terminy: Anthropic, IPO, Claude / Claude’a, Codex / Codexa / Codexie, GitHub Copilot / Copilota / Copilocie, Confluence, GitHubie, harnessy, bottlenecki, soft skills, Pomodoro, CRUD-y / CRUD-ów, SaaS, RAM.
- Imiona i marka: fonetyczne „karetan” / „Karytanem” → Kajetan / Kajetanem; „Better Death Clap Weekly” → Better Dev Club Weekly.
- Oczywiste błędy: „GRD” → giełdę, „tarapetą” → terapeutą, „spuczka” → spłuczka, „homonto” → chomąto, „budżet na pierwsze rano” → budzik na pierwszą rano, „superkrow” → superkrok. W otwarciu poprawiono składnię pytania o radzenie sobie z wypaleniem.
- Pełny audyt zamian (oryginał, wynik, segment i liczba wystąpień) jest w `episode-044-source-map.json`. Słowa w pliku Shorts zachowują **oryginalny ASR**, nie tę korektę; nie kopiować ich bez odsłuchu do finalnych napisów.

## Miejsca do odsłuchu i kontroli redakcyjnej

Czasy to początki grup na osi finalnego eksportu, nie wskazanie dokładnego nieczytelnego słowa.

- **00:01–00:22:** otwierający żart i stwierdzenie o dokumentach IPO Anthropic. Korekta nazw nie jest fact-checkiem IPO; jeśli zostaje jako informacja, sprawdzić osobno oficjalne dokumenty/ogłoszenie.
- **01:11:** „z nie wiem, w wojnę” — nie rekonstruowano urwanej końcówki.
- **05:21:** m.in. „chcą wymaksować to kranu”, „części dzieci w tej chwili zawodowe”, „ilomaż”, „na tyle kapowato” — zapis nie jest pewnym cytatem. Zostawiono nieczytelne frazy zamiast dopisywania sensu.
- **05:21–09:17:** hipoteza o osobach z ADHD — pozostawiono „nie wiem czy to jest prawda”. Nie przedstawiać jako ustalenia naukowego.
- **09:17:** „w swojej magie”, urwane pytanie o okno kontekstowe, „następna odpowiedź, Rada” oraz rytm pracy w nocy — nie rekonstruowano nazwy aplikacji ani dokładnej funkcji harnessu. Przed promowaniem takiego workflow sprawdzić granice autonomii i bezpieczeństwo działań.
- **09:17:** wątek organizacji nagrania i awarii zasilania ma urwane połączenia zdań. „20.00... 30” to niepewny zapis rozbitej godziny; nie dopisywano nowej wartości liczbowej.
- **13:27–13:29:** „Naprzednimi / naprzed nimi” — próba tłumaczenia frontier, pozostawiona jako element rozmowy, nie nazwa narzędzia.
- **15:41:** „media, szedularem, oporządzaczem”, „Zawiłem kogoś, byś tak nie płakał” — nie rozstrzygano słów ani nazwy projektu.
- **21:06–21:08:** „Duono, fault” i „duo to od iPhone” — pomyłka/żart o urządzeniach, wymaga odsłuchu. Nie podmieniono firmy na Microsoft tylko dlatego, że istnieje Surface Duo. W metadanych nie podano dokładnego modelu telefonu ani nie potwierdzono ceny.
- **21:08:** zmiana zawodu handlowiec → hydraulik to opowiedziana historia. Jej przyczyna pozostaje nieznana; nie dopisano wypalenia ani warunków finansowych bohatera.
- **23:53:** nieczytelne szczegóły rezygnacji pierwszego płatnego użytkownika („odkaz”, „dostał z wyrody”). Nie wyciągano wniosku o zwrocie pieniędzy ani nie wpisywano nazwy aplikacji.
- **27:13:** ASR miesza „rewolucję” i „ewolucję”. Zachowano te konkretne słowa, nie wymieniano ich według domyślnej tezy. Poprawiono techniczne „wytwarzanie oprogramowania” i „SaaS”, ale cały sporny fragment trzeba odsłuchać przed cytowaniem.
- **27:13:** „Mieć jakiegoś tura, którego niech tam” i „zrobi zestaw zwolni” — nie odtwarzano. Po cięciu usunięto wyłącznie zakres zapisany w montażu.
- **31:05–32:28:** uwagi o rocznicy i 6 listopada są słowami prowadzących. Nie wykorzystywano ich do samowolnego zmienienia daty premiery #44.
- **33:15:** urwane zdanie i autokorekta żartu o rodzinie — pozostawione; nie cytować bez odsłuchu.

## Weryfikacja zasobów

Dnia 2026-10-28 pobrano i sprawdzono tytuły oficjalnych stron GitHub Copilot, Claude Code, Confluence i repozytorium openai/codex — HTTP 200. Strona `https://openai.com/codex/` zwróciła 403; zamiast udawać jej odczyt, podano oficjalne repozytorium OpenAI. To linki do wspomnianych narzędzi, **nie dowody medyczne, badania przeciążenia ani aktualny fact-check limitów subskrypcji**.
