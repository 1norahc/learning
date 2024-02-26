# System rekomendacyjny filmówśśś

Napisz program w języku Python, który będzie działał jako prosty system rekomendacyjny filmów na podstawie ocen użytkowników. System powinien składać się z następujących kroków:

1. **Zbieranie danych**: Program powinien umożliwiać użytkownikowi wprowadzenie ocen dla kilku filmów w skali od 1 do 5 (gdzie 1 to najniższa ocena, a 5 to najwyższa ocena). Dane można przechowywać w formie słownika, gdzie kluczem będzie nazwa filmu, a wartością lista ocen.
2. **Obliczanie podobieństwa użytkowników**: Wykorzystaj algorytm obliczania podobieństwa kosinusowego między ocenami użytkowników w celu określenia, które oceny są najbardziej zbliżone do ocen użytkownika, dla którego chcemy zrobić rekomendacje.
3. **Rekomendowanie filmów**: Na podstawie ocen użytkowników podobnych do danego użytkownika, program powinien zaproponować filmy, które nie zostały jeszcze ocenione przez tego użytkownika, ale które zostały wysoko ocenione przez innych użytkowników podobnych do niego.
4. **Wyświetlanie rekomendacji**: Program powinien wyświetlić użytkownikowi listę rekomendowanych filmów wraz z ich tytułami i ewentualnie prosić użytkownika o ocenę tych filmów.

Możesz również zaimplementować dodatkowe funkcjonalności, takie jak:

* Obsługa nowych użytkowników poprzez proste pytanie o preferencje filmowe.
* Zastosowanie zaawansowanych metod obliczania podobieństwa, takich jak metoda k najbliższych sąsiadów (kNN) lub inne techniki uczenia maszynowego.
* Tworzenie interfejsu użytkownika graficznego (GUI) lub aplikacji internetowej.

To zadanie wymaga implementacji algorytmów obliczania podobieństwa użytkowników oraz algorytmów rekomendacji. Możesz wykorzystać biblioteki takie jak NumPy do obliczeń numerycznych, pandas do manipulacji danymi, a także scikit-learn lub inne biblioteki do uczenia maszynowego w celu zastosowania bardziej zaawansowanych technik.

## Matematyka
![matematyka](/img/cosine_similarity.png)

### AD. 1 Zbieranie danych

### AD. 2 Algorytm obliczania podobienstwa kosinusowego (cosine algorithm)

TODO:

* [X]  Ad. 1 Zbieranie danych
  * [X]  Pobieranie uzytkownika
  * [X]  Tworzenie danych "User: {"movie": "rate_num"}"
  * [X]  zapisywanie danych do pliku .json
  * [X]  klasa do tworzenia fakeowych uzytkownikow
* [ ]  Ad. 2 Obliczanie podobienstwa uzytkownikow
* [ ]  Ad. 3 Rekomendowanie filmow
* [ ]  Ad. 4 Wyswietlanie rekomendacji
