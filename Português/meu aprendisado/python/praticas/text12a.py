brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1.copy())
estado1['uf'] = 'Luanda'
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print('Fazendo fatiamento...')
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
print(brasil[1]['uf'])
