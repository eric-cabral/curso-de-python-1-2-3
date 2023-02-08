def aumentar(preco, porc):
    aum = preco + (preco * porc / 100)
    return aum


def diminuir(preco, porc):
    dim = preco - (preco * porc / 100)
    return dim

def dobro(preco):
    dob = preco * 2
    return dob


def metade(preco):
    met = preco / 2
    return met
