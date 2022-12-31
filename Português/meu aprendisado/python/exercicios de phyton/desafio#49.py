from time import sleep
print(f'\033[1;31m=================\033[4m TABUADA DE MULTIPLICAÇÃO \033[m\033[1;31m=================\033[m')
num = int(input('\033[1;33mDigite um numero para veres a sua tabuada:\033[m '))
for t in range(1, 13):
    print(f'\033[1;31m{num:2} X {t:2} = {t * num}\033[m')
    sleep(0.5)
print(f'\033[1;33mFim da tabuada de {num}\033[m')

