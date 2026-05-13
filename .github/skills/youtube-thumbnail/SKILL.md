---
description: Generuje krótkie, angażujące i łamiące wiersze teksty na miniatury (okładki) YouTube w stylu Better Dev Club. Wykorzystuj ten skill, gdy użytkownik prosi o teksty na okładkę YT.
---

# Generowanie Tekstów na Miniatury YouTube (Better Dev Club)

Kiedy użytkownik prosi o propozycje tekstów na okładkę (miniaturkę) na YouTube, zastosuj się do poniższych, bardzo restrykcyjnych zasad formatowania i stylu wypracowanych dla kanału Better Dev Club.

## Zasady Stylu i Formatowania
- **Zwięzłość:** Teksty muszą być ekstremalnie krótkie, skompresowane do niezbędnego minimum. Zwykle 1-3 słowa w jednej linii.
- **Układ Pionowy (Blokowy):** Łam tekst na 3 do 5 krótkich linii. Używaj spacji, aby wizualnie oddzielać i wyrównywać słowa.
- **Wersaliki (ALL CAPS):** Używaj wielkich liter dla maksymalnej czytelności na małych ekranach (z rzadkimi wyjątkami dla specyficznych słów, jeśli wymaga tego branding).
- **Emotikony:** Dodawaj pojedyncze, wymowne emotikony na końcach kluczowych wierszy (np. 🔥, 🚀, 🤖, 🛑, ✅, 🤷‍♂️, 💸).
- **Kontrasty i Konflikty:** Wykorzystuj formaty budujące napięcie, np. stawianie pojęć naprzeciw siebie (używając zwrotów takich jak `V.S.`), lub zadawanie krótkiego, prowokacyjnego pytania.

## Szablon Prezentacji Wyników
Zawsze generuj **dokładnie 5 różnych propozycji**, oddzielając je od siebie znacznikami `---`.

### Przykłady docelowego formatu:

---
Andrzej Krzywda
DDD,   TDD
I   Eventy
Oraz  A.I.
---

---
Opus 4.7 
Za  $$$$
V.S.
KIMI 2.6
za “FREE”
---

---
GIT PUSH
I   DO
DOMU? 🏠
A   PROD
LEŻY 🔥
---

## Proces Tworzenia (Workflow)
1. **Analiza Kontekstu:** Przeanalizuj agendę, tytuł odcinka (np. z pliku `episodes.json`) lub dostarczony plik transkrypcji JSON. Zidentyfikuj główny "haczyk" (tę najciekawszą, najbardziej kontrowersyjną lub klikalną rzecz z materiału).
2. **Ekstrakcja Słów Kluczowych:** Wyciągnij kluczowe, mocne słowa (np. AI, Deploy, Zero Day, MCP, Tokeny).
3. **Generowanie Wariantów:** Ułóż słowa kluczowe w 5 blokowych formach, pamiętając, by spójniki i krótkie wyrazy (I, DO, A) izolować tak, aby te "najważniejsze" (jak PROD, LEŻY) mogły zostać wyróżnione przez użytkownika innym kolorem.
