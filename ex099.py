lista = []
def maior(* lista):
    tam = len(lista)
    maior = 0
    for valor in lista:
        print(f'{valor} ', end='')
        if valor > maior:
            maior = valor
    print()
    print(f'Ao todo foram {tam} sendo {maior} o maior.')
    print('=-' * 40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
