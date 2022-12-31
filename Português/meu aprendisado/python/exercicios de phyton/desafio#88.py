from random import randint
from time import sleep
megasena = []
dados = []
print('=' * 49)
print(f'{"JOGO DA MEGA SENA":^49}')
print('=' * 49)
jogos = int(input('Quantos jogos você quer que eu sortei? '))
print(f'{f" SORTEANDO {jogos} JOGOS ":=^49}')
for c in range(0, jogos):
    while len(dados) < 6:
        numero = randint(1, 60)
        if numero not in dados:
            dados.append(numero)
    dados.sort()
    megasena.append(dados[:])
    dados.clear()
for pos, c in enumerate(megasena):
    print(f'Jogo {pos + 1:^3}: {c}')
    sleep(1)
print(f'{"< BOA SORTE! >":=^49}')
