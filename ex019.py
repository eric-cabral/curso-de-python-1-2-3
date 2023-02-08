import random
al1 = str(input('Primeiro aluno do sorteio: '))
al2 = str(input('Segundo aluno do sorteio: '))
al3 = str(input('Terceiro aluno do sorteio: '))
al4 = str(input('Quarto aluno do sorteio: '))
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)

print('O aluno escolhido foi o {}!!!'.format(escolhido))
