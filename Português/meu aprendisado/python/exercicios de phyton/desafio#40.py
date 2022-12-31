num = float(input('Primeira nota '))
num1 = float(input('Segunda nota '))
media = (num + num1) / 2
print(f'Tirando {num} e {num1}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('O aluno está REPROVADO')
elif 7 > media >= 5.0:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
