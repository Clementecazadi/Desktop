num = [2, 5, 9, 1]
print('Original')
print(num)
print('Trocar um numero por um outro')
num[2] = 3
print(num)
print('Adicionar um numero no final')
num.append(7)
print(num)
print('Organisa a lista em ordem descendente')
num.sort()
print(num)
print('Organisa a lista em ordem ascendente')
num.reverse()
print(num)
print('Adicionar um elemento em qualquer posição')
num.insert(2, 0)
print(num)
print('Remover um elemento')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
