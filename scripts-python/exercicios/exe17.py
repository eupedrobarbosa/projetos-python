
partidas = int (input ('Quantas partidas jogadas?'))
vitorias = int (input('Quantas partidas vencidas?'))

winrate = (vitorias / partidas) * 100

print ('Seu winrate: {:.2f}%'.format(winrate))


