#sistema para calcular quantidades de pisos e caixas para cobrir um área.

#Informações do piso

from math import ceil

cp = float (input ('Digite o comprimento do piso: '))
lp = float (input ('Digite a largura do piso: '))
qtd_por_caixa = int (input ('Digite a quantidade peças por caixa: '))
ap = cp * lp #

print (f'm² do piso: {ap :.2f}')

#informações da área

comprimento = float (input ('Digite o comprimento: '))
largura = float (input ('Digite a largura: '))
at = comprimento * largura

print (f'Área total: {at}m²')

#Quantidade de peças necessárias

qtd = at / ap

print (f'Será necessário usar {ceil(qtd)} peças.')

qtd_caixas = qtd / qtd_por_caixa

print (f'Será necessário comprar {qtd_caixas :.0f} caixas')