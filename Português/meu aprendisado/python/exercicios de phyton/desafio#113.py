def leiaInt(mgs):
    while True:
        try:
            numeroInt = int(input(mgs))
        except (TypeError, ValueError):
            print('\033[1;31mErro: por fovor, digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mErro: por fovor, digite um número inteiro valido.\033[m')
        else:
            break
    return numeroInt


def leiaFloat(mgs):
    while True:
        try:
            numeroReal = float(input(mgs))
        except:
            print('\033[1;31mErro: por fovor, digite um número Real valido.\033[m')
            continue
        else:
            return numeroReal


num1 = leiaInt('Digite um numero Inteiro: ')
num2 = leiaFloat('Digite um numro Real: ')
print(f'O valor Inteiro digitado foi {num1} e o Real foi {num2:.1f}')
