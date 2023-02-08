expressao = str(input('Digite uma expressão para validarmos: '))
separado = []

for rep in expressao:
    separado.append(rep)
if separado.count('(') == separado.count(')'):
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
