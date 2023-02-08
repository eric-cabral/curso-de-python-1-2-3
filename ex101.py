def voto(ano):
    from datetime import date
    if (date.today().year - ano) > 18:
        return print(f'Com {date.today().year - ano} anos o voto é obrigatório!')
    elif (date.today().year - ano) < 16:
        return print(f'Com {date.today().year - ano} anos o voto é negado!')
    else:
        return print(f'Com {date.today().year - ano} anos o voto é opcional!')


nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
