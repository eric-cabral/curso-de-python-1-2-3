pessoas = list()
pessoacad = list()
maispesada = maisleve = 0

print(f'{"CADASTROS DE PESSOAS":¨^40}')
while True:
    pessoacad.append(str(input('Nome: ')).strip())
    pessoacad.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maispesada = maisleve = pessoacad[1]
    else:
        if pessoacad[1] > maispesada:
            maispesada = pessoacad[1]
        elif pessoacad[1] < maisleve:
            maisleve = pessoacad[1]
    pessoas.append(pessoacad[:])
    pessoacad.clear()
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja continuar (S/N)? ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maispesada} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maispesada:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {maisleve} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maisleve:
        print(f'{p[0]} ', end='')
print()
