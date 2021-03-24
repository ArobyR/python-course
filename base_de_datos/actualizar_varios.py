import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432',
                        database='test_db')


cursor = connection.cursor()
sql_query = 'UPDATE persona SET nombre=%s, primer_apellido=%s, email=%s WHERE id_persona =%s;'

tuple_values = (
    ('Tuttancamon', 'F2', 'tf2_f@email.com', 7),
    ('Ron', 'jj', 'r_j@outlook.com', 1),
    ('Rudensigno', 'Junior', 'rdf@rdf.net', 10)
)

cursor.executemany(sql_query, tuple_values)
connection.commit()

registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

cursor.close()
connection.close()