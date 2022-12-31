import sqlite3
conexao = sqlite3.connect('database.ctg')
cursor = conexao.cursor()
cursor.execute('create table dados_alunos(ID int, Nome text,'
               ' Idade int, Sexo text, Numero int)')
cursor.execute('insert into dados_alunos(ID, Nome, Idade, Sexo, Numero) values(?, ?, ?, ?, ?)',
               (1256, 'clemen', '34', 'Mascolino', 9089))

conexao.commit()
cursor.close()
conexao.close()
