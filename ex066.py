cont = soma = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'{cont} foram digitados e a soma entre eles é {soma}.')
