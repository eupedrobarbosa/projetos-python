from random import choice

#sorteando um ganhador e um prêmio para o mesmo

nomes = [
    'Pedro',
    'Kaio',
    'Vanessa',
    'Orlando'
]

premios = [
    1000,
    2000,
    5000,
    10000
]

print (f'O ganhador foi {choice(nomes)} e recebeu um prêmio de R$ {choice(premios)}')