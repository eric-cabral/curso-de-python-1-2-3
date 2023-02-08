sal = float(input('Qual é o salário do funcionário? R$'))
aum = sal * 1.15

print('O funcionário com salário de R${:.2f} recebendo um aumento de 15%, \n'
      'passará a ganhar R${:.2f}.'.format(sal, aum))
