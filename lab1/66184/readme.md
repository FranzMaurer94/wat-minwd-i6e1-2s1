Zad
Rudnik Jakub I6E1S1
Python biblioteka PuLp

Tre��:

Jednostkowe nak�ady �rodk�w na produkcje wyrob�w przedstawiono w tabeli. Znaj�c zysk ze
sprzeda�y jednostki ka�dego z wyrob�w (ostatni wiersz) wyznaczy� optymalne z punktu widzenia
zysk�w rozmiary produkcji.

|      | 1  | 2  | 3  | 4  | �rodki produkcja |
|---   |--- |--- |--- |--- |---               |
| A    | 15 | 10 | 20 | 19 | 26000            |
| B    | 9  | 3  | 5  | 10 | 100000           |
| Zysk | 6  | 3  | 5  | 2  |                  |

Zbuduj model matematyczny i rozwi�� zadanie metod� geometryczn�.

Opis zmiennych:

x1 - zbi�r produkt�w nr 1
x2 - zbi�r produkt�w nr 2
x3 - zbi�r produkt�w nr 3
x4 - zbi�r produkt�w nr 4

Funkcja celu:

6x1 + 3x2 + 5x3 + 2x4 -> MAX

Ograniczenia:

A: 15x1 + 10x2 + 20x3 + 19x4 <= 26000
B: 9x1 + 3x2 + 5x3 + 10x4 <= 100000

Rozwi�zanie:

x1 = 1733
x2 = 0
x3 = 0
x4 = 0

Cel = 10398

Instalacja:
W folderze uruchomi� w terminal nast�pnie wpisa� nast�puj�ce komendy: 
1) pip install -r req.txt
2) python modelowanie.py

