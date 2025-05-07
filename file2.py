#25
def collatz(c, n):
    for _ in range(n):
        if c % 2 == 0:
            c = c // 2
        else:
            c = c * 3 + 1
    return c