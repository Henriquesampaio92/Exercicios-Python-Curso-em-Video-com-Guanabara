lista = list()
dados = dict()
somaidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA!')
    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    lista.append(dados.copy())
    while True:
        resposta = str(input('Queres continuar? [S/N]')).upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO! DIGITE UMA OPÇÃO VÁLIDA!')
    if resposta == 'N':
        break
print(f'{" DADOS CADASTRAIS ":*^50}')
print(' ')
totalcadastros = len(lista)
print(f'(A) Quantas pessoas temos cadastradas?\nR: {totalcadastros}')
print(' ')
print('=' * 50)
mediaidade= somaidade / totalcadastros
print(f'(B) Qual a média da idade das {totalcadastros} pessoas cadastradas?\nR: {mediaidade:5.2f}')
print(' ')
print('=' * 50)
print(f'(C) Quais foram as mulheres cadastradas?')
for c in lista:
    if c['sexo'] == 'F':
        print(f'- {c["nome"]}')
print(' ')
print('=' * 50)
print(f'(D) Lista com as pessoas que estão acima da média de idade:')
for c in lista:
    if c['idade'] >= mediaidade:
        for k, v in c.items():
            print(f'{k} = {v}')
    print(' ')


