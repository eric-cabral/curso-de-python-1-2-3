from random import randint

print(f'{"|MEGA SENA|" :_^35}')

vezes = int(input('Quantos palpites você quer gerar? '))
combinacoes = []
temp = []

for rep in range(0, vezes):
    while len(temp) <= 6:
            palpite = randint(1, 60)
            if palpite not in temp:
                temp.append(palpite)
    temp.sort()
    combinacoes.append(temp[:])
    temp.clear()

for indice, valor in enumerate(combinacoes):
    print(f'Jogo {indice+1}: {valor}')
