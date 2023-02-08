salario = float(input('Digite o salário de um funcionário para o aumento ser calculado: '))

if salario > 1250:
    aumento = salario + (salario * 0.10)

if salario <= 1250:
    aumento = salario + (salario * 0.15)

print(f'O salário com aumento é {aumento:.2f}.')
