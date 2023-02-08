din = float(input('Digite um valor em reais para ser convertido em outras moedas: R$'))
dolar = din / 5.61
euro = din / 6.35

print('Com {:.2f} reais você poderá comprar:\n'
      '{:.2f} dólares\n'
      '{:.2f} euros'.format(din, dolar, euro))
