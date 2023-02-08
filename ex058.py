#Exercício 58 é o exercício 28 só que melhorado aplicando WHILE.

import random

cont = 0
aleatorio = random.randint(0, 10)
print('Estou pensando em um número... entre 0 e 10...')

chute = int(input('Tenta adivinhar o número: '))
while chute != aleatorio:
    chute = int(input('Você ERROU, tente novamente, você consegue!: '))
    cont = cont + 1

print(f'Eu pensei no número {aleatorio}.')
if cont == 0:
    print('Você ACERTOU de primeira, isso é TALENTO!!!')
else:
    print(f'Foram necessárias {cont+1} tentativa mas o que importa é acertar!')
