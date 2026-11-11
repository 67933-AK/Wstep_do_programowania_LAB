imie = input("Podaj imie: ")
print(f"Witaj {imie}")

wiek = input("Podaj wiek: ")
print(f"Twoj wiek to: {wiek}")

nazwisko = input("Podaj nazwisko: ")
inicjaly = imie[0].upper() + "." + nazwisko[0].upper() + "."
print(f"Inicjaly: {inicjaly}")


tekst = input("Podaj tekst: ")
i=0
while i < 5:
    print(tekst)
    i +=1


tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")
tekst3 = tekst1 + " " + tekst2
print(tekst3)



tekst1 = input("Podaj pierwszy tekst: ")
tekst2 = input("Podaj drugi tekst: ")

polowa1 = len(tekst1) // 2
polowa2 = len(tekst2) // 2

tekst3 = tekst1[:polowa1] + tekst2[polowa2:]
print(tekst3)