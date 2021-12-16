#inicjalizer
    #jest to specialna metoda, pozwalajaca zainicjowalizowac obiekt jest uruchamiana automatycznie w momencie tworzenia nowej instacji


class Point:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

pl = Point()

print(pl.x, pl.y)


class Point2:
    def __init__(self,x,y) -> None:
        self.x = y
        self.y = y

p2 = Point2(-10,2)
p3 = Point2(-3,-2)

print(p2.x,p2.y,p3.x,p3.y)

class Point3:
    def __init__(self,x=0,y=0) -> None:
        self.x = y
        self.y = y

p4 = Point3(-10,2)
p5 = Point3(-3,-2)

print(p4.x,p4.y,p5.x,p5.y)