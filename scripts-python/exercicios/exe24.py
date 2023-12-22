import random

#sorteando uma pessoa para ganhar um prêmio aleátorio.

premios = [
    1000,
    2000,
    3000,
    4000
]

win_premios = random.choice(premios)

participante = [
    'Pedro',
    'Kaio',
    'Vanessa',
    'Orlando'
]

random_participantes = random.choice (participante)

print ('O participante {} ganhou R${:.2f}'.format(random_participantes, win_premios))
