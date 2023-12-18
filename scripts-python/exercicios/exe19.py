dias = int (input ('Dias alugados: '))
km = float (input ('Km rodados: '))

aluguel = 60
km_h = 0.15

resultado = (dias * aluguel) + (km * km_h)

print ('O valor total resultou em R${:.2f}'.format (resultado))