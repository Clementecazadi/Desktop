idadeh = contsex = maior = mner = cont = 0
while True:
    print('=' * 49)
    print(f'{"CADASTRE UMA PESSOA":^49}')
    print('=' * 49)
    cont += 1
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo [M/F]: ')).strip().lower()[0]
    if sexo == 'f' and idade < 20:
        mner += 1
    if idade > 18:
        maior += 1
    if sexo == 'm':
        contsex += 1
    if sexo == 'm' and cont == 1:
        idadeh = idade
    elif sexo == 'm' and idadeh < idade:
        idadeh = idade
    print('=' * 49)
    r = ' '
    while r not in 'sn':
        r = str(input('Quer continuar [S/N]: ')).lower().strip()[0]
    if r == 'n':
        break
print('=' * 49)
print(f'''Total de pessoas com mais de 18 anos: {maior}
Ao todo temos {contsex} homens cadastrado
O homen mais velho tem {idadeh} anos
E temos {mner} mulheres com menos de 20 anos.''')
print('=' * 49)
