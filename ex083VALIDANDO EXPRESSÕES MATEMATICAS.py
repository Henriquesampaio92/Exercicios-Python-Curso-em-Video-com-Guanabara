expressão = str(input('Digite sua expressão: '))
pilha = []
for simb in expressão:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão é válida.')
else:
    print('Essa expressão é inválida')
