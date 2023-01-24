print('=-' * 20)
print('SEQUENCIA DE FIBONACCI')
print('=-' * 20)
termo = int(input('Quantos termos da sequencia serão exibidos? '))
t1 = 0
t2 = 1
print('{} →'.format(t1), end=' ')
if termo > 1:
    c = 3
    print('{} →'.format(t2), end=' ')
    while c <= termo:
        t3 = t1 + t2
        print('{} →'.format(t3), end=' ')
        c += 1
        t1 = t2
        t2 = t3
print('FIM!')
