from sistemadecadastro import menu
from sistemadecadastro import validacoes

arq = 'pessoascadastradas'

if not menu.arquivoExiste(arq):
    menu.criarArquivo(arq)

opcao = 999

while opcao != 3:
    menu.menuInicial()
    try:
        opcao = validacoes.leiaInt(f'\033[0;33mOpção desejada:\033[m ')
    except KeyboardInterrupt:
        print('\033[1;41mERRO! Você interrompeu sem escolher uma opção.\033[m')
    else:
        if opcao == 3:
            menu.sair()
            break
        elif opcao == 1:
            menu.mostrarCad(arq)
        elif opcao == 2:
            validacoes.prints('\033[0;31mOPÇÃO 2 - NOVO CADASTRO\033[m')
            nome = str(input('Nome: ')).title().strip()
            idade = validacoes.leiaInt('Idade: ')
            menu.novoCad(arq, nome, idade)
