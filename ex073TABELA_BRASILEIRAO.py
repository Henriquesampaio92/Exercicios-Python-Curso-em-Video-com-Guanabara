tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Corinthians', 'Fluminense',
          'Atlético-PR','Atlético-MG', 'América-MG', 'Fortaleza', 'Botafogo',
          'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará',
          'Cuiabá', 'Atlético Goianiense', 'Avaí', 'Juventude')
print('=-' *50)
print('TABELA BRASILEIRÃO'.center(90))
print('=-' *50)
print(f'Os cinco primeiros times colocados são: \033[32m{tabela[0:5]}\033[m')
print('=-' *50)
print((f'Os ultimos quatro colocados são: \033[31m{tabela[-4:]}\033[m. '))
print('=-' *50)
print(sorted(tabela))
print('=-' *50)
print(f'A posição do flamengo na tabela é {tabela.index("Flamengo")+1}º lugar.')