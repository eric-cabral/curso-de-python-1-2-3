from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('JO')
sleep(1)
print('JO')
sleep(1)
print('=-' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('=-' * 12)

# Restante do exercício são os IF's basicamente como eu fiz no ex045,
# qualquer dúvida é só entrar no vídeo do exercício.