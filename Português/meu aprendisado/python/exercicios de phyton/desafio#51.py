print(f'''{"=" * 30}
{" 10 TERMOS DE UMA PA ":=^30}
{"=" * 30}''')
t = int(input('Primeiro termo: '))
r = int(input('A razão: '))
tr = (t + (10 - 1)) * r
for pa in range(t, tr + r, r):
    print(pa, end=" > ")
print('Acabou')
