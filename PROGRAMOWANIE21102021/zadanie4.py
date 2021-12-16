def podaj():
    imieInazwisko = input('Podaj imie i nazwisko: ')
    if len(imieInazwisko) < 4:
        print('Podaj co najmniej 3 znaki!')
        podaj()
    else:
        print("Twoje imie to: "+imieInazwisko)
    return

podaj()