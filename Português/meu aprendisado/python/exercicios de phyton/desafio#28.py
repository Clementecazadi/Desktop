from random import randint
from time import sleep
print('-=-' * 25)
print('Desafio#28')
print('-=-' * 25)
print('Vou pensar num numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 25)
rc = randint(0, 5)
ru = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if rc == ru:
    print('PARABENS! Você conseguiu vencer me!')
else:
    print(f'GANHEI! Eu pensei no numero {rc} e não no {ru}')
