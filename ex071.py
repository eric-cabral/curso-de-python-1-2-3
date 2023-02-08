cedulas50 = cedulas20 = cedulas10 = cedulas1 = 0

print('-' * 25)
print(' '*8, 'BANCOLA')
print('-' * 25)

while True:
    saque = int(input('Quantos você deseja sacar? R$ '))
    if (saque / 50) >= 1:
        cedulas50 = saque // 50
    saque = saque % 50
    if (saque / 20) >= 1:
        cedulas20 = saque // 20
    saque = saque % 20
    if (saque / 10) >= 1:
        cedulas10 = saque // 10
    cedulas1 = saque % 10
    break

print('Serão sacadas:')

if cedulas50 != 0:
    print(f'{cedulas50} cédulas de 50 reais.')
if cedulas20 != 0:
    print(f'{cedulas20} cédulas de 20 reais.')
if cedulas10 != 0:
    print(f'{cedulas10} cédulas de 10 reais.')
if cedulas1 != 0:
    print(f'{cedulas1} cédulas de 1 real.')
