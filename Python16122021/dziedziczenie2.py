class Widget:
    def __init__(self,label) -> None:
        self.label = label


class Button(Widget):
    def __init__(self, label,size) -> None:
        super().__init__(label)
        self.size = size

    def prezentacja(self):
        return "Cześć, to jest dziedziczenie byq"

w = Button("my new button","LARGE")

print(w.size,w.label)
print(w.prezentacja())


widget = Widget("My Widget")
