jogador = {'nome': str(input('Nome do jogador: ')).strip().lower(),
           'gols': list(), 'total': 0}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(1, partidas + 1):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}?: ')))
jogador['total'] = sum(jogador['gols'])
print('=' * 49)
print(jogador)
print('=' * 49)
for chaves, valores in jogador.items():
    print(f'- O campo {chaves} tem o valor {valores}.')
print('=' * 49)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, c in enumerate(jogador['gols']):
    print(f'   => Na partida {pos +1}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} de gols.')
