def contador(inicio, fim, passos):
    from time import sleep
    if inicio < fim and passos > 0:
        print('=' * 49)
        print(f'Contagem de {inicio} até {fim} de {passos} em {passos}')
        for c in range(inicio, fim + 1, passos):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    if inicio > fim and passos > 0:
        print('=' * 49)
        print(f'Contagem de {inicio} até {fim} de {passos} em {passos}')
        for c in range(inicio, fim - 1, -passos):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
    if passos < 0:
        passos = passos * -1
        contador(inicio, fim, passos)
    if passos == 0:
        passos = 1
        contador(inicio, fim, passos)


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 49)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Inicio: ')), int(input('Fim:    ')),
         int(input('Passos: ')))
print('=' * 49)
