#Programa básico para calcular quantos litros precisamos para pintar determinada parede de acordo com as informações.

altura = float (input ('Digite a altura da parede: '))
base = float (input ('Digite a base da parede: '))
area = altura * base

#2 litros de tinta por metro.
litro = 2
gasto = area / 2

print ('Para pintar uma parede {:.2f} x {:.2f}, será necessário usar {} litros.'.format(altura, base, gasto ))