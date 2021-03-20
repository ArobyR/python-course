import psycopg2 as db

connection = db.connect(user='postgres',
                              password='admin',
                              host='127.0.0.1',
                              port='5432', 
                              database='test_db')


cursor = connection.cursor()
sql_query = 'SELECT * FROM persona WHERE id_persona IN (%s, %s, %s)'
entrada = input("Proporciona las pk a buscar (separdas por coma): ")
tupla = tuple(entrada.split(','))
print(tupla)
# llaves_primarias = ((1, 2, 3),)
cursor.execute(sql_query, tupla)

data = cursor.fetchall()

for record in data:
    print(record)

cursor.close()
connection.close