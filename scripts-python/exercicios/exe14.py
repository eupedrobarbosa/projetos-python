preco = float (input ('Preço: R$'))
qtd = int (input ('Quantidade: '))
desconto = 0.05

soma = preco*qtd
subtotal = soma * desconto
total = soma - subtotal

print ('A compra deu R${}. Com desconto ficou R${}'.format(soma, total))

