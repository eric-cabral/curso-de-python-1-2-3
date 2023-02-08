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


def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    imagem('RESUMÃO TOP')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'Metade do preço: \t{moeda(metade(preco))}')
    print(f'{aumento}% de aumento: \t{moeda(aumentar(preco, aumento))}')
    print(f'{reducao}% de redução:  \t{moeda(diminuir(preco, reducao))}')
    print('-' * 35)


def imagem(msg):
    print('-' * 35)
    print(msg.center(35))
    print('-' * 35)
