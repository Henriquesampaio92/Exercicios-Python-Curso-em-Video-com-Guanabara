#from math import factorial
#from time import sleep
#numero = int(input('numero: '))
#print('CALCULANDO...')
#sleep(2)
#print(factorial(numero))

'''numero = int(input('Digite um numero para saber seu fatorial: '))
contador = numero
fatorial = 1
print('calculando {}! = '.format(numero), end='')
while contador > 0:
    print('{}'.format(contador), end=' ')
    print('x' if contador > 1 else '=', end=' ')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))'''

n = int(input('numero: '))
counter = n
factorial = 1
print('{}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    factorial *= c
print('{}'.format(factorial))
