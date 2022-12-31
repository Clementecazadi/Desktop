def sorteios(lista):
    from random import randint
    from time import sleep
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='')
        sleep(0.5)
    print('PONTO!')


def Soma_Par(lista):
    valor = 0
    for c in lista:
        if c % 2 == 0:
            valor += c
    print(f'A soma dos valores pares da lista {lista} é {valor}.')


numeros = list()
sorteios(numeros)
Soma_Par(numeros)
