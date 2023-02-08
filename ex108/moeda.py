def aumentar(preco=0, porc=0):
    aum = preco + (preco * porc / 100)
    return aum


def diminuir(preco=0, porc=0):
    dim = preco - (preco * porc / 100)
    return dim

def dobro(preco=0):
    dob = preco * 2
    return dob


def metade(preco=0):
    met = preco / 2
    return met


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco}'.replace('.', ',')