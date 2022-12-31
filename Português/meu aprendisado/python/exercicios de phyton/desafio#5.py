print('\033[1;35m&%' * 55)
print('Olá, eu sou o desafio#5, porfavor digite um numero,Canc®')
print('&%' * 55)
n = int(input('\033[mFaça a gentilesa de digitar um numero'))
a = n - 1
s = n + 1
print('O antecessor de {} é \033[1;33m{}\033[m e o sucessor de {} é \033[1;31m{}\033[m'.format(n, a, n, s))

