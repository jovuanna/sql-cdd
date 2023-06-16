import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cdd2023',
    database='escolaturmab'
)
print(banco)

meucursor = banco.cursor()
pesquisa = 'select * from alunos'
meucursor.execute(pesquisa)
resultado = meucursor.fetchall()
for x in resultado:
    print(x)
'''meucursor.close()
banco.close()'''
nome1 = 'Jamesson'
cpf1 = '12345678915'
telefone1 = '98765432115'
media1 = '6.5'
fk_turmas1 = '2'
cursor = banco.cursor()
sql = "insert into alunos (nome, cpf, telefone, media, fk_turmas) values (%s, %s, %s, %s, %s)"
data = (nome1, cpf1, telefone1, media1, fk_turmas1)
cursor.execute(sql, data)
banco.commit()
userid = cursor.lastrowid
print(userid)
cursor.close()
banco.close()
