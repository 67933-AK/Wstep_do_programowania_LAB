while True:
    liczba = int(input("Podaj liczbe calkowita: "))

    if liczba < 0:
        print("Wprowadzono liczbe ujemna. Koniec petli.")
        break

    print(f"Podano: {liczba}")
