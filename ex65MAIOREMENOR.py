r = 'S'
soma = contador = maior = menor = 0
while r in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero
    contador += 1
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if menor > numero:
            numero = menor
        if numero > maior:
            maior = numero
media = soma / contador
print('A media entre os {} numeros é {}'.format(contador, media))
print('O menor foi {} e o maior {}.'.format(menor, maior))
