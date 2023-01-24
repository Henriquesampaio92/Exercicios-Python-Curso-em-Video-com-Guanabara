'''nome = str(input('Escreva seu nome completo: '))
dividido = nome.split()
print(nome.upper())
print(nome.lower())
print(len(dividido))
print(len(dividido[0]))'''

nome = str(input('Escreva seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras.'.format(nome.find(' '))) FORMA ALTERNATIVA
separa = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(separa[0], len(separa[0])))
