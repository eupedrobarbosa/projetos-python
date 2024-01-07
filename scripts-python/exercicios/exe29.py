#Sistema para saber quantidades de caixas necessárias para tal área.

from math import ceil

comprimento = float (input ('Digite o comprimento da área: '))
largura = float (input ('Digite a largura da área: '))

at = comprimento * largura #área total
print (f'Área total: {at :.2f}m²')

#informações da caixa de piso

metro = float (input ('Digite o metro da caixa: '))
pecas = int (input ('Digite a quantidade de peças dentro da caixa: '))

somac = at / metro


print (f'Para colocar piso em uma área de {at :.2f}m², será necessário usar {ceil(somac) :.0f} caixas.')

