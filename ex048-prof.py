soma = 0 #Esse acumulador é usado para cada vez que for repetindo ir somando os números nele, começa no 0, na primeira vez vira 3 e na segunda vira 9 e etc.
cont = 0 #Esse contador é para cada repetição ter uma contagem, começa no 0 e na primeira repetição é 1 e assim por diante.

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
