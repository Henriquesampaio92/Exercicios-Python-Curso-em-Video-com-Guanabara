from random import randint
from time import sleep
contcomp = 0
contjogad = 0
while True:
    r = ' '
    lista = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = randint(0, 2)
    print('-==-' * 5)
    print('\033[7mESCOLHA SUA JOGADA\033[m')
    print('=-=-' * 5)
    print('''
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ''')
    jogador = int(input('>>> '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')

    print('=' * 28)
    print('Computador jogou: {}'.format(lista[computador]))
    print('Jogador jogou {}'.format(lista[jogador]))
    print('=' * 28)
    if computador == 0: #COMPUTADOR JOGOU PEDRA
       if jogador == 0:
           print(('\033[33mEMPATE!\033[m'))
           contcomp += 1
           contjogad += 1
       elif jogador == 1:
           contjogad += 1
           print('\033[32mVENCEU!\033[m')
       elif jogador == 2:
           contcomp += 1
           print('\033[31mPERDEU!!!\033[m')
       else:
            print('COMANDO INVÁLIDO!')

    if computador == 1: #COMPUTADOR JOGOU PAPEL
        if jogador == 0:
            contcomp += 1
            print('\033[31mPERDEU!!!\033[m')
        elif jogador == 1:
            contcomp += 1
            contjogad += 1
            print(('\033[33mEMPATE!\033[m'))
        elif jogador == 2:
            contjogad += 1
            print('\033[32mVENCEU!\033[m')
        else:
            print('COMANDO INVÁLIDO!')

    if computador == 2: #COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            contjogad += 1
            print('\033[32mVENCEU!\033[m')
        elif jogador == 1:
            contcomp += 1
            print('\033[31mPERDEU!!!\033[m')
        elif jogador == 2:
            contcomp += 1
            contjogad += 1
            print(('\033[33mEMPATE!\033[m'))
        else:
            print('COMANDO INVÁLIDO!')
    print(f'''
     ________________________
    |VOCÊ: {contjogad} COMPUTADOR: {contcomp}   |
     ________________________''')
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if r in 'N':
        break
