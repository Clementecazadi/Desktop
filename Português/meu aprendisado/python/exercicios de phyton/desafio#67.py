while True:
    n = int(input('\033[1;30mDigite um número para ver a sua tabuada: '))
    if n < 0:
        break
    print('=' * 49)
    for cont in range(1, 12):
        print(f'{n} x {cont:2} = {cont * n}')
    print('=' * 49)
print('=' * 49)
print('Fim do programa Tabuada. Volte sempre!')
