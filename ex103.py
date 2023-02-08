def ficha(nome='<Nenhum>', gols=0):
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nomeJogador = str(input('Nome do Jogador: ')).strip().title()
golsJogador = str(input('Número de Gols: '))
if golsJogador.isnumeric() is True:
    golsJogador = int(golsJogador)
else:
    golsJogador = 0
if nomeJogador == '':
    ficha(gols=golsJogador)
else:
    ficha(nomeJogador, golsJogador)
