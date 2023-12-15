altura = float (input ('Digite a altura: '))
base = float (input ('Digite a base: '))
area = altura*base
tinta = area / 2

print ('Será necessário usar {}L para pintar uma parede {:.0f} x {:.0f}'.format(tinta, altura, base))