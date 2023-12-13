jogador = input ('Qual nome do jogador?')
partidas = int (input ('Quantas partidas jogadas: '))
vitorias = int (input ('Quantas vitórias: '))
empates = int (input ('Quantos empates: '))
derrotas = int (input ('Quantas derrotas: '))
gols = int (input ('Quantos gols: '))

soma = (vitorias / partidas) * 100

print ('Estatísticas do {}: Partidas jogadas {}, vitórias {}, empates {}, derrotas {}, gols {}'.format(jogador, partidas, vitorias, empates, derrotas, gols), end = '')

print (', taxa de vitórias: {:.2f}%'.format(soma))


