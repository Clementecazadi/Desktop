def soma(*valores):
    s = 0
    for c in valores:
        s += c
    print(f'A soma dos valores {valores} é {s}')


soma(2, 90, 56)