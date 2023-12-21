import random
#sorteio de times...

poteA = ['Barcelona', 'Real Madrid', 'Liverpool', 'United']
poteB = ['City', 'Chelsea', 'Newcastle', 'Bayern']

gols = [0, 1, 2, 3, 4, 5, 6]

print (random.choice(poteA), random.choice(gols), '-', random.choice(gols), random.choice(poteB))