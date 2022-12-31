print('Desafio#26')
nome = str(input('Digite o seu nome completo ')).strip()
print(f'''O seu nome tem {nome.lower().count('a')} letras A
A letra A foi vista pela primeira vez na posição {nome.lower().find('a') + 1}
A letra A foi vista pela ultima vez na posição {nome.lower().rfind('a') + 1}''')
