from time import sleep

def contador(i, f, p):
    print('=' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p < 0:
        p += -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
        print('FIM!')
    print('=' * 40)

contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Número para iniciar: '))
fim = int(input('Número para terminar: '))
passo = int(input('Passos a dar: '))
contador(inicio, fim, passo)