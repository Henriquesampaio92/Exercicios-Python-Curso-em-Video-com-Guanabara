from datetime import date
ano = date.today().year
contadormaior = 0
contadormenor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano - nascimento
    if idade >= 21:
        contadormaior += 1
    else:
        contadormenor += 1
print('Entre as idades informadas {} são maiores de idade'.format(contadormaior))
print('Também tivemos {} pessoas menores de idade.'.format(contadormenor))
