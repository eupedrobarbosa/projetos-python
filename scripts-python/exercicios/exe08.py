nome = str (input ('Aluno: '))

b1 = int (input ('1º bimestre: '))
b2 = int (input ('2º bimestre: '))
b3 = int (input ('3º bimestre: '))
b4 = int (input ('4ª bimestre: '))

soma = b1 + b2 + b3 + b4
media = 5

resultado = soma / 5

print ('O aluno {} teve uma média de {}'.format(nome, resultado))

