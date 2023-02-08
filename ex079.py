valores = list()
erro = 0

valores.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso...')
while True:
    continuar = str(input('Deseja continuar adicionando (S/N)? ')).strip()[0]
    if continuar in 'Nn':
        print('PROCESSANDO DADOS.....')
        break
    else:
        novovalor = int(input('Digite outro valor: '))
        if novovalor not in valores:
            valores.append(novovalor)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor já adicionado, TENTE OUTRO!')
valores.sort()
print(' ')
print(f'{"DADOS CADASTRADOS":=^30}')
print(valores)
