def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m VALOR INVÁLIDO \033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Escreva um numero: ')
print(f'O valor digitado foi {n}')