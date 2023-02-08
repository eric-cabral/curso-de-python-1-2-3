print('Bom dia, iremos pedir algumas informações para calcular seu empréstimo!')
casa = float(input('Digite o valor da casa que você deseja comprar: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos você irá pagar? '))

meses = anos*12
prestacao = casa/meses

if prestacao > (salario*0.3):
    print('Infelizmente o empréstimo é inviável pelos dados que digitou.')
else:
    print('Empréstimo viável, o valor da prestação será de {:.2f}'.format(prestacao))
