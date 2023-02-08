preconormal = float(input('Digite o valor do produto: '))
print('''As formas de pagamento são as seguintes:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço formal
[4] 3x ou mais no cartão: 20% de juros''')

tipopagamento = int(input('Forma de pagamento escolhida: '))

if tipopagamento >= 1 and tipopagamento <= 4:
    if tipopagamento == 1:
        calculo = preconormal - (preconormal * 0.1)
        print(f'Pela forma de pagamento escolhida de R${preconormal:.2f} foi para R${calculo:.2f}')
    elif tipopagamento == 2:
        calculo = preconormal - (preconormal * 0.05)
        print(f'Pela forma de pagamento escolhida de R${preconormal:.2f} foi para R${calculo:.2f}')
    elif tipopagamento == 3:
        print(f'Pela forma de pagamento escolhida o preço permanece R${preconormal:.2f}')
    else:
        calculo = preconormal + (preconormal * 0.2)
        print(f'Pela forma de pagamento escolhida de R${preconormal:.2f} passou a ser R${calculo:.2f}')
else:
    print('Tipo de pagamento inválido.')
