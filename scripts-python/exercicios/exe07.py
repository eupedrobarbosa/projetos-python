from math import sqrt

#calculando o dobro, triplo e raiz de um número

num = int (input ('Digite um número: '))

d = num * 2
t = num * 3
r = sqrt(num)

print ('Número escolhido {}.'.format(num))
print ('Dobro: {}'.format(d))
print ('Triplo: {}'.format(t))
print ('Raiz quadrada: {:.0f}'.format(r))

