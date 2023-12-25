from random import sample

#organizando de forma aleatória

nomes = [
    'Pedro',
    'Kaio',
    'Vanessa',
    'Orlando'
]

r_names = sample(nomes, 4)

print ('A ordem ficou: ')
print (r_names)