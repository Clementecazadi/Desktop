from time import sleep
print('\033[33m-=-' * 25)
print('Desafio#35')
print('-=-' * 25)
print('\033[31mAnalizador de triângulo')
print('-=-' * 25)
s1 = float(input('\033[mPrimeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Treceiro segmento: '))
print('\033[1;33;41mPROCESSANDO...\033[m')
sleep(2)
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:
    print('Os segmento acima NÃO PODEM FORMAR um triângulo')
