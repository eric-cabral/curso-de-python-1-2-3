from random import randint
from time import sleep

dados = {'jogador 1': ' ', 'jogador 2': ' ', 'jogador 3': ' ', 'jogador 4': ' '}

for contagem in range(0, 4):
    for k, v in dados.items():
        sorteio = randint(1, 6)
        dados[k] = sorteio

print('VALORES SORTEADOS:')
for k, v in dados.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
print()

print('RANKING DOS JOGADORES:')
lugar = 1
for i in sorted(dados, key = dados.get, reverse=True):
    print(f'{lugar}° lugar: {i.title()} com {dados[i]}')
    lugar += 1
    sleep(0.5)
