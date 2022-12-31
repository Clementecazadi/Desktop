times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoence',
         'Atlético', 'Botafogo', 'Atlético-PR'.title(), 'Bahia',
         'São Paulo'.title(), 'Fluminense', 'Sport Recife'.title(), 'EC Vitória'.title(),
         'Coritiba', 'Avaí', 'Ponte Preta'.title(), 'Atlético-GO'.title())
print('\033[1m=' * 49)
print(f'{"Desafio#73.2":^49}')
print('\033[1m=' * 49)
print(f'{"Lista de times do brasileirão".upper():^49}')
print('-' * 49)
for po, c in enumerate(times):
    print(f'\033[1;33m{po + 1}) {c}\033[m')
print('\033[1m=' * 49)
print(f'{"Os 5 primeiros são".upper():^49}')
print('-' * 49)
for po, c in enumerate(times[:5]):
    print(f'\033[34;1m{po + 1}) {c}\033[m')
print('\033[1m=' * 49)
print(f'{"Os 4 ultimo são".upper():^49}')
print('-' * 49)
for po, c in enumerate(times[-4:]):
    print(f'\033[31;1m{po + 1}) {c}\033[m')
print('\033[1m=' * 49)
print(f'{"Times em ordem alfabética".upper():^49}')
print('-' * 49)
for po, c in enumerate(sorted(times)):
    print(f'\033[35;1m{po + 1}) {c}\033[m')
print('\033[1m=' * 49)
print(f'\033[36mO Chapecoense está na {times.index("Chapecoence") + 1}° posição\033[m')
print('\033[1m=' * 49)
print(f'{"PROCURE O TIME E A SUA POSIÇÃO":^49}')
print('-' * 49)
while True:
    nome = str(input("\033[1mDigite nome do time para mais infomações e n para sair: \033[m")).title().strip()
    if nome in times:
        print(f'\033[36;1mO {nome} está na posição {times.index(nome) + 1}\033[m')
    elif nome == "N":
        break
    else:
        print('\033[31;1mNome Invalido. Tente Novamente\033[m')
print('\033[1;33m=' * 49)
print('Fim Do Programa. Volte Sempre!')
print('=' * 49)
print('\033[m')

