def dobra(lista):
    for v, c in enumerate(lista):
        lista[v] = c * 2
    print(f'A sua lista com os numueros dobrados {lista}')


numero = [1, 5, 6, 7, 89]
dobra(numero)
print(numero)