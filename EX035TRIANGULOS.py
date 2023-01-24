n1 = int(input('Digite o lado 1 de um triangulo: '))
n2 = int(input('Digite o lado 2: '))
n3 = int(input('Digite o lado 3: '))
if n1 > (n2+n3) or n2 > (n1+n3) or n3 > (n1+n2):
    print('NÃO PODE FORMAR UM TRIANGULO!')
else:
    print('PODE SE FORMAR UM TRIANGULO!')
