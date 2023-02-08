from datetime import date

dadostrabalhador = {}

dadostrabalhador['Nome'] = str(input('Nome: '))
dadostrabalhador['Nascimento'] = int(input('Ano de nascimento: '))
dadostrabalhador['Idade'] = date.today().year - dadostrabalhador['Nascimento']
dadostrabalhador['Carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
if dadostrabalhador['Carteira'] != 0:
    dadostrabalhador['Contratação'] = int(input('Ano de Contratação: '))
    dadostrabalhador['Salário'] = float(input('Salário (R$): '))
    dadostrabalhador['Aposentadoria'] = (dadostrabalhador['Contratação'] + 35) - dadostrabalhador['Nascimento']

print()

print(f'{"DADOS DO TRABALHADOR CADASTRADO":.^50}')
for nome, valor in dadostrabalhador.items():
    print(f'   - {nome} tem o valor {valor}')
