print('Para calcular o valor do aluguel precisamos de algumas informações.')

perc = float(input('Quantidade de KM percorridos com o carro: '))
tempo = int(input('Quantidade de dias que o carro foi utilizado: '))
km = perc * 0.15
dias = tempo * 60
valor = km + dias

print('O valor pelos dias usados é de R${:.2f}, o valor dos KM percorridos é de R${:.2f},\n'
      'portanto o valor do alguel a ser pago é de R${:.2f}.'.format(dias, km, valor))
