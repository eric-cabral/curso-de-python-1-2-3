homens = mulheres = pessoasmaisdezoito = 0

while True:
    print('-' * 20)
    print('CADASTRO DE PESSOAS')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().lower()[0]
    if sexo != 'm' and sexo != 'f' or idade <= 0:
        print('Algum dos dados é inválido, preencha novamente!')
    else:
        if sexo == 'm':
            homens += 1
            if idade > 18:
                pessoasmaisdezoito += 1
        else:
            if sexo == 'f':
                if idade < 20:
                    mulheres += 1
                elif idade > 18:
                    pessoasmaisdezoito += 1
    novamente = str(input('Você deseja cadastrar mais alguma pessoa (S/N)? ')).strip().lower()
    if novamente == 'n':
        break
print('=' * 30)
print('Informações extraidas dos dados informados:')
print(f'''A) Maiores de 18 anos: {pessoasmaisdezoito}.
B) Total de homens cadastrados: {homens}.
C) Mulheres menores de 20 anos: {mulheres}.''')
