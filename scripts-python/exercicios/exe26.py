

#calculando hipotenusa

co = float (input ('Digite o cateto oposto: '))
ca = float (input ('Digite o cateto adjente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print ('A hipotenusa vai ser {:.2f}'.format(hi))