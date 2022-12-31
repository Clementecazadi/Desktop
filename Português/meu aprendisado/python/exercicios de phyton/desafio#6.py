print('\033[1;32m#$' * 55)
print('Desafio#6. Olá, eu sou o leitor de digitos, por favor digite algo, Canc•')
print('#$' * 55)
n = int(input('\033[mDigite algo '))
d = n + n
r = n ** (1 / 2)
print('\033[1;31mO dobro de {} é {}\033[m'.format(n, d))
print('\033[1;34mO triplo de {} é {}\033[m'.format(n, d + n))
print('\033[1;33mA raiz2 de {} é {:.3f}\033[m'.format(n, r))
