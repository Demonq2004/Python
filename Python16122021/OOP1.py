#OBIEK, WARTOSC, ZMIENNA
a = 1
print(id(a))
a = 2
print(id(a))
b = a
print(id(b))
print(type(a))


def mojafoo():
    return 10

print(dir(mojafoo))