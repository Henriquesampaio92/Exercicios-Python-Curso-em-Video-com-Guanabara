import moeda

numero = int(input('Digite um numero: '))
print(f'Aqui alguns dados sobre o numero {numero}:\nDOBRO: {moeda.dobro(numero)}\nMETADE: {moeda.metade(numero)}'
      f'\nSOMA 10:  {moeda.aumentar(numero)}\nSUBTRAI 10: {moeda.diminuir(numero)}')