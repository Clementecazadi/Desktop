numeros = list()
paresnum = list()
imparesnum = list()
while True:
    numeros.append(int(input('Digite um numero: ')))
    continuar = input('Quer continuar [S/N]: ').lower().strip()[0]
    while continuar not in 'sn':
        continuar = input('Quer continuar [S/N]: ').lower().strip()[0]
    if continuar == 'n':
        break
print('=' * 49)
print('A lista completa é  ', numeros)
for numero in numeros:
    if numero % 2 == 0:
        paresnum.append(numero)
    else:
        imparesnum.append(numero)
print('=' * 49)
if len(paresnum) > 0:
    print(f'A lista de pares é   {paresnum}')
else:
    print('Não há números pares na lista.')
if len(imparesnum) > 0:
    print(f'A lista de impares é {imparesnum}')
else:
    print('Não há números impares na lista.')
