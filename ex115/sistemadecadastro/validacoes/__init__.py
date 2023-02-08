def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Você interrompeu sem digitar nenhum número.\033[m')
        else:
            return n

def prints(msg):
    print('-' * 40)
    print(msg.center(50))
    print('-' * 40)
