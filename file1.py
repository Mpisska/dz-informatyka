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