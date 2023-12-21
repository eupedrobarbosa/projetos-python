import math

#calculando ângulo em seno, cosseno e tangente

angle = int (input ('Digite um ângulo: '))

sen = math.sin(math.radians(angle))
print ('Seno: {:.2f}'.format(sen))

cos = math.cos(math.radians(angle))
print ('Cosseno: {:.2f}'.format(cos))

tan = math.tan(math.radians(angle))
print ('Tangente: {:.2f}'.format(tan))