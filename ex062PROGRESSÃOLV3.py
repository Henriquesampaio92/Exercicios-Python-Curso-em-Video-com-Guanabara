print('=*' * 15)
print('      PROGRESSÁO LEVEL 2')
print('=*' * 15)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
mult = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while mult <= total:
        print('{} > '.format(termo), end=' ')
        termo += razao
        mult += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais: '))
print('progressão finalizada com {} termos mostrados!!!'.format(total))

