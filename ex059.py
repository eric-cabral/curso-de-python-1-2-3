import time

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

escolha = 0

while escolha !=5:
    escolha = int(input('OPERAÇÕES DISPONÍVEIS'
          '\n[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos números'
          '\n[5] Sair do programa'
          '\nESCOLHA UMA OPERAÇÃO: '))
    if escolha == 1:
        calculo = n1 + n2
        print(f'Os números {n1} e {n2} somados são {calculo}.')
        print('======================================')
    elif escolha == 2:
        calculo = n1 * n2
        print(f'Os números {n1} e {n2} mulitiplicados são {calculo}.')
        print('======================================')
    elif escolha == 3:
        if n1 < n2:
            print(f'O número {n2} é maior que o número {n1}.')
            print('======================================')
        elif n1 < n2:
                print(f'O número {n2} é maior que o número {n1}.')
                print('======================================')
        elif n1 == n2:
            print(f'Você digitou dois números {n1} e claro, são iguais.')
            print('======================================')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('======================================')
    else:
        print('Opção inválida. Tente novamente!')

print('FINALIZANDO PROGRAMA...')
time.sleep(1)
print('PROGRAMA FINALIZADO, MUITO OBRIGADO!!!')
