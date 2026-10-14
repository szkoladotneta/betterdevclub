# Odcinek 42 — materiały redakcyjne

**Tytuł:** AI ma decydować, nie gadać. Microsoft kontra Jev

**Premiera robocza:** 15 października 2026. **Długość z transkrypcji:** około 35:01.

**Status:** szkic, `notPublished: true`; linki do platform pozostają puste.

## Shortsy z nagrania

Timestampy po normalizacji początku transkrypcji Riverside; surowe nagranie ma przesunięcie +0,815 s. Przed cięciem sprawdzić początek i koniec w audio oraz przesunięcia po montażu. Cytaty poniżej są dosłownym wyciągiem ASR, nie zweryfikowanym zapisem audio.

### 1. AI ma zdecydować, a nie gadać
- Autor: Piotrek
- Zakres: 10:52.40–11:26.00 (33.60 s)
- Hook na ekranie: **AI ma zdecydować, a nie gadać**
- Montaż: Sekundy kontra milisekundy — fragment o oczekiwanej przewadze modeli decyzyjnych. Nie podpisywać tego jako pomiaru każdego modelu.

> Odpowiadając na Twoje pytanie co nam to zmienia w zasadzie zupełnie inny mechanizm podejmowania decyzji bo w przeciwieństwie do LLM takie modele są szybkie czyli przestajemy liczyć odpowiedzi w grube sekundy tylko zaczynamy liczyć odpowiedzi w milisekundy czyli jak gdyby jesteś w stanie spytać swojego szefa i To ja muszę pomyśleć, przyjdę do Ciebie z decyzją jutro, tłumacząc to na ludzki, tylko szef Ci mówi od razu tak, nie, nie ma.

### 2. Którego agenta wybrać? Niech zdecyduje model
- Autor: Piotrek
- Zakres: 21:42.23–22:20.00 (37.77 s)
- Hook na ekranie: **Którego agenta wybrać? Niech zdecyduje model**
- Montaż: Routing narzędzi i eskalacja. Pokazać prosty schemat: pytanie → decyzja → narzędzie.

> Ale jak spojrzysz na workflow, jak działają agenci, to to jest ogóle bardzo taki fajny klocek. Z jednej strony, że mi sobie podali jakieś przykłady do bawienia, ale jak mówimy w ogóle o modelu agentowym, to to jest bardzo fajny klocek, który jak gdyby zadajesz pytanie... Model decyzyjny ocenia czego powinien użyć, jakiego toola, jakiego narzędzia, czy powinien to wyeskalować, czy powinien to może dla odmiany odpuścić, bo to nie do Ciebie.

### 3. Lekarz pyta darmowego ChatGPT
- Autor: Kajetan + Piotrek
- Zakres: 28:20.19–28:54.00 (33.81 s)
- Hook na ekranie: **Lekarz pyta darmowego ChatGPT**
- Montaż: Anegdota Kajetana, nie badanie o lekarzach. Zachować dopowiedzenie o niewpisywaniu danych osobowych.

> Byłem ostatnio na trzech różnych wizytach u lekarza. Na szczęście to były bardzo proste wizyty wbrew pozorom. Natomiast na wszystkich tych trzech wizytach lekarz w połowie mniej więcej wizyty powiedział, że zapyta się kogoś mądrzejszego i widziałem jak promptuje czat a GPT. Takiego na darmowej subskrypcji. No daj mą we subskrypcję. Ooo! Tak, tak. Nie wpisywał tam żadnych danych osobowych, na szczęście,

### 4. AI nie wie, czego mu nie powiesz
- Autor: Piotrek
- Zakres: 32:37.50–33:00.80 (23.30 s)
- Hook na ekranie: **AI nie wie, czego mu nie powiesz**
- Montaż: Wywiad medyczny i znaczenie kontekstu. Nie robić z tego porady diagnostycznej.

> Znaczy tylko znowu, zadaniem lekarza jest wygrillowanie Cię i wyciągnięcie z Ciebie tej wiedzy, bo Ty sam, to temu modelowi nie powiesz, że Cię strzyka w kolanie. Znaczy przyjdziesz i powiesz, że Cię strzyka w kolanie, Ale już nie powiesz, że wywaliłeś się wczoraj po schodach, bo uznasz, że a co to ma do rzeczy, przecież tak mnie strzyka w kolanie.

## Teksty na miniaturę — 5 wariantów

### Konkretne

---
AI WYBIERA 🤖
MODEL
ZA CIEBIE
---
LEKARZ
PYTA
CHATGPT?! 🩺
---
SEKUNDY
CZY
MILISEKUNDY? ⚡
---

### Motyw ogólny

---
MNIEJ GADANIA 🛑
WIĘCEJ
DECYZJI 🤖
---
LLM
TO NIE
WYROCZNIA 🤯
---

## Rolki do osobnego nagrania

To pomysły wynikające z odcinka, nie przegląd #znaleziska (brak dostępu do historii kanału).

1. **Piotrek: Router modeli w 30 sekund.** Pokazać enum: tani model / mocny model / człowiek; następnie przykład błędnego routingu. Pointa: routing też wymaga testów i progów eskalacji.
2. **Kajetan: JSON nie gwarantuje dobrej decyzji.** Dwa poprawne składniowo JSON-y z przeciwstawnymi decyzjami. Pointa: oddziel walidację formatu od walidacji jakości decyzji.
3. **Duet: Wynik egzaminu to nie diagnoza.** Pokazać pytanie zamknięte i rozmowę z brakującym kontekstem. Pointa: benchmark nie jest dowodem bezpieczeństwa klinicznego.

## Uwagi przed publikacją

- Data premiery i czas trwania to robocze wartości: kolejny czwartek i zakres transkrypcji, nie długość gotowego montażu.
- Nie podawać początkowych, przybliżonych liczb o MedDecider jako ustalonej skuteczności. Piotrek wraca do wyników w 31:58; wyniki egzaminacyjne nie oznaczają skuteczności diagnostycznej.
- Wzmianki o modelu OpenAI i podstawie modelu „Drex” są w rozmowie niepewne. Nie robić z nich potwierdzonych newsów.
- Korekta nazw i oczywistych terminów w transkrypcji nie zastępuje odsłuchu. Niejednoznaczne frazy pozostają do sprawdzenia.

## Weryfikacja źródeł

- Jev to model TypeSafe AI, nie „Jeff” ani „drzewo”. Microsoft-Decision-1 bazuje na Qwen3.5-9B.
- MedDecider-27B: karta modelu podaje 87,1% na **4722** pytaniach z 26 sesji LEK, a nie 472 pytaniach, jak zapisano w ASR. Na nowych pytaniach autorzy podają 89,2% przy średniej zdających 71,3%. Liczby są deklaracjami autorów; nie były niezależnie reprodukowane. W transkrypcji zachowano liczby z ASR do odsłuchu.
- basal-1.0-4.5B bazuje na Bieliku, nie na Qwenie. Nie zmieniono w transkrypcji spekulacji rozmówców na potwierdzoną wiedzę.
- Drex v1.5 bazuje na MiMo-V2.6-Distill-Qwen-9B; istnieje też Drex DLM z inną bazą. Wersja omawiana w rozmowie pozostaje nieustalona.
- Nie potwierdzono polskiego pochodzenia MedDecider ani tego, że finansowanie TypeSafe ogłoszono tego samego dnia co model Microsoftu.
- Sześć zweryfikowanych linków znajduje się w `resources` wpisu #42 w `episodes.json`.
