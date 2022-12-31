from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 10)
ranking = []
print('valores sorteados: ')
for key, valores in jogadores.items():
    sleep(1)
    print(f'O {key} tiro {valores} nos dados.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('=' * 49)
print(f'{"RANKING":^49}')
print('=' * 49)
for pos, c in enumerate(ranking):
    sleep(1)
    print(f'O {c[0]} está em {pos + 1}° posição com {c[1]}.')
print('=' * 49)
