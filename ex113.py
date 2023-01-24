def leiaint(msg):
    while True:
        try:
            r = int(input(msg))
        except ValueError or TypeError:
            print('\033[0;31mO VALOR DIGITADO É INVÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mO USUÁRIO DECIDIIU PARAR O PROGRAMA!\033[m')
            return 'None'
        else:
            return r


def leiafloat(msg):
    while True:
        try:
            f = float(input(msg))
        except ValueError or TypeError:
            print(f'\033[0;31mO VALOR DIGITADO É INVÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mO USUÁRIO OPTOU POR NÃO DIGITAR NENHUM VALOR!\033[m')
            return 'NONE'
        return f


# Programa principal
n1 = leiaint('Escreva um numero Inteiro: ')
n2 = leiafloat('Escreva um numero Real: ')
print(f'Os valores digitados foram {n1} e {n2}')
