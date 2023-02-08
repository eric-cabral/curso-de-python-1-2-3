termo = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão da P.A.: '))
cont = 0
total = 0
mais = 10

while mais != 0:
        total = total + mais
        while cont < total:
                print(termo, end=' → ')
                termo = termo + razao
                cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont} termos mostrados.')
