# Better Dev Club 043 — weryfikacja źródeł

Stan: 2026-10-21. „Potwierdzone” oznacza zgodność z publikacją autora, nie niezależny audyt pomiarów. Notatka nie zmienia wypowiedzi ani transkrypcji.

## Anthropic / Scion

Oficjalny artykuł **„Redesigning source control at Anthropic”**, opublikowany 13.10.2026, z aktualizacją 15.10: Anthropic deklaruje pełną migrację swojego monorepo z Gita do wewnętrznego Scion w pięć miesięcy. Zastrzega: „Scion is by no means a suitable replacement for git for general use”. Nie jest to ogłoszenie uniwersalnego następcy Gita.[1]

| Twierdzenie z odcinka | Wynik weryfikacji |
| --- | --- |
| 30 tys. commitów dziennie | **Doprecyzowanie:** tekst mówi „as of September, we merged over 30,000 per day”, czyli **ponad 30 tys. scalonych zmian dziennie**, wobec ok. 2500 w maju 2026. Nie podaje liczby funkcjonalności ani wszystkich commitów agentów.[1] |
| Developer: pull latest 87 → 3,5 s | **Potwierdzone** na oficjalnym wykresie.[2] |
| Agent: new worktree 7,1 min → 5 s | **W przybliżeniu poprawne**; dokładnie **5,1 s**.[2] |
| Source control per change request 34 → 3,7 min | **Potwierdzone**, ale dla **środowisk agentowych**, nie programistów.[2] |
| 11 tys. agentogodzin dziennie | Wykres podaje **≈11 000 agent hours a day** obok redukcji 34 → 3,7 min: jest to deklarowana **oszczędność czasu**, nie liczba agentów ani całkowity czas ich pracy.[2] |

Wykres „Everyday source control commands on the monorepo” opisuje czasy jako **Median time** i rozdziela środowiska developerów, agentów oraz CI. Przykładowo agentowe „pull latest” wynosi **3,0 min → 9,0 s**, nie 87 → 3,5 s; tych kategorii nie należy mieszać.[2]

### Rozbieżności wymagające ostrożności w promocji

- **„Przy tym monorepo pracuje siedem osób” (ASR, 37:30): niepotwierdzone w takim znaczeniu.** Artykuł mówi: „A team of seven people built both Scion and Antique”, a także około sześciu powiązanych systemów i przeprowadził migrację. Siedem osób to zespół budujący narzędzia, nie deklarowana liczba wszystkich pracujących w monorepo. Możliwy błąd ASR lub skrót myślowy; sprawdzić audio, nie podmieniać po cichu sensu wypowiedzi.[1]
- **„Skopiowali Scion” (okolice 18:38): brak potwierdzenia zarzutu.** Oficjalna aktualizacja przyznaje wcześniejszy dorobek Google Piper i Meta Sapling; przypis wskazuje serwer **Mononoke** oraz model **Bonsai**: „It pioneered many of the techniques we use in Scion, in particular the Bonsai data model”. To potwierdza inspirację i wcześniejsze rozwiązania, ale nie dowodzi kopiowania kodu ani plagiatu. Nie przedstawiać plotki jako faktu.[1]

## Reverse Engineer Anything

Oficjalne repozytorium to **morluto/rea**, nie dowolny fork o podobnej nazwie. README przedstawia projekt jako narzędzia/MCP dla agentów do analizy binariów, aplikacji i zachowania w runtime; wspomina m.in. Hopper, Ghidra i IDA. Zastrzega legalne, autoryzowane zastosowania.[3]

**Nie potwierdzono** zdania z 17:52, że projekt „powstał po to, żeby cały pakiet Adobe przepisać od nowa”. Obecne oficjalne README nie podaje takiej genezy; jako przykłady pokazuje DX-Ball, Notion i TH04. Bez wypowiedzi autora o genezie nie używać tej tezy jako faktu.[3]

## Marc Lou / beehiiv / MailCheap

- **Potwierdzona relacja autora, 09.10.2026:** Marc Lou ogłosił własną platformę newsletterową po podwyżkach beehiiv. Podał pierwszy rachunek roczny **1000 USD**, przyszły **4000 USD**, oraz szacowany koszt własnego rozwiązania **poniżej 300 USD/rok**, opartego o **AWS SES + MongoDB**. Cytat: „My future bill would have been $4,000. Now I'm using AWS SES + MongoDB, and I will pay less than $300/year”. To jego rachunki i prognoza, nie zweryfikowana oszczędność dla każdego użytkownika.[4]
- Produkt nazywa się **MailCheap**. Oficjalna strona łączy historię odejścia z beehiiv z produktem i linkuje powyższy post; repozytorium **marclou/mailcheap** potwierdza otwarty kod (AGPL-3.0), self-hosting oraz integrację z Amazon SES.[5][6]
- **Nie potwierdzono** dokładnie „napisał przez weekend” ani przychodu **około 190 USD** z 29:34. Post mówi „It took a few prompts”, co nie jest informacją o czasie kalendarzowym. Nie utożsamiać przychodu ze zyskiem.
- Hasło „płacisz za wysłane maile, nie za subskrybentów” oddaje pozycjonowanie produktu, ale nie oznacza braku abonamentu: aktualna strona pokazuje plany miesięczne od **19 USD za 20 tys. maili**, a README wspomina także limity aktywnych subskrybentów w planach Cloud. Self-hosting i płatny hosting to różne oferty.[5][6]

## Amazon SES

AWS potwierdza model rozliczania zużycia. Aktualny cennik rozróżnia **à la carte: 0,10 USD / 1000 maili wychodzących** oraz plany, np. **Essentials: 0,16 USD / 1000** w pierwszym progu. Dochodzą m.in. opłaty za dane i opcjonalne funkcje; nie przedstawiać 0,10 USD jako pełnego kosztu infrastruktury newslettera.[7]

W odcinku Kajetan mówi o SES we własnym rozwiązaniu (33:33). Dokumentacja AWS potwierdza możliwości usługi i ceny, **nie potwierdza prywatnej konfiguracji Kajetana**. Twierdzenie „większość świata wysyła przez Amazon” (33:50) pozostaje niezweryfikowane — brak źródła udziału rynkowego.

## Źródła

[1] Anthropic — artykuł i aktualizacja: https://www.anthropic.com/research/redesigning-source-control

[2] Oficjalny wykres benchmarków osadzony w [1], odczytany także wizualnie: https://www-cdn.anthropic.com/images/4zrzovbb/website/c706fa6efb4b9e5cd2566cb080acbfce7218042d-3840x4684.png

[3] REA — oficjalne README: https://github.com/morluto/rea/blob/main/README.md

[4] Marc Lou — pierwotne ogłoszenie na X, 09.10.2026: https://x.com/marclou/status/2108509543810605218

[5] MailCheap — oficjalna strona i opis genezy: https://mailcheap.ai

[6] MailCheap — oficjalne README: https://github.com/marclou/mailcheap/blob/main/README.md

[7] AWS — oficjalny cennik SES: https://aws.amazon.com/ses/pricing/
