def aumentar(preco=0, porc=0, mostrar=False):
    aum = preco + (preco * porc / 100)
    return aum if mostrar is False else moeda(preco)


def diminuir(preco=0, porc=0, mostrar=False):
    dim = preco - (preco * porc / 100)
    return dim if mostrar is False else moeda(preco)

def dobro(preco=0, mostrar=False):
    dob = preco * 2
    return dob if mostrar is False else moeda(preco)


def metade(preco=0, mostrar=False):
    met = preco / 2
    return met if mostrar is False else moeda(preco)


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco}'.replace('.', ',')