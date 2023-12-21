import random
import math

#sorteio
#p = participante

p1 = input ('Participante 01: ')
p2 = input ('Participante 02: ')
p3 = input ('Participante 03: ')
p4 = input ('Participante 04: ')

participantes = [p1, p2, p3, p4]

print ('O participante sorteado foi {}'.format(random.choice(participantes)))