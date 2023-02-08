listaJogadores = []
dados = {}
golscad = []
total = 0
#somagolstotal = 0

print('-' * 40)
while True:
    dados['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for valores in range(0, partidas):
        gols = (int(input(f'     Quantos gols na partida {valores+1}? ')))
        golscad.append(gols)
        total = total + gols
        #somagolstotal = somagolstotal + gols

    dados['Gols'] = golscad[:]
    dados['Total'] = total
    #dados['soma dos gols totais'] = somagolstotal
    listaJogadores.append(dados.copy())
    total = 0
    golscad.clear()

    continuar = str(input('Deseja cadastrar mais jogadores (S/N)? '))
    while continuar not in 'SsNn':
        print('Dados inválidos!')
        continuar = str(input('Deseja cadastrar mais jogadores (S/N)? '))
    if continuar in 'Nn':
        break
    print('-' * 40)

print('=-=' * 20)

print('Cód.', end=' ')
for indice in dados.keys():
    print(f'{indice: <15}', end='')
print()
print('-' * 40)

for indice, valores in enumerate(listaJogadores):
    print(f'{indice: >3}', end='  ')
    for v in valores.values():
        print(f'{str(v): <15}', end='')
    print()

print('=-=' * 20)

while True:
    mostrarDados = int(input('Deseja mostrar dados de qual jogador (caso nenhum digite 999)? '))
    if mostrarDados == 999:
        print()
        print('MUITO OBRIGADO!!!')
        break
    elif mostrarDados >= len(listaJogadores):
        print(f'ERRO! Não existe jogador com código {mostrarDados}! Tente novamente.')
        print('=-=' * 20)
        mostrarDados = int(input('Deseja mostrar dados de qual jogador (caso nenhum digite 999)? '))
    else:
        print(f'ESTATÍSTICAS DO JOGADOR {listaJogadores[mostrarDados]["Nome"]}:')
        for indice, valores in enumerate(listaJogadores[mostrarDados]["Gols"]):
            print(f'    => Na partida {indice + 1}, fez {valores} gols;')
        print(f'Foi um total de {listaJogadores[mostrarDados]["Total"]} gols.')
    print('=-=' * 20)
print()
print('== VOLTE SEMPRE : ) ==')
