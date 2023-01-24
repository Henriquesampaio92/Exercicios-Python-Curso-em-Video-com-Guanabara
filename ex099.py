# FUNÇÕES
def lin():
    print('-' * 50)
def maior(* num):
    maiornum = 0
    lin()
    print('Analisando os Valores passados... ')
    for c in num:
        if maiornum == 0:
            maiornum = c
        else:
            if c > maiornum:
                maiornum = c
        print(f'{c}', end=' ')
    print(f'Foram informados {len(num)} ao todo.')
    print(f'Entre eles o maior é {maiornum}')


# PROGRAMA PRINCIPAL
maior(1, 2, 5, 3)
maior(6)
maior()