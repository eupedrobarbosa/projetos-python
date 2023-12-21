import random

#Sorteio de prêmios

lista_nomes = ['PythonA', 'PythonB', 'PythonC', 'PythonD']

random_names = random.choice(lista_nomes)

p1 = int (input ('Digite o valor do prêmio A: R$'))
p2 = int (input ('Digite o valor do prêmio B: R$'))
p3 = int (input ('Digite o valor do prêmio C: R$'))
p4 = int (input ('Digite o valor do prêmio D: R$'))

pote = [p1, p2, p3, p4]

print ('Parabéns {}, você ganhou o prêmio de R${:.2f}'.format(random_names, random.choice(pote)))
