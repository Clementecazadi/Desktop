from datetime import date
pes = ('zero', 'uma', 'duas', 'treis', 'quatro', 'sinco', 'seis', 'sete')
print(f'\033[1;34m{" Desafio#54 ":=^80}\033[m')
maior = 0
menor = 0
atual = date.today().year
for i in range(1, 8):
    nasc = int(input(f'\033[1;36m  Qual é a ano de nascimento da {i}° pessoa: '))
    print('\033[1;34m=' * 80)
    idade = atual - nasc
    if idade > 18:
        maior += 1
    else:
        menor += 1
if maior == 1 and menor > 1:
    print(f'Ao todo tivemos {pes[maior]} pessoa maior de idade e {pes[menor]} pessoas menor de idade')
elif maior > 1 and menor == 1:
    print(f'Ao todo tivemos {pes[maior]} pessoas maior de idade e {pes[menor]} pessoa menor de idade')
elif maior > 1 and menor > 1:
    print(f'Ao todo tivemos {pes[maior]} pessoas maior de idade e {pes[menor]} pessoas menor de idade')
elif maior == 0 and menor > 1:
    print(f'Ao todo tivemos nenhuma pessoa maior de idade e {pes[menor]} pessoas menor de idade')
else:
    print(f'Ao todo tivemos {pes[maior]} pessoas maior de idade e nenhuma pessoas menor de idade')
print('\033[1;34m=' * 80)
