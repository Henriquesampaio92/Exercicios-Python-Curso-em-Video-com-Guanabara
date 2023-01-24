numero = int(input('Escreva um número: '))
total = 0
for c in range(1, numero +1):
    if numero % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[33m',end=' ')
    print('{}'.format(c),end=' ')
print('\n\033[mO numero {}, é divisível {} vezes.'.format(numero, total))
if total == 2:
    print('Este É UM NUMERO PRIMO!')
else:
    print('Este NÃO É um número primo!')
    