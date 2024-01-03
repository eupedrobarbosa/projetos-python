from math import hypot 

co = float (input ('Digite o cateto oposto: '))
ca = float(input ('Digite o cateto adjente: '))
hi = hypot(co, ca)

print ('A hipotenusa vai ser {:.2f}'.format(hi))