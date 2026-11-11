moja_krotka = (10, 2, 6, 6, 9, 13, 0, 1)
print(f"Krotka początkowa: {moja_krotka}")

lista = list(moja_krotka)
lista.sort()
moja_krotka = tuple(lista)
print(f"Posortowana krotka: {moja_krotka}")
