nascimento = int(input('Digite sua data de nascimento para ver \nem qual categoria de natação você se encaixa: '))

idade = 2022 - nascimento
print(f'O atleta em questão tem {idade} anos.')

if idade <= 9:
    print('Na natação você é da categoria mirim, que é até 9 anos de idade.')
elif idade > 9 and idade <= 14:
    print('Na natação você é da categoria infantil, que é até 14 anos de idade.')
elif idade > 14 and idade <= 19:
    print('Na natação você é da categoria junior, que é até 19 anos de idade.')
elif idade > 19 and idade <= 25:
    print('Na natação você é da categoria sênior, que é até 20 anos de idade.')
else:
    print('Na natação você é da categoria master, que é acima de 20 anos de idade.')
