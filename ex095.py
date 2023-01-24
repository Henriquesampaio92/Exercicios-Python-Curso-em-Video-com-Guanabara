time = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())
    jogador.clear()
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
    if resposta == 'N':
        break
print('=' * 30)
print(f'{"COD":<3} {"nome":10} {"Gols":10} {"Total":10}')
print('-' * 30)
for i, v in enumerate(time):
    print(f'{i+1:<3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<10}', end=' ')
    print(' ')
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 to stop): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'VALOR INCORRETO TENTE NOVAMENTE UM VALOR ENTRE 1 E {len(time)}')
    else:
        print(f'LEVANTANDO DADOS DO JOGADOR {time[busca-1]["nome"]}:')
        for i, v in enumerate(time[busca]['gols']):
            print(f'     => Na partida {i+1} marcou {v} gols.')
