#dopoki nie bedzie break to nie przestanie pytac o cene
while True:
  cena = float(input("Podaj cene towaru w przedziale 100 do 10000 zł: "))
  if cena >= 100 and cena <= 10000:
    break
  else:
    print("Podales zla cene. Podaj od nowa: ")

while True:
    raty = int(input("Podaj ilosc rat miedzy 6 a 48: "))
    if 6 <= raty <= 48:
        break
    else:
        print("Podales zla ilosc rat. Podaj od nowa.")

if raty >= 6 and raty <=12:
  print(" oprocentowanie wynosi 2.5%")
  oprocentowanie = 0.025
elif raty >= 13 and raty <=24:
  print("oprocentowanie wynosi 5%")
  oprocentowanie = 0.05
elif raty >=25 and raty <=48:
  print("oprocentowanie wynosi 10%")
  oprocentowanie = 0.1

kosztzoprocentowaniem = cena + (cena * oprocentowanie)
ratamiesieczna = kosztzoprocentowaniem / raty

print("Rata miesieczna za towar wynosi {1} ",ratamiesieczna)

#Powiedzmy ze wezmie sie produkt za 10000 i 25 rat 
#10 % z 10000 to 1000 czyli kosztzoprocentowaniem wyjdzie 11000
#Pozniej te 11000 podzieli sie przez 25 rat co daje nam wynik 440
