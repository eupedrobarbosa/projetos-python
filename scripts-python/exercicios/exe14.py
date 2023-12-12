preco = int (input('Qual o preço do produto?'))
qtd = int (input('Quantos vai querer?'))

soma = preco*qtd
desconto = 0.05

resultado = soma*desconto
total_desconto = soma - resultado

print ('A compra deu {} e com desconto caiu para {}'.format(soma, total_desconto))

