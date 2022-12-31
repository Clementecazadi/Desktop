from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento '))
idade = atual - nasc
print(f'O atleta tem {idade} anos')
if idade <= 9:
    n = 'MIRIM'
elif 9 < idade <= 14:
    n = 'INFANTIL'
elif 14 < idade <= 19:
    n = 'JUNIOR'
elif 19 < idade <= 25:
    n = 'SENIOR'
else:
    n = 'MASTER'
print(f'Classificação: {n}')
