matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
maiors = 0
somaterceira = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o numero para a posição LINHA {l} COLUNA {c}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^10}]', end='')
    print('')
print('=-' * 20)
print(f'A soma dos valores pares é: {pares}')
for l in range(0, 3):
    somaterceira += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somaterceira}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maiors:
        maiors = matriz[1][c]
print(f'O maior numero da segunda linha é: {maiors}')