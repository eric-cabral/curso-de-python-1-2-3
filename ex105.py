def notas(* n, sit=False):
    """
    ==> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita vária);
    :param sit: opcional indicando se deve ou não adicionar a situação;
    :return: dicionário com várias informações sobre a situação da turma.
    """
    lista = {"Total": 0, "Maior": 0, "Menor": 10, "Média": 0}
    soma = 0
    for valores in n:
        lista["Total"] +=1
        soma += valores
        if valores > lista["Maior"]:
            lista["Maior"] = valores
        if valores < lista["Menor"]:
            lista["Menor"] = valores
    lista["Média"] = soma / lista["Total"]
    if sit:
        if lista["Média"] <= 5:
            lista["Situação"] = 'RUIM'
        elif 5 > lista["Média"] <= 6:
            lista["Situação"] = 'RAZOÁVEL'
        else:
            lista["Situação"] = 'BOA'
    return lista


resp = notas(5, 10, 10, 10, 5, sit=True)
print(resp)
