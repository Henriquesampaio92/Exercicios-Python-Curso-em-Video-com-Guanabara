import datetime

ano = datetime.date.today().year
nasc = int(input('Qual o ano de nascimento? '))
idade = ano - nasc
if idade <= 9:
    print('O atleta tem {} anos e se enquandra na categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e se enquadra na categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos e se enquadra na categoria JÚNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos e se enquadra na categoria SÊNIOR.'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos e se enquadra na categoria MASTER.'.format(idade))
