carteira = 100
maca = 3.99

comprar = int (input('O kg da maça custa {}. Quantas maças você vai querer?'.format(maca)))
pgto = maca*comprar

print ('O valor total é {}'.format(pgto))

saldo_atual = carteira - pgto

print ('Seu saldo atual é {}'.format(saldo_atual))

