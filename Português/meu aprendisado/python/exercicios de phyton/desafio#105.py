def notas(*notas, situacao=False):
    '''
    -> Essa uma função para calcular da media das notas,
    informaor o maior valor lido, o menor valor lido e
    a situação (opcional) [Ruim, Boa, Exelente] da media das notas.
    :param notas: introduzar numeros.
    :param situacao: (opcional) [Ruim, Boa, Exelente].
    :return: O retorno é um dicionario com o resumo.
    '''
    resumo = {'Total De Notas': 0, 'Maior': 0, 'Menor': 0, 'Media': 0}
    soma = 0
    for c in notas:
        if resumo['Total De Notas'] == 0:
            resumo['Maior'] = c
            resumo['Menor'] = c
        else:
            if resumo['Maior'] < c:
                resumo['Maior'] = c
            if resumo['Menor'] > c:
                resumo['Menor'] = c
        resumo['Total De Notas'] += 1
        soma += c
    resumo['Media'] = int(soma / resumo['Total De Notas'])
    if situacao:
        if resumo['Media'] < 5:
            resumo['Stuação'] = 'Ruim'
        elif 8 > resumo['Media'] >= 5:
            resumo['Stuação'] = 'Boa'
        elif resumo['Media'] >= 8:
            resumo['Stuação'] = 'Exelente'
    return resumo


alunos = notas(10, 6, 10, 5, situacao=True)
print(alunos)
print('\033[1;37;40m', end='')
help(notas)
