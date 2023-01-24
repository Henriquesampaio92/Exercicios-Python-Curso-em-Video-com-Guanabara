s = str(input('Qual seu sexo? [M/F]: ')).strip()[0]
while s not in 'MmFf':
    s = str(input('Qual seu sexo? [M/F]: ')).strip()[0]
print('sexo {} registrado com sucesso.'.format(s).upper())
