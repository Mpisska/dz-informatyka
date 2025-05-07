#1
haslo1 = "Podróże kształcą i otwierają umysł."
haslo2 = "Świat czeka na odkrycie – ruszaj w drogę!"
haslo3 = "Każda podróż to nowa historia do opowiedzenia."

print(haslo1 + "\n" + haslo2 + "\n" + haslo3)

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

#14
def cena(f):
    usd = 4.75
    funt = 0.45
    return (f*usd)/funt
print(cena(1.35))

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

#20
def lata(ile):
    if ile < 18:
        print(0)
    elif ile > 50:
        print(2)
    else:
        print(1)
print(lata(14))

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

#22
def naj(liczba1, liczba2, liczba3):
    return max(liczba1, liczba2, liczba3)
print(naj(1, 2, 3))

#23
def waga(pocz, n):
    przyrost = n / 2 * (2 * 2 + (n - 1) * 2)
    masa_koncowa = pocz + przyrost
    return masa_koncowa
print(waga(2, 2))

#24
def skarbonka(ile, n):
    suma_wrzut = 2 ** n - 1
    return ile + suma_wrzut
print(skarbonka(12, 2))