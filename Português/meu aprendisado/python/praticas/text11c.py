galera = list()
dados = list()
total1 = total2 = 0
for c in range(0, 5):
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for c in galera:
    if c[1] >= 18:
        print(f'{c[0]} é maior de idade e ele tem {c[1]} anos')
        total1 += 1
    else:
        print(f'{c[0]} é menor de idade e ele tem {c[1]} anos')
        total2 += 1
print(f'Ao todo temos {total1} maiores e {total2} menores de idade')