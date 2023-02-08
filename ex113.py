def leiaInt(msgInt):
    while True:
        try:
            nI = int(input(msgInt))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Você interrompeu sem digitar nenhum número.\033[m')
        else:
            return nI


def leiaFloat(msgFloat):
    while True:
        try:
            nF = input(msgFloat).strip().replace(',', '.')
            valor = float(nF)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número REAL válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Você interrompeu sem digitar nenhum número.\033[m')
            return 0
        else:
            return valor


nI = leiaInt('Digite um número inteiro: ')
nF = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número {nI} e {nF:.2f}.')
