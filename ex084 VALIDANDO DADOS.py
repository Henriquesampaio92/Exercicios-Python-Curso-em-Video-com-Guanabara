pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
while True:
    resposta = ' '
    print('__' * 20)
    dados.append(str(input('Nome: ').strip()))
    dados.append(float(input('Peso: ').strip()))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if maiorpeso < dados[1]:
            maiorpeso = dados[1]
        if menorpeso > dados[1]:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while resposta not in 'SsNn':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta not in 'SsNn':
            print('\033[31mCOMANDO INVÁLIDO, DIGITE UM COMANDO VÁLIDO!\033[m')
    if resposta == 'N':
        break
print('-_' * 50)
print(f'Ao todo foram registradas {len(pessoas)} perfis.')
print(f'O menor peso foi {menorpeso}Kg')
for p in pessoas:
    if p[1] == menorpeso:
        print(p[0])
print(f'O maior peso foi {maiorpeso}Kg')
for p in pessoas:
    if p[1] == maiorpeso:
        print(p[0])
