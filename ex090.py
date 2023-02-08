dados = {}

dados['Nome'] = str(input('Digite seu nome: '))
dados['Média'] = float(input('Digite sua média: '))
if dados['Média'] < 5:
    dados['Situação'] = 'Reprovado'
elif 5 <= dados['Média'] <= 6:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Aprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}')
