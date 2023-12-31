#Calculando quantos reais gasto para andar x km.

km = int (input ('Quantos km por litro? '))
pcom = float (input ('Preço do combustível: '))
kmr = int (input ('Quantos km quer rodar? '))

s = (kmr / km) * pcom

print ('Será necessário gastar R$ {:.2f} para andar {}km'.format(s, kmr))


