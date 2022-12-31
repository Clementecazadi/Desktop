nome = str(input('qual é o seu nome?... ')).lower().strip()
if 'cazadi' in nome:
    print('Que nome lindo você tem ')
elif 'joão' in nome or 'prisca' in nome or 'manuela' in nome:
    print('O seu nome é bem popular em angola')
print(f'Tenha um bom dia, {nome}')