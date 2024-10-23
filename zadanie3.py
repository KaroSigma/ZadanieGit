"""
Napisać program, który pobiera od użytkownika liczbę całkowitą dodatnią, a na-
stępnie wyświetla na ekranie kolejno wszystkie liczby nieparzyste nie większe od

podanej liczby. Przykład, dla 15 program powinien wyświetlić 1, 3, 5, 7, 9, 11,
13, 15. Rozszerz zadanie, aby użytkownik podał dwie liczby, a program wyświetlił
wszystkie liczby nieparzyste w zakresie między tymi liczbami.

"""
print("1 czesc zadania")
while True:
  liczba = int(input("Podaj 1 liczbe calkowita: dodatnia "))
  if liczba >0: 
    break
  else:
    print("Podales liczbe ujemna. Podaj jeszcze raz: ")

for i in range(1, liczba + 1):
    if i % 2 != 0:
        print(i)
        
print("")
print("2 czesc zadania")

while True:
  liczba1 = int(input("Podaj 1 liczbe calkowita: dodatnia "))
  liczba2 = int(input("Podaj 2 liczbe calkowita: dodatnia "))
  if liczba1 >0 and liczba2 >0: 
    break
  else:
    print("Podales conajmniej jedna liczbe ujemna. Podaj jeszcze raz: ")


for i in range(min(liczba1, liczba2), max(liczba1, liczba2)+1):
    if i % 2 != 0:
        print(i)
