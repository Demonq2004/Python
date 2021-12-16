#Atrybut klasy kontraAtrybut instancji
class Point:
    points_counter = 0

    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y
        Point.points_counter +=1
    
    def dodaj_nowe_koordynaty(self,x=0,y=0):
        self.x = x
        self.y = y

p1 = Point(3,5)
p2 = Point(5,6)
p2.points_counter = 12

print(p2.points_counter)
print(Point.points_counter)