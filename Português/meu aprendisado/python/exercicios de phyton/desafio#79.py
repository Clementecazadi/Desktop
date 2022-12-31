numeros = list()
while True:
    numero = int(input('Digite um numero: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = input('Quer continuar [S/N]: ').lower().strip()[0]
    while continuar not in 'sn':
        continuar = input('Quer continuar [S/N]: ')
    if continuar == 'n':
        break
print('=' * 36)
numeros.sort()
print(f'Você digitou os valores {numeros}')
