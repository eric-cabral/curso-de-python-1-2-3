from ex107 import moeda

p = float(input('Valor que deseja calcular: R$ '))

print(f'O dobro de {p:.2f} é {moeda.dobro(p):.2f};')
print(f'A metade de {p:.2f} é {moeda.metade(p):.2f};')
print(f'Aumentando 10% de {p:.2f} temos {moeda.aumentar(p, 10):.2f};')
print(f'Diminiundo 5% de {p:.2f} temos {moeda.diminuir(p, 5):.2f}.')
