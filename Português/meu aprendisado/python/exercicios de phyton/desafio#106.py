from time import sleep


def escreva(msg):
    msg.strip()
    s = len(msg) + 4
    print('=' * s)
    print(f'  {msg}  ')
    print('=' * s)


while True:
    print('\033[42;1m', end='')
    escreva('SISTEMA DE AJUDA PyHELP.')
    sleep(0.5)
    pergunta = str(input('\033[mFunção ou Biblioteca > '))
    if pergunta == 'fim':
        print('\033[41;1m', end='')
        escreva('ATÉ LOGO.')
        break
    print('\033[1;44m', end='')
    escreva(f"Acessando o manual de '{pergunta}'")
    print('\033[1;40m', end='')
    help(pergunta)
    sleep(2)
