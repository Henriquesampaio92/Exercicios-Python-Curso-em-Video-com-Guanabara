#forma que eu resolvi a rotina
'''import math
c1 = int(input('qual o valor do cateto 1? '))
c2 = int(input('Qual o valor do cateto 2? '))
hipo = math.pow(c1, 2) + math.pow(c2, 2)
print(math.sqrt(hipo))'''

#forma de resolver a rotina sem importar da biblioteca...
'''co = float(input('qual é o comprimento do cateto oposto: '))
ca = float(input('qual o comprimento do cateto adjacente: '))
hipo = (co ** 2 + ca ** 2) ** (1/2)
print(' Hipotenusa vai medir {:.2f}'.format(hipo))'''

#Resolução com a biblíoteca math
from math import hypot
co = float(input('qual o cateto oposto? '))
ca = float(input('Qual o cateto adjacente? '))
hipo = hypot(co, ca)
print('O resultado da hipotenusa é: {:.2f}'.format(hipo))







