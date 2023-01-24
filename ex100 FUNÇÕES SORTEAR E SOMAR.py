from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando os numerous: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valors pares é {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)
