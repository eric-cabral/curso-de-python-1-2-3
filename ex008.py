n = int(input('Digite a quantidade de metros que serão convertidos:'))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000

print('Essas são as conversões para {} metros:\n'
      'Em quilômetros é {}\n'
      'Em hectómetros é {}\n'
      'Em decametros é {}\n'
      'Em decímetros é {}\n'
      'Em centímetros é {}\n'
      'Em milímetros é {}\n'
      'Obrigado!!!'.format(n, km, hm, dam, dm, cm, mm))
