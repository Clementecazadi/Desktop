n = int(input('Digite um numero inteiro '))
print('''Escolha uma das bases de converção
[ 1 ]  Converter para BINARIO
[ 2 ]  Converter para OCTAL
[ 3 ]  Converter para HEXADEECIMAL''')
op = int(input('Qual e a sua opção '))
if op == 1:
    print(f'{n} convertido para BINARIO é {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para OCTAL é {oct(n)[2:]}')
elif op == 3:
    print(f'{n} convertido para HEXADECIMAL é {hex(n)[2:]}')
else:
    print('Opção invalida, por favor tente novamente')
