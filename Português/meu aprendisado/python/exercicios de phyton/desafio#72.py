print('=' * 49)
print(f'{"Desafio#72":^49}')
print('=' * 49)
n = ('zero', 'um', 'dois', 'três', 'quatro', 'sinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'cinze', 'dezaceis', 'dezasete', 'dezoito', 'dezanove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20:'))
    print(f'Você digito o número {n[num]}')
    print('=' * 49)
    r = str(input('Quer continuar: ')).strip().lower()[0]
    while r not in 'sn':
        r = str(input('Quer continuar: ')).strip().lower()[0]
    if r == 'n':
        break
print('\033[33;1m=' * 49)
print(f"{'Fim Do Programa. Volte Sempre!':^49}")
print('=' * 49)
