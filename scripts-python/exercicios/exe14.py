#Desconto

p = float (input ('Digite o preço do produto: R$'))
q = int (input ('Digite a quantidade: '))
s = p * q #soma

#5% de desconto
desconto = s - (s * 5 / 100)

print ('A compra deu R$ {}, e com desconto ficou R$ {}'.format(s, desconto))
