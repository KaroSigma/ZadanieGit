"""1. Napisać program, który oblicza wartość współczynnika BMI (ang. body mass
index) wg. wzoru: waga

wzrost2 . Jeżeli wynik jest w przedziale (18,5 - 24,9) to wypisu-
je ”waga prawidłowa”, jeżeli poniżej to ”niedowaga”, jeżeli powyżej ”nadwaga”.

Program powinien sprawdzić, czy podane dane są dodatnie. W przypadku nie-
prawidłowych danych, program powinien poinformować użytkownika i poprosić o

ponowne wprowadzenie.
"""

waga = float(input("Podaj wage: "))
while waga < 0:
  waga = float(input("Podales na minusie. Podaj wage jeszcze raz: "))
wzrost = float(input("Podaj wzrost: "))
while wzrost < 0:
  wzrost = float(input("Podales na minusie. Podaj wzrost jeszcze raz: "))

bmi = waga/(wzrost*wzrost)
if bmi >= 18.5 and bmi <=24.9:
  print("waga prawidłowa")
elif bmi < 18.5:
  print("niedowaga")
elif bmi > 24.9:
  print("nadwaga")
