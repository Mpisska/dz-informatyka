#26
def collatz(c, n):
    for _ in range(n):
        if c % 2 == 0:
            c = c // 2
        else:
            c = c * 3 + 1
    return c
print(collatz(11, 5))
print(collatz(1, 10))

#27
def suma(liczba):
    suma_nieparzystych = 0
    for cyfra in str(liczba):
        if int(cyfra) % 2 == 1:
            suma_nieparzystych += int(cyfra)
    return suma_nieparzystych
print(suma(1122445))
print(suma(986713))

#28
def NWD(a, b):
    i = 0
    while a != b:
        if a > b:
            a = a - b
            i += 1
        else:
            b = b - a
            i += 1
    return i
print(f'liczba itercij {NWD(30, 8)}')

#29
def ile_pol():
    while True:
        try:
            n = int(input("Podaj liczbę od 2 do 32: "))
            if 2 <= n <= 32:
                return n * n
            else:
                print("Błąd: liczba spoza dozwolonego zakresu. Spróbuj ponownie.")
        except ValueError:
            print("Błąd: podano nieprawidłową wartość (nie liczbę). Spróbuj ponownie.")

print(f'Liczba pól na szachownicy: {ile_pol()}')

#30
def ile_kolorowych(n, kolor):
    total_fields = n * n
    if total_fields % 2 == 0:
        return total_fields // 2
    else:
        return total_fields // 2 + (1 if kolor == 'c' else 0)

while True:
    try:
        n = int(input("Podaj rozmiar szachownicy (2–32): "))
        if not (2 <= n <= 32):
            print("Błąd: rozmiar musi być w zakresie od 2 do 32.")
            continue

        kolor = input("Podaj kolor ('b' – biały, 'c' – czarny): ").strip().lower()
        if kolor not in ['b', 'c']:
            print("Błąd: kolor musi być 'b' (biały) lub 'c' (czarny).")
            continue

        wynik = ile_kolorowych(n, kolor)
        print(f'Liczba pól koloru {"białego" if kolor == "b" else "czarnego"} na szachownicy {n}x{n}: {wynik}')
        break

    except ValueError:
        print("Błąd: podano nieprawidłową wartość. Wprowadź liczbę całkowitą.")
