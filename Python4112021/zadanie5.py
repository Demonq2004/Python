#suma wsztstkich liczb od 1 do 100 i srednia aytmetyczna
zasieg = 101
listaLiczb = [el for el in range(1,zasieg)]
wynik = 0
for el in listaLiczb:
    wynik+=el

wynik = wynik/100
print(wynik)