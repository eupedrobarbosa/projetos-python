preco = int (input ('Digite um valor: '))
qtd = int (input ('Digite a quantidade: '))

soma = preco*qtd

desconto = 0.05 * soma

total = soma - desconto

print ('O total com desconto de 5% é {}'.format(total))

