cont = 0
acum = 0

n = int(input('Digite um número (999 para parar): '))

while n != 999:
    acum = acum + n
    cont += 1
    n = int(input('Digite um número (999 para parar): '))
print(f'Você digitou {cont} números e a soma entre eles é {acum}.')
