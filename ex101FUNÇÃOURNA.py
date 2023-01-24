def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <= 15:
        return f'{idade} ANOS NÃO VOTA!'
    if 16 <= idade < 18 or idade >= 65:
        return f'{idade} ANOS O VOTO É FACULTATIVO!'
    else:
        return f'{idade} ANOS VOTA!'


# PROGRAMA PRINCIPAL
nasc = int(input('Qual ano você nasceu? '))
print(voto(nasc))
