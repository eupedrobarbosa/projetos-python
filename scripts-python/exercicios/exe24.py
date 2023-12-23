import random

#sorteando vencedor e prêmios.

premios = [
    1000,
    2000,
    3000,
    4000
]

names = [
    'Pedro',
    'Kaio',
    'Vanessa',
    'Orlando'
]

print ('O sorteado foi {}.'.format(random.choice(names)), end =' ')
print ('E com isso venceu um prêmio de {}.'.format(random.choice(premios)))
