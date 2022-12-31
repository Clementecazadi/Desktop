'''print('desafio#17,CANC')
co = float (input('qual é o comprimento do cateto oposto '))
ca = float (input('qual é o comprimentp do cateto adjacente '))
hi = (co**2+ca**2)**(1/2)
print(f'O compriment da hipotenusa vai medir {hi:.3f}')'''
co = float (input('qual é o comprimento di cateto oposto '))
ca = float (input('qual é o comprimento do cateto adjacente '))
from math import hypot
hi= hypot(co,ca)
print (f'O comprimento da hipotenusa vai medir {hi:.2f}')