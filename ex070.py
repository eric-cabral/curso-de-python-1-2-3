totvalor = mais1000 = precobarato = nomebarato= 0

print('-' * 25)
print('CADASTRO DE PRODUTOS')
print('-' * 25)
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Valor do produto: R$ '))
    if precobarato == 0:
        precobarato = preco
    if preco < precobarato:
        nomebarato = nome
        precobarato = preco
    if preco > 1000:
        mais1000 += 1
    totvalor += preco
    continuar = str(input('Deseja cadastrar mais produtos (S/N)? ')).strip().lower()[0]
    if continuar == 'n':
        print('-------------- FIM DO CADASTRO --------------')
        break
print(f'''A) Valor total gasto na compra: {totvalor}.
B) Produtos que custam mais de R$ 1.000,00: {mais1000}.
C) Produto mais barato: {nomebarato} custando {precobarato} reais.''')