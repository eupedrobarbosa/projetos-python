preco = int (input ('Quanto custa esse produto?'))
qtd = int (input ('Quantos vai querer?'))

soma = preco*qtd
desconto = 0.05

resultado = soma*desconto
preco_total = soma - resultado

print ('O preço {} caiu para {}'.format(soma, preco_total))

