lista1 = []
lista2 = []
lista3 = []
while True:
    numero = int(input('Digite um numero para acrescentar a lista: '))
    lista1.append(numero)
    if numero % 2 == 0:
        lista2.append(numero)
    else:
        lista3.append(numero)
    resposta = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resposta in 'Nn':
        break
print(f'Lista: {lista1}\nLista par: {lista2}\nLista impar: {lista3}')
