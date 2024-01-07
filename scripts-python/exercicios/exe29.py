#sistema para verificar quantas caixas de piso necessárias para cobrir uma área.

from math import ceil

com = float (input ('Digite o comprimento da área: '))
lar = float (input ('Digite a largura da área: '))

area = com * lar #área total

#informações do piso

metro = int (input ('Digite o metro da caixa: '))

caixas =  area / metro

print (f'Área total: {area :.2f}m²')
print (f'Piso: {metro}m²')
print (f'Será necessário comprar {ceil(caixas)} caixas para cobrir uma área de {area :.2f}²')
