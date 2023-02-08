print('Digite o comprimento de três retas para ver se elas formam um triângulo.')

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceita reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!!!')
    if r1 == r2 == r3:
        print('O triângulo formado é equilátero.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado é escaleno.')
    else:
        print('O triângulo formado é isósceles.')
else:
    print('Os segmentos NÃO podem formar um triângulo :(')
