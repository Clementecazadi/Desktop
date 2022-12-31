print('Desafio#22')
nome = str(input('Digite o seu nome completo ')).strip()
n = nome.split()
print(f'''Analizando o seu nome...
O seu nome em maiuscula é {nome.upper()}
O seu nome em minuscula é {nome.lower()}
O seu nome tem ao todo {len(''.join(n))} letras
O seu nome tem ao todo {len(nome) - nome.count(' ')} letras
O seu primeiro é {n[0].capitalize()} e ele tem {len(''.join(n[0]))} letras''')
