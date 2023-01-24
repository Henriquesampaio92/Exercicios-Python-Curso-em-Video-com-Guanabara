km = int(input('Qual a distancia em Km da sua viagem? '))
'''if km <= 200:
    n1 = km * 0.50
    print('Para viajens à menos de 200 Km o custo é de R$ 0.50/km o total é : R$ {}'.format(n1))
else:
    n2 = km + 0.45
    print('Para viajens maiores do que 200 km o custo é de R$ 0.45/km o total é de: R$ {}.'.format(n2))'''
preço = km * 0.50 if km < 200 else km * 0.45
print('O valor da sua viajem foi R$ {}.'.format(preço))
