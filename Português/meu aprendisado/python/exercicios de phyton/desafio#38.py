print('\033[1;33m%' * 40)
print('Desafio#38')
print('%' * 40)
num1 = int(input('\033[mPrimeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O \033[1;31mPRIMEIRO\33[m valor é maior que o segundo')
elif num1 < num2:
    print('O \033[1;31mSEGUNDO\033[m valor é maior que o primeiro ')
else:
    print('Não existe valor \033[1;32mMAIOR\033[m')
