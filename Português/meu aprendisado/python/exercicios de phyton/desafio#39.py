from datetime import date
sexo = int(input('''Qual é o seu sexo
[ 1 ]   Masculino
[ 2 ]   Feminino
Digite a opção '''))
if sexo == 1:
    atual = date.today().year
    nac = int(input('Ano de nascimento: '))
    idade = atual - nac
    alis = 18 - idade
    if alis < 0:
        alis = alis * -1
    else:
        alis = alis
    print(f'Quem nasceu em {nac} tem {idade} anos em {atual}')

    if idade < 18:
        if alis == 1:
            print(f'Ainda falta {alis} ano para o seu alistamento')
        else:
            print(f'Ainda faltam {alis} anos para o seu alistamento')
        print(f'O seu alistamento será em {atual + alis}')
    elif idade == 18:
        print('Voce tem que se alistar \033[1;31mIMEDIATAMENTE\033[m')
    else:
        if alis == 1:
            print(f'Voce já deveria ter se alistado a {alis} ano atra')
        else:
            print(f'Voce já deveria ter se alistado a {alis} anos atras')
        print(f'O seu alistamento foi em {atual - alis}')
elif sexo == 2:
    print('O alistamento não é obrigatorio para as mulheres')
else:
    print('Opção invalida. Tente novamente')
