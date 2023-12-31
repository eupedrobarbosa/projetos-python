#Calculando a média de um aluno.

nome = str (input ('Qual nome do aluno? '))

b1 = int (input ('1º bimestre: '))
b2 = int (input ('2º bimestre: '))
b3 = int (input ('3º bimestre: '))
b4 = int (input ('4º bimestre: '))

m = 5
soma = (b1+b2+b3+b4) / m

print ('O aluno {} obteve uma média {}'.format(nome, soma))