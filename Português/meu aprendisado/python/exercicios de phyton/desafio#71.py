print('=' * 49)
print(f'{" BANCO CANC ":^49}')
print('=' * 49)
valor = int(input('Que valor você quer sacar: R$'))
print('\033[33;1m=' * 49)
co50 = co20 = co10 = co1 = 0
while True:
    while valor >= 50:
        valor -= 50
        co50 += 1
    while valor >= 20:
        valor -= 20
        co20 += 1
    while valor >= 10:
        valor -= 10
        co10 += 1
    while valor >= 1:
        valor -= 1
        co1 += 1
    if valor == 0:
        break
if co50 > 0:
    print(f'Total {co50} de cédulas de R$50' if co50 > 1 else f'Total {co50} de cédula de R$50')
if co20 > 0:
    print(f'Total {co20} de cédulas de R$20' if co20 > 1 else f'Total {co20} de cédula de R$20')
if co10 > 0:
    print(f'Total {co10} de cédulas de R$10' if co10 > 1 else f'Total {co10} de cédula de R$10')
if co1 > 0:
    print(f'Total {co1} de cédulas de R$1' if co1 > 1 else f'Total {co1} de cédula de R$1')
print('=' * 49)
print("\033[mVolte sempre ao BANCO CANC! Tenha um bom dia!")
print('=' * 49)
