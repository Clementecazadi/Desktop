from datetime import date
actual = date.today().year
pessoa = {'nome': str(input('Nome: ')).strip().lower(),
          'idade': actual - int(input('Ano de nascimento: ')),
          'ctps': int(input('Carteira de trabalho: '))}
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: Kzs'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - (actual - pessoa['idade'])) + 35
print('=' * 49)
for chaves, valores in pessoa.items():
    print(f'- {chaves} tem o valor de {valores}.')
