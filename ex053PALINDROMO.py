frase = str(input('Escreva uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
'''inverso = ''
for letra in range(len(junto) -1, -1, -1):             MÉTODO USANDO O |FOR|
    inverso += junto[letra]'''
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO É PALÍNDROMO!')
