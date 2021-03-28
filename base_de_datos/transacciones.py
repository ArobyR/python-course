import psycopg2 as db

connection = db.connect(user='postgres',
                        password='admin',
                        host='127.0.0.1',
                        port='5432', 
                        database='test_db')

# connection.autocommit = True
try:
    cursor = connection.cursor()
    sql_query = 'INSERT INTO persona (nombre, primer_apellido, email) VALUES (%s, %s, %s);'
    tuple_values = ('test', 'last test', 'test@test.ch')
    cursor.execute(sql_query, tuple_values)

    sql_query = 'UPDATE persona SET nombre=%s, primer_apellido=%s, email=%s WHERE id_persona=%s;'
    tuple_values = ('G', 'force', 'gforce@g.com', 3)
    cursor.execute(sql_query, tuple_values)

    # guardamos la informacion
    connection.commit()
except Exception as e:
    # rollback da marcha atras a todas las operaciones pendientes
    connection.rollback()
    print(f'Error: {e}')

finally:    
    cursor.close()
    connection.close()