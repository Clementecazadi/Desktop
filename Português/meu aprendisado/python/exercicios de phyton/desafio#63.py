print(f'\033[1;33m{" Desafio#63 ":=^60}')
print('=' * 60)
print(f'{"Sequencia De Fibonacci":^60}')
print('=' * 60)
num = int(input('\033[34mQuantos termos voê quer mostrar: \033[33m'))
t1 = 0
t2 = 1
t3 = 0
cont = 2
print('~' * 60)
print(f'{t1} > {t2} >', end=' ')
while cont < num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(f'{t3} >', end=' ')
print('Acabou!')
print('~' * 60)
