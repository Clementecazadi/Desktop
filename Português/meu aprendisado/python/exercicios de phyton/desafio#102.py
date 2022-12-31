def factorial(numero, shoW=False):
    """
    -> Calcula o factoria de um número.
    :param numero: O numero a ser factoriado.
    :param shoW: (Opcional) Mostrar ou não a conta.
    :return: O volor do fatoria do numero introduzido.
    """
    fact = 1
    for c in range(numero, 0, -1):
        if shoW == True:
            print(f'{c} × ' if c > 1 else f'{c} = ', end='')
        fact *= c
    return fact


# Programa Principal
print('=' * 49)
print(factorial(4))
print(factorial(5, True) - 2)
help(factorial)