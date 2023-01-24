n1 = int(input('Digite o lado 1 de um triangulo: '))
n2 = int(input('Digite o lado 2: '))
n3 = int(input('Digite o lado 3: '))
if n1 <= (n2 + n3) and n2 <= (n1 + n3) and n3 <= (n1 + n2):
    print('PODE SE FORMAR UM TRIANGULO!', end=' ')
    if n1 == n2 == n3:
        print('EQUILÁTERO')
    if n1 != n2 != n3 != n1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('NÃO PODE FORMAR UM TRIANGULO!')
