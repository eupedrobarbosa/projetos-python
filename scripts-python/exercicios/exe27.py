#importação hipotenusa

from math import hypot

co = float (input ('Digite o cateto oposto: '))
ca = float (input ('Digite o cateto adjcente: '))
hi = hypot(co, ca)

print ('A hipotenusa vai medir {:.2f}'.format (hi))