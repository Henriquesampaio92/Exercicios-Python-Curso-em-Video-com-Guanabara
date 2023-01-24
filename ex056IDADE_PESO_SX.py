somaidade = 0
maioridadeh = 0
maisvelho = ''
totmulher = 0
for c in range(1, 5):
    print('=== DADOS DA {}ª PESSOA ==='.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO? F/M?: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadeh = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é: {}'.fomat(mediaidade))
print('O homem mais velho tem {} anos e seu nome é: {}'.format(maioridadeh, maisvelho))
print('O total de mulheres com menos de 20 anos é: {}'.format(totmulher))
r