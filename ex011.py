print('Iremos calcular o tanto de tinta que você precisará para pintar sua parede;\n'
      'Nos informe alguns dados.')

larg = float(input('Largura da parede (em metros):'))
alt = float(input('Altura da parede (em metros):'))
dim = larg * alt
tinta = dim / 2

print('Sua parede tem a área de {}m²;\n'
      'Necessitando de {}l de tinta para ser pintada por inteira!'.format(dim, tinta))
