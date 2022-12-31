print(f'\033[1;36m{" Desafio#50 ":=^60}')
p = 0
soma = 0
nur = ('zero', 'um', 'dois', 'treis', 'quatro', 'sinco', 'seis')
for c in range(1, 7):
    num = int(input(f' \033[0;34mDigite o {c}° numero inteiro:\033[m '))
    if num % 2 == 0:
        p += 1
        soma += num
if p == 1:
    print(f'\033[1;36m{f" Você informou apenas um numero pare e ele foi {soma} ":=^60}')
elif p == 0:
    print(f'\033[1;36m{" Você não informou nenhum numero pare ":=^60}')
else:
    print(f'\033[1;36mVocê informou {nur[p]} numeros pares e a soma entre eles foi {soma}')
