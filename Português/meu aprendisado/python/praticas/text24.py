import sqlite3 as sq
# [(1256, 'clemen', 34, 'Mascolino', 9089), (3442, 'Clemenaet', 23, 'masculino', 1667),
# (3342, 'Clemaet', 13, 'masculino', 1637), (3322, 'gort', 18, 'masculino', 1631),
# (3442, 'Clemenaet', 23, 'masculino', 1667), (3342, 'Clemaet', 13, 'masculino', 1637),
# (3322, 'gort', 18, 'masculino', 1631)]

print('Mude os dados em dos aluno.')
iden = int(input('digite o ID do aluno: '))
nome = input('nome: ')
conexao = sq.connect('database.ctg')
cursor = conexao.cursor()
cursor.execute(f'update dados_alunos set Nome=? where ID=?', (nome, iden))
conexao.commit()
cursor.execute('select * from dados_alunos')
pf = cursor.fetchall()
cursor.close()
conexao.close()
print(pf)
