import math 

#calcular o seno, cosseno e tangente de qualquer ângulo 

angle = int (input ('Digite um ângulo: '))

sen = math.sin(math.radians(angle))
print ('O ângulo {} em SENO é {:.2f}'.format(angle, sen))

cos = math.cos(math.radians(angle))
print ('O ângulo {} em COSSENO é {:.2f}'.format(angle, cos))

tan = math.tan(math.radians(angle))
print ('O ângulo {} em TANGENTE é {:.2f}'.format(angle, tan))