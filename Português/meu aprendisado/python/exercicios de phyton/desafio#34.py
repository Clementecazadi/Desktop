print('Desafio#34')
sal = float(input('Qual é o salario do funcionário R$'))
novo = sal + ((sal * 10)/100) if sal > 1250 else sal + ((sal * 15)/100)
print(f'Que ganhava R${sal:.2f} passa a ganhar \033[1mR${novo:.2f}\033[m agora')
