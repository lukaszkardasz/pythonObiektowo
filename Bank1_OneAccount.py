# Wersja proceduralna.
# Bank — wersja 1.
# Tylko jedno konto.

accountName = 'Jan'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('Wybierz opcję b, aby wyświetlić saldo')
    print('Wybierz opcję d, aby dokonać wpłaty')
    print('Wybierz opcję w, aby dokonać wypłaty')
    print('Wybierz opcję s, aby wyświetlić informacje o koncie')
    print('Wybierz opcję q, aby zakończyć działanie programu')
    print()

    action = input('Co chcesz teraz zrobić? ')
    action = action.lower()  # Wymuszenie użycia małych liter.
    action = action[0]  # Użycie po prostu pierwszej litery.
    print()

    if action == 'b':
        print('Wyświetl saldo:')
        userPassword = input('Proszę podać hasło: ')
        if userPassword != accountPassword:
            print('Hasło jest nieprawidłowe.')
        else:
            print('Wysokość salda wynosi:', accountBalance)
    
    elif action == 'q':
        break

print('Gotowe')