def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um numero
    :param n: O número a ser calculado.
    :param show: (Opcional) mostrar ou não a conta.
    :return: O valor do fatorial de N
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


print(fatorial(5))