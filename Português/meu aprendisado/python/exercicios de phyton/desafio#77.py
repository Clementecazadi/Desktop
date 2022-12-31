tupla = ('Aprender', 'Porgamar', 'Linguagem',
         'Python', 'Curso', 'Gratis',
         'Estudar', 'Praticar', 'Trabalhar',
         'Mercado', 'Programador', 'Futuro',)
for c in tupla:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for letra in c:
        if letra.lower() in 'aeuioy':
            print(letra.lower(), end=' ')
