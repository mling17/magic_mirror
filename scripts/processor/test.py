s = input('>>>')

m, n = eval(s)
print(f'{m}/{n}')
if m % n == 0:
    print(f'{m} / {n}')
else:
    for i in range(1, min((m, n))):
        if (m % i == 0) and (n % i == 0):
            m = m // i
            n = n // i

    print(f'{m}/{n}')
