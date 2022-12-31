print('-=-' * 25)
print('Desafio#31')
print('-=-' * 25)
d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print(f'Você está prestes a começar uma vigem de {d:.1f}Km')
print(f'E o preço da sua passagem será de R${p:.0f}')
# istrutura simplicada
preco = d * 0.50 if d <= 200 else d * 0.45
print('-=-' * 25)
print(f'E o preço de sua passagem será de R${preco:.0f}')
print('-=-' * 25)
