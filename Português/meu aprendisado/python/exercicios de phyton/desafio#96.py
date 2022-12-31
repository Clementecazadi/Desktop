def area(largura, comprimento):
    s = largura * comprimento
    print(f'A área de um terreno {largura:.1f}×{comprimento:.1f} é de {s:.1f}m².')


print('=' * 49)
print(f'{"Controle de terrenos":^49}')
print('=' * 49)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
