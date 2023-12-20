preco = float (input ('Digite o preço: R$'))
qtd = int (input ('Quantidade: '))
soma = preco * qtd
#desconto de 5%
desconto = soma - (soma * 5 / 100)

print ('A compra deu R${:.2f}, e com desconto caiu para R${:.2f}'.format(soma, desconto))
