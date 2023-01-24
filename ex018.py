import math
an = float(input('Digite o angulo: '))
seno = math.sin(math.radians(an))
print ('o angulo {} tem o seno {:.2f}.'.format(an, seno))
cosseno = math.cos(math.radians(an))
print ('O angulo de {}º tem o COSSENO {:.2f} .'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print ('O angulo {}º tem tangente {:.2f}.'.format(an, tangente))
