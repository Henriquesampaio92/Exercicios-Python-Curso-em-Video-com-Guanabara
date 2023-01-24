peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print('Seu IMC é = {:.2f}. Você está \033[37mABAIXO\033[m do peso.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('IMC = {:.2f} \033[32mPESO IDEAL!\033[m'.format(imc))
elif imc > 25 and imc <= 30:
    print('IMC = {:.2f}. Você está com \033[37mSOBREPESO\033[m'.format(imc))
elif imc > 30 and imc < 40:
    print('IMC = {:.2f}. \033[33mOBESIDADE!\033[m'.format(imc))
elif imc > 40:
    print('IMC = {:.2f}. \033[31mOBESIDADE MÓRBIDA!\033[m'.format(imc))
