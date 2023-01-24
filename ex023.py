'''numumero = str(input('Escreva um numero de 0 à 9999.'))
x = numero.split()
print('O numero {}'.format(numero))
print('Unidade: ', x[0][3])
print('Dezena: ', x[0][2])
print('Centena: ', x[0][1])
print('Milhar: ', x[0][0])
FORMA STRING, FALTA ELEMENTOS PARA O PROGRAMA RODAR SEM ERRO!'''
num = int(input('Escreva um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o numero {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
