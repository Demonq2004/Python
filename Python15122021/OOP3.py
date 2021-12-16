class Point:
    def __init__(self, x=0,y=0) -> None:
        self.x = x
        self.y = y

    def dodaj_kordy(self,x=0,y=0) -> int:
        self.x = x
        self.y = y 
        return x + y

p1 = Point(3,5)
print (p1.x,p1.y)
p1.x = 7
p1.y = 12
print (p1.x,p1.y)

wynik = p1.dodaj_kordy(62,21)
print(wynik)