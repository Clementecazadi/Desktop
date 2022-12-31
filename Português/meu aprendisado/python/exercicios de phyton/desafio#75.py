numero = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
          int(input("Digite mais um número: ")), int(input('digite o ultimo número: ')))
print("Você digito os valores: ", end='')
for n in numero:
    print(f'{n} ', end='')
print(f'\rO valor 9 apareceu {numero.count(9)}')
if 3 in numero:
    print(f'O valore 3 apareceu na {numero.index(3) + 1}° posição')
else:
    print(f'O valore 3 não apareceu em nenhuma posição')
n2 = ''
for n in numero:
    if n % 2 == 0:
        n2 += f'{n} '
print(f'Os valores pares digitados foram {n2}')
