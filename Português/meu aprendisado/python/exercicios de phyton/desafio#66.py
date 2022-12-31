print(f'\033[1;33m{" Desafio#66 ":=^49}')
cont = soma = 0
while True:
    n = int(input('\033[34mDigite um número ( -1 para parar ): '))
    if n == -1:
        break
    cont += 1
    soma += n
if cont > 1:
    print(f'\033[33mA soma dos {cont} valores foi {soma}')
else:
    print(f'\033[33mVoce digito um unico valor que é {n}')
print('=' * 49)
