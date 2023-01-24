extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        numero = int(input('Digite um numero entre 0 e 20: '))
        if numero < 0 or numero > 20:
            print('tente novamente', end=' ')
        else:
            break
    print(f'O número escolhido foi: {extenso[numero]}')
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont in 'Nn':
        break
