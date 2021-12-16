#utworz liste z przedziału od 100 do 200, wyznacz sume liczb nieparzystych, wartosc srednia arytmetyczna, geometryczna
import math
lista = [v for v in range(100,201)]
nieparzyste = 0
for i in lista:
    if i % 2 == 0:
        continue
    nieparzyste += i

print(nieparzyste)

geometryczna = 1

for i in lista:
    geometryczna *= i

print(math.sqrt(geometryczna))
arytmetyczna = 0
for i in lista:
    arytmetyczna += i

print(arytmetyczna/100)