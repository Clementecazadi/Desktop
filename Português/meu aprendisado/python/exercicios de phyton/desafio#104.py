def LeiaInt(numero):
    numero = str(numero)
    while not numero.isnumeric():
        print('\033[1;31mErro! Digite um numero inteiro válido.\033[m')
        numero = input('Digite um numero: ')
    numero = int(numero)
    return numero


# Programa Principal
numero = LeiaInt(input('Digite um numero: '))
print(f'Vovê acabou de digitar o número {numero}')
