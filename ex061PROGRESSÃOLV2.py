print('=*' * 15)
print('      PROGRESSÁO LEVEL 2')
print('=*' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
mult = 1
while mult <= 10:
    print('{} > '.format(termo), end= ' ')
    termo += razao
    mult += 1
print('FIM')
