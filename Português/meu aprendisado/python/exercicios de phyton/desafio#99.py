def maior(*num):
	"""
	-> funçào de verrificação do maior valor inteiro.
	:param num: um o mais numeros
	:return: none
	função criada por clemente canc.
	"""
	from time import sleep
	valor = 0
	print('=' * 49)
	print(f"{'Analizando os valores passados...':49}")
	for c in range(0, len(num)):
		print(f' {num[c]}', end='', flush=True)
		sleep(0.5)
		if c == 0:
			valor = num[c]
		else:
			if valor < num[c]:
				valor = num[c]
	print(f'foram {len(num)} valores ao todo')
	print(f' O maior valor lido foi {valor}')
	sleep(1)
			
		
help(maior)
maior(3, 5, 7, 9)
maior(4, 6, 1, 89, 3, 2, 90, 1, 6)
maior()
