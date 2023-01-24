n1 = int(input('Digite um numero '))
n2 = int(input('Digite outro numero '))
n3 = int(input('Digite outro numero '))
#DEFININDO MAIOR
if n1 > n2 and n1 >n3:
    maior =n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
#DEFININDO MENOR
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print('O maior numero escolhido foi {} e o menor é {}.'.format(maior,menor))
