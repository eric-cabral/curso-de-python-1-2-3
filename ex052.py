n = int(input('Digite um número: '))
s = 0

for rep in range(1, n+1):
    if n % rep == 0:
        s = s + 1
if s == 2:
    print(f'O número {n} É primo!')
else:
    print(f'O número {n} NÃO é primo!')
#Corrigir esse exercício