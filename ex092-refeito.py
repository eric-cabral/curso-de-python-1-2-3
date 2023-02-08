from datetime import date
from time import sleep

dados = dict()

dados['Nome'] = str(input('Digite seu nome: ')).title()
sexo = str(input('Qual seu sexo (M/F)? '))
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Qual seu sexo (M/F)? '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['CTPS'] = int(input('Digite a sua CTPS (Caso não tenha digite 0): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Qual seu salário (R$)? '))
    dados['Aposentadoria'] = (dados['Contratação'] + 35) - nascimento

print('PROCESSANDO DADOS... 1')
sleep(0.5)
print('PROCESSANDO DADOS... 2')
sleep(0.5)
print('PROCESSANDO DADOS... 3')
sleep(0.5)
print('PROCESSANDO DADOS... 4')
sleep(0.5)
print('PROCESSANDO DADOS... 5')
sleep(0.5)
print('DADOS PROCESSADOS COM SUCESSO!!!')
sleep(1)

for item, valor in dados.items():
    print(f'    - {valor} é {item}.')
