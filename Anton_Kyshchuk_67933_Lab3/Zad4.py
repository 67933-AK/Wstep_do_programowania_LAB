liczba_gosci = int(input("Liczba osob: "))
liczba_dan = int(input("Liczba zamowionych dan: "))

suma = 0.0
i = 0

while i < liczba_dan:
    cena = float(input(f"Cena dania nr {i + 1}: ").replace(",", "."))

    if cena < 0:
        print("Cena nie moze byc ujemna.")
        continue

    suma += cena
    i += 1

srednia = suma / liczba_dan
na_osobe = suma / liczba_gosci

print(f"Suma rachunku: {suma:.2f} zl")
print(f"Srednia cena dania: {srednia:.2f} zl")
print(f"Kwota na osobe: {na_osobe:.2f} zl")
