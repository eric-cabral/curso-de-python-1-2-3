alunos = []
dados = {}
n = 0

print(f'{" ANALISE DE MÉDIA DE ALUNO ":=^31}')

for rep in range(1, 3):
    dados['nome'] = str(input('Nome: ')).capitalize()
    dados['media'] = float(input('Média: '))

    if dados['media'] <= 4.9:
        dados['situacao'] = 'Reprovado'
    elif 5 <= dados['media'] <= 5.9:
        dados['situacao'] = 'Recuperação'
    else:
        dados['situacao'] = 'Aprovado'
    alunos.append(dados.copy())

for rep in alunos:
    for k, v in dados.items():
        print(f'O {k} é {v}')
