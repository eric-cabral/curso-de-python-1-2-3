listacompleta = []
pares = []
impares = []

while True:
    n = (int(input('Valor para adicionar: ')))
    listacompleta.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    continuar = str(input('Deseja continuar (S/N)? ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Resposta inválida, deseja continuar (S/N)? ')).strip()[0]
    if continuar in 'Nn':
        break
print(' ')
print(f'Todos os valores adicionados: {listacompleta}')
print(f'Apenas os pares: {pares}')
print(f'Apenas os ímpares: {impares}')
