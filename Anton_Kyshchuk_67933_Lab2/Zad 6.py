litera = input('Podaj literę: ')

if litera.isupper():
    print(litera, '- jest wielką literą.')
elif litera.islower():
    print(litera, '- jest małą literą.')
else:
    print('Nie można określić wielkości liter w podanym tekście.')