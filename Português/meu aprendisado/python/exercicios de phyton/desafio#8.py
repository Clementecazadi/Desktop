print('\033[1;34msc' * 60)
print('Ola, eu sou sou o desafio#8, faça a gentilesa de colocar um valor em metros que eu o converto em dm, em cm e em mm...')
print('sc' * 60)
n = float(input('\033[mDigite um valor em metro '))
km = n*0.001
hm = n*0.01
dam = n*0.1
dm = n*10
cm = n*100
mm = n*1000
print('\033[31m='*30, f'\n{n} metros\nconvertido em km dá {km:.3f}\nconvertido em hm {hm:.2f}\nconvertido em dam dá {dam:.1f}\nconvertido dm dá {dm:.0f}\nconvertido em cm dá {cm:.0f}\nE convertido em mm dá {mm:.0f}')
print('='*30)
print('\033[m')
