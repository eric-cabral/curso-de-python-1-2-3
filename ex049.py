n = int(input('Digite um número para calcularmos a tabuada: '))

for tabuada in range(1, 11):
    calculo = n * tabuada
    print(f'{n} x {tabuada} = {calculo}')
print('Bom demais!')
