from random import randint
tabela = (randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10), )
print('Os valores sorteados foram: ', end= ' ')
for c in tabela:
    print(f'{c}', end= ' ')
print(f'\nO maior valor foi: {max(tabela)}')
print(f'O menor valor foi: {min(tabela)}')
