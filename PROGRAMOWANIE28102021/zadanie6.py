# listy - struktury danych
# zbiór wartości
# index - rozpoczyna od 0, lista jest strukturą danych mutowanych

mojalista = [1,2,3,4]
print(mojalista)

mojalista2 = [2,5.3,True,"f","OOO"]

mojalista2[4] = False
for i in mojalista2:
    print(i)

print("--------------------------------------")

mojalista2.append("Arek to dzik")
for i in mojalista2:
    print(i)

print("--------------------------------------")

mojalista2.reverse()
for i in mojalista2:
    print(i)

print("--------------------------------------")

mojalista2.sort()
for i in mojalista2:
    print(i)