import sqlite3 as sq
import shutil
conexao = sq.connect('database.ctg')
cursor = conexao.cursor()
cursor.execute('select * from dados_alunos')
dados = cursor.fetchone()
cursor.close()
conexao.close()
print(dados)
