print('\033[1;31mxc' * 55)
print('Ola, eu sou o desafio#7, faça a gentilesa de digitar dois numeros que eu calculo a media entre eles.')
print('xc' * 55)
n1 = float(input('\033[mDigite um numero '))
n2 = float(input('Digite mais um numero '))
m = (n1 + n2) / 2
print('\033[33m-' * 50, f'\na media entre {n1} e {n2} vale {m:.2f}')
print('-' * 50)
print('\033[m')
