def calculoArea(l, c):
    area = l * c
    print(f'A área de um terreno de {l} X {c} é {area} m².')


print(f'{"CONTROLE DE TERRENOS": ^30}')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
calculoArea(largura, comprimento)
