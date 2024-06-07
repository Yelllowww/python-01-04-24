import sqlite3
database='livraria.db'
conexao=sqlite3.connect(database)
cur=conexao.cursor()

sql='''create table if not exists tb_cliente(
    cpf text primary key,
    nome text not null,
    idade integer)'''

cur.execute(sql)
cur.close()
conexao.close()
print("fechou a base de dados")
import sqlite3
conexao=sqlite3.connect("livraria.db")
cur=conexao.cursor()
sql = "insert into tb_cliente(cpf, nome, idade) values ('1234', 'paula', 31)"
cur.execute(sql)
conexao.commit()
cur.close()
conexao.close()
print("fechou a base de dados")
import sqlite3
conexao = sqlite3.connect("livraria.db")
cur = conexao.cursor()
sql = "select * from tb_cliente"
cur.execute(sql)
l_registros = cur.fetchall()
print(l_registros)
cur.close()
conexao.close
print("fechou a base de dados")
import sqlite3
conexao=sqlite3.connect("livraria.db")
cur=conexao.cursor()

sql = "update tb_cliente set nome=? where cpf=?"
cur.execute(sql, ('Carla', '123'))

conexao.commit()
cur.close()
conexao.close()
print("Fechou a base de dados")
