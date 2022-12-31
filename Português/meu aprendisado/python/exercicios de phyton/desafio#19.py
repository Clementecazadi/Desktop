print('desafio#19, CANC')
n1 = str(input('digite o nome do primeiro aluno! '))
n2 = str(input('digite o nome do secondo aluno! '))
n3 = str(input('digite o nome do treceiro aluno! '))
n4 = str(input('digite o nome do quarto aluno! '))
lista = [n1, n2, n3, n4]
from random import choice
el = choice(lista)
print(f'O aluno eleito para apagar o quadro foi {el}')
