import random

aleatorio = random.randint(0, 5)
print('Estou pensando em um número... entre 0 e 5')

chute = int(input('Tente adivinhar o número: '))

if chute == aleatorio:
    print('Paaaarabéns, você acertou!!!')
    print(f'O número correto é {aleatorio} :)')
else:
    print(f'Você é terrível mas pode tentar outra vez. E o número correto era {aleatorio}')
