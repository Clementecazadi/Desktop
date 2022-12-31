from time import sleep
print(f'\033[1;35m{" Desafio#56 ":=^60}')
print('''\033[1;34mO desafio#56.1 foi criado pela CANC design™ PROCESSANDO...''', end='')
sleep(3)
idadeg = 0
nomev = ''
idadev = 0
ctm = 0
nomevm = ''
idadevm = 0
for p in range(1, 5):
	print(f'\r\033[1;34m{f" {p}° pessoa ":=^60}')
	nome = str(input(f'  \033[0;1;36mDigite o nome da {p}° pessoa: ')).strip().lower()
	idade = int(input('  Digite a idade: '))
	idadeg += idade
	sexo = str(input('  Digite o sexo [M/F]:\033[m '))
	if sexo in 'M m' and p == 1:
		nomev = f'{nome}'
		idadev = idade
	elif sexo in 'M m' and idadev < idade:
		nomev = f'{nome}'
		idadev = idade
	if sexo in 'F f' and idade < 20:
		ctm += 1
	if sexo in 'F f' and p == 1:
		nomevm = f'{nome}'
		idadevm = idade
	elif sexo in 'F f' and idadevm < idade:
		nomevm = f'{nome}'
		idadevm = idade
idadem = int(idadeg / 4)
print(f'\033[1;34m=' * 60)
print(f'\033[36mA idade media do grupo é {idadem} anos')
if idadev > 0:
	print(f'O homem mais velho tem {idadev} anos e ele se chama {nomev}')
if idadevm > 0:
	print(f'A mulher mais velha tem {idadevm} anos e ele se chama {nomevm}')
if ctm > 0:
	print(f'Ao todo são {ctm} mulhers com menos de 20 anos')
print(f'\033[1;34m=' * 60)
