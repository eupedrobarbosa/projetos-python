salario = float (input('Digite seu salário: R$'))
#20% de aumento do salário.
salario_aumentado = salario + (salario * 15 / 100)

print ('Seu salário subiu de R${:.2f} para R${:.2f}'.format(salario, salario_aumentado))