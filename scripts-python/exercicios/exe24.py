import random

#sorteio

pote1 = 5000
pote2 = 100000000 #1 milhão
pote3 = 10000
pote4 = 1000

sorteio = [pote1, pote2, pote3, pote4]

print ('Você ganhou um prêmio de R${}'.format(random.choice(sorteio)))