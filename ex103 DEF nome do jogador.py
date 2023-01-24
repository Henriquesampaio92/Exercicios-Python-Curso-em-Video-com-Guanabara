def ficha(nome='desconhecido', gol=0):
    print(f'O jogador {nome} marcou {gol} gols.')


# programa principal
n = str(input('Qual o nome do jogador? '))
g = str(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gol=g)
else:
    ficha(n, g)