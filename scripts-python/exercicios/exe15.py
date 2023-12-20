salario = float (input ('Digite seu salário: R$'))
#aumento em 20% do salário
aumento = salario + (salario * 20 / 100)

print ('Seu salário subiu de R${:.2f} para R${:.2f}'.format(salario, aumento))