"""
Napisać program, który pobiera od użytkownika ciąg liczb całkowitych. Pobieranie

danych kończone jest podaniem wartości 0 (nie wliczana do danych). W następ-
nej kolejności program powinien wyświetlić sumę największej oraz najmniejszej

z podanych liczb oraz ich średnią arytmetyczną. Rozszerz zadanie, aby program
wyświetlał całą sekwencję liczb wprowadzonej przez użytkownika.
Przykład:
Użytkownik podał ciąg: 1, -4, 2, 17, 0.
Wynik programu:
13 // suma min. i maks.
6.5 // średnia
"""

numery = []
i = int(input("Podaj liczbę: "))
while i != 0:
    numery.append(i)
    i = int(input("Podaj liczbę: "))

print("Pełna podana sekwencja: ", end=" ")
for i in numery:
    print(i, end=" ")
print()
minimalna = min(numery)
maksymalna = max(numery)
print("Minimalna wychodzi: ",minimalna)
print("Maksymalna wychodzi: ",maksymalna)
srednia = round(sum(numery) / len(numery), 2)
print("Srednia wynosi: ",srednia)
