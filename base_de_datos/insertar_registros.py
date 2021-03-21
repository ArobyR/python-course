import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')


cursor = connection.cursor()
sql_query = 'INSERT INTO persona (nombre, primer_apellido, email) VALUES (%s, %s, %s);'

values = (
    ('Maria', 'Altagracia', 'mal@gmail.com'),
    ('Jimena', 'Mendez', 'mendez@gmail.com'),
    ('Shin', 'Fui', 'ff@gmail.com')
    )
cursor.executemany(sql_query, values)
connection.commit()

registros = cursor.rowcount
print(f'Registros insertados: {registros}')

cursor.close()
connection.close()