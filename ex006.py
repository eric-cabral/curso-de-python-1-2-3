n = int(input('Digite um que número e mostrarei o resultado de alguns cálculos:'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O dobro de {} é {}'.format(n, dobro))
print('O triplo de {} é {}'.format(n, triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n, raiz))
# O {:.2f} é para mostrar 2 casas decimais float

print('Muito obrigado!!!')
