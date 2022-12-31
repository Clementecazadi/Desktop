expressao = str(input('Digite uma expressão: '))
conte = 0
for termos in expressao:
    if termos == '(' or termos == ')':
        conte += 1
if conte % 2 == 0:
    print('Sua expressão está valida.')
else:
    print('Sua epressão está invalida')
