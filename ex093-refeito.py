dados = {}
gols = []
total = 0

dados['nome'] = str(input('Nome de Jogador: ')).title()
partidas = int(input('Número de partidas jogadas: '))

for rep in range(1, partidas+1):
    gol = int(input(f'Quantos gols na {rep}ª partida? '))
    gols.append(gol)
    total += gol
dados['gols'] = gols[:]

print(f'{dados["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(dados['gols']):
    print(f'   => Foram feitos {v} gols na {k+1}ª partida.')
print(f'Foram feitos ao todo {total} gols.')
print(f'   => Média de gols por partida de {total/partidas:.2f}.')
