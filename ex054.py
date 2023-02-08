maiores = 0
menores = 0

for rep in range(1, 8):
    ano = int(input('Digite uma data de nascimento: '))
    if ano <= 2004:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('{} pessoas são maiores de idade.'.format(maiores))
print('{} pessoas são menores de idade.'.format(menores))
