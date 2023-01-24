dados = {}
dados['nome'] = str(input('Nome do aluno: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] < 7:
    dados['situação'] = 'REPROVADO'
else:
    dados['situação'] = 'APROVADO'
print(f'O nome é: {dados["nome"]}')
print(f'A média é: {dados["media"]}')
print(f'A situação é: {dados["situação"]}')