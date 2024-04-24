szam = int(input('Adj meg egy PIN-kódot: '))
talalat = 0

while talalat != szam:
    talalat += 1
    print(talalat)
    if talalat == szam:
        print("A helyes PIN-kód:", talalat)
