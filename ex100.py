from random import randint

numeros = []

def sorteia():
    for num in range(0, 5):
        numeros.append(randint(0, 50))
    print(f'Os valores sorteados foram {numeros}.')

def somaPar():
    soma = 0
    for valores in numeros:
        if valores % 2 == 0:
            soma += valores
    print(f'A soma entre os números pares sorteados é {soma}.')


sorteia()
somaPar()
