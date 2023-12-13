km = int (input ('Quantos km por litro? '))
combutisvel = float (input ('Qual valor do combustível? '))
kmr = int (input ('Quantos km quer rodar? '))

soma = (kmr/km) * combutisvel

print ('Para percorrer uma distância de {}km você gastará R$ {} de combustível.'.format(kmr, soma))


