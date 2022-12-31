from random import shuffle, choice
from time import sleep
print('Ola eu sou o jogo de pedra, papel e tesorra')
print('Pedra    1\nPapel    2\nTesorra  3')
m1 = 'Pedra'
m2 = 'Papel'
m3 = 'Tesora'
m = [m1, m2, m3]
shuffle(m)
rc = choice(m)
ru = input('Escolha uma opção ')
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ!!!')
r = f'{rc} {ru}'
if r == 'Pedra 1':
    print('Pedra contra pedra é um empate')
elif r == 'Pedra 2':
    print('Vôce venceu o papel vence pedra')
elif r == 'Pedra 3':
    print('Ah que pena vôce perdeu a pedra vence a tesora')
elif r == 'Papel 1':
    print('Ah que pena vôce perdeu o papel vence a pedra')
elif r == 'Papel 2':
    print('Papel contra Papel é um empate')
elif r == 'Papel 3':
    print('Vôce venceu a tesora vence papel')
elif r == 'Tesora 1':
    print('Vôce venceu a pedra vence a tesora')
elif r == 'Tesora 2':
    print('Ah que pena vôce perdeu a tesora vence o papel')
elif r == 'Tesora 3':
    print('Tesora contra tesora é um empate')
else:
    print('Vôce não introduziu um numero que esta nas opções do jogo  por favor reinicialise o jogo')
