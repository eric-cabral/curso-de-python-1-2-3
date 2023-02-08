n1 = int(input('Digite o primeiro número da comparação: '))
n2 = int(input('Digite o segundo número da comparação: '))

if n1 == n2:
    print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
    print('O número {} é o maior!'.format(n1))
else:
    print('O número {} é o maior!'.format(n2))
