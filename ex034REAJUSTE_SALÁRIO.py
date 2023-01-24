salario = float(input('Qual o seu salário? '))
if salario > 1250:
    a1 = salario + (salario * 10 / 100)
    print('seu aumento salárial é R$ {:.2f}, agora você receberá {}'.format(a1 - salario,a1))
else:
    a1 = salario + (salario * 15 / 100)
    print('Seu aumento salarial é R$ {:.2f}, agora você receberá R$ {}.'.format(a1 - salario,a1))
