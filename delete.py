import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='cdd2023',
    database='escolaturmab'
)
print(banco)
cursor = banco.cursor()
sql = "delete from alunos where mat = 13;"
cursor.execute(sql)
banco.commit()
cursor.close()
banco.close()
