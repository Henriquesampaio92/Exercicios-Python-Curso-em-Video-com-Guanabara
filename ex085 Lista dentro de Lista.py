numeros = [[], []]
contador = 0
for c in range(1, 8):
    contador = int(input(f'Digite o {c}º valor: '))
    if contador % 2 == 0:
        numeros[0].append(contador)
    else:
        numeros[1].append(contador)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares digitados foram {numeros[0]}')
print(f'Os números impares digitados foram {numeros[1]}')
