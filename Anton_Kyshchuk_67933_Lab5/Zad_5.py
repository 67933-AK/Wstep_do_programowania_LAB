waga = float(input("Wpisz wagę: "))
wzrost = float(input("Wpisz wzrost (cm): "))
wzrost_m = wzrost / 100

def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print(f"Twoje BMI wynosi: {bmi:.2f}")

    if bmi < 18.5:
        zakres = "Niedowaga"
    elif bmi < 25:
        zakres = "Pożądana masa ciała"
    elif bmi < 30:
        zakres = "Nadwaga"
    elif bmi < 35:
        zakres = "Otyłość I stopnia"
    elif bmi < 40:
        zakres = "Otyłość II stopnia"
    else:
        zakres = "Otyłość III stopnia"

    print("Zakres:", zakres)

    return bmi, zakres

if waga > 0 and wzrost_m > 0:
    oblicz_bmi(waga, wzrost_m)
else:
    print("Nieprawidłowe dane")