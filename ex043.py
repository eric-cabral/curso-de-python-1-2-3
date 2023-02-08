print('Iremos calcular seu IMC, só precisamos de alguns dados.')

peso = float(input('Digite seu peso (00kg): '))
altura = float(input('Digite sua altura (0.00m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('O seu IMC é {:.2f} e está abaixo do peso.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é {:.2f} e está no peso ideal, parabéns!'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é {:.2f} e está com sobrepeso.'.format(imc))
elif imc >= 30 and imc < 40:
    print('O seu IMC é {:.2f} e está com obesidade.'.format(imc))
else:
    print('O seu IMC é {:.2f} e está com obesidade mórbida, cuidado!'.format(imc))
