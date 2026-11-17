oceny = [4, 5, 3, 5, 4]

def oblicz_srednia(lista_liczb):
    if len(lista_liczb) == 0:
        return 0
    return sum(lista_liczb) / len(lista_liczb)

print(f"Średnia wynosi: {oblicz_srednia(oceny)}")
