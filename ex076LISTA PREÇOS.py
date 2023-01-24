itens = ('Caderno', 10,
         'Lapis', 2,
         'Caneta', 3,
         'Caderno', 15.90,
         'Mochila', 82,
         'Mesa', 200,
         'Cadeira', 50,
         'Sofá', 1500,
         'Moto', 8000,
         'Ferro de passar', 55,
         'Tv Smart', 2500,
         'Rack', 300)
print('*_*_*_' * 9)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('*_*_*_' * 9)
for prod in range(0, len(itens)):
    if prod % 2 == 0:
        print(f'{itens[prod]:.<30}', end='')
    else:
        print(f'R$ {itens[prod]:>10.2f}')