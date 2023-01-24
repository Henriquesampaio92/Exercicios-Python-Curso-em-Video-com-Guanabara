n1 = float(input('Qual a nota da primeira prova: '))
n2 = float(input('Qual a nota da segunda provra: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[41mREPROVADO!!!\033[m')
elif media >= 5 and media <= 6.9:
#elif 7 > media >=5: OUTRA ALTERNATIVA
    print('\033[43mRECUPERAÇÃO!!!\033[m')
elif media <= 7:
    print('\033[42mAPROVADO!!!\033[m')
