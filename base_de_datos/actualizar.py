import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')


cursor = connection.cursor()
sql_query = 'UPDATE persona SET nombre=%s, primer_apellido=%s, email=%s WHERE id_persona =%s;'

tuple_value = ('Hack', 'World', 'email@email.com', 11)
cursor.execute(sql_query, tuple_value)
connection.commit()

registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

cursor.close()
connection.close()