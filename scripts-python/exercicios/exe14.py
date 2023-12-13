preco = int (input ('Qual o valor do produto?'))
qtd = int (input ('Quantos vai querer?'))

soma = preco*qtd
desconto = 0.05

subtotal = soma * desconto
total = soma - subtotal

print ('Deu R$ {}, com o desconto dá {}'.format(soma, total))


