lista = list()
r = 'S'
contador = 0
while r not in 'N':
    n = int(input('Digite um valor: '))
    contador += 1
    lista.append(n)
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print(f'Ao todo foram digitados {contador} numeros.')                     # OU LEN.(LISTA)
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'O valor 5 está na lista na posição {lista.index(5)+1}')
else:
    print('O valor 5 NÃO está na lista.')