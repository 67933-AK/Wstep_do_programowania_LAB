gol = int(input('Podaj liczbe goli: '))
bonus = 0

wynik = gol * 10


#---------------- A ----------------
if gol > 10: 
    bonus += 10
elif gol > 5:
    bonus +=5

wynik = wynik+bonus
print('Wynik a) : ', wynik)

#---------------- B ----------------
wynik = gol * 10
bonus = 0

if gol > 5:
    bonus +=5
if gol > 10: 
    bonus += 10

wynik = wynik + bonus
print('Wynik b) : ', wynik)