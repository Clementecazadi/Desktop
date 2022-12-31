try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Nao é possivel fozer um divição por zero')
except KeyboardInterrupt:
    print('O usuário preferio não informar os dados')
except Exception as rfs:
    print(f'Infelizmente tivemos um problema :(, devido á o erro {rfs.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito Obrigado.')
