from emoji import emojize
from random import randint
from time import sleep
print(emojize(f'\033[33m{" JOGO DE PPT ✊✋✌ ":=^40}\033[m'))
itens = ('Pedra', 'Papel', 'Tesora')
usuario = int(input('''Suas Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesora
Qual é a sua jogada? '''))
computador = randint(0, 2)
if computador == 0:
    if usuario == 0:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✊
O jogador jogo {itens[usuario]} ✊'''))
        print('=' * 42)
        print('\033[1;35mÉ um empate\033[m\033[35m 😒\033[m')
    elif usuario == 1:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(f'''O computador jogo {itens[computador]} ✊
O jogador jogo {itens[usuario]} ✋''')
        print('=' * 42)
        print(emojize('\033[1;34mVocê venceu\033[m\033[34m 😊\033[m'))
    elif usuario == 2:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✊
O jogador jogo {itens[usuario]} ✌'''))
        print('=' * 42)
        print(emojize('\033[1;31mVocê perdeu\033[m\033[31m 🙁\033[m '))
    else:
        print(emojize('\033[1;31m✖ Jogada invalida. Tente novamente\033[m'))
elif computador == 1:
    if usuario == 0:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✋
O jogador jogo {itens[usuario]} ✊'''))
        print('=' * 42)
        print(emojize('\033[1;31mVocê perdeu\033[m\033[31m 🙁\033[m '))
    elif usuario == 1:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(f'''O computador jogo {itens[computador]} ✋
O jogador jogo {itens[usuario]} ✋''')
        print('=' * 42)
        print('\033[1;35mÉ um empate\033[m\033[35m 😒\033[m')
    elif usuario == 2:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✋
O jogador jogo {itens[usuario]} ✌'''))
        print('=' * 42)
        print(emojize('\033[1;34mVocê venceu\033[m\033[34m 😊\033[m'))
    else:
        print(emojize('\033[1;31m✖ Jogada invalida. Tente novamente\033[m'))
elif computador == 2:
    if usuario == 0:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✌
O jogador jogo {itens[usuario]} ✊'''))
        print('=' * 42)
        print(emojize('\033[1;34mVocê venceu\033[m\033[34m 😊\033[m'))
    elif usuario == 1:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(f'''O computador jogo {itens[computador]} ✌
O jogador jogo {itens[usuario]} ✋''')
        print('=' * 42)
        print(emojize('\033[1;31mVocê perdeu\033[m\033[31m 🙁\033[m '))
    elif usuario == 2:
        print('\033[1;35mJO ', end='')
        sleep(1)
        print('KEN ', end='')
        sleep(1)
        print('PO!!!')
        print('\033[m\033[33m=' * 42)
        print(emojize(f'''O computador jogo {itens[computador]} ✌
O jogador jogo {itens[usuario]} ✌'''))
        print('=' * 42)
        print('\033[1;35mÉ um empate\033[m\033[35m 😒\033[m')
    else:
        print(emojize('\033[1;31m✖ Jogada invalida. Tente novamente\033[m'))
