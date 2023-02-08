parar = False
cont = 0
soma = 0
maior = 0
menor = 0

n = int(input('Digite um número: '))

while not parar:
    if maior < n:
        maior = n
        cont += 1
        soma += n
    else:
        menor = n
        cont += 1
        soma += n
    continuar = str(input('Deseja continuar (Sim ou não)? ')).lower().strip()
    if continuar == 'n':
        parar = True
    else:
        n = int(input('Digite um número: '))

media = soma/cont
print('Você digitou {} números e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
