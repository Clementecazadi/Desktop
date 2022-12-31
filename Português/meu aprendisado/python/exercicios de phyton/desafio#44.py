print('\033[33;1m=' * 20, end='')
print(' CANC STORE ', end='')
print('=' * 20)
preco = float(input('\033[mPreço das compras: Kzs'))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ]  Á vista dinheiro/cheque
[ 2 ]  Á vista no cartão
[ 3 ]  Em até 2x no cartão
[ 4 ]  3x ou mais no cartão
Qual é a opção '''))
if pagamento == 1:
    print(f'A sua compra de Kzs{preco:.2f} vai custar Kzs{preco - (preco * 10 / 100):.2f} no final. Obrigado por utilizar os nosso servicos')
elif pagamento == 2:
    print(f'A sua compra de Kzs{preco:.2f} vai custar Kzs{preco - (preco * 5 / 100):.2f} no final. Obrigado por utilizar os nosso servicos')
elif pagamento == 3:
    print(f'A sua compra será parcelada em 2x de Kzs{preco / 2:.2f} SEM JUROS')
    print(f'A sua compra de kzs{preco:.2f} vais custar Kzs{preco:.2f} no final. Obrigado por utilizar os nosso servicos')
elif pagamento == 4:
    parcela = int(input('Quantas parcelas '))
    print(f'A sua compra será parcelada em {parcela}x de Kzs{preco / parcela:.2f} COM JUROS')
    print(f'A sua compra de kzs{preco:.2f} vais custar Kzs{preco + (preco * 20 / 100):.2f} no final. Obrigado por utilizar os nosso servicos')
else:
    print('Opção invalida. TENTE NOVAMENTE')
    print(f'A sua compra de kzs{preco:.2f} vais custar Kzs{preco:.2f} no final. Obrigado por utilizar os nosso servicos')
