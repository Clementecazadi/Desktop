import sqlite3 as sq

dadas = [(3442, 'Clemenaet', 23, 'masculino', 1667),
         (3342, 'Clemaet', 13, 'masculino', 1637),
         (3322, 'gort', 18, 'masculino', 1631)]

conexao = sq.connect('database.ctg')
cursor = conexao.cursor()
cursor.executemany('insert into dados_alunos(ID, Nome, Idade, Sexo, Numero)'
                   ' values(?, ?, ?, ?, ?)', dadas)
conexao.commit()
cursor.close()
conexao.close()
