print(f'{" Desafio#64 ":=^60}')
n = 0
t = 0
s = 0
while n != -100:
    n = int(input('Digite um número [-100 para parar]:'))
    if n != -100:
        t += 1
        s += n
if t > 1:
    print(f'Você digitou {t} números e a soma entre eles é {s}.')
elif t == 0:
    print(f'Você não digitou nada.')
else:
    print(f'Você digitou {t} número e ele é {s}.')
