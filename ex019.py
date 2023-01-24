import random
nome1 = input('escolha um nome: ')
nome2 = input('escolha outro nome: ')
nome3 = input('escolha outro nome: ')
nome4 = input('escolha outro nome: ')
list = [nome1, nome2, nome3, nome4]
escolha = random.choice(list)
print('O aluno escolhido foi {}.'.format(escolha))

