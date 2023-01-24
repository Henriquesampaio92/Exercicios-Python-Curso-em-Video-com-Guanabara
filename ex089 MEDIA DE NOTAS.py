lista1 = list()
lista2 = list()
while True:
    nome = str(input('Digite seu nome: '))
    nota1 = float(input('Digite a nota da prova 1: '))
    nota2 = float(input('Digite a nota da prova 2: '))
    media = (nota1 + nota2) / 2
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while resposta not in 'NnSs':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    lista2.append(nome)
    lista2.append([nota1, nota2])
    lista2.append(media)
    lista1.append(lista2[:])
    lista2.clear()
    if resposta == 'N':
        break

print('=-' * 30)
print(f'Nº '.center(10), f'NOME'.center(10), f'MÉDIA'.center(10))
print('--' * 20)
for p, n in enumerate(lista1):
    print(f'{p}'.center(10), f'{n[0]}'.center(10), f'{n[2]}'.center(10))

while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista1) -1:
       print(f'as notas de {lista1[opc][0]} são {lista1[opc][1]}')

