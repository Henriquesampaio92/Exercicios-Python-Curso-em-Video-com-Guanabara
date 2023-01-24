from random import randint
from time import sleep
print('=-' * 30)
print(f'JOGA NA MEGA SENA'.center(55))
print('=-' * 30)
lista = list()
jogada = list()
cont2 = 0
resposta = int(input('Quantos jogos você quer sortear? '))
while cont2 < resposta:
    cont1 = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogada:
            jogada.append(numero)
            cont1 += 1
        if cont1 >= 6:
            break
    jogada.sort()
    lista.append(jogada[:])
    jogada.clear()
    cont2 += 1
print('~*' * 3, f'  SORTEANDO {resposta} JOGOS  ', '~*' * 3)
print('AGUARDE.', end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
for i, l in enumerate(lista):
    print(f'JOGO {i+1} :', end='')
    sleep(0.5)
    print(f' {l}')
    sleep(0.5)