from ex115.sistemadecadastro import validacoes
from time import sleep


def menuInicial():
    print('\033[1;32m-\033[m' * 40)
    print(f'\033[1;32m{"MENU PRINCIPAL": ^40}\033[m')
    print('\033[1;32m-\033[m' * 40)
    print('\033[1;34m1 -\033[m Ver Pessoas Cadastradas')
    print('\033[1;31m2 -\033[m Cadastrar Nova Pessoa')
    print('\033[1;35m3 -\033[m Sair do Sistema')
    print('\033[1;32m-\033[m' * 40)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo "{nome}" criado com sucesso')


def mostrarCad(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        validacoes.prints('\033[0;36mOPÇÃO 1 - PESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')

    finally:
        a.close()


def novoCad(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados!')
        else:
            a.close()
            validacoes.prints('\033[0;31mCadastro realizado com sucesso!!!\033[m')
            sleep(0.5)


def sair():
    validacoes.prints('\033[1;35mSaindo do sistema... Valeu meu querido!\033[m')
    sleep(1)
