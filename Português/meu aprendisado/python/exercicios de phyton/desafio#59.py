from time import sleep
print(f'\033[1;33m{" Desafio#59 ":=^60}')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
p = 0
while p != 5:
    p = int(input('''\033[34m[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Qual é a sua opção? '''))
    if p == 1:
        s = num1 + num2
        print(f'\033[33mA soma entre {num1} + {num2} é {s}')
    elif p == 2:
        m = num1 * num2
        print(f'\033[33mO resultado de {num1} X {num2} é {m}')
    elif p == 3:
        if num1 > num2:
            ma = num1
        else:
            ma = num2
        print(f'\033[33mEntre {num1} e {num2} o maior valor é {ma}')
    elif p == 4:
        print('\033[33mInforme os numeros novamente')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif p == 5:
        print('\033[33mFinalisando o programa...')
    else:
        print('\033[35mOpção invalida. Tente novamente.')
    print('=' * 60)
    sleep(1)
print('Fim do programa. Volte sempre!')
