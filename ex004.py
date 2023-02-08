algo = input('Digite qualquer coisa que eu lhe mostrarei informações sobre isso:')

print('O tipo primitivo desse valor é:', type(algo))

print('É alfanumérico?', algo.isalnum())
print('Só letras maiúsculas?', algo.isupper())
print('Só letras minúsculas?', algo.islower())
print('É alfabético?', algo.isalpha())
print('É decimal?', algo.isdecimal())
