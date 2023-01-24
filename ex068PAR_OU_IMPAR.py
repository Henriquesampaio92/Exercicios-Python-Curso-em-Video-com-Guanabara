from random import randint
contador = 0
while True:
    parouimparjogador = ' '
    print('*=*=' * 10)
    print('           PAR OU IMPAR')
    print('*=*=' * 10)
    numerojogador = int(input('Qual número? '))
    while parouimparjogador not in 'PI':
        parouimparjogador = str(input('PAR OU IMPAR? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    resultadonumero = numerojogador + computador
    if resultadonumero % 2 == 0:
        resultadoparouimpar = 'PAR'
    else:
        resultadoparouimpar = 'IMPAR'
    if resultadoparouimpar[0] == parouimparjogador[0]:
        print('--' * 10)
        print('Você jogou {} e o computador jogou {} total {} é {}'.format(numerojogador, computador, resultadonumero, resultadoparouimpar))
        print('VOCÊ VENCEU, VAMOS JOGAR NOVAMENTE')
        print('--' * 10)
        contador += 1
    if resultadoparouimpar[0] != parouimparjogador[0]:
        print(f'Você jogou {numerojogador} e o computador jogou {computador} total {resultadonumero} é {resultadoparouimpar}')
        print(f'O numero de vitórias consecutivas foi {contador}')
        break
print('FIM')