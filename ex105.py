def notas(*n, sit=False):
    """
    -> Essa função tem como objetivo recolher notas de alunos, responder qual foi a média e a situação deste aluno.
    :param n: Recolhe todas as notas do aluno (não há limites para a quantidade de notas que deseja inserir
    :param sit: Aqui voce recebe informações sobre qual é a situação do aluno de acordo com sua média
    :return: dicionário com varias informações sobre a situaçáo da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RÁZOAVEL'
        else:
            r['situação'] = 'RUIM'
    return r


# programa principal
resposta = notas(1, 5, 5.5, 8, 3, sit=True)
print(resposta)
help(notas)