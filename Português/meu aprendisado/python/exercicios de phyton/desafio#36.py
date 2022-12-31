casa = float(input('Qual é o valor da casa: Kzs'))
salario = float(input('Salário do comprador: Kzs'))
minimo = salario * 30 / 100
tempo = str(input('O comprador vai pagar em anos o em meses ')).strip().lower()
if tempo == 'anos':
    anos = int(input('Quantos anos de financiamento '))
    prestacao = casa / (anos * 12)
    print(f'Para pagar um casa de {casa:.2f}Kzs em {anos} anos a prestação será de {prestacao:.2f}Kzs')
    if prestacao <= minimo:
        print('Emprestimo Aprovado')
    else:
        print('Emprestimo Negado')
else:
    meses = int(input('Quantos meses de financiamento? '))
    prestacao = casa / meses
    print(f'Para pagar um casa de {casa:.2f}Kzs em {meses} meses a prestação será de {prestacao:.2f}Kzs')
    if prestacao <= salario * 40 / 100:
        print('Emprestimo Aprovado')
    else:
        print('Emprestimo Negado')
