def fatorial(n=1, show=False):
    """
    ==> Cálculo de fatorial de um número.
    :param n: Número que será calculado;
    :param show: Exibe ou não os cálculos;
    :return: Valor fatorial de um número.
    """
    f = 1
    if show is True:
        for rep in range(n, 0, -1):
            f *= rep
            if rep != 1:
                print(f'{rep} x ', end='')
            else:
                print(f'{rep} = ', end='')
        print(f'{f}')
    else:
        for rep in range(n, 0, -1):
            f *= rep
        return print(f'O resultado do fatorial de {n} é {f}.')


numero = int(input('Valor para ser cálculado o fatorial: '))
mostrar = str(input('Exibir cálculos (S/N)? ')).strip()
if mostrar in 'Ss':
    mostrar = True
else:
    mostrar = False
print(fatorial(numero, show=mostrar))
help(fatorial)
