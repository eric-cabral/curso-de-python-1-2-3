valores = [[], []]

for rep in range(1, 8):
    n = int(input(f'Digite o {rep}° valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort()
print(f'Valores pares digitados: {valores[0]}')
print(f'Valores ímpares digitados: {valores[1]}')
