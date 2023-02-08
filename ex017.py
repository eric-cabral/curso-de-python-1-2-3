from math import pow, sqrt
print('Iremos calcular o valor da hipotenusa do triângulo, só precisamos de \n'
      'informações.')

catop = float(input('Digite um valor para o cateto oposto: '))
catad = float(input('Digite um valor para o cateto adjacente: '))
hipoquad = (pow(catop, 2) + pow(catad, 2))
hipofinal = sqrt(hipoquad)

print('Um triângulo que o catetos medem {} e {} terá sua hipotenusa no valor de {}.'.format(catop, catad, hipofinal))
