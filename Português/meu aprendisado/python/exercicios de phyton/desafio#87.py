matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
print('=' * 49)
total1pares = total1coluna2 = maior1coluna1 = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            total1pares += matriz[linha][coluna]
        if coluna == 2:
            total1coluna2 += matriz[linha][2]
        if linha == 1:
            if coluna == 0 or maior1coluna1 < matriz[1][coluna]:
                maior1coluna1 = matriz[1][coluna]
        print(f'[{matriz[linha][coluna]:^5}]', end=' ')
    print()
print('=' * 49)
print(f'A soma dos valores pares é {total1pares}')
print(f'A soma dos valores da terceira coluna é {total1coluna2}')
print(f'O maior valor da segunda linha é {maior1coluna1}')
print('=' * 49)
