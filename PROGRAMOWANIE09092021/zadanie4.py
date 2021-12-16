
import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

dodawanie = int(a+b)
odejmowanie = int(a-b)
mnozenie = int(a*b)
potegowanie = int(a**b)
pierw1 = float(math.sqrt(a))
pierw2 = float(math.sqrt(b))


if b!=0:
    dzielenie = float(a/b)
else:
    dzielenie = "Nie dziel przez 0!"

if b!=0:
    dzielenie2 = int(a//b)
else:
    dzielenie2 = "Nie dziel przez 0!"

if b!=0:
    modulo = int(a%b)
else:
    modulo = "Nie dziel przez 0!"



print("wynik dodawania = " + str(dodawanie))
print("wynik odjemowania = " + str(odejmowanie))
print("wynik mnozenia = " + str(mnozenie))
print("wynik dzielenia = " + str(dzielenie))
print("wynik dzielenia = " + str(dzielenie2))
print("wynik potegowania = " + str(potegowanie))
print("wynik modulo = " + str(modulo))
print("wynik pierwiastek liczby a = " + str(pierw1))
print("wynik pierwiastek liczby b = " + str(pierw2))