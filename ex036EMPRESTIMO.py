valor = float(input('Qual o valor da casa que pretende comprar? R$ '))
salario = float(input('Qual o seu salário? R$ '))
parcelas = int(input('Em quantos anos você pretende pagar esse empréstimo? '))
x = valor / (parcelas * 12)
if x <= 30 / 100 * salario:
    print('\033[7;42m!PARABÉNS!\033[m seu empréstimo foi APROVADO!')
else:
    print('sentimos muito o valor das parcelas excedeu 30% de sua renda mensal, seu empréstimo foi \033[7;41m!REPROVADO!\033[m ')
