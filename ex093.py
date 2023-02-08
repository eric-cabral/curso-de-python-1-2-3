dados = {}
golscad = []
somagols = 0

dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for valores in range(0, partidas):
    gols = (int(input(f'     Quantos gols na partida {valores}? ')))
    golscad.append(gols)
    somagols = somagols + gols

dados['gols'] = golscad[:]
dados['soma dos gols'] = somagols

print('=-=' * 20)

print(dados)

print('=-=' * 20)

for indice, valores in dados.items():
    print(f'O campo {indice} tem o valor {valores}')

print('=-=' * 20)

print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for indice, valores in enumerate(dados['gols']):
    print(f'    => Na partida {indice}, fez {valores} gols;')
print(f'Foi um total de {dados["soma dos gols"]} gols.')
