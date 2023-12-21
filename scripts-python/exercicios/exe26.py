#calcular hipotenusa

co = float (input ('Digite  o cateto oposto: '))
ca = float (input ('Digite o cateto adjcente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print ('A hipotenusa vai medir {:.2f}'.format (hi))