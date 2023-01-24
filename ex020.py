import random
n1 = input('Escolha um nome: ')
n2 = input('agora escolha outro: ')
n3 = input('mais um nome: ')
n4 = input('ultima vez, escolha um nome: ')
list = [n1, n2, n3, n4]
random.shuffle(list)
print('A ordem de apresentação será: ')
print(list)

