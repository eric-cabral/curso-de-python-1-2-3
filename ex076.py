produtos_precos = ('Camiseta', 30.00,
                   'Camisa', 100.00,
                   'Sapato Social', 279.90,
                   'Tênis Shopee', 95.00,
                   'Vans Ultrarange', 479.00,
                   'Calça Jeans', 150.00,
                   'Vestido', 120.00,
                   'Sapato Feminino', 150.00,
                   'Calça Wide Leg', 110.00,
                   'Jaqueta', 240.00)
print('+' * 50)
print('LOJÃO DO ERICÃO'.center(50, ' '))
print('+' * 50)
for rep in range(0, len(produtos_precos)):
    if rep % 2 == 0:
        print(f'{produtos_precos[rep]:.<41}', end='')
    else:
        print(f'R${produtos_precos[rep]:>7.2f}')
print('-' * 50)
