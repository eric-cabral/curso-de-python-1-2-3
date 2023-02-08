todos = []
dados = {}
mulheres = []
acimaIdadeMedia = []
idadeTotal = 0
pessoasTotal = 0


while True:
    dados['nome'] = str(input('Nome: ')).title()
    dados['sexo'] = str(input('Sexo (M/F): '))
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = str(input('Inválido. Sexo (M/F): '))
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    todos.append(dados.copy())
    pessoasTotal += 1
    idadeTotal += dados['idade']
    continuar = str(input('Deseja continuar (S/N)? '))
    if continuar in 'Nn':
        print()
        print('ANALISANDO DADOS.....')
        break
print()

media = idadeTotal / pessoasTotal
print(f'Foram cadastradas {pessoasTotal} pessoas.')
print(f'A média de idade do grupo foi de {media:.1f} anos.')
print(f'As mulheres são ', end= '')
for mulher in mulheres:
    if mulher != dados['nome']:
        print(mulher, end=', ')
    else:
        print(mulher, end='.')
print()
for indice, valor in enumerate(todos):
    if valor['idade'] > media:
        acimaIdadeMedia.append(valor['nome'])
print(f'As pessoas com idade acima da média foram ', end= '')
for acima in acimaIdadeMedia:
    if acima != dados['nome']:
        print(acima, end=', ')
    else:
        print(acima, end='.')
print()