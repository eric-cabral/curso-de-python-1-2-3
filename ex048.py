s = 0

for n in range(1, 501):
    teste = n % 2
    if teste != 0:
        teste2 = n % 3
        if teste2 == 0:
            s = s + n
print('Os números impares e divisíveis por três de 1 a 500 somados são {}'.format(s))
