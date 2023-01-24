from time import sleep

def contador(i, f, p):
    print('-' * 50)
    print(f'Iniciando congagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            sleep(0.1)
            print(f'{cont}', end=' ')
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            sleep(0.1)
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')

# Programa Principal
contador(1, 10, 1)
contador(10, 1, 2)
print('-' * 50)
print('AGORA É SUA VEZ, DIGITE UM INÍCIO, FIM E PASSO!')
ini = int(input('INICIO:  '))
fim = int(input('FIM:    '))
passo = int(input('PASSO: '))
if passo < 0:
    passo = passo * -1
if passo == 0:
    passo = 1
contador(ini, fim, passo)