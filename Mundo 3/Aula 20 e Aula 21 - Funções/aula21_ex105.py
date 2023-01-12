def notas(*num, sit=False):
    '''
    -> Calcula média de notas e mostra a situação do aluno:
    :param num: adiciona as notas (aceita várias)
    :param sit: opcional, mostra a situação do aluno se sit=True
    :return: dicionario com as notas, média, situação
    '''
    dic = {}
    s = 0
    dic['Total de notas digitadas'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Média'] = sum(num) / len(num)
    if sit:
        if dic['Média'] < 5:
            dic['Situação'] = 'Ruim'
        elif 5 <= dic['Média'] < 7:
            dic['Situação'] = '+/-'
        elif dic['Média'] >= 7:
            dic['Situação'] = 'Boa'

    return dic


# Programa Principal
print(notas(9.5, 10, 7.5, sit=True))
print(notas(2, 5, 7, 1, 6))
print()
help(notas)
