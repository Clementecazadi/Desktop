brasil = list()
estado = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidada federativa: ')).strip()
    estado['sigla'] = str(input('Informe a sua sigla: ')).strip()
    brasil.append(estado.copy())
for c in brasil:
    for chave, valor in c.items():
        if chave == 'uf':
            print(f'O {valor} tem como sigla', end=' ')
        if chave == 'sigla':
            print(valor)
