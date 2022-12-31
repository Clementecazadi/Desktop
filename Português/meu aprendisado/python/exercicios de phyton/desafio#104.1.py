def LeiaInt(mensagem):
    ok = False
    while True:
        valor = str(input(mensagem))
        if valor.isnumeric():
            valor = int(valor)
            ok = True
        else:
            print('\033[31;1mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


numero = LeiaInt('Digite um número: ')
print(f'Vovê acabou de digitar o número {numero}.')
