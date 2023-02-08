from random import randint

cont = 0

print('Vamos jogar par ou ímpar...')
while True:
    computador = randint(1,2)
    numero = int(input('Qual número você escolhe? '))
    escolha = str(input('Par ou ímpar (P/I)? ')).lower().strip()[0]
    if ((computador + numero) % 2) == 0:
        if escolha == 'p':
            cont += 1
            print('Parabéns você ganhou, deu PAR!!!')
            print(f'Você escolheu {numero} e par e o computador escolheu {computador}')
        else:
            print('Você perdeu, deu ÍMPAR!!!')
            print(f'Você escolheu {numero} e ímpar e o computador escolheu {computador}')
            print(f'Você ganhou {cont} vezes antes de perder!')
            break
    else:
        if escolha == 'i':
            cont += 1
            print('Parabéns você ganhou, deu ÍMPAR!!!')
            print(f'Você escolheu {numero} e ímpar e o computador escolheu {computador}')
        else:
            print('Você perdeu, deu ÍMPAR!!!')
            print(f'Você escolheu {numero} e par e o computador escolheu {computador}')
            print(f'Você ganhou {cont} vezes antes de perder!')
            break
