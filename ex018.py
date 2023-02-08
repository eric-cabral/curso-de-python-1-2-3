from math import cos, sin, tan, radians
ang = float(input('Digite um ângulo que você deseja (em graus): '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('Para um ângulo de {:.2f} graus:\n'
      'O cosseno será {:.2f}\n'
      'O seno será {:.2f}\n'
      'A tangente será {:.2f}'.format(ang, seno, cosseno, tangente))
