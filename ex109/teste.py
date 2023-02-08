from ex109 import moeda

p = float(input('Valor que deseja calcular: R$ '))

print(f'O dobro de {p} é {moeda.dobro(p, True)};')
print(f'A metade de {p} é {moeda.metade(p)};')
print(f'Aumentando 10% de {p} temos {moeda.aumentar(p, 10)};')
print(f'Diminiundo 5% de {p} temos {moeda.diminuir(p, 5)}')
