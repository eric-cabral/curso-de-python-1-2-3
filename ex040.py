print('Digite o valor das suas duas notas por favor.')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if n1 >= 0 and n1 <= 10:
    if n2 >= 0 and n2 <= 10:
        if media < 5:
            print('Sua média foi {}, portanto está reprovado.'.format(media))
        elif media >= 7:
            print('Sua média foi {}, portanto está aprovado.'.format(media))
        else:
            print('Sua média foi {}, portanto está de recuperação.'.format(media))
    else:
        print('O segundo número digitado é inválido!')
else:
    print('O primeiro número digitado é inválido!')
