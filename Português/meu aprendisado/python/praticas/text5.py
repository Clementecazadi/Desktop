tempo = int(input('O seu carro tem quantos anos '))
if tempo <= 3:
    print('O seu carro ainda é novo')
else:
    print('O seu carro é velho não pensa em comprar outro?')
# condição simplificada
print('O seu carro ainda é novo' if tempo <= 3 else 'O seu carro é velho não pensa em comprar outro?')
print('-'*3, 'FIM', '-'*3)
