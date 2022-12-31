print(f"{'Gerador De PA':^20}")
print('-=' * 10)
num = int(input('Primeiro termo: '))
raz = int(input('Razão da PA: '))
cont = 1
s = num
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total:
        print(f'{s} > ', end="")
        s += raz
        cont += 1
    print('Pausa')
    mais = int(input('Queres ver mais '))

