print("\n--------- A ---------")

n = int(input("Liczba studentow: "))

suma = 0
studenty = 0

while studenty < n:
    punkty = int(input(f"Punkty studenta nr {studenty + 1} (0-100): "))

    if punkty < 0 or punkty > 100:
        print("Nieprawidlowe punkty. Powtorz.")
        continue

    suma += punkty
    studenty += 1

srednia = suma / n
print(f"Srednia liczba punktow: {srednia:.2f}")


print("\n--------- B ---------")


n = int(input("Liczba studentow: "))

suma = 0
studenty = 0

while True:
    if studenty == n:
        break

    punkty = int(input(f"Punkty studenta nr {studenty + 1} (0-100): "))

    if punkty < 0 or punkty > 100:
        print("Nieprawidlowe punkty. Powtorz.")
        continue

    suma += punkty
    studenty += 1

srednia = suma / n
print(f"Srednia liczba punktow: {srednia:.2f}")
