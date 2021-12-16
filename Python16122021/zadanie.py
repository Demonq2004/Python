class Operacje:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def wybor(self,w):
        if w == '+':
            wynik = Dodawanie(self.a,self.b)
            pokaz = "Wynik dodawania = "+str(wynik.wynik())
            return pokaz
        if w == '-':
            wynik = Odejmowanie(self.a,self.b)
            pokaz = "Wynik odejmowania = "+str(wynik.wynik())
            return pokaz
        if w == '*':
            wynik = Mnozenie(self.a,self.b)
            pokaz = "Wynik mnozenia = "+str(wynik.wynik())
            return pokaz
        if w == '/':
            wynik = Dzielenie(self.a,self.b)
            pokaz = "Wynik dzielenia = "+str(wynik.wynik())
            return pokaz
        if w == '**':
            wynik = Potegowanie(self.a,self.b)
            pokaz = "Wynik potegowania = "+str(wynik.wynik())
            return pokaz

class Dodawanie(Operacje):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    
    def wynik(self):
        return self.a+self.b
        

class Odejmowanie(Operacje):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    def wynik(self):
        return self.a-self.b

class Mnozenie(Operacje):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    def wynik(self):
        return self.a*self.b

class Dzielenie(Operacje):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    def wynik(self):
        if self.b == 0:
            return 0
        else:
            return self.a*self.b

class Potegowanie(Operacje):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    def wynik(self):
            return self.a**self.b     

a = int(input('Podaj liczbe1: '))
b = int(input('Podaj liczbe1: '))
w = Operacje(a,b)
operacja = input('Wybierz dzialanie +,-,*,/,** : ')
print(w.wybor(operacja))