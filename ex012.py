prod = float(input('Qual é o preço do produto que deseja comprar? R$'))

desc = prod - (prod * 0.05)

print('O produto almejado que custava {:.2f} reais com o desconto de 5% \n'
      'da promoção passará a custar {:.2f} reais'.format(prod, desc))
