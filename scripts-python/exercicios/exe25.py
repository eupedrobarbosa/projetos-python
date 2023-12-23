from random import choice

pote1 = [
    'Arsenal', 
    'Barcelona',
    'Chelsea',
    'Dortmund'
]

pote2 = [
    'Real Madrid',
    'Liverpool',
    'City',
    'Bayern'
]

gols = [0, 1, 2, 3, 4, 5, 6]

print (choice(pote1), choice(gols), '-', choice(gols), choice(pote2))