alunos = []
alunoscad = []

while True:
    alunoscad.append(str(input('Nome: ')).title())
    alunoscad.append(float(input('Nota 1: ')))
    alunoscad.append(float(input('Nota 2: ')))
    alunoscad.append((alunoscad[1] + alunoscad[2]) / 2)
    alunos.append(alunoscad[:])
    alunoscad.clear()

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Gostaria de continuar (S/N)? ')).strip()
    if continuar.lower() == 'n':
        break

print(f'{"N° | NOME    | MÉDIA":^20}')
print('-' * 20)
for i, v in enumerate(alunos):
    print(f'{i}{" "*4}{v[0]}    {v[3]:>6}')
print('-' * 20)

while True:
    mostrar = int(input('Deseja mostrar as notas de qual aluno (999 interrompe)? '))
    if mostrar == 999:
        print()
        print('PROGRAMA SENDO FINALIZADO........')
        break
    else:
        print(f'As notas de {alunos[mostrar][0]} são {alunos[mostrar][1]} e {alunos[mostrar][2]}')
    print('-' * 20)

print('FINALIZADO COM SUCESSO, MUITO OBRIGADO!')
