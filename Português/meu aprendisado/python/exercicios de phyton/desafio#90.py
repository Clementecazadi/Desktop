dict = {'nome': str(input('Digite o seu nome: ')).strip().lower(), 'media': float(input(f'Digite a sua media: '))}
if dict['media'] < 5:
	dict['sit'] = 'reprovado(a)'
if 7 > dict['media'] >= 5:
	dict['sit'] = 'em recuperação'
if dict['media'] >= 7:
	dict['sit'] = 'aprovado(a)'
print('=' * 49)
print(f'''O nome é {dict['nome']}
A media dele(a) foi {dict['media']}
E ele(a) esta {dict['sit']}''')	
print('=' * 49)
