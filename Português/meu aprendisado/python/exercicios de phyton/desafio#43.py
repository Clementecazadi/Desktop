peso = float(input('Qual é seu peso (Kg)'))
altura = float(input('Qual é a sua altura (m)'))
IMC = peso / (altura ** 2)
print(f'O IMC dessa pessoa é {IMC:.1f}')
if IMC < 18.5:
    n = 'Abaixo do peso'
elif 18.5 <= IMC < 25:
    n = 'Peso ideal'
elif 25 <= IMC < 30:
    n = 'Sobrepeso'
elif 30 <= IMC <= 40:
    n = 'Obesidade'
else:
    n = 'Obesidade Morbida'
print(f'A classificação desta pessoa é: {n}')
