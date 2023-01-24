d = int(input('Quantos dias o carro foi utilizado? '))
km = int(input('Quantos quilometros esse carro andou? Km '))
vd = d * 60
vkm = km * 0.15
v = vd + vkm
print('o custo foi de R$ {} por {} dias + {} por {} Km. O total é R$ {}.'.format(vd, d, vkm, km, v))
