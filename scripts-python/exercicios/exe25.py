from random import choice

#sorteando equipes and gols

pote1 = [
    'Barceloa',
    'Real Madrid'
]

pote2 = [
    'City',
    'Arsenal'
]

goals = [0, 1, 2, 3, 4, 5, 6]

print (choice(pote1), choice(goals), '-', choice(goals), choice(pote2))