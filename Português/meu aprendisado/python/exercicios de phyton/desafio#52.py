print(f'\033[1;33m{" Desafio#52 ":=^60}\033[m')
c = 0
num = int(input('\033[1;35mDigite um numero inteiro:\033[m '))
for d in range(1, num + 1):
    if num % d == 0:
        c += 1
        print(f'\33[1;33m{d}\033[m', end=' ')
    else:
        print(f'\033[1;31m{d}\033[m', end=' ')
if c == 0:
    print(f'\033[1;35mO numero {num} foi dividido zero vezes.\033[34m Por isso ele não é PARE nem PRIMO.\033[m')
elif num == 1:
    print(f'\n\033[1;35mO numero {num} foi dividido uma unica vez.\033[34m Por isso ele é NULO.\033[m')
elif c > 2:
    print(f'\n\033[1;35mO numero {num} foi dividido {c} vezes.\033[34m Por isso ele é PARE')
else:
    print(f'\n\033[1;35mO numero {num} foi dividido {c} vezes.\033[34m Por isso ele é PRIMO')
