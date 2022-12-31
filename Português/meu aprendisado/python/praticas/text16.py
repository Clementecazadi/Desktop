chave = 3
mesagem = str(input('Digite um mensagem a ser incriptada: ')).lower()
cifrada = ''
alphabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z']
n = 128
for letra in mesagem:
    # indice = alphabeto.index(letra)
    indice = ord(letra)
    # nova_letra = alphabeto[(indice + chave) % n]
    nova_letra = chr((indice + chave) % n)
    cifrada += nova_letra
print(cifrada)
print(mesagem)
