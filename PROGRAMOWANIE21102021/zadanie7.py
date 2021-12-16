x = int(input("Podaj x: "))

if x >= 0:
    y = 0
elif x > -10 and x <= -5:
    y = 1
elif x <= -10:
    y = 2
else:
    y = "Brak zakresu"

wynik = "y = {}".format(y)
print(wynik) 
