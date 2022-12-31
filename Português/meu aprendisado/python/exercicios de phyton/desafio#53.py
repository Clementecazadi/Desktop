frase = str(input('Digite uma frase: ')).upper().strip()
se = frase.split()
jus = ''.join(se)
'''d = ''
for c in range(len(jus) - 1, -1, -1):
    d = d + jus[c]'''
d = jus[::-1]
print(f'{jus} e {d}')
if d == jus:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')
