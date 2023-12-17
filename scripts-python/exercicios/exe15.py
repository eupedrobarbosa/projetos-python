salario = float (input ('Qual seu salário? R$'))
aumento = 0.20

salario_cal = salario * aumento
salario_total = salario + salario_cal

print ('Seu salário subiu de {} para {}'.format(salario, salario_total))