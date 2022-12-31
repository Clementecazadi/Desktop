print(f'{" Desafio#60.2 ":=^60}')
n = int(input('Digite um numero para calcular o seu factorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    f *= c
    print(' x ' if c > 1 else ' = ', end='')
print(f)
