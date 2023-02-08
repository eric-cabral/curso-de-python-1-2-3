nome = str(input('Digite seu nome completo: ')).strip()
separados = nome.split()

print('Seu primeiro nome é {}'.format(separados[0]))
print('Seu último nome é {}'.format(separados[len(separados)-1]))
