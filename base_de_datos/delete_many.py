import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')


cursor = connection.cursor()
sql_query = 'DELETE FROM persona WHERE id_persona =%s;'
pk_values = input("Introduce las pk de los registros a eliminar separado por coma: ")

tuple_values = tuple(pk_values.split(','))
cursor.executemany(sql_query, tuple_values)
connection.commit()

registro_eliminado = cursor.rowcount
print(f'Registros eliminados: {registro_eliminado}')

cursor.close()
connection.close()