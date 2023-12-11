salario_atual = float (input ('Qual o seu salário atual?'))

print ('Seu salário atual {:.1f}'.format(salario_atual))

aumento = 0.20

soma = salario_atual*aumento

resultado = salario_atual + soma

print ('Seu salário subiu de R$ {} para R$ {}'.format(salario_atual, resultado))