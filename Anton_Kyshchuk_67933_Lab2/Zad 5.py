from pathlib import Path

sciezka = Path(__file__).with_name("notowania_gieldowe.txt")



print('\n---------------- A ----------------\n')

with open(sciezka, "r") as plik:
    for linia in plik:
        print(linia, end="")



print('\n\n---------------- B ----------------\n')

znaleziono = False

with open(sciezka, "r") as plik:
    for linia in plik:
        if linia.strip() == 'ALR, 113':
            znaleziono = True

if not znaleziono:
    with open(sciezka, "a") as plik:
        plik.write('ALR, 113\n')

with open(sciezka, "r") as plik:
    for linia in plik:
        print(linia, end="")