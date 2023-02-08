n = int(input('Digite um número entre 0 e 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Esse número tem:')
print('{} milhares;'.format(m))
print('{} centenas;'.format(c))
print('{} dezenas;'.format(d))
print('{} unidades.'.format(u))

#print('Esse número tem:')
#print('{} milhares;'.format(n[0]))
#print('{} centenas;'.format(n[1]))
#print('{} dezenas;'.format(n[2]))
#print('{} unidades.'.format(n[3]))