print('''======================
PROGRESSÃO ARITMÉTICA
======================''')

comeco = int(input('Digite um número para começar a P.A.: '))
razao = int(input('Digite a razão da P.A.: '))

for rep in range(comeco, razao*10, razao):
    print(rep, end=' → ')
print('ACABOU!')
