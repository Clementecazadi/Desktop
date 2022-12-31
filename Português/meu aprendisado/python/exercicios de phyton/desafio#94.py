pessoas = list()
media = cont = 0
while True:
    pessoa = {'nome': str(input('Nome: ')).lower().strip(),
              'sexo': str(input('Sexo [M/F]: ')).strip().lower()}
    while pessoa['sexo'] not in 'mf':
        print('Erro! por favor digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
    pessoa['idade'] = int(input('Idade: '))
    cont += pessoa['idade']
    pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar [S/N]: ')).lower().strip()[0]
    while continuar not in 'ns':
        print('Erro! por favor digite apenas S ou N.')
        continuar = str(input('Quer continuar [S/N]: ')).lower().strip()
    if continuar == 'n':
        break
print('=' * 49)
print(f'- Ao todo temos {len(pessoas)} cadastradas.')
media = int(cont / len(pessoas))
print(f'- A media de idade é de {media} anos.')
print(f'- As mulheres cadastradas são ', end='')
for c in pessoas:
    if c['sexo'] == 'f':
        print(c['nome'], end=' ')
print()
print('- Lista de pessoas que estão acima de media:')
for c in pessoas:
    if c['idade'] > media:
        print(f"  => Nome = {c['nome'].capitalize()}; Sexo = {c['sexo'].upper()} ; Idade = {c['idade']} anos.")
print('=' * 49)
