frase = str(input('Digite uma frase: ').strip().upper())

print('A letra A aparece {} vezes na frase digitada;'.format(frase.count('A')))
print('A primeira vez que a letra A aparece na frase foi na posição {};'.format(frase.find('A')+1))
print('A última vez que a letra A aparece na frase foi na posição {}.'.format(frase.rfind('A')+1))

#Linha 4 - Vai buscar a primeira letra A na frase e o +1 é pq o python identifica a primeira letra da frase como caractere 0
#Linha 5 - Igual a linha de cima com a diferença que na função find eu irei usar a rfind que busca da direita para a esquerda
