#Sistema de cálculos com aluguel, financeiro, etc.

import math
import random

#salario

print ('-' * 20)

salario = int (input ('Digite seu salário: R$'))

print ('Salário: R${}'.format(salario))

aumento = salario + (salario * 20 / 100) #Aumento no salário em 20%.

print ('Salário com aumento: R$ {}'.format(aumento))

#aluguel por mês.

print ('-' * 20)
print ('ALUGUEL')

aluguel = 600
print ('Aluguel: R$ {}'.format(aluguel))

cmes = int (input ('Meses contratados: ')) #contrato meses

gasto_alugel = cmes * aluguel

print ('Valor à pagar: R$ {}'.format(gasto_alugel))

print ('-' * 20)

print ('GASTO COM CARRO')

km = int (input ('Digite a quantidade de km por litro: '))

comb = float (input ('Preço combustível: R$ '))

kmr = float (input ('Digite a quantidade de km rodados: '))

gasto = (kmr / km) * comb

print ('GASTO COM COMBUSTÍVEL: R$ {:.2f}'.format(gasto))

print ('-' * 20)

gt = gasto_alugel + gasto #aluguel + combustível

print ('GASTO TOTAL: R$ {}'.format(gt))