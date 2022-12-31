def criptar(msg, key):
    alphabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'ã', 'â', 'à',
                 'ú', 'ù', 'ü', 'û', 'é', 'è', 'ë', 'ê', 'í', 'ì',
                 'ï', 'î', 'ý', 'æ', 'œ', 'å', '1', '2', '3', '4',
                 '5', '6', '7', '8', '9', '0', ' ', '[', ']', '{',
                 '}', '(', ')', '/', '-', '_']
    n = len(alphabeto)
    nova_letra = ''
    for letra in msg:
        indice = alphabeto.index(letra)
        if letra.isalpha():
            nova_letra += alphabeto[((indice + key) % n)]
        else:
            nova_letra += alphabeto[indice]
    return nova_letra


def descriptar(meg, key):
    nova_letra = criptar(meg, -key)
    return nova_letra


e = criptar('a mãe da francisca foi-se embora 34', 9)
print(e)
e = descriptar(e, 9)
print(e)