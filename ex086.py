matrizes = [[], [], []]

for c in range(0, 3):
        matrizes[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(0, 3):
        matrizes[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(0, 3):
        matrizes[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
print(f'[{matrizes[0][0]:^5}] [{matrizes[0][1]:^5}] [{matrizes[0][2]:^5}]')
print(f'[{matrizes[1][0]:^5}] [{matrizes[1][1]:^5}] [{matrizes[1][2]:^5}]')
print(f'[{matrizes[2][0]:^5}] [{matrizes[2][1]:^5}] [{matrizes[2][2]:^5}]')
