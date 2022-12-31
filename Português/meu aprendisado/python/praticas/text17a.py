frase = 'abacaxi'
chave = 3
n = 128
lista = [chr((ord(letra) + chave) % n) for letra in frase]
decifrada = ''.join(lista)
print('A mensagem abacaxi cifrada é:', decifrada)
