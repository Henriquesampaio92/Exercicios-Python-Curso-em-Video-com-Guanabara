from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.today().year - nasc
dados['ctps'] = str(input('Nº carteira de trabalho (0 p/ não possui): '))
if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano'] + 35) - datetime.today().year)
print('=-' * 30)
for k, v in dados.items():
    print(f'    - {k} recebe: {v}.')
