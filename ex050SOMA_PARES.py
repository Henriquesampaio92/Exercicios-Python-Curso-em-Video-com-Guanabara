soma = 0
contador = 0
for c in range (1, 7):
    numeros = int(input('Digite o {}º valor: '.format(c)))
    if numeros % 2 == 0:
        soma += numeros
        contador += 1
print('A soma dos {} valores PARES, é {}.'.format(contador, soma))
