lista = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor acrescentado com sucesso...')
    else:
        print('Valor repetido, não vou adcionar...')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
lista.sort()
print(lista)