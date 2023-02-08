from random import randint

n1 = [randint(0, 100)]
n2 = [randint(0, 100)]
n3 = [randint(0, 100)]
n4 = [randint(0, 100)]
n5 = [randint(0, 100)]
juncao = n1 + n2 + n3 + n4 + n5

print(f'Número gerados: {juncao}.')
print(f'O menor número sorteado foi {min(juncao)}'
      f' e o maior foi {max(juncao)}.')