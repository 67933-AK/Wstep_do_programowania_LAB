zdanie = input("Wpisz zdanie: ").lower()

alfabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
litery = ''
brakujace = ''

for litera in alfabet:
    for znak in zdanie:
        if znak == litera:
            litery += litera

    if litera not in zdanie:
        brakujace += litera + ' '

print(f"Litery w kolejności alfabetycznej: {litery}")
print(f"Brakujące litery alfabetu: {brakujace}")

