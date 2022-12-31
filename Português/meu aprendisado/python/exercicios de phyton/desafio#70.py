print('=' * 49)
print(f'{" LOJA CANC Design ":^49}')
print('=' * 49)
total = cont = p10 = pbar = 0
bar = ''
while True:
    nome = str(input('Nome do produto: ')).strip().lower()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < pbar:
        pbar = preco
        bar = nome
    if preco > 1000:
        p10 += 1
    r = ' '
    while r not in 'sn':
        r = str(input('Quer continuar [S/N]: ')).strip().lower()[0]
    if r == 'n':
        break
    print('=' * 49)
print(f'\033[1;34m{" Fim Do Programa ".upper():=^49}')
print(f'''O total da compra Foi R${total:.2f}
Temos {p10} produtos custando mais de R$1000
O produto mais barato foi: {bar} que custa R${pbar}\033[m''')
