num = cont = soma = maior = menor = 0
resp = 's'
while resp == 's':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    resp = str(input('Quere continuar [S/N]: ')).lower()
media = soma / cont
print(f'Você digitou {cont} números e a media entres eles foi {media} ')
print(f'O maior valor lido foi {maior} e o menor valor lido foi {menor}')
