from time import sleep
inicio = str(input('Pressione enter para iniciar a contagem regressiva: '))
for c in range(10, -1, -1,):
    sleep(1)
    print(c)
print('''
============================
      FELIZ 2022
============================''')