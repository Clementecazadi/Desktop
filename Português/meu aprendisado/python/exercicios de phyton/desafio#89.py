lista = []
dados = []
print('=' * 49)
print(f'{"CANC GEST":^49}')
print('=' * 49)
while True:
	notas = []
	dados.append(str(input('Nome: ')).capitalize().strip())
	notas.append(float(input('Nota 1: ')))
	notas.append(float(input('Nota 2: ')))
	dados.append(notas[:])
	dados.append(float((notas[0] + notas[1]) / 2))
	lista.append(dados[:])
	dados.clear()
	continuar = str(input('Quer continuar? [S/N]: '))[0]
	if continuar in 'Nn':
		break
print('=' * 49)
print('No. NOME                              MÉDIA')
print('=' * 49)
for pos, c in enumerate(lista):
	print(f'{pos:^3} {c[0]:18} {c[2]:>20.1f}')
print('=' * 49)
numero = 0
while numero != 999:
	numero = int(input('Mostrar notas de qual aluno? (999 interompe): '))
	if numero < len(lista):
		print(f'Notas de {lista[numero][0].lower()} são {lista[numero][1]}')
	else:
		print('Erro. Aluno não encontrado...')
	print('=' * 49)
print(f'{"FIM DO PROGAMA.":^49}')
print(f'{"< VOLTE SEMPRE! >":=^49}')
