tabuada = 1
n = 0

while True:
    n = int(input('Número para tabuada: '))
    if n >= 0:
        tabuada = 1
        while tabuada <= 10:
            calculo = n * tabuada
            print(f'{n} x {tabuada} = {calculo}')
            tabuada += 1
    else:
        print('Programa finalizado com sucesso!!!')
        break
