valores = list()

while True:
    valores.append(int(input('Digite um valor para adicionar a lista: ')))
    continuar = str(input('Você deseja continuar adicionando (S/N)? ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Resposta inválida, deseja continuar  (S/N)? ')).strip()[0]
    if continuar in 'Nn':
        break
print(' ')
print(f'{"VALORES PROCESSADOS":.^50}')
print(f'Valores adicionados: {len(valores)}')
valores.sort(reverse=True)
print(f'Ordem decrescente: {valores}')
if 5 in valores:
    print('Existe o valor 5 na lista!')
else:
    print('NÃO existe o valor 5 na lista.')
