#Sistema básico para calcular o gasto de tinta para pintar uma parede.

a = float (input ('Altura da parede: '))
b = float (input ('Base da parede: '))

area = a * b
t = 2 #tinta
g = area / t #gasto

print ('Para pintar uma parede {:.0f} x {:.0f}, será necessário usar {}L'.format(a, b, g))