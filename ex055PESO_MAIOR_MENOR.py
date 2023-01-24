pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa. Kg '.format(c)))
    if c == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
print('O mais gordinho pesa {} KG'.format(pesomaior))
print('O mais franguinho pesa {} KG.'.format(pesomenor))
