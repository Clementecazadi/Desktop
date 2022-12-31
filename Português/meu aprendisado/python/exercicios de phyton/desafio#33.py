print('Desafio#33')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Treceiro valor: '))
if n1 < n2 and n1 < n3 :
	menor = n1
if n2 < n1 and n2 < n3 :
	menor = n2
if n3 < n1 and n3 <n2 :
	menor = n3
print(f'O menor valor digitado foi {menor}')
if n1 > n2 and n1 > n3 :
	maior = n1
if n2 > n1 and n2 > n3 :
	maior = n2
if n3 > n1 and n3 > n2 : 
	maior = n3
print(f'O maior valor digitado foi {maior}')
