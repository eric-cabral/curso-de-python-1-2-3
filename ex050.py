s = 0
c = 0

for rep in range(1, 7):
    n = int(input(f'Digite o {rep}o número: '))
    if n % 2 == 0:
        s = s + n
        c = c + 1
print('Você informou {} números PARES e a soma foi {}'.format(c, s))
