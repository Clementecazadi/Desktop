valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um numero inteiro: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v:2}!')
print('Cheguei ao final da lista.')
