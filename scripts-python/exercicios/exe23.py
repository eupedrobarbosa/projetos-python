import random
#lista sorteada

n1 = input ('Nome: ')
n2 = input ('Nome: ')
n3 = input ('Nome: ')
n4 = input ('Nome: ')

nomes = [n1, n2, n3, n4]

print (random.sample(nomes, 4))