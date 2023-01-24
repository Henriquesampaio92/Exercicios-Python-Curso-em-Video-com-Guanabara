numeros = list()
maior = menor = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite o {n+1}º número: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('-' * 50)
print(f'Você digitou os valores: {numeros}')
print(f'O maior valor digitado foi {maior}, ele apareceu nas posições: ',end='')
for p, n in enumerate(numeros):
    if n == maior:
        print(f'{p+1}...',end='')
print('')
print(f'O menor valor digitado foi {menor}, e ele apareceu nas posições: ', end='')
for p, n in enumerate(numeros):
    if n == menor:
        print(f'{p+1}...', end='')
