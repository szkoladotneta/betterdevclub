# Jak czytac YouTube Studio Analytics - Przewodnik

Przewodnik krok-po-kroku dla Better Dev Club. Otwieraj studio.youtube.com i sprawdzaj te dane co tydzien (najlepiej w poniedzialek rano, ~5 min).

---

## 1. Skad przychodza widzowie (Traffic Sources)

**Gdzie:** YouTube Studio > Analytics > zakladka **Zasieg** (Reach)

**Sciezka:** studio.youtube.com > (lewe menu) Analytics > Zasieg > "Typy zrodel ruchu"

**Co zobaczysz:**
- **Sugerowane filmy (Suggested Videos)** - YouTube poleca cie obok innych filmow. To najlepsze zrodlo wzrostu.
- **Przegladanie (Browse Features)** - YouTube wyswietla cie na stronie glownej. Tez swietne.
- **Wyszukiwanie YouTube (YouTube Search)** - ludzie szukaja tagow/slow kluczowych. Dlatego tagi sa wazne.
- **Zewnetrzne (External)** - LinkedIn, X, Facebook, linki bezposrednie. To Twoja wlasna promocja.
- **Bezposrednie (Direct/Unknown)** - ktos wpisal link lub kliknal z zakladek.

**Na co patrzec:**
- Jesli >60% ruchu to "External" = algorytm YouTube Cie nie poleca. Trzeba poprawic retention.
- Jesli "Suggested Videos" i "Browse Features" rosna = algorytm zaczyna Cie dostrzegac.
- Jesli "YouTube Search" jest wysokie = SEO dziala (tagi, tytuly, opisy).

**Jak sprawdzic dla konkretnego filmu:**
1. YouTube Studio > Zawartosc (Content)
2. Kliknij w konkretny film
3. Kliknij "Statystyki" (Analytics) po lewej
4. Zakladka "Zasieg" (Reach)
5. Przewin do "Typy zrodel ruchu"

---

## 2. Jak dlugo ludzie ogladaja (Retention / Utrzymanie uwagi)

**Gdzie:** YouTube Studio > Zawartosc > (kliknij film) > Statystyki > zakladka **Zaangazowanie** (Engagement)

**Sciezka:** studio.youtube.com > Content > kliknij film > Analytics > Engagement

**Co zobaczysz:**
- Wykres "Utrzymanie uwagi widzow" (Audience Retention) - krzywa pokazujaca % widzow w kazdej sekundzie.
- "Sredni czas ogladalnosci" (Average View Duration) - ile srednio minut ktos ogladal.
- "Sredni % obejrzany" (Average Percentage Viewed) - kluczowy wskaznik.

**Jak czytac wykres retention:**
```
100% |___
     |   \___          <- lekki spadek = normalne
     |       \___
     |           \___  <- plaski = ludzie ogladaja do konca (swietnie!)
     |    ↓ KLIF       <- nagly spadek = cos poszlo nie tak (nudne, zbyt dlugie wstepy)
  0% |________________
     0:00        koniec
```

**Na co patrzec:**
- **Klif w pierwszych 30 sekundach** = problem z "hakiem" (hookiem). Ludzie odchodza, bo intro jest nudne.
- **Klif w polowie** = srodek odcinka sie dluzy. Rozwaz krotsze odcinki lub lepsze przejscia miedzy tematami.
- **Plaski wykres od srodka** = ludzie ktory zostali, ogladaja do konca. Dobrze!
- **Szpilki w gore** = ludzie przewijaja DO tego momentu (ciekawy fragment). Rozwazyc Short z tej chwili.

**Cel:** 40-50% sredniej retention dla podcastu IT (obecnie ~25-35%, poprawa w ostatnich odcinkach).

---

## 3. Kto sie zapisuje i kto odchodzi (Subscriber Funnel)

**Gdzie:** YouTube Studio > Analytics > zakladka **Odbiorcy** (Audience)

**Sciezka:** studio.youtube.com > Analytics > Audience

**Co zobaczysz:**
- "Subskrybenci" - ile nowych subskrybentow i ile straconych (w wybranym okresie)
- Kliknij "Wiecej" (See More) przy subskrybentach
- Przelacz widok na **poszczegolne filmy** aby zobaczyc ktore filmy zyskuja/traca subs

**Gdzie zobaczyc unsubscribes:**
1. Studio > Analytics > Audience
2. Kliknij "Wiecej" (See more) w sekcji subskrybentow
3. W tabeli zobaczysz "Zyskani subskrybenci" i "Utraceni subskrybenci" per film
4. Jesli konkretny film ma duzo unsubscribes = widzowie nie dostali tego, czego sie spodziewali po tytule/miniaturce

**Na co patrzec:**
- Ktory film przynosi najwiecej subskrypcji? (wiecej takich tematow!)
- Ktory film traci subskrybentow? (sprawdz czy tytul/miniaturka nie sa "clickbait" lub temat odbiega od normy)
- Stosunek nowi vs utraceni = tempo netto wzrostu

---

## 4. CTR (Click-Through Rate) - Czy miniaturka dziala?

**Gdzie:** YouTube Studio > Analytics > Zasieg (Reach)

**Lub per film:** Content > kliknij film > Analytics > Reach > "Wyswietlenia vs CTR"

**Co to jest:** % osob ktore WIDZIALY miniaturke i KLIKNELY w niej.

**Benchmarki:**
- 2-3% = slabo (wczesne odcinki BDC)
- 4-6% = przyzwoicie (wiekszosc kanalow)
- 7-10% = bardzo dobrze (obecny #19 = 7.27%)
- >10% = wyjatkowo (zwykle virale)

**Na co patrzec:**
- CTR spada z czasem (to normalne - YouTube testuje coraz szersza publicznosc)
- CTR pierwszych 48h jest najwazniejsze
- Jesli CTR < 3% = zmien miniaturke lub tytul (nawet po publikacji!)

---

## 5. Impressions - Ile razy YouTube Cie pokazuje

**Gdzie:** YouTube Studio > Analytics > Zasieg > "Wyswietlenia" (Impressions)

**Co to jest:** Ile razy YouTube POKAZAL Twoja miniaturke (nie ile razy ktos kliknal).

**Kluczowa zasada:** Wiecej impressions = YouTube ufa Twojemu content'owi.
YouTube daje impressions filmom z dobrym retention i CTR.

**Schemat dzialania algorytmu:**
```
Nowy film -> YouTube pokazuje 100 widzom
   |
   v
Dobry CTR + dobry retention? -----> TAK -> YouTube pokazuje 1000 widzom
   |                                        |
   NO                                       v
   |                                 Nadal dobry? -> TAK -> 10,000+
   v                                        |
Algorytm przestaje                          NO -> Zatrzymuje sie
polecac film
```

**Dlaczego to wazne:** Ep #18 dostal tylko 1,406 impressions (vs #19 = 2,297). YouTube nie polecal #18 bo:
- Brakowal tagow (dodano pozniej)
- Tytul zmieniano kilka razy (algorytm nie lubi zmian po publikacji)
- Temat (polityka/geopolityka) mogl nie pasowac do oczekiwan widzow IT

---

## 6. Cotygodniowy audyt (5 minut, poniedzialek rano)

1. **Otworz** studio.youtube.com > Analytics
2. **Ustaw zakres** na "Ostatnie 7 dni"
3. **Sprawdz:**
   - [ ] Impressions: rosna, spadaja czy stale? (zakladka Reach)
   - [ ] CTR ostatniego filmu: > 5%? (zakladka Reach)
   - [ ] Average View Duration: > 40% dlugosci filmu? (zakladka Engagement)
   - [ ] Traffic Sources: czy "Suggested" i "Browse" rosna? (zakladka Reach)
   - [ ] Subskrybenci netto: + ile w tym tygodniu? (zakladka Audience)
4. **Zapisz** w notatce (Excel/Notion/karteczka) 5 liczb:
   - Impressions, CTR, Avg Retention %, Nowi subs, Zrodlo #1 ruchu
5. **Porownaj** z poprzednim tygodniem

---

## 7. Szybkie skroty w YouTube Studio

| Chce zobaczyc... | Sciezka |
|------------------|---------|
| Ogolny dashboard | studio.youtube.com > Dashboard |
| Statystyki konkretnego filmu | Content > kliknij film > Analytics |
| Retention wykres | Content > film > Analytics > Engagement |
| Skad ruch | Analytics > Reach > Traffic Source Types |
| Kto subskrybuje/odchodzi | Analytics > Audience > See more (przy subscribers) |
| CTR + Impressions | Analytics > Reach |
| Porownanie filmow | Analytics > See More > Compare To |
| Real-time dane (ostatnie 48h) | Analytics > Overview > Realtime card |

---

*Przewodnik dla Better Dev Club - 2026-03-13*
