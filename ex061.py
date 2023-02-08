termo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))
cont = 0

while cont < 10:
        print(termo, end=' → ')
        termo = termo + razao
        cont += 1
print('ACABOU!')
