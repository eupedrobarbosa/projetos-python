partidas = int (input ('Partidas: '))
vitorias = int (input ('Vitórias: '))

winrate = vitorias / partidas * 100

print ('A taxa de winrate é {:.2f}%'.format(winrate))