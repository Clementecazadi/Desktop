def vota(ano_de_nascimento):
    from datetime import date
    atual = date.today().year - ano_de_nascimento
    if atual < 17:
        return f'Com {atual} anos: Não vota.'
    if  18 <= atual < 65:
        return f'Com {atual} anos: Voto Obrigatorio.'
    if atual == 17 or atual >= 65:
        return f'Com {atual} anos: Voto Opcional.'

print('=' * 49)
print(vota(int(input('Em que ano você nasceu: '))))
