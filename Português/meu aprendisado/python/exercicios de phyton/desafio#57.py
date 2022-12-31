sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'M F':
    sexo = str(input('Dados invalidos. Por favor, informe o seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} restirado com sucesso.')
