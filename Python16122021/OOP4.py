
def my_dekorator(fn):
    def wrapper():
        print("Początkowe odliczanie")
        fn()
        print("Koniec odliczania")
    return wrapper

@my_dekorator
def get_5_values():
    for v in range(1,6):
        print(v)

get_5_values()

print("-------------------------------")

def moj_dekorator(fn):
    def pokaz():
        print("Początkowe odliczanie")
        fn()
        print("Koniec odliczania")
    return pokaz  

@moj_dekorator
def liczby_podzielne_przez_3_i_4_do_100():
    for v in range(1,101):
        if (v%3==0) and (v%4==0):
            print(v)

liczby_podzielne_przez_3_i_4_do_100()