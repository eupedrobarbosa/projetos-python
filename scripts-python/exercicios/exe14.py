preco = int (input ('Qual o preço do produto?'))
qtd = int (input ('Quantidada: '))

desconto = 0.05

soma = preco*qtd
desconto_sub = soma*desconto

total = soma - desconto_sub

print ('Deu {} e com desconto deu {}'.format(soma, total))

