numero = int(input('Escolha um número: '))
print('''Escolha uma das bases de conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('O número {} convertido para binário é: {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('O número {} convertido para octal é {}.'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(numero, hex(numero)[2:]))
else:
    print(('ERROR'))