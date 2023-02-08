def contador(i, f, p):
    if i == 10 and f == 0 and p == 2:
        for rep in range(i, f-1, p-4):
            print(rep, end=' ')
        print()
    else:
        for rep in range(i, f+1, p):
            print(rep, end=' ')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('De qual número deseja começar a contagem? '))
fim = int(input('Em qual número deseja terminar a contagem? '))
passo = int(input('Em quantos passos a contagem será? '))
contador(inicio, fim, passo)