"""
Napisać program, który wczytuje od użytkownika liczbę całkowitą dodatnią n, a
następnie wyświetla na ekranie wszystkie potęgi liczby 2 nie większe, niż podana
liczba. Przykładowo, dla liczby 71 program powinien wyświetlić:
1
2
4
8
16
32
64
Dodaj możliwość wybrania dowolnej liczby bazowej, aby program wyświetlał jej
potęgi do określonej wartości.
"""

while True:
  n = int(input("Podaj 1 liczbe calkowita dodatnia: "))
  if n >0: 
    break
  else:
    print("Podales liczbe n ujemna. Podaj jeszcze raz: ")

bazowa = int(input("Podaj liczbę bazową : "))

poczatek = 1

while poczatek <= n:
    print(poczatek)
    poczatek *= bazowa

