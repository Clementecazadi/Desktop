numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    continuar = input('Quer continuar [S/N]: ').strip().lower()[0]
    if continuar == 'n':
        break
print('=' * 49)
print(f'Você digirou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado  na lista!')
