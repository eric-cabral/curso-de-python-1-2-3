velo = float(input('Digite a velocidade de um carro (em Km/H): '))

if velo <= 80:
    print('Velocidade permitida, continue assim!!!')
else:
    print('Velocidade máxima excedida, uma multa será aplicada.')
    excesso = (velo-80)
    multa = (excesso*7)
    print(f'A multa será no valor de R$ {multa:.2f}.')
