expressao = str(input('Digite uma expressão: '))
pilha = []
for termos in expressao:
    if termos == '(':
        pilha.append('(')
    else:
        if termos == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está valida.')
else:
    print('Sua epressão está invalida')
