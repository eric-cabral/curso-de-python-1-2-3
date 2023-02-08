#from datetime import date
#atual = date.today().year -> puxar o ano atual na variável

sexo = str(input('Você é homem ou mulher? ').lower().strip())

if sexo == 'homem':

    nascimento = int(input('Digite o ano de seu nascimento: '))
    idade = 2022 - nascimento

    if idade == 18:
        print('Está na hora de se alistar no serviço militar!')
    elif idade < 18:
        tempo = 18 - idade
        print(f'Você irá se alistar no serviço militar daqui {tempo} anos!')
    else:
        tempo = idade - 18
        print(f'Você passou pelo serviço militar há {tempo} anos!')

else:
    print('Era sobre serviço militar então não se aplica mas obrigado por responder!!!')
