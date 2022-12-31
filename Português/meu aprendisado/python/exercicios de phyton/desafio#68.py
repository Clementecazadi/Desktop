from random import randint
print(f'\033[1;33m{" Desafio#68 ":=^49}')
cont = -1
while True:
    comp = randint(1, 10)
    usa = int(input('\033[33mDigite um valor: '))
    pi = ' '
    while pi not in 'pi':
        pi = str(input('Pare ou Impare [P/I]: ')).lower().strip()[0]
    s = comp + usa
    cont += 1
    print('=' * 49)
    print(f'\033[34mVocê jogou {usa} e computador {comp}. O total e {s} ', end='')
    if pi == 'p':
        if s % 2 == 0:
            print('PARE.')
            print('Venceu. PARABENS!')
        else:
            print('IMPARA')
            print('PERDEU.')
            break
    elif pi == 'i':
        if s % 2 == 0:
            print('PARE.')
            print('PERDEU.')
            break
        else:
            print('IMPARA')
            print('Venceu. PARABENS!')
print('\033[33m=' * 49)
print(f'Game Over! Você venceu {cont} vezes' if cont > 1 else f'Game Over! Você venceu {cont} veze')
print('\033[33m=' * 49)
print('\033[m')
