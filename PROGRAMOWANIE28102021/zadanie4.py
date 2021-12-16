while True:
    liczba = int(input('Podaj liczbe wieksza od 0: '))
    
    if liczba >= 0:
        print(f'Twoja liczba to: {liczba}')
        break
    else:
        print(f'Twoja liczba jest mniejsza od 0')
        break