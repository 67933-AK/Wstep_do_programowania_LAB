Moja_lista=[1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(f"Lista: {Moja_lista}")

print(f"Pierwszy element listy {Moja_lista[0]}")
print(f"Ostatni element listy {Moja_lista[-1]}")
print(f"długość listy: {len(Moja_lista)} elementów")
print(f"największa wartość: {max(Moja_lista)}, najmniejsza wartość: {min(Moja_lista)}")
print(f"Suma elementów listy: {sum(Moja_lista)}")
print(f"Posortowane elementy: {sorted(Moja_lista)}")

print('\n\n')

Moja_lista.append(67)
print(f"{Moja_lista} <- dodano element 67")
Moja_lista.insert(8,234564) 
print(Moja_lista)
print(f"Usunięty element: {Moja_lista.pop()}")
print(f"{Moja_lista} <- 67 tu więcej nie ma")
Moja_lista.reverse()
print(f"Odwrócona lista: {Moja_lista}")
Moja_lista.reverse()


Nowa_lista=[17, 25, 64, 21, 38, 4]
print(f"Łączenie dwóch list: {Moja_lista + Nowa_lista}")
n=int(input("Wpisz dowolną liczbę: "))
print(f"Powtórzenie wartości listy n razy: {Nowa_lista * n}")
print(f"{Moja_lista[:8]}")
print(f"{Moja_lista[8:]}")
print(f"{Moja_lista[0:8:2]}")
print(f"{Moja_lista[::-1]}")

print('\n\n')

tekst = "ababagalamaga"
find = input("Wpisz szukany tekst: ")

if find in tekst:
    print(f"Znaleziono fragment {find}")
    tekst = tekst.replace(find, "_Nowy_Tekst_")
    print(f"Zmieniony tekst: {tekst}")
else:
    print("Fragment nie istnieje")

tekst = "ababagalamaga"
print(tekst.upper())
print(tekst.lower())

print(f"Podział tekstu: {tekst.split('a')}")

print('\n\n')

Moja_lista.extend([100, 200])
print(f"{Moja_lista} <- dodano elementy (100, 200)")

Moja_lista.remove(3)
print(f"{Moja_lista} <- usunięto pierwsze wystąpienie liczby 3")

Moja_lista.sort()
print(f"Posortowana lista: {Moja_lista}")

Moja_lista.clear()
print(f"Lista po usunięciu wszystkich elementów: {Moja_lista}")