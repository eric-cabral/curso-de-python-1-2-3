nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
fatorado = nome.split()
print('Seu nome primeiro nome é {} e tem {} letras'.format(fatorado[0], len(fatorado[0])))
