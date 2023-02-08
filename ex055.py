maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoas}ª pessoa: '))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if pessoas > 1:
            if peso < maior:
                menor = peso
            else:
                maior = peso
print('O maior peso lido foi de {:.2f} Kg '.format(maior))
print('O menor peso lido foi de {:.2f} Kg '.format(menor))
