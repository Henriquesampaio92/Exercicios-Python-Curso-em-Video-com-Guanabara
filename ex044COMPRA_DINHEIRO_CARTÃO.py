from time import sleep

price = float(input('How muhc the product costs? R$ '))
paymentmethod = int(input('''Choose the payment method:
[ 1 ] Cash/Check
[ 2 ] by Card
[ 3 ] Splited in 2x
[ 4 ] splited by 3x

'''))
if paymentmethod == 1:
    nprice = price - (10 / 100 * price)
    print('For this payment method you are going to receive 10% discount.')
    print('$ ', nprice)
elif paymentmethod == 2:
    nprice = price - (5 / 100 * price)
    print('For this payment method you are going to receive 5% discount.')
    print(nprice)
elif paymentmethod == 3:
    print('no discount available, you are paying $ ', end=' ')
    print(price)
elif paymentmethod == 4:
    nprice = price + (20 / 100 * price)
    print('CALCULATING FEES...')
    sleep(2)
    print('$ ', nprice)
else:
    print(' Try it again ')
