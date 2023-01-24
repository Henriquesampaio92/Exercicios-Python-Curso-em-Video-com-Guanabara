t = int(input('Qual o primeiro termo da progressão: '))
r = int(input('Qual a razão da progressão: '))
d = t + (11 - 1) * r
for c in range(t, d, r):
    print(c, end=' -> ')
print('ACABOU!')