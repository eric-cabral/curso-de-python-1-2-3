lista = []
maior = menor = 0
for rep in range(0, 5):
    lista.append(int(input('Digite um valor numérico: ')))
    if rep == 0:
        maior = menor = lista[rep]
    else:
        if lista[rep] < menor:
            menor = lista[rep]
        if lista[rep] > maior:
            maior = lista[rep]
print(f'O maior valor digitado foi {maior} e está na ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}ª posição... ', end='')
print()
print(f'O menor valor digitado foi {menor} e está na ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}ª posição... ', end='')
print()
