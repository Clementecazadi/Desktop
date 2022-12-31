nome = str(input('Qual é o seu nome? ')).strip()
if nome[:8].lower() == 'clemente':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal')
print(f'Bom dia {nome.title()}')
