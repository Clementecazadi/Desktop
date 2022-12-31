print('-' * 49)
print(f'{"LISTAGEM DE PREÇOS":^49}')
print('-' * 49)
fr = ('Lapis', 1.75, 'Borracha', 2,
      'Caderno', 15, 'Estojo', 25,
      'Transferidor', 4.20, 'Compasso', 9.99,
      'Mochila', 120.32, 'Canetas', 22.30,
      'Livro', 34.90)
for c in range(0, len(fr)):
    if c % 2 == 0:
        print(f'{fr[c]:.<39}', end='')
    else:
        print(f'R${fr[c]:>6.2f}')
print('-' * 49)
