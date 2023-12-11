bem_vindo = 'Olá, seja bem-vindo(a)!'
print (bem_vindo)

nome = str(input('Qual seu nome?'))
print(nome, ', vamos calcular!')

n1 = int (input('Digite um valor: '))
n2 = int (input('Digite outro valor: '))
a = n1 + n2
s = n1 - n2
d = n1 / n2
m = n1 * n2
e = n1 ** n2

print ('A adição de {}, subtração {}, divisão {}, multiplicação {} e exponencial {}'.format(a,s,d,m,e), end = ' ')

print ('Obrigado!')



