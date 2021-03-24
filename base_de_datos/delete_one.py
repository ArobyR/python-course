import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')


cursor = connection.cursor()
sql_query = 'DELETE FROM persona WHERE id_persona =%s;'

tuple_value = (1,)
cursor.execute(sql_query, tuple_value)
connection.commit()

registro_eliminado = cursor.rowcount
print(f'Registros eliminados: {registro_eliminado}')

cursor.close()
connection.close()