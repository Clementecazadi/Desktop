n = 1
c = 0
d = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if n % 2 == 0 and n != 0:
        c += 1
    if n != 0:
        d += 1
print(f'''Ao todu foram {d} numeros digitados, {c} entre eles foram pares
FIM''')

