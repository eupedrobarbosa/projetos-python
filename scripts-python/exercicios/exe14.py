preco = float (input ('Preço do produto: R$'))
qtd = int (input ('Quantidade: '))
soma = preco*qtd

desconto = soma - (soma * 5 / 100)

print ('A compra deu R${:.2f}, e com desconto ficou R${:.2f}'.format(soma, desconto))
