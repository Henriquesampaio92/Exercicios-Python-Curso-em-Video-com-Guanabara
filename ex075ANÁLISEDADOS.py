num = (int(input('numero: ')),
        int(input('numero: ')),
        int(input('numero: ')),
        int(input('numero: ')))
print(f'O valor 9 apareceu: {num.count(9)} vezes')
if 3 in num:
        print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
        print('O numero 3 não foi digitado.')
print('Os números pares digitados foram: ', end=' ')
for c in num:
        if c % 2 == 0:
                print(f'{c} ', end=' ')







numero = (int(input('\nDigite um numero')),
          int(input('digite um numero')),
          int(input('digite um numero')),
          int(input('digite um numero')))
print(f'O numero 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
        print(f'O numero 3 apareceu na posição {numero.index(3)+1}ª posição.')
else:
        print('o valor 3 não foi digitado.')
print('Os valores impares digitados foram:', end= ' ')
for n in numero:
        if n % 2 == 0:
                print(f'{n}', end=' ')
