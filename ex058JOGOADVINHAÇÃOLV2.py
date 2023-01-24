from random import randint
computador = randint(0, 11)
tentativas = 0
print('=*' * 15)
print('     JOGO DA ADIVINHAÇÃO')
print('=*' * 15)
jogador = 12
while jogador != computador:
    jogador = int(input('Qual número eu estou pensando? '))
    if jogador != computador:
        tentativas += 1
        if jogador < computador:
            print('MAIS, TENTE NOVAMENTE!')
        else:
            print('MENOS, TENTE NOVAMENTE!')
    else:
        print('PARABENS VOCÊ ADIVINHOU!')
        tentativas += 1
print('O numero de tentativas foi {}'.format(tentativas))
