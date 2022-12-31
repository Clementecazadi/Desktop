print('desafio#18, CANC')

from math import cos, tan, sin, radians

angulo = float(input('digite um ângulo '))
n = radians(angulo)
s = sin(n)
c = cos(n)
t = tan(n)
print(
    f'O ângulo de {angulo} tem o SENO de {s:.2f}\nO ângulo de de {angulo} tem o COSSENO de {c:.2f}\nO ângulo de {angulo} tem a TAGENTE de {t:.2f}')
