a, b, c = 1, 2, 1
delta = b**2 - 4*a*c
if delta > 0:
  x1 = (-b + delta**(1/2))/(2a)
  x2 = (-b - delta**(1/2))/(2a)
  print('As raizes sao {} e {}'.format(x1, x2))
elif delta == 0:
  x = -b/(2a)
  print('As raiz é {}'.format(x))
else:
  print('Sem raiz real')
