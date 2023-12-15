partidas = int (input ('Partidas: '))
vitorias = int (input ('Vitórias: '))

soma = (vitorias / partidas) * 100

print ('Taxa de winrate: {:.2f}%'.format(soma))