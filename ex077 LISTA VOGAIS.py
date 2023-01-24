lista = ('palavra', 'laço', 'ingles', ' Noah', 'python',
         'rua', 'interatividade', 'positividade',
         'pensamento', ' lua', 'dia', 'noite', 'paz',
         'Deus', 'nome', 'acabar', 'exercicio')
for palavra in lista:
    print(f'\nPara a palavra \033[34m{palavra.upper()}\033[m temos: ', end=' ')
    for letras in palavra:
        if letras in 'aeiou':
            print(f'\033[31m{letras}\033[m', end=' ')