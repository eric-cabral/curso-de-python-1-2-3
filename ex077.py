palavras = ('Carro', 'Computador', 'Eric', 'Tecnologia',
            'Programacao', 'Trocar', 'Curso', 'Em', 'Video',
            'Python', 'aeiou')

print(f'{" Palavras e suas respectivas vogais ":-^50}')
for p in palavras:
    print('\n',p, '- ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
