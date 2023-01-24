'''frase = str(input('Escreva uma frase: '))
print ( frase.count('A'))
print(frase.find('A'))
print(frase.count('A', ))
COMO NÃO RESOLVER O EXERCICIO ^^^ '''
frase = str(input('Escreva uma frase: ')).upper().strip()
print('A letra >A< aparece {} vezes na frase'.format(frase.count('A')))
print('A letra >A< apareceu pela primeira vez na posição {}'.format(frase.find('A')+ 1))
print('A ultima letra >A< apareceu na posição {}'.format(frase.rfind('A')+1))
