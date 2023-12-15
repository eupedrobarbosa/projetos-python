km = int (input ('Quantos km por litro: '))
comb = float (input ('Qual preço do comnustível? '))
kmr = int (input ('Quantos km para rodar: '))

soma = (kmr / km) * comb

print ('Para andar {}km será necessário gastar {} reais'.format(kmr, soma))


