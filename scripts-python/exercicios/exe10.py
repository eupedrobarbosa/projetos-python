print ('Olá, seja bem-vindo! Loja de pinturas.')

altura = int (input ('Qual a altura da parede?'))
base = int (input ('Qual a base da parede?'))

soma = altura*base
tinta = 2

gasto = soma / tinta

print ('Será necessário usar {} litros para pintar a parede desejada de acordo com as informações passadas.'.format(gasto))