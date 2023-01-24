'''import random

list = ['1', '2', '3', '4', '5']
n = random.choice(list)
v = input('Eu escolhi um numero de 1 a 5 tente advinhar: ')
if n == v:
    print('Parabens você acertou, eu também escolhi {}.'.format(n))
else:
    print('Errou! Eu escolhi {}'.format(n))'''
from random import randint
from time import sleep
n = randint(0, 5)
print('--=' * 20)
print('ESTOU PENSANDO EM UM NUMERO ENTRE 0 E 5, TENTE ADVINHAR')
print('--=' * 20)
n2 = int(input('digite: '))
print('PROCESSANDO...')
sleep(2)
if n2 == n:
    print('PARABENS VOCÊ VENCEU!')
else:
    print('NÃO FOI DESSA VEZ, EU PENSEI NO NUMERO {}'.format(n))
