valor = 0
soma = 0
contador = 0
while valor != 999:
    valor = int(input('Digite um valor a ser somado [999 para PARAR]: '))
    soma = (soma + valor)
    contador = contador + 1
contador = contador - 1
soma = soma - 999
print('A SOMA DOS {} VALORES DIGITADOS FOI {}'.format(contador,soma))