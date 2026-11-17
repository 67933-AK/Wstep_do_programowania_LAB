a = float(input("Podaj liczbę a: "))
n = int(input("Podaj potęgę n: "))

def potega(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * potega(a, n - 1)
    else:
        return 1 / potega(a, -n)

if a == 0 and n < 0:
    print("Nieprawidłowe dane")
else:
    print(f"Wynik wynosi: {potega(a, n)}")