print('-' * 35)
print('       LOJA SUPER BARATÃO')
print('-' * 35)
soma = 0
maisdemil = 0
maisbarato = 0
produtobarato = ''
contador = 0
while True:
    continuar = ' '
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    soma += preco
    contador += 1
    if contador == 1:
        maisbarato = preco
    else:
        if preco < maisbarato:
            maisbarato = preco
            produtobarato = produto
    if preco > 1000:
        maisdemil += 1
    while continuar not in 'SN':
        continuar = str(input('QUER CONTINUAR? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('O total da compra foi: R$ {:.2f}'.format(soma))
print(f'temos {maisdemil} produto(s) que custa(m) mais de R$ 1.000,00 reais.')
print('O produto mais barato foi {}, que custou {}'.format(produtobarato, maisbarato))
