maioridade = 0
homens = 0
mulher20 = 0
while True:
    sexo = pergunta = ' '
    print('-_-_' * 10)
    idade = int(input('Qual a idade? '))
    if idade > 18:
        maioridade += 1
    while sexo not in 'MF':
        sexo = str(input('Qual é o sexo? [M/F] ')).strip().upper()[0]
        if sexo in 'M':
            homens += 1
        if sexo in 'F' and idade < 20:
            mulher20 += 1
    print('-' * 20)
    while pergunta not in 'SN':
        pergunta = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
    if pergunta in 'Nn':
        break
print('Total de pessoas com mais de 18 anos: {}.'.format(maioridade))
print('Total homens: {}'.format(homens))
print(f'total mulheres com menos de 20 anos: {mulher20}')
