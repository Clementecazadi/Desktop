print(f"{'Gerador De PA':^20}")
print('-=' * 10)
num = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
s = num
while cont < 10:
    print(f'{s} > ', end='')
    s += raz
    cont += 1
print('Acabou!')
