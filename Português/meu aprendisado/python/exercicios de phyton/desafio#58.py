from random import randint
from time import sleep
print(f'\033[1;33m{" Desafio#58 ":=^60}')
print('PROCESSANDO...\033[m', end='')
sleep(1.5)
comp = randint(1, 10)
tn = 0
jogador = int(input('''\r\033[1;35mOlá sou o seu computador...
Acabei de pensar em um numero entre 1 e 10
Sera que você consegue advinhar qual foi?
Qual é o seu palpite?\033[m '''))
while jogador != comp:
    if jogador < comp:
        print('\033[1;34m  Mais... Tente mais uma vez.')
    else:
        print('\033[1;36m  Menos... Tente mais uma vez.')
    jogador = int(input('  Qual é o seu palpite? '))
    tn += 1
if tn > 0:
    print(f'\033[35mAcertou com {tn} tentativas. Parabéns\033[m')
else:
    print(f'\033[1;35mAcertou. Parabéns\033[m')
print('\033[1;33m=' * 60)
print('\033[m')
