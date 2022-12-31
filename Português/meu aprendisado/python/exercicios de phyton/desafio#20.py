print ('desafio#20, CANC')
n1 = str (input('primeiro aluno '))
n2 = str (input('secondo aluno '))
n3 = str (input('terceiro aluno '))
n4 = str (input('quarto aluno '))
lista = [n1, n2, n3, n4]
from random import shuffle
shuffle(lista)
print (f'A ordem de apresentação é\n{lista}')