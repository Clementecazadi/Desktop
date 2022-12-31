print(f'{" Desafio#60.1 ":=^60}')
num = int(input('Digite um numero para calcular o seu factorial: '))
f = 1
print(f'Calculando o {num}! = ', end='')
while num > 0:
    print(num, end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1
print(f)
