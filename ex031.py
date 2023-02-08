distancia = float(input('Qual a distância da sua viagem em Km: '))

if distancia <= 200:
    curta = distancia * 0.5
    print(f'O preço da passagem é R$ {curta:.2f}')
else:
    longa = distancia * 0.45
    print(f'O preço da passagem é R$ {longa:.2f}')

print('Tenha uma ótima viagem!!!')
