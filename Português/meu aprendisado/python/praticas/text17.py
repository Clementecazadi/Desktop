# Recebendo dados
num = str(input('Digite varios numeros separando-os com ",": ').strip())
numeros = num.split(',')
numeros = [int(numero) for numero in numeros]
print(numeros)
print('A soma entre este numeros é:', sum(numeros))
