print('Digite o comprimento de três retas para ver se elas conseguem formar um triângulo.')

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!!!')
else:
    print('Os segmentos NÃO podem formar um triângulo :(')
