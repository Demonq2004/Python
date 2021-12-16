#Tuples - struktura danych przypominającą liste, posiada index, rozpoczyna index od 0,posiada dane mieszane, 
# ale jest strukturą nie mutowalaną co nie pozwala edytować danych,
#stosujemy do zestawów danych których nie chcemy edytować, 


mojaTupla = (1,2,3,5,4,6,7,5)
print(mojaTupla)

nowaTupla = mojaTupla[:5]
print(nowaTupla)

print(len(mojaTupla))

for el in mojaTupla:
    if el == 5:
        print("Posiada 5 w tablicy")
        break
    else:
        print("Nie ma")