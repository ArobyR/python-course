import psycopg2 as db

connection = db.connect(user='postgres',
                              password='admin',
                              host='127.0.0.1',
                              port='5432', 
                              database='test_db')


cursor = connection.cursor()
sql_query = 'SELECT * FROM persona WHERE id_persona = %s and nombre = %s'
id_persona = input("Introduce la pk: ")
nombre = input("nombre: ")
llave_primaria_nombre = (id_persona, nombre)

cursor.execute(sql_query, llave_primaria_nombre)

data = cursor.fetchone()

print(data)

cursor.close()
connection.close