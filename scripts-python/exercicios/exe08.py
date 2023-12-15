nome = str (input ('Aluno: '))

b1 = int (input ('1º bimestre: '))
b2 = int (input ('2º bimestre: '))
b3 = int (input ('3º bimestre: '))
b4 = int (input ('4º bimestre: '))

media = 5
soma = (b1+b2+b3+b4)/media

print ('{} teve uma média de {}'.format(nome, soma))