def Baskhara(a, b, c):
  delta = b**2 - 4*a*c
  if delta > 0:
    x1 = round((-b + delta**(1/2))/(2a), 3)
    x2 = round((-b - delta**(1/2))/(2a), 3)
    print('As raizes sao {} e {}'.format(x1, x2))
  elif delta == 0:
    x = round(-b/(2a), 3)
    print('As raiz é {}'.format(x))
  else:
    print('Sem raiz real')
