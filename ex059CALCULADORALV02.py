from time import sleep
v1 = int(input('Digite um valor '))
v2 = int(input('Digite outro valor '))
opçao = 0
while opçao != 5:
    opçao = int(input(''' ESCOLHA UMA OPERAÇÃO:
    
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA
    '''))
    if opçao == 1:
        print('A soma dos dois valores é: ', v1 + v2)
    elif opçao == 2:
        print('A multiplicão dos dois números é: ', v1 * v2)
    elif opçao == 3:
        if v1 > v2:
            print('{} é maior!'.format(v1))
        else:
            print('{} é maior'.format(v2))
    elif opçao == 4:
        v1 = int(input('Digite um novo número: '))
        v2 = int(input('Digite outro valor: '))
    else:
        if opçao != 5:
            print('OPÇÃO INVÁLIDA, VOCÊ NÃO SABE LER?')
    print('=*=' * 10)
    sleep(2)
print('FIM, ESPERAMOS VOCE DE NOVO!')
