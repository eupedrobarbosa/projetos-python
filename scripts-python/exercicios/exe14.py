preco = float (input ('Preço: '))
qtd = int (input ('Quantidade: '))
desconto = 0.05
subtotal = (preco*qtd)
total_desconto = subtotal * desconto
total = subtotal - total_desconto

print ('A compra deu R${}, e com desconto caiu para R${}'.format(subtotal, total))

