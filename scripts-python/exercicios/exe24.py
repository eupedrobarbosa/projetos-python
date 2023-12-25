import random

#sorteando um participante
#sorteando um prêmio para o participante

nomes = [
    'Pedro',
    'Vanessa',
    'Kaio'
    'Orlando',
    'Ágata'
]

premios = [
    10000, #10k
    20000, #20k
    10000000, #1 milhão
]

print ('O sorteado foi {}'.format(random.choice(nomes)))
print ('E ganhou um prêmio de R${}'.format(random.choice(premios)))
