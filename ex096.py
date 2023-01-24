def lin():
    print('-' * 50)
def area(larg, comp):
    m = larg * comp
    print(f'Um terreno com LARGURA {l} x COMPRIMENTO {c} = ÁREA {m}')

lin()
print(f'{"CALCULANDO ÁREA":^50}')
lin()
l = float(input('qual é a LARGURA (m) do terreno: '))
c = float(input('Qual o COMPRIMENTO (m) do terreno: '))
area(l, c)
