pessoas = list()
total1pessoas = 0
while True:
    total1pessoas += 1
    print(f'{f" {total1pessoas}ª Pessoa ":=^49}')
    dados = list()
    dados.append(str(input('Nome: ')).capitalize().strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    continuar = str(input('Quer continuar [S \ N]: ')).strip().lower()[0]
    if continuar == 'n':
        break
print('=' * 49)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
maior = menor = 0
for pos, c in enumerate(pessoas):
    if pos == 0:
        menor = maior = c[1]
    else:
        if maior < c[1]:
            maior = c[1]
        if menor > c[1]:
            menor = c[1]
print(f'O maior peso lido foi de {maior:.2f}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == maior:
        print(c[0], end=' ')
print(f'\nO menor peso lido foi de {menor:.2f}Kg. Peso de ', end='')
for c in pessoas:
    if c[1] == menor:
        print(c[0], end=' ')
print(f"\n{'=' * 49}")
