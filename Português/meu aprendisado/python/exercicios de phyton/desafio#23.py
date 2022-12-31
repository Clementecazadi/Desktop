print('Desafio#23')
nu = int(input('Digite de numero '))
u = nu // 1 % 10
d = nu // 10 % 10
c = nu // 100 % 10
m = nu // 1000 % 10
print(f'''Unidade:  {u}
Dezena:   {d}
Centena:  {c}
Milhar:   {m}''')
