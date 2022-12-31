print('Desafio#27')
n = str(input('Digite o seu nome completo ')).title().strip()
nome = n.split()
nome1 = n.rfind(' ') + 1
print(f'''O seu primeiro nome é {nome[0]}
O seu ultimo nome é {n[nome1:]}
Ola {nome[0]} {n[nome1:]}''')
