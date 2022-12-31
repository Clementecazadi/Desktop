print(f'\033[1;31m{" Desafio#55 ":=^60}\033[m')
menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input(f'  \033[1;33mQual é o peso da {p}° pessoa: Kg\033[m'))
    print('\033[1;31m=' * 60)
    if p == 1:
        maior = peso
        menor = peso
    if menor > peso:
        menor = peso
    if peso > maior:
        maior = peso
print(f"""\033[0;1;33mO maior pesso lido foi de {maior}Kg
O menor peso lido foi de {menor}Kg\033[m""")
print('\033[1;31m=' * 60)
