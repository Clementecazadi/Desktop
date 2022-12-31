numeros = list()
maior = 0
menor = 0
for posicao in range(0, 5):
    numeros.append(int(input(f'Digite um valor na posição {posicao}: ')))
    if posicao == 0:
        maior = numeros[0]
        menor = numeros[0]
    else:
        if numeros[posicao] > maior:
            maior = numeros[posicao]
        elif numeros[posicao] < menor:
            menor = numeros[posicao]
print('=' * 50)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao, c in enumerate(numeros):
    if c == maior:
        print(posicao, end='...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for posicao, c in enumerate(numeros):
    if c == menor:
        print(posicao, end='...')
