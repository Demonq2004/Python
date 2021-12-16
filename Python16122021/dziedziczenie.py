class Widget:
    name = "Dawid"
    nazwisko = "Grzegorzek"
    def __init__(self,label) -> None:
        self.label = label

    def info(self) -> str:
        return Widget.nazwisko


# w = Widget("My new Widget")
# print(w.label)

class Button(Widget):
    pass

w =  Button("Kochamy Was!")
print(w.label)
print(w.info)