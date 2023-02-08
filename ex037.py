numero = int(input('Digite um número inteiro para conversão: '))
print('''Converter número para qual formato: 
[1] Converter em binário
[2] Converter em octal
[3] Converter em hexadecimal''')
escolha = int(input('Qual opção de conversão você deseja? '))

if escolha == 1:
    print('O número {} em binário é {:}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} em octal é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Esse número não é uma opção!')
