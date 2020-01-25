Zad
Rudnik Jakub I6E1S1
Python biblioteka PuLp

Treœæ:

Jednostkowe nak³ady œrodków na produkcje wyrobów przedstawiono w tabeli. Znaj¹c zysk ze
sprzeda¿y jednostki ka¿dego z wyrobów (ostatni wiersz) wyznaczyæ optymalne z punktu widzenia
zysków rozmiary produkcji.

|      | 1  | 2  | 3  | 4  | Œrodki produkcja |
|---   |--- |--- |--- |--- |---               |
| A    | 15 | 10 | 20 | 19 | 26000            |
| B    | 9  | 3  | 5  | 10 | 100000           |
| Zysk | 6  | 3  | 5  | 2  |                  |

Zbuduj model matematyczny i rozwi¹¿ zadanie metod¹ geometryczn¹.

Opis zmiennych:

x1 - zbiór produktów nr 1
x2 - zbiór produktów nr 2
x3 - zbiór produktów nr 3
x4 - zbiór produktów nr 4

Funkcja celu:

6x1 + 3x2 + 5x3 + 2x4 -> MAX

Ograniczenia:

A: 15x1 + 10x2 + 20x3 + 19x4 <= 26000
B: 9x1 + 3x2 + 5x3 + 10x4 <= 100000

Rozwi¹zanie:

x1 = 1733
x2 = 0
x3 = 0
x4 = 0

Cel = 10398

Instalacja:
W folderze uruchomiæ w terminal nastêpnie wpisaæ nastêpuj¹ce komendy: 
1) pip install -r req.txt
2) python modelowanie.py

