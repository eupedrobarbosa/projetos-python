import math

#calculando seno, cosseno e tangente

angle = int (input ('Digite um ângulo: '))
    
sen = math.sin(math.radians(angle))
print ('SENO: {:.2f}'.format(sen))

cos = math.cos(math.radians(angle))
print ('COSSENO: {:.2f}'.format(cos))

tan = math.tan(math.radians(angle))
print ('TANGENTE: {:.2f}'.format(tan))