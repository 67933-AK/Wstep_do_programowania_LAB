liczby_pierwsze = []
liczba = 2

while len(liczby_pierwsze) < 10:
    dzielnik = 2
    czy_pierwsza = True

    while dzielnik * dzielnik <= liczba:
        if liczba % dzielnik == 0:
            czy_pierwsza = False
            break

        dzielnik += 1

    if czy_pierwsza:
        liczby_pierwsze.append(str(liczba))

    liczba += 1

print(",".join(liczby_pierwsze))
