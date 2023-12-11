altura = float (input ('Digite a altura da parede: '))
base = float (input ('Digite a base da parede: '))

resultado = altura*base
tinta = 2 #2 litros por metro

gasto = resultado / tinta

print ('Será necessário usar {} litros para pintar a parede!'.format(gasto))