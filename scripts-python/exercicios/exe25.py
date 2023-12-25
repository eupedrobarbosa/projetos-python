from random import choice

#sorteado um duelo de clubes

pote1 = [
    'Barcelona',
    'Arsenal',
    'Chelsea',
    'Real Madrid'
]

pote2 = [
    'Liverpool',
    'City',
    'Dortmund',
    'Bayern'
]

goals = [0, 1, 2, 3, 4, 5, 6]

print (choice(pote1), choice(goals), '-', choice(goals), choice(pote2))