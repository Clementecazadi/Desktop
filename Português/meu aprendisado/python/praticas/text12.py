pessoa = {'nome': 'Clemente', 'sexo': 'M', 'idade': 16}
print(pessoa)
print('fazendo fatiamento...')
print(pessoa['nome'])
print(pessoa['sexo'])
print(pessoa['idade'])
print(f'O {pessoa["nome"].lower()} tem {pessoa["idade"]} anos')
print('Mostrando as chaves...')
print(pessoa.keys())
print('Mostrando os valores...')
print(pessoa.values())
print('Mostrando os itens...')
print(pessoa.items())
print('Usando o laço for no dicionario...')
for chave, valore in pessoa.items():
    print(f'{chave} = {valore}')
print('Removendo um elemento...')
del pessoa['sexo']
print(pessoa)
print('Adicionando um elementos...')
pessoa['peso'] = 78.5
print(pessoa)
print('Modificando elementos...')
pessoa['nome'] = "Valter"
print(pessoa)
