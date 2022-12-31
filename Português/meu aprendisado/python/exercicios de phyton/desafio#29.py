print('-=-' * 25)
print('Desafio#29')
print('-=-' * 25)
velocidade = float(input('Qual é a volociddade atual do carro? '))
print('-=-' * 25)
if velocidade > 80:
    print(f'''MULTADO! Você excedeu o limite de velocidade que é de 80km/h
Você deve pagar uma multa de R${(velocidade - 80) * 7}''')
    print('-=-' * 25)
print('Tenha um bom dia! Dirija com segurança')
print('-=-' * 25)
