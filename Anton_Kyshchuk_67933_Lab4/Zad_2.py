Lista_imion = ["Adam", "Piotr", "Kasia", "Ewa"]
print(f"Lista początkowa: {Lista_imion}")

Lista_imion.sort()
print(f"Lista posortowana alfabetycznie: {Lista_imion}")

Lista_imion.extend(["Ola", "Marek"])
print(f"Lista po dodaniu dwóch osób: {Lista_imion}")
print(f"Ostatnia osoba (Usunięta przez pop()): {Lista_imion.pop()}")

Lista_imion.insert(2, "Anna")
print(f"Lista po dodaniu Anny: {Lista_imion}")

Lista_imion.reverse()
print(f"Odwrócona lista: {Lista_imion}")

Lista_imion = Lista_imion * 2
print(f"Zdublowana lista: {Lista_imion}")
