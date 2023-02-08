media = 0
idademaisvelho = 0
nomemaisvelho = 0
menoresdevinte = 0

for pessoas in range(1, 5):
    print('====|DADOS DA {}ª PESSOA ANALISADA|===='.format(pessoas))
    nome = str(input('Nome: '.format(pessoas)))
    idade = int(input('Idade: '.format(pessoas)))
    sexo = str(input('Sexo (M ou F): ').strip().upper())
    print('=======================================')
    if pessoas == 1:
        media = media + idade
        if sexo == 'F':
            if idade <= 20:
                menoresdevinte = menoresdevinte + 1
        elif sexo == 'M':
            idademaisvelho = idade
            nomemaisvelho = nome
    if pessoas > 1:
        media = media + idade
        if sexo == 'F':
            if idade <= 20:
                menoresdevinte = menoresdevinte + 1
        if sexo == 'M' and idade > idademaisvelho:
            idademaisvelho = idade
            nomemaisvelho = nome
media = (media/4)
print('A média de idade das 4 pessoas é {:.2f} anos.'.format(media))
print(f'O homem mais velho é o {nomemaisvelho} com a idade de {idademaisvelho} anos.')
print(f'{menoresdevinte} mulher(es) têm menos de 20 anos.')
