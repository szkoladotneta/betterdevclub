# BDC45 — weryfikacja oficjalnych źródeł

Data sprawdzenia: **2026-11-04 (UTC)**. Odczytano pełne strony źródłowe, nie tylko wyniki wyszukiwania. ASR porównano wyłącznie z relacją przekazaną w zleceniu; nie odsłuchiwano nagrania.

## 1. Deno → Cloudflare

**Potwierdzone, ogłoszenie 9 października 2026:** cały zespół Deno przechodzi do Cloudflare; wspólny komunikat opisuje połączenie prac nad `celld` i `workerd` oraz rozwój samodzielnego hostowania Workers i Durable Objects.[4][8]

- Runtime: jeszcze **rok wsparcia**, z **comiesięcznymi wydaniami zawierającymi poprawki błędów i bezpieczeństwa**; potem zespół kończy jego rozwój, ale kod pozostaje open source.[4]
- Deploy: będzie działać jeszcze **sześć miesięcy**, po czym zostanie wyłączony; płacący klienci mają otrzymać pomoc w migracji do Workers.[4]
- **Korekta ASR:** prawidłowa nazwa to **`celld`**, nie „Shell D” ani „shelld”; projekt już istnieje, a plan obejmuje połączenie jego kodu i pomysłów z `workerd`, nie budowę od zera.[8]
- Sformułowanie „przejęcie” pasuje do klasyfikacji wpisu Cloudflare jako „Acquisitions”, ale najściślejszy opis treści to „cały zespół Deno dołącza do Cloudflare”; komunikaty nie podają ceny ani szczegółów transakcji.[4][8]

**Ocena ASR:** okresy 12 i 6 miesięcy zgodne, z doprecyzowaniem, że rok runtime obejmuje także bugfixy, a sześć miesięcy Deploy oznacza działanie usługi do zamknięcia, nie sam okres aktualizacji bezpieczeństwa.[4]

## 2. Cal.com / Cal.diy

**Potwierdzone, ale data wcześniejsza niż październik:** założyciel Bailey Pumfleet ogłosił zmianę **14 kwietnia 2026**, a techniczny opis opublikowano **15 kwietnia 2026**.[15][13]

- Produkcyjny kod Cal.com przeniesiono do prywatnego repozytorium; publiczne repozytorium stało się **`calcom/cal.diy`**, otwartą wersją społecznościową do self-hostingu, z usuniętymi funkcjami komercyjnymi/enterprise i licencją zmienioną z AGPL 3.0 na MIT.[13]
- **Deklarowany powód to bezpieczeństwo**, zwłaszcza skanowanie publicznego kodu pod kątem podatności przez AI oraz ochrona danych klientów; nie walka z klonowaniem produktu.[15]
- **Ważne rozróżnienie:** to argumentacja firmy, nie niezależny dowód, że zamknięty kod jest bezpieczniejszy; Cal.diy nie zostało zamknięte, lecz pozostało open source.[15][13]
- Dokumentacja Cal.diy, z datą aktualizacji **18 października 2026**, zaleca je wyłącznie do osobistego, nieprodukcyjnego użytku i ostrzega o braku gwarancji bezpieczeństwa.[6]

**Ocena ASR:** motyw „security, nie klonowanie” zgodny z aktualnym ogłoszeniem; skrót „Cal.com i Cal.diy zamknięte” byłby błędny, ponieważ zamknięto produkcyjną gałąź Cal.com, a nie Cal.diy.[15][13]

## 3. Pico CSS

**Potwierdzone:** oficjalna dokumentacja mówi, że projekt nie jest już utrzymywany, **v2.1.1 jest ostatnim wydaniem**, repozytoria zarchiwizowano i nie będzie nowych zgłoszeń, PR-ów ani wydań; strona, npm i CDN pozostają dostępne.[5]

**Przyczyny według autora:** AI potrafi generować samodzielny HTML z potrzebnym CSS, więc sens takiego minimalnego frameworka maleje; dalszy rozwój wymagałby pełnego przepisania na nowoczesny CSS zamiast Sass, m.in. z OKLCH, cascade layers, Popover i anchor positioning oraz własnym kompilatorem usuwającym nieużywany CSS.[5]

**Ocena ASR:** „stary Sass kontra modern CSS” oddaje część wyjaśnienia, lecz pomija wskazany przez autora kontekst AI; autor nie twierdzi, że Sass sam w sobie przestał działać.[5]

**Data:** odczytana strona nie podaje daty ogłoszenia. Nie potwierdzono dokładnego dnia zakończenia utrzymania ani jego przypisania do października 2026.

## 4. ArtCraft jako alternatywa dla Adobe

**Potwierdzony projekt:** oficjalna rodzina **ArtCraft Crafting Apps** obejmuje natywne, darmowe narzędzia open source napisane w Rust do edycji zdjęć, wektorów, wideo, PDF, motion graphics i składu publikacji, dostępne na macOS, Windows i Linux; autor deklaruje brak Electron/webview.[10]

**Konkret:** PhotoCraft to edytor obrazów z warstwami, maskami i obsługą warstwowych PSD/PSB, ale oficjalnie nadal oznaczony jako **early alpha**; wiele pozostałych programów ma status „in development”.[17][10]

**Zastrzeżenie redakcyjne:** „alternatywa dla Adobe” jest zasadnym skrótem opisującym obszar zastosowań, nie potwierdzeniem pełnej zgodności, dojrzałości ani równoważności z całym pakietem Adobe; osobny produkt ArtCraft Studio służy generowaniu obrazów i wideo, więc nie należy mylić go z rodziną Crafting Apps.[9][10]

**Data:** oficjalne odczytane strony aplikacji nie podają daty premiery rodziny. Nie przypisuję im konkretnego dnia startu w październiku 2026; powyżej opisano stan odczytany 4 listopada.

## 5. Paint.NET — czy tylko Windows?

**Nie używać bezwarunkowego „tylko Windows” w odniesieniu do całego stanu projektu w październiku 2026.** Oficjalny wpis autora z **24 października 2026**, dotyczący **Paint.NET 5.2 Beta, build 9793**, udostępnia eksperymentalne kompilacje dla **Wine na Linuxie** i dodaje, że mogą działać również na Macu, choć nie jest to główny cel prac.[18]

Bezpieczne sformułowanie do odcinka: **„Paint.NET jest aplikacją kojarzoną z Windows; w becie 5.2 są już eksperymentalne wydania uruchamiane przez Wine na Linuxie, z możliwością działania na Macu — to nie deklaracja natywnego, stabilnego portu”.**[18]

## Ograniczenia i ślad sprawdzenia

Główna witryna getpaint.net zwracała HTTP 406, ale udało się odczytać bieżący oficjalny blog autora. Wyszukiwarki Google i DuckDuckGo zwracały ekran zgód/challenge; źródła Cal.com odnaleziono również przez oficjalną mapę witryny. Nie publikowano niczego i nie zmieniano repozytoriów. Kopie tekstu stron i rejestr cytowań zapisano w katalogu `bdc45-evidence/` obok raportu.

## Sources

[4] https://deno.com/blog/cloudflare
    > "We will support the Deno runtime for another year with monthly releases containing bug fixes and security updates."
    > "Deno Deploy will continue operating for six months before shutting down."
    > "Today we’re announcing that the entire Deno team is joining Cloudflare to take that work further."
    > "JSR will continue operating, with its infrastructure moving to Cloudflare."
[5] https://picocss.com/docs/maintenance
    > "v2.1.1 is the final release."
    > "Today, AI can generate lightweight, standalone, accessible HTML with just the CSS it needs, so a Minimal CSS Framework for Semantic HTML matters less than it used to."
    > "plain modern CSS instead of Sass"
    > "The repositories are archived. No new issues, PRs or releases."
[6] https://cal.diy
    > "Last updated on October 18, 2026"
    > "Cal.diy is community maintained and strictly recommended for personal, non-production use."
[8] https://blog.cloudflare.com/deno-joins-cloudflare
    > "October 9, 2026"
    > "This will involve merging code and ideas from celld back into workerd."
[9] https://getartcraft.com
    > "ArtCraft makes two things: the Crafting Apps and ArtCraft Studio."
[10] https://getartcraft.com/apps
    > "Native, open-source apps from the ArtCraft team, built in Rust and free to use."
    > "Photo Craft The open-source image editor you already know how to use. Early alpha"
    > "No Electron, no web views."
[13] https://cal.com/blog/cal-diy-open-source-to-closed-source
    > "Apr 15, 2026"
    > "We moved Cal.com's production codebase from a public repository to a private one."
    > "We changed Cal.diy's license from AGPL 3.0 to MIT."
[15] https://cal.com/blog/cal-com-goes-closed-source-why
    > "Apr 14, 2026"
    > "Today, we are making the very difficult decision to move to closed source, and there’s one simple reason: security."
    > "Today, AI can be pointed at an open source codebase and systematically scan it for vulnerabilities ."
[17] https://getartcraft.com/apps/photocraft
    > "Image editor · Early alpha"
    > "Opens and saves layered PSD and PSB documents."
[18] https://blog.paint.net/2026/10/24/paint-net-5-2-beta-build-9793
    > "For Linux, the experimental builds for Wine can be downloaded here . It can also work on Mac but that is not the primary focus at this time."
