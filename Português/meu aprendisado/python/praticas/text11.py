text = list()
text.append('Gustavo')
text.append(40)
galera = list()
galera.append(text)
print(galera)
text[0] = 'Maria'
text[1] = 12
galera.append(text)  # Tem de aver [:] para criar uma copia galera.append(text[:])
print(galera)
