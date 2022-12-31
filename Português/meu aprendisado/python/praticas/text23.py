import sqlite3 as sq

conexao = sq.connect('database.ctg')
cursor = conexao.cursor()
cursor.execute('select * from dados_alunos')
fr = cursor.fetchall()
cursor.close()
conexao.close()
print(fr)
