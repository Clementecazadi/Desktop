print('=' * 49)
numeros = [[], []]
for c in range(0, 7):
    numero = int(input(f'Digite o {c + 1}° valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('=' * 49)
numeros[0].sort()
numeros[1].sort()
print(f'''Os valores pares digitados foram: {numeros[0]}
Os valores impares digitados foram: {numeros[1]}''')
print('=' * 49)
