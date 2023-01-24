velocidade = int(input('Qual é a velocidade? '))
if velocidade > 80:
    multa = float((velocidade - 80) * 7)
    print('Você foi multado!, o custo da multa é R$ 7.00 por cada Km acima do limite = R$ {}'.format(multa))
else:
    print('Parabens por andar no limite de velocidade!')