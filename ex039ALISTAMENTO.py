from datetime import date
a = date.today().year
n = int(input('Qual teu ano de nascimento? '))
i = a - n
print('quem nasceu em {} tem {} anos em {}.'.format(n, i,a))
if i == 18:
    print('VOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE SOLDADO!')
elif i < 18:
    saldo = 18 - i
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = a + saldo
    print('Seu alistamento será em {}'.format(ano))
elif i > 18:
    saldo = i - 18
    print('Você já deveria ter se alsitado há {} anos.'.format(saldo))
    ano = a - saldo
    print('Seu alistamento foi em {}'.format(ano))
