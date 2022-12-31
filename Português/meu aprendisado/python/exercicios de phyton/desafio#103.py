def ficha(nome_do_jogador = '<desconhecido>', golos_do_jogador = 0):
    print(f'O jogador {nome_do_jogador} fez {golos_do_jogador} '
          f'gol(s) no campionato.')


print('=' * 49)
nome = str(input('Nome do jogador: ')).strip('')
gols = str(input('quantos golos fez no campionato: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(golos_do_jogador=gols)
else:
    ficha(nome, gols)
