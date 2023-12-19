salario = float (input ('Digite seu salário: R$'))
#Aumento de salário em 20%
aumento_total = salario + (salario * 20 / 100)

print ('Seu salário subiu de R${:.2f} para R${:.2f}'.format(salario, aumento_total))