times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 15)
print(f'Os 4 ultimo são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoence") + 1}° posição')
