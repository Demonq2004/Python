#pętla while i break, continue
#continue uzywamy gdy chcemy pominac np. liczby parzyste

licznik = 0

while licznik < 10:
    licznik += 1
    if licznik % 2 == 0:
        continue
    print(licznik)

licznik2 = 0
while licznik2 < 10:
    licznik2 += 1
    if licznik2 == 5:
        break
    print(licznik2)
