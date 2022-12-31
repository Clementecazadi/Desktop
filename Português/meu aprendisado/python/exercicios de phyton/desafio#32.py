from datetime import date
print('Desafio#33')
ano = int(input('Que ano quer analizar? coloque 0 para analizar atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é BISSEXTO')
else:
    print(f'O ano de {ano} não é BISSEXTO')
