valores = list()

for lista in range(0, 5):
    novovalor = int(input('Digite um valor para ser adicionado a lista: '))
    if lista == 0 or novovalor > valores[-1]:
        valores.append(novovalor)
    else:
        pos = 0
        while pos < len(valores):
            if novovalor <= valores[pos]:
                valores.insert(pos, novovalor)
                break
            pos += 1
print(valores)
