salario = int (input ('Digite um salário: '))
desconto = 0.20

salario_desconto = salario*desconto
total = salario + salario_desconto

print ('Seu salário de {} subiu para {}'.format(salario, total))