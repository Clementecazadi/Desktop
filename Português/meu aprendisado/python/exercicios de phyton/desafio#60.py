print(f'{" Desafio#60 ":=^60}')
n = int(input('''Digite um número para calcular seu factorial: '''))
s = n + 1
d = 1
st = ''
while s > 1:
    s = s - 1
    d = d * s
    st = st + f' {s} x'
print(f'Calculando {n}!= {st[1:-1]}= {d}')
