#1
haslo =["Podróże kształcą i otwierają umysł.",
        "Świat czeka na odkrycie – ruszaj w drogę",
        "Każda podróż to nowa historia do opowiedzenia."]
for h in haslo:
    print(h)

#2
a = 10
b = 3

suma = a + b
roznica = a - b
iloczyn = a * b
iloraz = a / b
iloraz_calkowity = a // b
reszta = a % b
kwadrat = a ** 2

#3
kurs = 4.74
cena = 126
zloty = kurs * cena
print(f'Do zapłaty: {zloty} zł')

#4
kurs =  4.76
cenaP = 200
cenaG = 49 * kurs
if cenaG < cenaP:
    print('W Grecji taniej')
else:
    print('w Polsce taniej')

#5
day1 = 12
day2 = 14
day3 = 18
suma = day1+day2+day3
srednia = suma/2

#6
def jak_szybko(t, s):
    srednia_predkosc = s / t
    return srednia_predkosc

print(f"Wynik 1 {jak_szybko(2.5, 1320)}")
print(f"Wynik 2: {jak_szybko(3, 1320)}")

#7
def zamiana(m):
    km = m * 1.609
    return km

print(f'Wynik: {zamiana(10)}')
print(f'Wynik: {zamiana(12)}')

#8
def godzina(n):
    wyjazd = 21
    przyjazd = (wyjazd + n)%24
    return przyjazd
print(f'wynik: {godzina(14)}')
print(f'wynik: {godzina(20)}')

#9
def godz_nj(g):
    return (g - 6) % 24
print(f'godz_nj(18) = {godz_nj(18)}')
print(f'godz_nj(2) =  {godz_nj(2)}')

#10
def pole_kw(bok):
    return bok * bok
print(pole_kw(25))
print(pole_kw(101))

#11
def obw_pr(bok1, bok2):
    return bok1 * 2 + bok2 *2
print(obw_pr(25, 30))
print(obw_pr(105, 95))

#12
def waga(kg):
    return kg * 2.2
print(waga(2))
print(waga(15))

#13
def godz_waw(g):
    return (g + 9) % 24
print(godz_waw(8))
print(godz_waw(21))

#14
def cena(f):
    usd = 4.75
    funt = 0.45
    return (f*usd)/funt
print(cena(1.35))
print(cena(3.98))

#15
x = 3
y = 5
x, y = y, x

#16
n = int(input('Enter n: '))
if n%3 == 0 and n%7 ==0:
    print('yes')
else:
    print('no')

#17
def ile(k):
    return k * k
print(ile(5))
print(ile(6))

#18
def ile_kolor(k, kolor):
    if kolor not in ['c', 'n']:
        return "Nieprawidłowy kolor. Użyj 'c' dla czerwonego lub 'n' dla niebieskiego."
    liczba_korali = k * k
    if kolor == 'c':
        return (liczba_korali + 1) // 2
    else:
        return liczba_korali // 2
print(ile_kolor(6, "c"))
print(ile_kolor(7, "c"))
print(ile_kolor(6, "n"))
print(ile_kolor(7, "n"))

#19
def piramida(k):
    if k < 1:
        return 0
    return k * (k + 1) // 2
print(piramida(5))
print(piramida(6))

#20
def lata(ile):
    if ile < 18:
        print(0)
    elif ile > 50:
        print(2)
    else:
        print(1)
print(lata(14))
print(lata(46))
print(lata(65))

#21
def bmi(kg, m):
    bmi = kg/(m * m)
    if bmi < 18.5:
        print('niedowaga')
    elif bmi > 25:
        print('nadwaga')
    else:
        print('prawidlowa waga')
print(bmi(50, 1.63) )
print(bmi(44, 1.63))
print(bmi(90, 1.63))

#22
def naj(liczba1, liczba2, liczba3):
    return max(liczba1, liczba2, liczba3)
print(naj(1, 2, 3))
print(bmi(90, 1.63))
print(naj(99, 33, 12))

#23
def waga(pocz, n):
    przyrost = n / 2 * (2 * 2 + (n - 1) * 2)
    masa_koncowa = pocz + przyrost
    return masa_koncowa
print(waga(2, 2))
print(waga(5, 3))

#24
def skarbonka(ile, n):
    suma_wrzut = 2 ** n - 1
    return ile + suma_wrzut
print(skarbonka(12, 2))
print(skarbonka(0, 5))

#25
# nie wiem