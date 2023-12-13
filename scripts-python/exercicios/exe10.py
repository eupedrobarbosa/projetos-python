altura = float (input ('Digite a altura da parede: '))
base = float (input ('Digite a base dessa parede: '))

soma = altura * base
tinta = 2
gasto = soma / tinta

print ('Será necessário usar {} litros para pintar a parede.'.format(gasto))
