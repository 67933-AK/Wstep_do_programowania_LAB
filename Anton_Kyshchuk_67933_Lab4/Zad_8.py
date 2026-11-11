stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżancie",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik"
)

ilość_stopnii = len(stopnie)
Major_index = stopnie.index("Major")
Pułkownik_wstepowanie = "Pułkownik" in stopnie

print(f"Liczba stopni wojskowych: {ilość_stopnii}")
print(f"Indeks stopnia Major: {Major_index}")
print(f"Czy Pułkownik występuje w krotce: {Pułkownik_wstepowanie}")
