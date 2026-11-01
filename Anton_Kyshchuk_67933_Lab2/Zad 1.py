punkty = float(input('Podaj liczbę zdobytych punktów: '))

if punkty > 80:
    print('Gratulacje! Egzamin zaliczony w terminie zerowym.')
elif punkty >= 50:
    print('Egzamin zaliczony. Możesz poprawić swój wynik.')
else:
    print('Egzamin niezaliczony. Musisz przystąpić do poprawy.')