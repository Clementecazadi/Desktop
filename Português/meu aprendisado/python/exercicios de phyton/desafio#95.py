jogadores = list()
while True:
    jogador = {'nome': str(input('Nome do jogador: ')).strip().lower(),
               'gols': list(), 'total': 0}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(1, partidas + 1):
        jogador['gols'].append(int(input(f'  Quantos gols na partida {c}?: ')))
    continuar = str(input('Quer continuar [S/N]: ')).lower().strip()[0]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while continuar not in 'ns':
        print('Erro! Por favor, digite apenas S ou N.')
        continuar = str(input('Quer continuar [S/N]: ')).lower().strip()
    if continuar == 'n':
        break
print('=' * 49)
print('Cod Nome              Gols               Total')
print('=' * 49)
for pos, c in enumerate(jogadores):
    print(f'''{pos:>3} {c['nome'].capitalize():<17} {f"{c['gols']}":<20} {c['total']}''')
print('=' * 49)
while True:
    continuar = 0
    continuar = int(input('Mostrar dados de qual jogador? (100 para parar) '))
    if continuar == 100:
        break
    if continuar >= len(jogadores):
        print(f'ERRO! Não existe jogador com codigo {continuar}.')
    else:
        print(f'-- LEVANTANDO DO JOGADOR {jogadores[continuar]["nome"].upper()} --')
        for part, valore in enumerate(jogadores[continuar]['gols']):
            print(f'     No jogo {part + 1} fez {valore} gols.')
    print('=' * 49)
print('=' * 49)
