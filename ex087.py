matrizes = [[[],[],[]],[[],[],[]],[[],[],[]]]
pares = maior = soma = 0

for linhas in range(0, 3):
    for colunas in range(0, 3):
        matrizes[linhas][colunas] = int(input(f'Valor para matriz [{linhas}, {colunas}]: '))
        if matrizes[linhas][colunas] % 2 == 0:
            pares += matrizes[linhas][colunas]
    if linhas == 0:
        maior = matrizes[linhas][colunas]
    elif linhas == 1 and matrizes[linhas][colunas] > maior:
        maior = matrizes[linhas][colunas]

for linhas in range(0, 3):
    soma += matrizes[linhas][2]

for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matrizes[linhas][colunas]}]', end=' ')
    print()

print('_' * 25)

print(f'Soma dos números pares: {pares}')
print(f'Soma dos valores da terceira coluna: {soma}')
print(f'Maior número da segunda linha: {maior}')
