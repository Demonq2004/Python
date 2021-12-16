#kalkulator + - * / a)funkcja anonimowa, b)funkcja ktora posiada argumenty kluczowe c)ktora posiada slownik d)*arg

def kalkulator(a,b):
    print("Dodawanie = ",a+b)
    print("Odejmowanie = ",a-b)
    print("Mnożenie = ",a*b)
    if(b!=0):
        print("Dzielenie = ",a/b)
    else:
        print("Dzielenie = NIE WOLNO DZIELIĆ PRZEZ ZERO!")

def kalkulator2(*arg):
    print("Dodawanie = ",arg+arg)
    print("Odejmowanie = ",arg-arg)
    print("Mnożenie = ",arg*arg)
    if(b!=0):
        print("Dzielenie = ",arg/arg)
    else:
        print("Dzielenie = NIE WOLNO DZIELIĆ PRZEZ ZERO!")



a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

kalkulator(a,b)



