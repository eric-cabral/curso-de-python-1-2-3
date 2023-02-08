import random

pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

jokenpo = [pedra, papel, tesoura]
usuario = str(input('Vamos jogar Jokenpô? ...\nVocê quer o quê? ').lower().strip())
sorteio = random.choice(jokenpo)

if usuario == sorteio:
    print('Caraaaamba empatou, o PC também escolheu {}'.format(sorteio))
elif usuario == 'papel':
    if sorteio == pedra:
        print(f'O computador escolheu {sorteio}, portanto você ganhou, PARABÉNS!!!')
    elif sorteio == tesoura:
        print(f'O computador escolheu {sorteio}, portanto você perdeu!')
elif usuario == 'pedra':
    if sorteio == tesoura:
        print(f'O computador escolheu {sorteio}, portanto você ganhou, PARABÉNS!!!')
    elif sorteio == papel:
        print(f'O computador escolheu {sorteio}, portanto você perdeu!')
elif usuario == 'tesoura':
    if sorteio == papel:
        print(f'O computador escolheu {sorteio}, portanto você ganhou, PARABÉNS!!!')
    elif sorteio == pedra:
        print(f'O computador escolheu {sorteio}, portanto você perdeu!')
else:
    print('Opção inválida, tente novamente!')
