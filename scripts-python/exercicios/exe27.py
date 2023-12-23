from math import hypot

co = float (input ('Digite um cateto oposto: '))
ca = float (input ('Digite um cateto adjente: '))
hi = hypot (co, ca)

print ('A hipotenusa vai ser {:.2f}'.format(hi))